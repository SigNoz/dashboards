# Bun and ElysiaJS Dashboard

This dashboard shows how a Bun application built with ElysiaJS handles traffic, and how the Bun runtime behaves under that load. It covers request rate, latency, errors, event loop delay, CPU, and heap memory.

It reads from the HTTP request metric and request spans of the Elysia OpenTelemetry plugin, plus the runtime and host metrics of the OpenTelemetry Node.js instrumentations.

For setup instructions, see the [SigNoz Bun and ElysiaJS OpenTelemetry guide](https://signoz.io/docs/instrumentation/opentelemetry-bun/). For the panel list and a preview, see the [dashboard template page](https://signoz.io/docs/dashboards/dashboard-templates/bun-elysia-dashboard/).
