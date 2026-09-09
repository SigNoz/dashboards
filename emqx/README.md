# EMQX Dashboard

This dashboard provides detailed insights into your EMQX MQTT brokers, monitoring key metrics for cluster and connection health, message throughput, message loss, subscriptions and routing, authentication and authorization, and Erlang VM runtime.

It is built on the metrics EMQX exports from inside the broker over OTLP, configured through the `opentelemetry` block in `emqx.conf`. These names are dotted and carry no `emqx` prefix, which separates them from the `emqx_*` names on the Prometheus scrape endpoint.

Scope the dashboard with the `service.name` variable, which EMQX reports as `emqx` unless you set `OTEL_SERVICE_NAME`, and break panels down by node with `service.instance.id`.

For setup instructions and more details, please visit the [SigNoz EMQX Integration Documentation](https://signoz.io/docs/integrations/opentelemetry-emqx/).
