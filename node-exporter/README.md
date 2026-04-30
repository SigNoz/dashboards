# Node Exporter Full Dashboard

This dashboard provides a comprehensive view of host metrics collected by Prometheus Node Exporter.

## Metrics Included

- **CPU Usage**: Real-time CPU utilization across all modes (excluding idle).
- **Memory Usage**: Percentage of used memory.
- **Disk Usage**: Disk space utilization for the root partition.
- **Load Average**: System load for 1m, 5m, and 15m intervals.
- **Network Traffic**: Inbound and outbound network bandwidth consumption.

## Configuration

Ensure that your `node_exporter` metrics are being scraped by SigNoz and are available in the `signoz_metrics` database. The dashboard uses the `instance` label to filter by host.
