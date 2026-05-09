# Kafka Server Monitoring Dashboard

This dashboard provides a comprehensive view of Kafka broker and consumer metrics collected via the OpenTelemetry Kafka metrics receiver or Prometheus exporter.

## Metrics Included

- **Messages In**: Rate of messages entering the broker.
- **Bytes In/Out**: Network throughput for the Kafka cluster.
- **Consumer Group Lag**: Monitor if consumers are falling behind.
- **Active Controller**: Ensure high availability of the cluster.
- **Under Replicated Partitions**: Identify potential data loss or health issues.

## Configuration

Requires `kafka_cluster_alias` label for filtering. Ensure your OTel collector is configured with the `kafkametrics` receiver.
