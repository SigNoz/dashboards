# AWS MSK Cluster Monitoring Dashboard — Prometheus

Comprehensive AWS Managed Streaming for Apache Kafka (MSK) monitoring dashboard for SigNoz, built on CloudWatch and JMX Exporter metrics exposed via Prometheus.

## Metrics Ingestion

### 1. Enable Open Monitoring on MSK

```bash
aws kafka update-monitoring \
  --cluster-arn <CLUSTER_ARN> \
  --current-version <CLUSTER_VERSION> \
  --open-monitoring '{"Prometheus":{"JmxExporter":{"EnabledInBroker":true},"NodeExporter":{"EnabledInBroker":true}}}'
```

JMX metrics are exposed on port `11001` and Node Exporter on port `11002`.

### 2. OpenTelemetry Collector Configuration

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'aws-msk'
          scrape_interval: 15s
          static_configs:
            - targets:
                - 'b-1.msk-cluster.region.amazonaws.com:11001'
                - 'b-2.msk-cluster.region.amazonaws.com:11001'
                - 'b-3.msk-cluster.region.amazonaws.com:11001'

exporters:
  otlp:
    endpoint: "ingest.signoz.io:443"
    tls:
      insecure: false
    headers:
      "signoz-ingestion-key": "<SIGNOZ_INGESTION_KEY>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Variables

- `{{cluster_name}}`: MSK cluster name
- `{{broker_id}}`: Filter by broker ID
- `{{topic}}`: Filter by topic
- `{{consumer_group}}`: Filter by consumer group

## Dashboard Sections

1. **Cluster Overview** — Active controller, offline partitions, under-replicated partitions, broker count
2. **Throughput** — Messages/bytes in/out per second, replication bytes
3. **Request Performance** — Produce/fetch latency, handler/processor idle %
4. **Storage** — Disk usage, partition count, log segments
5. **Consumer Group** — Offset lag, time lag, partition count
6. **CPU & Memory** — CPU user/system, memory, swap, network packets
7. **Replication** — ISR shrink/expand, leader count, min-ISR
8. **Connections** — Connection count, creation/close rate, auth errors
