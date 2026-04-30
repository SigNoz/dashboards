# AWS MSK Cluster Monitoring - Prometheus

A comprehensive SigNoz dashboard for monitoring AWS Managed Streaming for Apache Kafka (MSK) clusters using Prometheus metrics collected via the JMX exporter or AWS Distro for OpenTelemetry (ADOT).

## Prerequisites

- AWS MSK cluster with Prometheus monitoring enabled
- JMX exporter configured on MSK brokers **or** AWS ADOT collector set up for MSK
- SigNoz with Prometheus metrics ingestion enabled

## Metrics Source

Enable Prometheus monitoring on your MSK cluster in the AWS console under **Monitoring** → **Prometheus metrics**. Then configure one of:

- **JMX Exporter** (port 11001) — broker-level JVM and Kafka metrics
- **Node Exporter** (port 11002) — OS-level metrics (CPU, memory, disk, network)
- **AWS ADOT Collector** — scrapes JMX and node exporter endpoints and ships to SigNoz

Refer to the [AWS MSK Prometheus monitoring docs](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html) for setup instructions.

## Dashboard Sections

### Broker Metrics
Key health indicators for the broker cluster:
- **Active Controller Count** — should always be 1; anything else indicates a controller election issue
- **Offline Partitions Count** — should be 0; any offline partitions mean data unavailability
- **Request Handler Avg Idle %** — percentage of idle request handler threads; below 30% means the broker is under load
- **Total Log Size** — aggregate disk usage across all brokers

### Topic Metrics
Throughput data broken down by topic:
- **Messages In Per Second** — producer message rate per topic
- **Bytes In Per Second** — producer byte throughput per topic
- **Bytes Out Per Second** — consumer byte throughput per topic
- **Produce & Fetch Request Rate** — total produce and fetch request rates

### Partition Metrics
Replication and partition health:
- **Under-Replicated Partitions** — partitions that do not have enough in-sync replicas; alert if > 0
- **Total Partition Count** — total partitions across the cluster
- **Leader Count** — number of partition leaders per broker (uneven distribution indicates imbalance)
- **ISR Shrinks Per Second** — rate at which in-sync replica sets are shrinking (indicates follower lag)
- **Under-Replicated Partitions per Broker** — time-series view per broker
- **Log Size by Topic** — disk usage breakdown by topic

### Consumer & Error Metrics
Error rates and failed request tracking:
- **Failed Produce & Fetch Requests Per Second** — broken down by topic
- **Error Rate % (Produce & Fetch)** — ratio of failed to total requests; alert above 1%

### Network & Request Metrics
End-to-end request latency and throughput:
- **Network Requests Per Second by Type** — Produce, Fetch, Metadata, etc.
- **Request Total Time (ms) Mean by Type** — end-to-end latency for each request type
- **Request Handler Idle % per Broker** — per-broker thread pool utilization trend
- **Cluster-Wide Throughput (Bytes In/Out)** — aggregate network I/O for the entire cluster

## Dashboard Variables

| Variable | Description |
|---|---|
| `deployment.environment` | Filter metrics by deployment environment |
| `broker` | Filter by specific broker instance(s) |
| `topic` | Filter by specific Kafka topic(s) |

## Key Prometheus Metrics Used

```
kafka_controller_KafkaController_ActiveControllerCount
kafka_controller_KafkaController_OfflinePartitionsCount
kafka_server_KafkaRequestHandlerPool_RequestHandlerAvgIdlePercent_Mean
kafka_log_Log_Size
kafka_server_BrokerTopicMetrics_MessagesInPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_BytesInPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_BytesOutPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_TotalProduceRequestsPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_TotalFetchRequestsPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_FailedProduceRequestsPerSec_OneMinuteRate
kafka_server_BrokerTopicMetrics_FailedFetchRequestsPerSec_OneMinuteRate
kafka_server_ReplicaManager_UnderReplicatedPartitions
kafka_server_ReplicaManager_PartitionCount
kafka_server_ReplicaManager_LeaderCount
kafka_server_ReplicaManager_IsrShrinksPerSec_OneMinuteRate
kafka_network_RequestMetrics_RequestsPerSec_OneMinuteRate
kafka_network_RequestMetrics_TotalTimeMs_Mean
```

## Import Instructions

1. Open SigNoz → **Dashboards** → **New Dashboard** → **Import JSON**
2. Upload `aws-msk-prometheus-v2.json`
3. Select the appropriate `deployment.environment` from the variable dropdown
4. Optionally filter by broker and topic variables
