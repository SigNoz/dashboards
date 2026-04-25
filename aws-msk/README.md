# AWS MSK Cluster Monitoring Dashboard

Comprehensive monitoring dashboard for Amazon MSK (Managed Streaming for Apache Kafka) clusters with CloudWatch metrics integration.

## Metrics Ingestion

### AWS CloudWatch Metrics via OpenTelemetry

Configure the OpenTelemetry Collector to scrape AWS MSK CloudWatch metrics:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    poll_interval: 60s
    metrics:
      named:
        aws_kafka:
          namespace: AWS/Kafka
          period: 60s
          dimensions:
            - name: Cluster Name
              value: "*"
            - name: Broker ID
              value: "*"
            - name: Topic
              value: "*"
            - name: Consumer Group
              value: "*"

exporters:
  otlp:
    endpoint: "ingest.<your-region>.signoz.cloud:443"
    headers:
      "signoz-ingestion-key": "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [awscloudwatch]
      exporters: [otlp]
```

### Enhanced Monitoring

For full dashboard functionality, enable MSK enhanced monitoring at **PER_TOPIC_PER_BROKER** level:

```bash
aws kafka update-monitoring \
    --cluster-arn <cluster-arn> \
    --enhanced-monitoring PER_TOPIC_PER_BROKER
```

## Dashboard Sections

### 1. Broker Metrics
- **CPU Usage** - CPU utilization percentage per broker
- **Memory Usage** - Memory consumption per broker
- **Network Traffic In/Out** - Network bytes received/transmitted
- **Disk Usage** - Kafka data logs disk utilization
- **Disk Throughput** - Read/write throughput per broker

### 2. Topic Metrics
- **Messages In Per Second** - Message production rate per topic
- **Messages Out Per Second** - Message consumption rate per topic
- **Bytes In Per Second** - Data volume produced per topic
- **Bytes Out Per Second** - Data volume consumed per topic

### 3. Partition Metrics
- **Under-Replicated Partitions** - Replication health indicator (alert threshold: >0)
- **Partition ISR Health** - Partitions under minimum ISR count
- **Partition Count** - Partition distribution per topic
- **Offline Partitions** - Critical alert for unavailable partitions

### 4. Consumer Metrics
- **Consumer Lag** - Estimated max time lag per consumer group
- **Consumer Fetch Time** - Average consumer request latency

### 5. AWS CloudWatch Metrics
- **CPU Credit Usage** - For burstable T-series instances
- **Burst Balance** - Remaining CPU burst credits (warning at <20%)
- **Network I/O** - Dropped packets monitoring

## Variables

| Variable | Description |
|----------|-------------|
| `cluster_name` | MSK cluster name |
| `broker_id` | Broker ID (multi-select) |
| `topic` | Kafka topic (multi-select) |
| `deployment_environment` | Environment filter |

## AWS MSK Metrics Reference

| Metric | Description |
|--------|-------------|
| `aws_kafka_cpu_user_average` | Broker CPU utilization |
| `aws_kafka_memory_used_average` | Broker memory usage |
| `aws_kafka_kafka_data_logs_disk_used_average` | Log storage utilization |
| `aws_kafka_bytes_in_per_sec_average` | Bytes produced per second |
| `aws_kafka_bytes_out_per_sec_average` | Bytes consumed per second |
| `aws_kafka_messages_in_per_sec_average` | Messages produced per second |
| `aws_kafka_under_replicated_partitions_average` | Under-replicated partition count |
| `aws_kafka_offline_partitions_count_average` | Offline partition count |
| `aws_kafka_burst_balance_average` | EBS burst credits remaining |

## Documentation

- [Amazon MSK Metrics](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html)
- [MSK CloudWatch Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/cloudwatch-metrics.html)
- [SigNoz AWS MSK Integration](https://signoz.io/docs/aws-monitoring/msk/)
- [Apache Kafka with AWS Distro for OpenTelemetry](https://aws.amazon.com/about-aws/whats-new/2023/04/apache-kafka-aws-distro-opentelemetry/)
