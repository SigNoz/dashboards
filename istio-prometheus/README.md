# Istio Service Mesh Dashboard - Prometheus

Monitor an Istio service mesh in SigNoz using the standard Istio Prometheus telemetry exposed by every Envoy sidecar (`istio_requests_total`, `istio_request_duration_milliseconds`, `istio_request_bytes`, `istio_response_bytes`, `istio_tcp_*_total`).

The dashboard ships 17 panels across five sections — General Overview, Traffic Management, Performance, Error Metrics, and TCP Data Plane — and three filter variables for namespace / workload / source selection.

## Metrics Ingestion

Istio's data plane (Envoy sidecar) exposes Prometheus metrics on each pod at `:15090/stats/prometheus`. The control plane (`istiod`) exposes its metrics on `:15014/metrics`. Scrape both with the OpenTelemetry Collector Prometheus receiver and forward to SigNoz.

### Option A — Annotate-and-scrape (recommended for in-cluster sidecars)

Istio injection adds the `prometheus.io/scrape: "true"`, `prometheus.io/path: "/stats/prometheus"`, and `prometheus.io/port: "15090"` annotations to every meshed pod. The Prometheus receiver can pick these up via Kubernetes service discovery.

Add this job to the `prometheus` receiver in your `otel-config.yaml`:

```yaml
receivers:
  prometheus:
    config:
      global:
        scrape_interval: 30s
      scrape_configs:
        # Istio sidecars (Envoy)
        - job_name: 'envoy-stats'
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_container_port_name]
              action: keep
              regex: '.*-envoy-prom'
            - source_labels: [__meta_kubernetes_pod_label_app]
              action: replace
              target_label: app
            - source_labels: [__meta_kubernetes_namespace]
              action: replace
              target_label: namespace

        # Istio control plane (istiod)
        - job_name: 'istiod'
          kubernetes_sd_configs:
            - role: endpoints
              namespaces:
                names:
                  - istio-system
          relabel_configs:
            - source_labels: [__meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
              action: keep
              regex: 'istiod;http-monitoring'
```

### Option B — Static targets

If you do not run the OpenTelemetry Collector inside the cluster, port-forward (or expose) the proxies and scrape statically:

```yaml
receivers:
  prometheus:
    config:
      global:
        scrape_interval: 30s
      scrape_configs:
        - job_name: istio-mesh
          metrics_path: /stats/prometheus
          static_configs:
            - targets: ['<pod-ip>:15090']
```

### Pipeline

Wire the `prometheus` receiver into your metrics pipeline alongside the SigNoz exporter:

```yaml
service:
  pipelines:
    metrics:
      receivers: [otlp, prometheus]
      processors: [batch]
      exporters: [otlp/signoz]
```

The dashboard expects the metrics under their stock Istio names — no metric renaming is required at the collector. The standard label set (`reporter`, `destination_workload`, `destination_workload_namespace`, `source_workload`, `response_code`, `response_flags`, `request_protocol`, `connection_security_policy`) is preserved by Istio's default telemetry config.

### Reporter filter — why every panel pins `reporter=destination`

Istio's telemetry pipeline emits the same request twice — once from the source proxy (`reporter=source`) and once from the destination proxy (`reporter=destination`). Counting both would double every count. All counter and histogram queries in this dashboard pin `reporter=destination` so totals match reality. This matches the official Istio recommendation for monitoring server-side traffic.

If you want to monitor outgoing traffic from a specific source workload's perspective instead, edit the panel's filter and switch to `reporter=source`.

## Variables

| Variable | Description |
|---|---|
| `{{destination_workload_namespace}}` | Filter by destination workload namespace. Multi-select, includes "ALL". |
| `{{destination_workload}}` | Filter by destination workload. Multi-select, cascades from namespace. |
| `{{source_workload}}` | Filter by source workload. Multi-select, useful for service-to-service drill-down. |

## Dashboard Panels

### General Overview (4 value tiles)

| Panel | Metric / Computation |
|---|---|
| **Total Request Rate** | `sum_rate(istio_requests_total)` |
| **Active Destination Workloads** | `sum_rate(istio_requests_total)` grouped by `destination_workload`, merged active count |
| **Average Request Latency** | Formula `A/B` where A = `sum_rate(istio_request_duration_milliseconds_sum)`, B = `sum_rate(istio_request_duration_milliseconds_count)` (repo precedent: `apm/apm-metrics.json` "Database Calls Avg Duration") |
| **Error Rate (5xx %)** | Formula `(A/B)*100` where A = 5xx-only request rate, B = total request rate |

### Traffic Management

| Panel | Metric |
|---|---|
| **Request Rate by Destination Workload** | `istio_requests_total` grouped by `destination_workload` |
| **Request Rate by Response Code** | `istio_requests_total` grouped by `response_code` (stacked) |
| **Request Protocol Distribution** | `istio_requests_total` grouped by `request_protocol` (stacked) |
| **Connection Security Policy (mTLS coverage)** | `istio_requests_total` grouped by `connection_security_policy` (stacked) |

### Performance

| Panel | Metric |
|---|---|
| **Average Request Latency Over Time** | `A/B` over `istio_request_duration_milliseconds_{sum,count}` (mesh-wide) |
| **Average Latency by Destination Workload** | Same formula, grouped by `destination_workload` |
| **Throughput by Destination Workload** | `istio_requests_total` rate grouped by `destination_workload` (stacked) |
| **Average Request / Response Body Sizes** | Two formulas: `A/B` for request bytes, `C/D` for response bytes |

> **Note on percentile latency.** This first version reports averages (rate-of-sum / rate-of-count) rather than p50/p95/p99, because SigNoz Query Builder's `Histogram + p99` aggregator pattern is established for traces-source metrics, not for Prometheus-source histograms in this repo. An average latency panel is the conservative choice that is guaranteed to render against any Prometheus histogram. Future versions can extend with bucket-based percentile panels once a Prometheus-source p99 example is established in the repo.

### Error Metrics

| Panel | Metric |
|---|---|
| **HTTP Error Rates (4xx / 5xx)** | `istio_requests_total` filtered to 4xx/5xx code list, grouped by `response_code` (stacked) |
| **Failed Requests by Destination Workload (5xx)** | 5xx-only rate grouped by `destination_workload` |
| **Envoy Response Flags** | `istio_requests_total` grouped by `response_flags` (excluding `-`). Surfaces UH/UF/NR/UR proxy events. |

> **Note on filter syntax.** SigNoz Query Builder filters use explicit lists (`op: in`) rather than range comparisons because `response_code` is a string-typed Prometheus label. The 4xx and 5xx code lists are enumerated explicitly inside each affected panel.

### TCP Data Plane

| Panel | Metric |
|---|---|
| **TCP Connection Rate (Opened / Closed)** | Rate of `istio_tcp_connections_opened_total` and `istio_tcp_connections_closed_total` |
| **TCP Throughput (Sent / Received)** | Rate of `istio_tcp_sent_bytes_total` and `istio_tcp_received_bytes_total` |

## References

- [Istio Standard Metrics](https://istio.io/latest/docs/reference/config/metrics/) — canonical list of mesh metrics and their labels.
- [Istio Observability — Querying Metrics from Prometheus](https://istio.io/latest/docs/tasks/observability/metrics/querying-metrics/) — scrape configuration guidance.
- [SigNoz Prometheus Receiver setup](https://signoz.io/docs/userguide/send-metrics/) — wiring the OpenTelemetry Collector Prometheus receiver into a SigNoz pipeline.
