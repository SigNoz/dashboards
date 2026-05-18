# AWS MSK Cluster Monitoring Dashboard - Prometheus

## Overview
Monitor AWS MSK cluster health, topics, partitions and consumer lag.

## Metrics Ingestion
Use the JMX Exporter with Kafka broker and scrape via OpenTelemetry Collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: msk
          static_configs:
            - targets: ['<broker1>:11001', '<broker2>:11001']
```

## Variables
- `{{deployment.environment}}`: Deployment environment
