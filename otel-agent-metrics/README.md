# OpenTelemetry Collector Metrics Dashboard

This dashboard monitors the health and performance of the OpenTelemetry Collector (Agent/Gateway).

## Metrics Included

- **CPU/Memory**: Resource consumption of the collector process.
- **Span Throughput**: Rate of accepted and sent spans across receivers and exporters.
- **Data Loss**: Monitor dropped spans to identify bottlenecks or configuration issues.
- **Uptime**: Ensure the collector is running and stable.

## Configuration

The dashboard uses the `instance` label to filter by collector instance. Ensure the collector is configured to export its own internal metrics (usually via the `prometheus` exporter on a specific port).
