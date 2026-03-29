# AWS MSK Cluster Monitoring Dashboard

Comprehensive monitoring for AWS MSK (Managed Streaming for Apache Kafka) clusters using Prometheus JMX exporter metrics.

## Sections

| # | Section | Covers |
|---|---------|--------|
| 1 | Broker Metrics | CPU utilization, disk usage, network bytes in/out |
| 2 | Topic Metrics | Messages/bytes produced per topic, fetch request rate |
| 3 | Partition Health | Under-replicated/offline partitions, active controller, leader elections |
| 4 | Consumer Metrics | Consumer group lag, consumer offset progress |

## Setup

### Enable Prometheus Monitoring on MSK

Enable open monitoring with Prometheus in your MSK cluster configuration:

```bash
aws kafka update-monitoring \
  --cluster-arn <CLUSTER_ARN> \
  --current-version <CURRENT_VERSION> \
  --open-monitoring '{
    "Prometheus": {
      "JmxExporter": {"EnabledInBroker": true},
      "NodeExporter": {"EnabledInBroker": true}
    }
  }'
```

### OTel Collector Configuration

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'msk-cluster'
          static_configs:
            - targets:
                - 'broker1:11001'
                - 'broker2:11001'
                - 'broker3:11001'
          metrics_path: '/metrics'
```

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `cluster` | MSK cluster job name (matches Prometheus `job` label) |
| `topic` | Kafka topic name filter |

## Key Metrics

| Metric | Description |
|--------|-------------|
| `kafka_server_BrokerTopicMetrics_MessagesInPerSec_total` | Messages produced per topic/sec |
| `kafka_server_BrokerTopicMetrics_BytesInPerSec_total` | Bytes produced per topic/sec |
| `kafka_server_BrokerTopicMetrics_BytesOutPerSec_total` | Bytes consumed per topic/sec |
| `kafka_server_ReplicaManager_UnderReplicatedPartitions` | Under-replicated partition count |
| `kafka_controller_KafkaController_OfflinePartitionsCount` | Offline partition count |
| `kafka_consumer_group_lag` | Consumer group lag per partition |

## References

- [AWS MSK Prometheus Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html)
- [Kafka JMX Metrics](https://kafka.apache.org/documentation/#monitoring)
