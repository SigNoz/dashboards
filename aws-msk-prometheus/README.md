# AWS MSK Cluster Monitoring - Prometheus

Comprehensive monitoring dashboard for **AWS Managed Streaming for Apache Kafka (MSK)** clusters using Prometheus metrics collected via `kafka_exporter` (Daniel Czerwonk) and the JMX Prometheus exporter, with optional CloudWatch metrics sourced through `prometheus-cloudwatch-exporter`.

---

## Metrics Ingestion

### Option A: kafka_exporter (recommended)

Deploy [kafka_exporter](https://github.com/danielqsj/kafka_exporter) pointing at your MSK bootstrap brokers:

```bash
docker run -d \
  --name kafka-exporter \
  -p 9308:9308 \
  danielqsj/kafka-exporter \
  --kafka.server=<MSK_BOOTSTRAP_BROKER>:9092
```

Then add the following scrape config to your OpenTelemetry Collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: kafka-exporter
          scrape_interval: 30s
          static_configs:
            - targets: ["kafka-exporter:9308"]
              labels:
                cluster_name: my-msk-cluster

exporters:
  otlp:
    endpoint: "<signoz-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

### Option B: JMX Prometheus Exporter (for JVM metrics)

Enable JMX on each MSK broker and deploy the [jmx_prometheus_javaagent](https://github.com/prometheus/jmx_exporter) to expose `jvm_memory_bytes_used`, `jvm_gc_collection_seconds_sum`, and Kafka server metrics.

### Option C: CloudWatch via prometheus-cloudwatch-exporter (optional)

To populate the CloudWatch-backed panels (`aws_msk_bytes_in_per_sec_average`, `aws_msk_cpu_user_average`, `aws_msk_consumer_lag_offsets_maximum`), deploy [yet-another-cloudwatch-exporter](https://github.com/nerdswords/yet-another-cloudwatch-exporter) with a config targeting MSK metrics from the `AWS/Kafka` namespace.

---

## Variables

This dashboard uses no template variables by default. All panels work with metric labels for grouping. You can optionally add a SigNoz variable for `cluster_name` or `broker_id` to filter panels to a specific cluster.

---

## Dashboard Panels

### Cluster Overview (4 value panels)

| Panel | Metric | Notes |
|---|---|---|
| Active Brokers | `kafka_brokers` | Count of reachable brokers |
| Active Controllers | `kafka_controller_kafkacontroller_activecontrollercount` | Should always be exactly 1 |
| Offline Partitions | `kafka_controller_kafkacontroller_offlinepartitionscount` | Should always be 0 |
| Total Topics | `count(count by (topic)(kafka_topic_partitions))` | Distinct topic count |

### Throughput (3 graph panels)

- **Bytes In per Second** — `kafka_server_broker_metrics_bytes_in_per_sec` + `aws_msk_bytes_in_per_sec_average`
- **Bytes Out per Second** — `kafka_server_broker_metrics_bytes_out_per_sec` + `aws_msk_bytes_out_per_sec_average`
- **Messages In per Second** — `kafka_server_broker_metrics_messages_in_per_sec`

### Consumer Groups (3 graph panels)

- **Consumer Group Lag** — `kafka_consumergroup_lag` + `aws_msk_consumer_lag_offsets_maximum` (critical SLA metric)
- **Consumer Group Lag Sum** — `kafka_consumergroup_lag_sum` aggregated per group
- **Consumer Offset Commit Rate** — derived from `kafka_consumergroup_current_offset`

### Partitions (3 graph panels)

- **Partition Count by Topic** — `kafka_topic_partitions`
- **Under-Replicated Partitions** — `kafka_topic_partition_replicas - kafka_topic_partition_in_sync_replica`
- **In-Sync Replicas** — `kafka_topic_partition_in_sync_replica`

### Performance (4 graph panels)

- **Request Latency P99** — `histogram_quantile(0.99, ...)` over `kafka_network_request_metrics_total_time_ms_bucket`
- **Broker CPU Utilization** — `aws_msk_cpu_user_average`
- **JVM Heap Memory Used** — `jvm_memory_bytes_used{area="heap"}`
- **JVM GC Pause Time** — `rate(jvm_gc_collection_seconds_sum[5m])`

### Storage (3 graph panels)

- **Log Size by Topic** — `kafka_log_log_size`
- **Current Offset by Topic** — `kafka_topic_partition_current_offset`
- **Oldest Offset by Topic** — `kafka_topic_partition_oldest_offset`

### Replication & Stability (3 graph panels)

- **Replica Count by Topic** — `kafka_topic_partition_replicas`
- **Leader Election Rate** — `kafka_controller_kafkacontroller_leaderelectionrateandtimems_count`
- **Unclean Leader Election Rate** — should be 0; any non-zero value indicates potential data loss

---

## Key Alerts to Configure

| Condition | Threshold | Severity |
|---|---|---|
| `kafka_controller_kafkacontroller_offlinepartitionscount > 0` | Immediate | Critical |
| `kafka_controller_kafkacontroller_activecontrollercount != 1` | Immediate | Critical |
| `kafka_consumergroup_lag_sum > <threshold>` | SLA-dependent | Warning |
| `kafka_topic_partition_replicas - kafka_topic_partition_in_sync_replica > 0` | Sustained >5m | Warning |
| Unclean leader elections > 0 | Any occurrence | Critical |

---

## Related Issue

Requested in [signoz/signoz#6036](https://github.com/signoz/signoz/issues/6036).
