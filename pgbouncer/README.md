# PgBouncer Dashboard

This dashboard provides detailed insights into your PgBouncer connection pooler, monitoring key metrics for client and server pools, query and transaction throughput, wait times, network traffic, prepared statements, and per-database connections.

It is built on the metrics exposed by the [prometheus-community PgBouncer exporter](https://github.com/prometheus-community/pgbouncer_exporter), scraped via the OpenTelemetry Collector Prometheus receiver.

For setup instructions and more details, please visit the [SigNoz PgBouncer Integration Documentation](https://signoz.io/docs/metrics-management/pgbouncer/).
