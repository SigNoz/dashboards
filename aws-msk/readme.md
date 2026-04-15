# AWS MSK Cluster Monitoring Dashboard - OTEL

## Metrics Ingestion

This dashboard uses metrics collected from AWS MSK via the AWS Distro for OpenTelemetry (ADOT) or the Prometheus JMX exporter with CloudWatch integration.

### otel-config.yaml

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'aws-msk'
          static_configs:
            - targets: ['msk-broker:9092']
          metrics_path: /metrics

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]

exporters:
  otlp:
    endpoint: "signoz-otel-collector:4317"
    tls:
      insecure: true
```

Refer to [AWS docs on Kafka with ADOT](https://aws.amazon.com/about-aws/whats-new/2023/04/apache-kafka-aws-distro-opentelemetry/) for additional setup instructions.

## Variables

- `deployment_environment`: Deployment environment (e.g., production, staging)
- `cluster_name`: MSK Cluster name

## Dashboard Panels

### Broker Metrics
- **Broker CPU Usage**: CPU utilization per broker
- **Broker Memory Usage**: Memory consumption per broker
- **Network Traffic In/Out**: Network traffic per broker
- **Broker Disk Usage**: Disk space usage per broker
- **Broker Disk Throughput**: Read/write throughput per broker

### Topic Metrics
- **Messages In Per Second**: Messages sent to each topic per second
- **Bytes In Per Second**: Data produced to each topic per second
- **Bytes Out Per Second**: Data consumed from each topic per second
- **Messages Out Per Second**: Messages consumed from each topic per second

### Partition Metrics
- **Under-Replicated Partitions**: Under-replicated partition count
- **Partition ISR Count**: In-sync replicas per topic
- **Partition Count per Topic**: Partitions per topic

### Consumer Metrics
- **Consumer Lag**: Lag for each consumer group
- **Consumer Error Rate**: Error rate for consumer requests

### AWS CloudWatch Metrics
- **CPU Credit Usage**: CPU credit usage for burstable instances
- **Burst Balance**: CPU burst balance per broker
- **Network I/O**: Network input/output via CloudWatch
