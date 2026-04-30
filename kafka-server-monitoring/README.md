# Kafka Server Monitoring Dashboard

A comprehensive monitoring dashboard for Apache Kafka brokers in SigNoz. This dashboard provides deep visibility into all critical aspects of Kafka cluster operations, from high-level cluster health to low-level JVM metrics.

## Overview

This dashboard contains **125+ panels** organized into **13 sections**, covering every major Kafka subsystem:

| Section | Panels | Description |
|---------|--------|-------------|
| Cluster Overview | 12 | Controller status, partition health, ISR dynamics, leader elections |
| Throughput | 14 | Message rates, byte rates, replication traffic, failed requests |
| Request Performance | 18 | Request handler idle, latency breakdown (queue/local/remote/send), error rates |
| Consumer Group Lag | 8 | Consumer lag per partition, offset commit rates, group membership |
| Topic Details | 10 | Per-topic message/byte rates, log offsets, segment counts, log sizes |
| Broker Resources (JVM & System) | 16 | Heap/non-heap memory, GC, threads, file descriptors, CPU, RSS |
| Network & Connections | 10 | Connection counts/rates, byte rates, request/response queue sizes |
| Log Flush & Compaction | 6 | Flush rate/latency, cleaner buffer utilization, dirty ratio |
| Delayed Operations (Purgatory) | 9 | Purgatory sizes for Produce/Fetch/DeleteRecords/ElectLeader/Rebalance |
| ZooKeeper Client Metrics | 8 | Request latency, session expiry, disconnects, auth failures |
| KRaft Controller Metrics | 6 | Leader, commit latency, log offset, election latency |
| Quotas & Throttling | 4 | Produce/Fetch/Request throttle times and rates |
| Authentication & Authorization | 4 | Auth success/failure rates, reauthentication |

## Prerequisites

### Metrics Collection

This dashboard requires Kafka JMX metrics exported in Prometheus format. There are two supported approaches:

### Option A: JMX Exporter + OpenTelemetry Collector (Recommended)

**1. Configure the JMX Exporter agent on each Kafka broker:**

Download the [Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter) JAR and create a configuration file:

```yaml
# kafka-jmx-config.yaml
lowercaseOutputName: true
lowercaseOutputLabelNames: true
whitelistObjectNames:
  # Broker Topic Metrics
  - "kafka.server:type=BrokerTopicMetrics,*"
  # Request Metrics
  - "kafka.network:type=RequestMetrics,*"
  # Controller Metrics
  - "kafka.controller:type=KafkaController,*"
  - "kafka.controller:type=ControllerStats,*"
  # Replica Manager
  - "kafka.server:type=ReplicaManager,*"
  # Request Handler Pool
  - "kafka.server:type=KafkaRequestHandlerPool,*"
  # Network Processor
  - "kafka.network:type=SocketServer,*"
  # Log Metrics
  - "kafka.log:type=LogFlushStats,*"
  - "kafka.log:type=Log,*"
  - "kafka.log:type=LogCleaner,*"
  # Delayed Operation Purgatory
  - "kafka.server:type=DelayedOperationPurgatory,*"
  # ZooKeeper / Session Expire Listener
  - "kafka.server:type=ZooKeeperClientMetrics,*"
  - "kafka.server:type=SessionExpireListener,*"
  # Socket Server Metrics
  - "kafka.server:type=socket-server-metrics,*"
  # Client Quota Manager
  - "kafka.server:type=ClientQuotaManager,*"
  # KRaft Raft Manager
  - "kafka.server:type=raft-manager-metrics,*"
  # JVM Metrics (built-in with JMX exporter)
rules:
  - pattern: ".*"
```

Add the JMX exporter as a Java agent to each Kafka broker's startup:

```bash
export KAFKA_OPTS="-javaagent:/path/to/jmx_prometheus_javaagent.jar=7071:/path/to/kafka-jmx-config.yaml"
```

**2. Configure the OpenTelemetry Collector to scrape JMX metrics:**

```yaml
# otel-collector-config.yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "kafka-broker"
          scrape_interval: 15s
          static_configs:
            - targets:
                - "kafka-broker-1:7071"
                - "kafka-broker-2:7071"
                - "kafka-broker-3:7071"
              labels:
                service_name: "kafka"

processors:
  batch:
    send_batch_size: 10000
    timeout: 10s
  resourcedetection:
    detectors: [env, system]
    timeout: 5s

exporters:
  otlp:
    endpoint: "<your-signoz-endpoint>:4317"
    tls:
      insecure: true  # Set to false in production with proper certs

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [resourcedetection, batch]
      exporters: [otlp]
```

