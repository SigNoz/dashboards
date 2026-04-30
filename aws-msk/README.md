# AWS MSK Cluster Dashboard - CloudWatch

Monitoring dashboard for Amazon Managed Streaming for Apache Kafka (MSK) using CloudWatch metrics ingested via the SigNoz AWS integration.

## Metrics Ingestion

This dashboard uses CloudWatch metrics from the `AWS/Kafka` namespace. Metrics are collected automatically when you enable the [SigNoz AWS integration](https://signoz.io/docs/integrations/aws/) and configure a CloudWatch Metric Stream that includes the `AWS/Kafka` namespace.

### Prerequisites

- An active AWS MSK cluster
- SigNoz AWS integration configured with CloudWatch Metric Streams
- The `AWS/Kafka` namespace included in your metric stream filter

### Setup

1. Follow the [SigNoz AWS integration guide](https://signoz.io/docs/integrations/aws/) to connect your AWS account
2. Ensure your CloudWatch Metric Stream includes the `AWS/Kafka` namespace
3. Import this dashboard JSON into SigNoz

### Alternative: OpenTelemetry Collector with CloudWatch Receiver

If you prefer using the OpenTelemetry Collector directly, configure the [`awscloudwatch` receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/awscloudwatchmetricsreceiver):

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    poll_interval: 300s
    metrics:
      named:
        AWS/Kafka:
          - metric_name: CpuUser
            statistics: [Maximum]
          - metric_name: CpuSystem
            statistics: [Maximum]
          - metric_name: MemoryUsed
            statistics: [Maximum]
          - metric_name: MemoryFree
            statistics: [Maximum]
          - metric_name: KafkaDataLogsDiskUsed
            statistics: [Maximum]
          - metric_name: BytesInPerSec
            statistics: [Sum]
          - metric_name: BytesOutPerSec
            statistics: [Sum]
          - metric_name: MessagesInPerSec
            statistics: [Sum]
          - metric_name: UnderReplicatedPartitions
            statistics: [Maximum]
          - metric_name: UnderMinIsrPartitionCount
            statistics: [Maximum]
          - metric_name: PartitionCount
            statistics: [Maximum]
          - metric_name: GlobalPartitionCount
            statistics: [Maximum]
          - metric_name: MaxOffsetLag
            statistics: [Maximum]
          - metric_name: EstimatedMaxTimeLag
            statistics: [Maximum]
          - metric_name: BurstBalance
            statistics: [Minimum]
          - metric_name: ActiveControllerCount
            statistics: [Maximum]
          - metric_name: OfflinePartitionsCount
            statistics: [Maximum]
          - metric_name: ConnectionCount
            statistics: [Maximum]
          - metric_name: NetworkRxPackets
            statistics: [Sum]
          - metric_name: NetworkTxPackets
            statistics: [Sum]

processors:
  batch:
    send_batch_size: 1000
    timeout: 10s
  resource/env:
    attributes:
      - key: deployment.environment
        value: production
        action: upsert

exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [awscloudwatch]
      processors: [resource/env, batch]
      exporters: [otlp]
```

## Variables

- `{{deployment_environment}}`: Deployment environment (e.g., production, staging). Filters all panels to a specific environment.
- `{{broker_id}}`: MSK Broker ID. Supports multi-select to compare brokers side-by-side. Use "ALL" to view all brokers.
- `{{topic}}`: Kafka topic name. Filters topic-level panels. Supports multi-select.
- `{{consumer_group}}`: Consumer group name. Filters consumer lag panels. Supports multi-select.

## Dashboard Panels

### Broker Metrics

Monitors the health and resource utilization of individual MSK brokers.

- **Broker CPU Usage** — User and system CPU utilization per broker, displayed as a stacked graph. High sustained CPU (>80%) indicates the broker may need scaling.
  - Metrics: `aws_Kafka_CpuUser_max`, `aws_Kafka_CpuSystem_max`

- **Broker Memory Usage** — Memory consumed by each broker in bytes.
  - Metric: `aws_Kafka_MemoryUsed_max`

- **Network Packets In/Out** — Packet counts for inbound and outbound network traffic per broker.
  - Metrics: `aws_Kafka_NetworkRxPackets_sum`, `aws_Kafka_NetworkTxPackets_sum`

- **Disk Usage** — Percentage of disk space used for Kafka data logs. Alert if this approaches 85%.
  - Metric: `aws_Kafka_KafkaDataLogsDiskUsed_max`

- **Broker Network Throughput (Kafka)** — Bytes per second flowing through the Kafka protocol on each broker (producer/consumer traffic).
  - Metrics: `aws_Kafka_BytesInPerSec_sum`, `aws_Kafka_BytesOutPerSec_sum`

- **Broker Memory Free** — Free memory available on each broker in bytes.
  - Metric: `aws_Kafka_MemoryFree_max`

### Topic Metrics

Tracks throughput at the topic level to identify hot topics or throughput imbalances.

- **Messages In Per Second** — Rate of messages produced to each topic.
  - Metric: `aws_Kafka_MessagesInPerSec_sum`

- **Bytes In Per Second** — Data volume produced to each topic per second.
  - Metric: `aws_Kafka_BytesInPerSec_sum`

- **Bytes Out Per Second** — Data volume consumed from each topic per second.
  - Metric: `aws_Kafka_BytesOutPerSec_sum`

### Partition Metrics

Monitors partition health across the cluster. Under-replicated or under-min-ISR partitions indicate potential data durability risks.

- **Under-Replicated Partitions** — Partitions where one or more replicas are not in sync. Non-zero values require investigation.
  - Metric: `aws_Kafka_UnderReplicatedPartitions_max`

- **Under Min ISR Partition Count** — Partitions below the minimum in-sync replica threshold. This is a critical alert condition.
  - Metric: `aws_Kafka_UnderMinIsrPartitionCount_max`

- **Partition Count** — Total partitions per broker. Uneven distribution indicates a need for partition reassignment.
  - Metric: `aws_Kafka_PartitionCount_max`

- **Global Partition Count** — Total partitions across the entire cluster.
  - Metric: `aws_Kafka_GlobalPartitionCount_max`

### Consumer Metrics

Tracks consumer group lag to detect slow or stalled consumers.

- **Consumer Lag — Max Offset Lag** — Maximum offset lag per consumer group in message count. Grouped by consumer group for per-group visibility.
  - Metric: `aws_Kafka_MaxOffsetLag_max`

- **Consumer Lag — Estimated Time** — Estimated time (seconds) for each consumer group to catch up. Grouped by consumer group.
  - Metric: `aws_Kafka_EstimatedMaxTimeLag_max`

### AWS Metrics / Cluster Health

Cluster-wide health indicators and AWS-specific resource metrics.

- **Burst Balance** — Remaining CPU burst credits for burstable broker instance types. Approaching 0% means the broker will be throttled.
  - Metric: `aws_Kafka_BurstBalance_min`

- **Active Controller Count** — Number of active controllers in the cluster. Should always be exactly 1.
  - Metric: `aws_Kafka_ActiveControllerCount_max`

- **Offline Partitions Count** — Partitions with no active leader. Should always be 0. Any non-zero value is a critical issue.
  - Metric: `aws_Kafka_OfflinePartitionsCount_max`

- **Connection Count** — Total active connections per broker.
  - Metric: `aws_Kafka_ConnectionCount_max`

## Reference

- [AWS MSK CloudWatch Metrics](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html)
- [AWS Distro for OpenTelemetry with MSK](https://aws.amazon.com/about-aws/whats-new/2023/04/apache-kafka-aws-distro-opentelemetry/)
- [Grafana MSK Dashboard (reference)](https://grafana.com/grafana/dashboards/12009-aws-kafka-cluster/)
