# AWS MSK Dashboard - OTLP

This dashboard covers Amazon MSK cluster health, broker connectivity, topic traffic, and storage pressure using CloudWatch-backed metrics ingested into SigNoz.

## Metrics Ingestion

Follow SigNoz's Amazon MSK integration guide:

- https://signoz.io/docs/aws-monitoring/msk/

AWS metric semantics and monitoring levels are documented here:

- https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html
- https://docs.aws.amazon.com/msk/latest/developerguide/cloudwatch-metrics.html

To populate all topic and broker level panels in this dashboard, enable enhanced monitoring at least at `PER_TOPIC_PER_BROKER`.

## Variables

- `{{cluster_name}}`: Amazon MSK cluster name
- `{{broker_id}}`: Broker ID within the selected cluster
- `{{topic}}`: Kafka topic within the selected cluster

## Dashboard Panels

- `ActiveControllerCount` - cluster controller health
- `GlobalPartitionCount` - total partitions across the cluster
- `OfflinePartitionsCount` - partitions currently offline
- `UnderReplicatedPartitions` - replication health indicator
- `ConnectionCount by Broker` - total active broker connections
- `ClientConnectionCount by Broker` - authenticated client connections
- `BytesInPerSec by Broker` - broker ingress throughput
- `BytesOutPerSec by Broker` - broker egress throughput
- `MessagesInPerSec by Topic` - topic ingest rate
- `PartitionCount by Topic` - partition fanout by topic
- `KafkaDataLogsDiskUsed by Broker` - broker log storage usage
- `BurstBalance by Broker` - remaining EBS burst credits

## Notes

- This dashboard assumes CloudWatch metrics are ingested into SigNoz with metric names normalized under the `aws_kafka_*` prefix, consistent with SigNoz's existing AWS dashboard templates.
- Some Amazon MSK metrics appear only after traffic becomes non-zero for the first time.
