# Kafka Server Monitoring Dashboard - OTLP

## Metrics Ingestion

This dashboard uses metrics from the [OpenTelemetry Kafka metrics receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver).

Add the Kafka metrics receiver to your OpenTelemetry Collector configuration:

```yaml
receivers:
  kafkametrics:
    brokers:
      - localhost:9092
    protocol_version: 2.0.0
    scrapers:
      - brokers
      - topics
      - consumers
    collection_interval: 30s
    # Enable optional metrics for full dashboard coverage
    metrics:
      kafka.broker.log_retention_period:
        enabled: true
      kafka.topic.replication_factor:
        enabled: true
      kafka.topic.min_insync_replicas:
        enabled: true
      kafka.topic.log_retention_period:
        enabled: true
      kafka.topic.log_retention_size:
        enabled: true

processors:
  resource/env:
    attributes:
      - key: deployment.environment
        value: "production"
        action: upsert

exporters:
  otlp:
    endpoint: "<signoz-otel-collector-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [kafkametrics]
      processors: [resource/env]
      exporters: [otlp]
```

For full configuration options, see the [receiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver).

## Variables

- `{{deployment.environment}}`: Deployment environment filter
- `{{kafka.cluster.alias}}`: Kafka cluster alias (optional resource attribute set on the receiver)

## Dashboard Sections

### Broker Metrics
Cluster-level broker count (current value and over time) and per-broker log retention period configuration.

### Consumer Metrics
Consumer group lag aggregated by topic and broken down by partition, consumer group member counts, committed offset sums, per-partition offsets, and total lag per consumer group.

### Topic Metrics
Per-topic partition counts, replication factor, minimum in-sync replicas, log retention period, and log retention size.

### Partition Metrics
Per-partition current offset, oldest offset, total replicas, and in-sync replicas.

## Metrics Reference

All 16 metrics from the OTel Kafka metrics receiver are used:

| Metric | Type | Section |
|--------|------|---------|
| `kafka.brokers` | Sum | Broker |
| `kafka.broker.log_retention_period` | Gauge (optional) | Broker |
| `kafka.consumer_group.lag` | Gauge | Consumer |
| `kafka.consumer_group.lag_sum` | Gauge | Consumer |
| `kafka.consumer_group.members` | Sum | Consumer |
| `kafka.consumer_group.offset` | Gauge | Consumer |
| `kafka.consumer_group.offset_sum` | Gauge | Consumer |
| `kafka.topic.partitions` | Sum | Topic |
| `kafka.topic.replication_factor` | Gauge (optional) | Topic |
| `kafka.topic.min_insync_replicas` | Gauge (optional) | Topic |
| `kafka.topic.log_retention_period` | Gauge (optional) | Topic |
| `kafka.topic.log_retention_size` | Gauge (optional) | Topic |
| `kafka.partition.current_offset` | Gauge | Partition |
| `kafka.partition.oldest_offset` | Gauge | Partition |
| `kafka.partition.replicas` | Sum | Partition |
| `kafka.partition.replicas_in_sync` | Sum | Partition |

Metrics marked **(optional)** are disabled by default in the receiver and must be explicitly enabled in the collector config (shown above).
