# CloudNativePG Dashboard

This dashboard provides detailed insights into your CloudNativePG clusters, monitoring key metrics for cluster health, connections, throughput, cache, replication, WAL and archiving, checkpoints, and storage.

It is built entirely on the native `cnpg_*` metrics that each CloudNativePG instance exposes on its metrics endpoint (`:9187/metrics`), scraped via the OpenTelemetry Collector Prometheus receiver.

For setup instructions and more details, please visit the [SigNoz CloudNativePG Integration Documentation](https://signoz.io/docs/metrics-management/cloudnative-pg/).
