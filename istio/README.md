# Istio Service Mesh Dashboard

Monitor Istio service mesh performance using Prometheus metrics.

## Panels

| Panel | Type | Description |
|-------|------|-------------|
| Request Volume | Graph | Incoming request rate per service |
| Success Rate | Value | Percentage of non-5xx requests |
| Request Duration P50 | Graph | 50th percentile latency by service |
| Request Duration P99 | Graph | 99th percentile latency by service |
| TCP Connections Opened | Graph | TCP connection open rate per service |
| TCP Connections Closed | Graph | TCP connection close rate per service |
| Pilot xDS Pushes | Graph | Istiod config push rate by type |
| Pilot Proxy Convergence Time P99 | Graph | P99 config convergence latency |
| Envoy Proxy CPU Usage | Graph | CPU usage per istio-proxy sidecar |
| Envoy Proxy Memory Usage | Graph | Memory usage per istio-proxy sidecar |

## Variables

- `namespace` — Istio destination service namespace
- `deployment_environment` — Deployment environment
- `cluster` — Kubernetes cluster name

## Metrics Used

- `istio_requests_total` — Request counter
- `istio_request_duration_milliseconds_bucket` — Request latency histogram
- `istio_tcp_connections_opened_total` — TCP connections opened
- `istio_tcp_connections_closed_total` — TCP connections closed
- `pilot_xds_pushes` — Pilot xDS push counter
- `pilot_proxy_convergence_time_bucket` — Proxy convergence histogram
- `container_cpu_usage_seconds_total` — Container CPU (istio-proxy)
- `container_memory_working_set_bytes` — Container memory (istio-proxy)

## Query Type

PromQL
