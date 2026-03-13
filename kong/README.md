# Kong Gateway Dashboard

Monitors Kong API Gateway metrics including requests, latency, errors, bandwidth, connections, and upstream health.

## Prerequisites

- Kong with the [Prometheus plugin](https://docs.konghq.com/hub/kong-inc/prometheus/) enabled
- Prometheus scraping Kong metrics endpoint

## Metrics Used

Kong Prometheus plugin metrics: `kong_http_requests_total`, `kong_latency_ms_*`, `kong_bandwidth_bytes`, `kong_connections_*`, `kong_upstream_target_health`, `kong_memory_workers_lua_vms_bytes`, `kong_datastore_reachable`
