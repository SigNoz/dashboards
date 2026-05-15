# Kafka Server Monitoring Dashboard - OTEL

## Metrics Ingestion

This dashboard uses the [OpenTelemetry Kafka Metrics Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kafkametricsreceiver) to collect Kafka broker, topic, partition, and consumer group metrics.

### otel-config.yaml

```yaml
receivers:
  kafkametrics:
    collection_interval: 10s
    brokers: kafka:9092
    auth:
      authenticator: nop
    metrics:
      topic:
        enabled: true
      consumer_group:
        enabled: true

service:
  pipelines:
    metrics:
      receivers: [kafkametrics]
      exporters: [otlp]

exporters:
  otlp:
    endpoint: "signoz-otel-collector:4317"
    tls:
      insecure: true
```

## Variables

- `deployment_environment`: Deployment environment (e.g., production, staging)
- `kafka_cluster_alias`: Kafka cluster alias identifier

## Dashboard Panels

### Broker Metrics
- **Messages In Per Second**: Rate of messages received by brokers
- **Bytes In Per Second**: Rate of bytes received by brokers
- **Bytes Out Per Second**: Rate of bytes sent by brokers
- **Active Controllers**: Number of active controller brokers
- **Under Replicated Partitions**: Number of under-replicated partitions

### Topic Metrics
- **Messages In by Topic**: Rate of messages received per topic
- **Bytes In by Topic**: Rate of bytes received per topic
- **Bytes Out by Topic**: Rate of bytes sent per topic
- **Total Topic Count**: Total number of topics in the cluster

### Partition Metrics
- **Under-Replicated Partitions**: Under-replicated partitions by topic
- **Offline Partitions**: Number of offline partitions
- **Partition Count by Topic**: Number of partitions per topic
- **ISR (In-Sync Replicas)**: In-sync replica count per topic

### Consumer Metrics
- **Consumer Group Lag**: Lag for each consumer group
- **Consumer Group Members**: Members in each consumer group
- **Consumer Group Count**: Total number of consumer groups
- **Consumer Lag by Topic**: Consumer lag broken down by topic