### Option B: OpenTelemetry JMX Receiver (Alternative)

Use the [OpenTelemetry JMX Receiver](https://github.com/open-telemetry/opentelemetry-java-contrib/tree/main/jmx-metrics) with the built-in Kafka configuration:

```yaml
receivers:
  jmx:
    jar_path: /path/to/opentelemetry-jmx-metrics.jar
    endpoint: "kafka-broker-1:9999"  # JMX remote port
    target_system: kafka,jvm
    collection_interval: 15s

exporters:
  otlp:
    endpoint: "<your-signoz-endpoint>:4317"

service:
  pipelines:
    metrics:
      receivers: [jmx]
      exporters: [otlp]
```

### Consumer Lag Metrics

For consumer group lag metrics (`kafka_consumergroup_lag`, `kafka_consumergroup_lag_sum`, etc.), use one of:

- [kafka-lag-exporter](https://github.com/seglo/kafka-lag-exporter) (recommended)
- [Burrow](https://github.com/linkedin/Burrow) with a Prometheus exporter
- OpenTelemetry Kafka metrics receiver

Configure the lag exporter scrape in your OTel collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "kafka-lag-exporter"
          scrape_interval: 15s
          static_configs:
            - targets: ["kafka-lag-exporter:8000"]
```

## Dashboard Variables

| Variable | Description | Source |
|----------|-------------|--------|
| `kafka_cluster` | Deployment environment / cluster name | `deployment_environment` label |
| `service_name` | Kafka service name in OTel | `service.name` resource attribute |
| `instance` | Individual broker instance | `instance` label |
| `topic` | Kafka topic name | `topic` label |
| `consumer_group` | Consumer group name | `group` label from lag exporter |

## Key Metrics Reference

### Critical Health Metrics (Alert on these)

| Metric | Healthy Value | Alert Threshold |
|--------|--------------|-----------------|
| `kafka_controller_kafkacontroller_activecontrollercount` | Exactly 1 | != 1 |
| `kafka_controller_kafkacontroller_offlinepartitionscount` | 0 | > 0 |
| `kafka_server_replicamanager_underreplicatedpartitions` | 0 | > 0 for 5 min |
| `kafka_controller_controllerstats_uncleanleaderelections_total` | 0 rate | > 0 |
| `kafka_server_kafkarequesthandlerpool_requesthandleravgidle_percent` | > 0.3 | < 0.3 |
| `kafka_network_socketserver_networkprocessoravgidle_percent` | > 0.3 | < 0.3 |

### Performance Metrics

| Metric | Description |
|--------|-------------|
| `kafka_network_requestmetrics_totaltimems` | Total request processing time (queue + local + remote + send) |
| `kafka_network_requestmetrics_requestqueuetimems` | Time request waits in the request queue |
| `kafka_network_requestmetrics_localtimems` | Time for leader to process the request |
| `kafka_network_requestmetrics_remotetimems` | Time waiting for follower replication (acks=all) |
| `kafka_network_requestmetrics_responsesendtimems` | Time to send the response to the client |

### JVM Metrics

| Metric | Description |
|--------|-------------|
| `jvm_memory_bytes_used{area="heap"}` | Current heap memory usage |
| `jvm_gc_collection_seconds_sum` | Cumulative GC time |
| `jvm_gc_collection_seconds_count` | Cumulative GC invocation count |
| `jvm_threads_current` | Current thread count |
| `process_open_fds` | Open file descriptor count |

## Troubleshooting

### No data showing in panels

1. Verify the OTel collector is running and scraping your Kafka brokers
2. Check that the JMX exporter port (default 7071) is accessible
3. In SigNoz, go to **Metrics Explorer** and search for `kafka_server` to verify metrics are being ingested
4. Ensure the dashboard variable filters match your actual label values

### Metrics naming differences

Different JMX exporter versions may produce slightly different metric names. The most common format used by this dashboard follows the `kafka_server_*` / `kafka_network_*` convention from the standard Prometheus JMX exporter. If your metric names differ:

- Check with `kafka.server:type=` vs `kafka_server_` naming
- The JMX exporter `lowercaseOutputName: true` setting is required
- Verify with SigNoz Metrics Explorer that the exact metric names match

### Consumer lag metrics missing

Consumer lag requires a separate exporter (kafka-lag-exporter or similar). The standard JMX exporter does not expose consumer group lag. Install and configure the kafka-lag-exporter as described in the Prerequisites section.

## License

This dashboard is provided under the Apache 2.0 license as part of the SigNoz dashboards repository.
