# Kafka Server Monitoring Dashboard

This dashboard provides comprehensive monitoring for Apache Kafka clusters using the [OpenTelemetry Kafka Metrics Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver).

## Dashboard Sections

### Broker Metrics
Overview gauges for the entire cluster:
- **Number of Brokers** — total active brokers (`kafka.brokers`)
- **Number of Topics** — distinct topics with partitions
- **Total Partitions** — sum of all partitions across topics
- **Consumer Groups** — number of distinct consumer groups

### Topic Metrics
Per-topic visibility:
- **Partitions per Topic** — `kafka.topic.partitions` grouped by topic (top 20)
- **Replicas per Topic** — total replicas summed per topic (`kafka.partition.replicas`)

### Partition Metrics
Partition-level health:
- **Partition Current Offset** — log-end offset per partition, showing produce progress (`kafka.partition.current_offset`)
- **Partition Oldest Offset** — log-start offset, showing retention boundary (`kafka.partition.oldest_offset`)
- **In-Sync Replicas per Partition** — minimum ISR count; drops below replication factor indicate risk (`kafka.partition.replicas_in_sync`)
- **Partition Leader Election Status** — 1 = healthy leader, 0 = under election (`kafka.partition.leader`)

### Consumer Group Metrics
Consumer health and throughput:
- **Consumer Group Lag per Partition** — per-partition lag for each group (`kafka.consumer_group.lag`)
- **Total Consumer Group Lag** — lag summed per group across all topics
- **Consumer Group Offset per Partition** — consumer progress through the log (`kafka.consumer_group.offset`)
- **Consumer Group Members** — active members per group (`kafka.consumer_group.members`)

## Metrics Source

All metrics are collected via the **OpenTelemetry Kafka Metrics Receiver** (`kafkametricsreceiver`) and ingested via OTLP.

| Metric | Description |
|--------|-------------|
| `kafka.brokers` | Number of brokers in the cluster |
| `kafka.topic.partitions` | Number of partitions per topic |
| `kafka.partition.replicas` | Total replicas for a partition |
| `kafka.partition.replicas_in_sync` | In-sync replicas for a partition |
| `kafka.partition.leader` | 1 if partition has a leader, 0 otherwise |
| `kafka.partition.current_offset` | Current (log-end) offset |
| `kafka.partition.oldest_offset` | Oldest (log-start) offset |
| `kafka.consumer_group.lag` | Lag for a consumer group on a partition |
| `kafka.consumer_group.lag_sum` | Total lag summed across partitions |
| `kafka.consumer_group.offset` | Consumer group committed offset |
| `kafka.consumer_group.members` | Number of members in the group |

## Setup

### Configure OpenTelemetry Collector

Add the following to your OpenTelemetry Collector configuration:

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

service:
  pipelines:
    metrics:
      receivers: [kafkametrics]
      exporters: [otlp]
```

For authentication (SASL/TLS), refer to the [kafkametricsreceiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver).

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by deployment environment (e.g., `production`, `staging`) |
| `kafka.cluster.alias` | Filter by Kafka cluster alias when monitoring multiple clusters |

## Importing the Dashboard

1. Open SigNoz and navigate to **Dashboards**.
2. Click **New Dashboard** → **Import JSON**.
3. Paste the contents of `kafka-server-monitoring-otlp-v1.json`.
4. Set the `deployment.environment` variable to match your cluster.

## References

- [OpenTelemetry Kafka Metrics Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver)
- [SigNoz Kafka Monitoring Guide](https://signoz.io/docs/messaging-queues/kafka/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
