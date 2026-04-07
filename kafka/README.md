# Kafka Server Monitoring Dashboard

Kafka monitoring dashboard for [SigNoz](https://signoz.io/). Fixes [SigNoz/signoz#6026](https://github.com/SigNoz/signoz/issues/6026).

Uses the OpenTelemetry [`kafkametrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/kafkametricsreceiver/README.md) receiver.

## Sections

| #   | Section          | Covers                                                             |
| --- | ---------------- | ------------------------------------------------------------------ |
| 1   | Broker Metrics   | Broker count, log retention period                                 |
| 2   | Consumer Metrics | Consumer group lag, members, offset by topic, lag by partition      |
| 3   | Topic Metrics    | Partitions per topic, replication factor, ISR, retention period/size |
| 4   | Partition Metrics | Current/oldest offset, replicas, ISR, under-replicated partitions  |

## OTel Collector Config

```yaml
receivers:
  kafkametrics:
    brokers:
      - "kafka-broker:9092"
    protocol_version: "2.0.0"
    collection_interval: 30s
    scrapers:
      - brokers
      - topics
      - consumers

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "kafka"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [kafkametrics]
      processors: [batch, resource]
      exporters: [otlp]
```

## Dashboard Variables

- `deployment.environment` — Deployment Environment
- `kafka.cluster.alias` — Kafka Cluster
- `service.name` — Service Name

### Notes

- Screenshots will be added to the `assets/` directory.
