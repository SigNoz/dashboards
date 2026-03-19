# AWS MSK Cluster Dashboard - OTLP

Comprehensive monitoring dashboard for AWS Managed Streaming for Apache Kafka (MSK) clusters using CloudWatch metrics collected via OpenTelemetry.

## Metrics Ingestion

This dashboard uses AWS CloudWatch metrics collected via the OpenTelemetry Collector's `awscloudwatch` receiver (or the AWS CloudWatch exporter). Metrics follow the `aws_kafka_*` naming convention from the `AWS/Kafka` CloudWatch namespace.

### OpenTelemetry Collector Configuration

Add the following to your `otel-collector-config.yaml`:

```yaml
receivers:
  awscloudwatch:
    region: us-east-1
    poll_interval: 5m
    metrics:
      named:
        AWS/Kafka:
          - metric_name: CpuUser
          - metric_name: CpuSystem
          - metric_name: MemoryUsed
          - metric_name: MemoryFree
          - metric_name: KafkaDataLogsDiskUsed
          - metric_name: BytesInPerSec
          - metric_name: BytesOutPerSec
          - metric_name: MessagesInPerSec
          - metric_name: ProduceTotalTimeMsMean
          - metric_name: UnderReplicatedPartitions
          - metric_name: OfflinePartitionsCount
          - metric_name: ActiveControllerCount
          - metric_name: PartitionCount
          - metric_name: LeaderCount
          - metric_name: SumOffsetLag
          - metric_name: EstimatedMaxTimeLag
          - metric_name: BurstBalance
          - metric_name: CpuCreditUsage
          - metric_name: TrafficShaping
          - metric_name: ConnectionCount
          - metric_name: HeapMemoryAfterGC
          - metric_name: NetworkRxPackets
          - metric_name: NetworkTxPackets
          - metric_name: VolumeReadBytes
          - metric_name: VolumeWriteBytes

exporters:
  otlp:
    endpoint: "<signoz-otel-collector-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [awscloudwatch]
      exporters: [otlp]
```

## Variables

- `{{cluster_name}}`: MSK cluster name
- `{{broker_id}}`: Broker ID (multi-select)
- `{{deployment.environment}}`: Deployment environment

## Dashboard Panels

### Section: Broker Metrics
- **Broker CPU Usage (User)** - CPU percentage in user space per broker (`aws_kafka_cpu_user_average`)
- **Broker CPU Usage (System)** - CPU percentage in kernel space per broker (`aws_kafka_cpu_system_average`)
- **Broker Memory Usage** - Memory in use (bytes) per broker (`aws_kafka_memory_used_average`)
- **Broker Memory Free** - Free memory (bytes) per broker (`aws_kafka_memory_free_average`)
- **Broker Disk Usage (Data Logs)** - Percentage of disk used for data logs (`aws_kafka_kafka_data_logs_disk_used_average`)
- **Broker Disk Throughput** - Read/write bytes per broker (`aws_kafka_volume_read_bytes_sum`, `aws_kafka_volume_write_bytes_sum`)
- **Network Traffic In (Packets)** - Network packets received per broker (`aws_kafka_network_rx_packets_sum`)
- **Network Traffic Out (Packets)** - Network packets transmitted per broker (`aws_kafka_network_tx_packets_sum`)

### Section: Topic Metrics
- **Bytes In Per Second** - Bytes received from producers per broker (`aws_kafka_bytes_in_per_sec_average`)
- **Bytes Out Per Second** - Bytes sent to consumers per broker (`aws_kafka_bytes_out_per_sec_average`)
- **Messages In Per Second** - Incoming messages per second per broker (`aws_kafka_messages_in_per_sec_average`)
- **Produce Total Time (Mean)** - Mean produce latency in milliseconds (`aws_kafka_produce_total_time_ms_mean_average`)

### Section: Partition Metrics
- **Under-Replicated Partitions** - Count of under-replicated partitions (`aws_kafka_under_replicated_partitions_average`)
- **Offline Partitions Count** - Total offline partitions (`aws_kafka_offline_partitions_count_average`)
- **Active Controller Count** - Number of active controllers (`aws_kafka_active_controller_count_average`)
- **Partition Count** - Total partitions per broker including replicas (`aws_kafka_partition_count_average`)
- **Leader Count** - Partition leaders per broker (`aws_kafka_leader_count_average`)

### Section: Consumer Metrics
- **Consumer Lag (Sum Offset Lag)** - Aggregated offset lag by consumer group and topic (`aws_kafka_sum_offset_lag_average`)
- **Estimated Max Time Lag** - Time estimate to drain max offset lag (`aws_kafka_estimated_max_time_lag_average`)

### Section: AWS Metrics (CloudWatch Integration)
- **Burst Balance** - EBS burst credit balance per broker (`aws_kafka_burst_balance_average`)
- **CPU Credit Usage** - CPU credits spent (burstable instances) (`aws_kafka_cpu_credit_usage_average`)
- **Traffic Shaping** - Packets shaped due to network limits (`aws_kafka_traffic_shaping_sum`)
- **Connection Count** - Total active connections per broker (`aws_kafka_connection_count_average`)
- **Heap Memory After GC** - JVM heap usage post-GC per broker (`aws_kafka_heap_memory_after_gc_average`)
