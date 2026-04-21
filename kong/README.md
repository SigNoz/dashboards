# Kong Gateway Monitoring Dashboard — Prometheus

## Details

This dashboard provides visibility into a Kong Gateway deployment using metrics exposed by the [Kong Prometheus plugin](https://docs.konghq.com/hub/kong-inc/prometheus/). It covers request throughput, latency percentiles (request, upstream and Kong processing time), status code distribution, bandwidth, worker connections, Lua VM memory and datastore health.

The dashboard is intended for Kong 3.x with the Prometheus plugin enabled. Metrics are scraped from Kong's `/metrics` endpoint by the SigNoz OpenTelemetry Collector's `prometheus` receiver and stored as metrics in SigNoz.

## Metrics ingestion

Enable the Prometheus plugin on your Kong Gateway globally (or per service/route):

```bash
curl -X POST http://localhost:8001/plugins \
  --data "name=prometheus" \
  --data "config.per_consumer=false" \
  --data "config.status_code_metrics=true" \
  --data "config.latency_metrics=true" \
  --data "config.bandwidth_metrics=true" \
  --data "config.upstream_health_metrics=true"
```

Then point the SigNoz OTel Collector at Kong's metrics endpoint (default `:8100/metrics` on the Admin API listener):

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: kong
          scrape_interval: 30s
          static_configs:
            - targets: ['kong:8100']

service:
  pipelines:
    metrics/kong:
      receivers: [prometheus]
      exporters: [clickhousemetricswrite]
```

## Variables

- `$service` — Kong service name (multi-select). Populated from distinct `service` label values of `kong_http_requests_total` during the last 5 minutes.

## Dashboard panels

### Overview (stat panels)

**Total Requests** — Cumulative HTTP requests handled by Kong.
`sum(kong_http_requests_total{service=~"$service"})`

**Request Rate** — Current request rate in req/s.
`sum(rate(kong_http_requests_total{service=~"$service"}[5m]))`

**Active Connections** — Nginx worker connections currently active.
`sum(kong_nginx_connections_total{state="active"})`

**5xx Error Rate** — Server-side error rate in req/s.
`sum(rate(kong_http_requests_total{code=~"5..", service=~"$service"}[5m]))`

### Request rate and status codes

**Request Rate by Service** — Per-service request rate.
`sum by (service) (rate(kong_http_requests_total{service=~"$service"}[5m]))`

**Response Status Code Distribution** — Requests grouped by response code.
`sum by (code) (rate(kong_http_requests_total{service=~"$service"}[5m]))`

### Latency

**Request Latency Percentiles** — End-to-end latency as seen by Kong.

- P50: `histogram_quantile(0.50, sum by (le) (rate(kong_request_latency_ms_bucket{service=~"$service"}[5m])))`
- P95: `histogram_quantile(0.95, sum by (le) (rate(kong_request_latency_ms_bucket{service=~"$service"}[5m])))`
- P99: `histogram_quantile(0.99, sum by (le) (rate(kong_request_latency_ms_bucket{service=~"$service"}[5m])))`

**Upstream Latency Percentiles** — Time spent waiting on upstream services.
Uses `kong_upstream_latency_ms_bucket` with the same `histogram_quantile` pattern.

**Kong Processing Latency** — Time spent inside Kong (plugins, routing), excluding upstream wait.
Uses `kong_kong_latency_ms_bucket`.

### Errors

**4xx vs 5xx Error Rate** — Client vs server error rates plotted together.

- 4xx: `sum(rate(kong_http_requests_total{code=~"4..", service=~"$service"}[5m]))`
- 5xx: `sum(rate(kong_http_requests_total{code=~"5..", service=~"$service"}[5m]))`

**Top 5 Services by 5xx Errors** — Services producing the most server errors.
`topk(5, sum by (service) (rate(kong_http_requests_total{code=~"5..", service=~"$service"}[5m])))`

### Bandwidth

**Ingress Bandwidth** — Bytes received by Kong from clients.
`sum by (service) (rate(kong_bandwidth_bytes{type="ingress", service=~"$service"}[5m]))`

**Egress Bandwidth** — Bytes sent by Kong to clients.
`sum by (service) (rate(kong_bandwidth_bytes{type="egress", service=~"$service"}[5m]))`

### Connections and resources

**Nginx Connections by State** — Worker connections grouped by state (active, waiting, reading, writing).
`sum by (state) (kong_nginx_connections_total)`

**Lua VM Memory by Node** — Memory used by Kong's Lua VMs per node.
`sum by (node_id) (kong_memory_workers_lua_vms_bytes)`

**Datastore Reachability** — 1 when the configured datastore (PostgreSQL or Cassandra) is reachable, 0 otherwise.
`kong_datastore_reachable`

## Notes on Kong metric names

The dashboard targets Kong 3.x with the default Prometheus plugin. If your Kong version exposes latency as a single `kong_latency_ms_bucket` metric with a `type` label (request / kong / upstream) instead of three separate metrics, adjust the latency queries accordingly:

```promql
# Single-metric form (some Kong versions)
histogram_quantile(0.99,
  sum by (le) (rate(kong_latency_ms_bucket{type="request", service=~"$service"}[5m])))
```
