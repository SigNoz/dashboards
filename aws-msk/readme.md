# AWS MSK Cluster Monitoring Dashboard for SigNoz

Pre-built SigNoz dashboard for monitoring AWS Managed Streaming for Apache Kafka (MSK) clusters using OpenTelemetry (OTLP) metrics.

## Sections

- **Broker Metrics** -- CPU usage, memory usage, network traffic in/out, disk usage, disk throughput
- **Topic Metrics** -- Messages in/s, messages out/s, bytes in/s, bytes out/s
- **Partition Metrics** -- Under-replicated partitions, ISR count, partition count
- **Consumer Metrics** -- Consumer lag, consumer fetch rate
- **AWS Metrics** -- CPU credit usage, burst balance, network I/O aggregate

## OTLP Metrics Used

| Metric | Type | Description |
|--------|------|-------------|
| `kafka.broker.cpu.usage` | Gauge | Broker CPU utilization |
| `kafka.broker.memory.usage` | Gauge | Broker memory utilization |
| `kafka.network.io` | Sum | Network bytes with `direction` label (in/out) |
| `kafka.broker.disk.usage` | Gauge | Broker disk utilization |
| `kafka.topic.messages.in` | Sum | Messages produced per topic |
| `kafka.topic.messages.out` | Sum | Messages consumed per topic |
| `kafka.topic.bytes.in` | Sum | Bytes produced per topic |
| `kafka.topic.bytes.out` | Sum | Bytes consumed per topic |
| `kafka.partition.under_replicated` | Gauge | Under-replicated partition count |
| `kafka.partition.isr` | Gauge | In-sync replica count |
| `kafka.partition.count` | Gauge | Total partition count |
| `kafka.consumer.fetch_manager.records_lag` | Gauge | Consumer group lag |
| `kafka.consumer.fetch_manager.fetch_rate` | Gauge | Consumer fetch rate |

## Variables

The dashboard includes three template variables for filtering:

- `deployment.environment` -- Filter by deployment environment
- `kafka.cluster.name` -- Filter by MSK cluster name
- `broker.id` -- Filter by individual broker ID

## Installation

Import `aws-msk-otlp-v1.json` into SigNoz via Settings > Dashboards > Import JSON.
