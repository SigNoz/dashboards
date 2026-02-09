# Kafka Server Monitoring

Comprehensive monitoring dashboard for self-hosted Apache Kafka clusters using OpenTelemetry (OTLP) metrics collected by the [OpenTelemetry Kafka metrics receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver).

## Dashboard Sections

### Cluster Overview
- **Broker Count** — Total number of brokers in the cluster (value panel)
- **Total Partitions** — Sum of partitions across all topics (value panel)
- **In-Sync Replicas** — Total ISR count across all partitions (value panel)
- **Under-Replicated Partitions** — Computed as total replicas minus in-sync replicas (graph with formula)

### Throughput
- **Messages In Rate** — Rate of messages received per second, grouped by service
- **Network Bytes In/Out** — Network I/O bytes per second, split by direction (in/out)
- **Request Rate** — Total request rate grouped by request type
- **Partitions Per Topic** — Partition count broken down by topic

### Consumer Groups
- **Consumer Group Lag** — Lag per consumer group and topic
- **Consumer Group Offset (Sum)** — Committed offset sum per group
- **Consumer Group Members** — Active member count per group

### Request Performance
- **Request Count by Type** — Request rate grouped by type and service
- **Failed Requests** — Failed request rate by type
- **Avg Request Time** — Average request processing time by type
- **Purgatory Size** — Delayed request queue size by type

### Log Management
- **Log Flush Rate** — Rate of log flush operations per service
- **Log Flush Time (Median)** — Median flush latency per service
- **Current vs Oldest Offset** — Offset gap per topic for retention monitoring

## Metrics Used

| Metric | Type | Description |
|--------|------|-------------|
| `kafka.brokers` | Gauge | Number of brokers in the cluster |
| `kafka.topic.partitions` | Gauge | Number of partitions per topic |
| `kafka.partition.current_offset` | Gauge | Current partition offset |
| `kafka.partition.oldest_offset` | Gauge | Oldest retained partition offset |
| `kafka.partition.replicas` | Gauge | Total replica count per partition |
| `kafka.partition.replicas_in_sync` | Gauge | In-sync replica count per partition |
| `kafka.request.count` | Sum | Number of requests received |
| `kafka.request.failed` | Sum | Number of failed requests |
| `kafka.request.time.avg` | Gauge | Average request processing time |
| `kafka.network.io` | Sum | Network I/O bytes (with `direction` attribute) |
| `kafka.message.count` | Sum | Total messages received |
| `kafka.logs.flush.time.count` | Sum | Log flush operation count |
| `kafka.logs.flush.time.median` | Gauge | Median log flush time |
| `kafka.purgatory.size` | Gauge | Request purgatory queue size |
| `kafka.consumer_group.lag` | Gauge | Consumer group lag per partition |
| `kafka.consumer_group.offset_sum` | Gauge | Total consumer group offset |
| `kafka.consumer_group.members` | Gauge | Consumer group member count |

## Variables

| Variable | Attribute | Description |
|----------|-----------|-------------|
| `deployment.environment` | `deployment.environment` | Filter by deployment environment |
| `service.name` | `service.name` | Filter by Kafka service name |
| `topic` | `topic` | Filter by Kafka topic |

## Prerequisites

1. Deploy the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) with the [Kafka metrics receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver) enabled.
2. Configure the receiver to scrape your Kafka brokers.
3. Export metrics to SigNoz using the OTLP exporter.

### Example Collector Configuration

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

exporters:
  otlp:
    endpoint: "<signoz-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [kafkametrics]
      exporters: [otlp]
```

## Import

1. Open SigNoz UI
2. Navigate to **Dashboards** > **New Dashboard** > **Import JSON**
3. Upload `kafka-server-otlp-v1.json`
