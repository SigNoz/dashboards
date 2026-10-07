# Neon Postgres Dashboard

This dashboard shows the health of Neon Postgres projects. It covers connections, database activity, the Local File Cache, PgBouncer connection pooling, read replica lag, and compute CPU and memory.

It reads the `neon_*` and `host_*` metrics that Neon exports through its built-in OpenTelemetry integration, available on the Neon Scale plan.

For setup instructions, see the [SigNoz Neon OpenTelemetry integration guide](https://signoz.io/docs/integrations/opentelemetry-neondb/). For the panel list and a preview, see the [dashboard template page](https://signoz.io/docs/dashboards/dashboard-templates/neon-dashboard/).
