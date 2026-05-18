# Kafka Server Monitoring Dashboard - Prometheus

## Overview
Monitor Kafka server health, topics, partitions and consumer groups using OTel Kafka metrics receiver.

## Metrics Ingestion
Use the OpenTelemetry Kafka metrics receiver:

```yaml
receivers:
  kafkametrics:
    brokers:
      - <kafka-broker>:9092
    scrapers:
      - brokers
      - topics
      - consumers
```

## Variables
- `{{deployment.environment}}`: Deployment environment
- `{{kafka.cluster.alias}}`: Kafka cluster alias
