# AWS MSK Cluster Dashboard for SigNoz

This dashboard provides comprehensive monitoring for AWS Managed Streaming for Apache Kafka (MSK) clusters using Prometheus metrics.

## Prerequisites

To use this dashboard, you must have **Open Monitoring with Prometheus** enabled on your AWS MSK cluster. You can enable this in the MSK console under the "Monitoring" tab for your cluster.

The dashboard expects metrics from:
- **JMX Exporter** (Port 11001) for Kafka-specific metrics.
- **Node Exporter** (Port 11002) for broker-level resource metrics (CPU, Memory, Disk).

## Metrics Tracked

### Cluster Health
- **Active Controller Count**: Ensures cluster stability (should be 1).
- **Offline Partitions**: Critical alert metric for partition availability.
- **Under Replicated Partitions**: Key indicator of replication lag or broker issues.

### Broker Resources
- **CPU Utilization**: Average CPU usage across brokers.
- **Memory Usage**: Freeable and used memory tracking.
- **Disk Usage**: Monitoring disk space for Kafka logs.

### Throughput
- **Messages In**: Rate of messages being produced to the cluster.
- **Network Bytes In/Out**: Overall network throughput of the MSK cluster.

### Partition & Topic Metrics
- **Leader Count**: Distribution of partition leadership across brokers.
- **Partition Count**: Total partitions managed by the cluster.

## Setup Instructions

1.  Enable **Open Monitoring** in your MSK Cluster settings.
2.  Configure your SigNoz OpenTelemetry Collector to scrape the MSK Prometheus endpoints (Ports 11001 & 11002).
3.  Import this `aws-msk-dashboard.json-` file into your SigNoz dashboard manager.
