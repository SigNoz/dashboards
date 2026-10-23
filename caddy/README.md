# Caddy Dashboard

This dashboard shows the health of Caddy as a web server and reverse proxy: request rate, status codes, request duration, time to first byte, errors, bandwidth, reverse proxy upstream health, and config reloads. Filter it by `service.name` to look at one Caddy service or a group of them.

The dashboard reads the `caddy_http_*`, `caddy_reverse_proxy_upstreams_healthy`, and `caddy_config_*` metrics. Caddy v2.11.3 and newer push them over OTLP when the `metrics` global option has `otlp`. Caddy counts a request once for each route it matches, so the request panels read one route, set by the `route` variable (default `tracing`).

For setup instructions, see [Monitor Caddy with OpenTelemetry](https://signoz.io/docs/integrations/opentelemetry-caddy/). For the panel list and a preview, see the [dashboard template page](https://signoz.io/docs/dashboards/dashboard-templates/caddy-dashboard/).
