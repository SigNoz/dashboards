# Istio Service Mesh Monitoring Dashboard

Comprehensive monitoring for Istio service mesh using Prometheus metrics scraped from Envoy sidecar proxies.

## Sections

| # | Section | Covers |
|---|---------|--------|
| 1 | General Overview | Total request rate, global error rate, p99/p95 latency |
| 2 | Traffic Management | Request distribution, HTTP response codes, retries, circuit breaker opens |
| 3 | Performance Metrics | Request/response throughput in bytes |
| 4 | TCP Traffic | TCP connections opened/closed, bytes sent |
| 5 | Control Plane (Istiod) | Pilot xDS push rate and errors |

## Setup

### Prerequisites

Istio with Prometheus integration enabled. Ensure Prometheus scrapes the Istio metrics endpoints:

```yaml
# istio-operator.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    enablePrometheusMerge: true
  values:
    telemetry:
      v2:
        prometheus:
          enabled: true
```

### SigNoz Configuration

Configure your SigNoz OpenTelemetry Collector to scrape Prometheus metrics from Istio:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'istio-mesh'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
              action: keep
              regex: 'true'
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
              action: replace
              target_label: __metrics_path__
              regex: (.+)
```

## Dashboard Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `namespace` | Kubernetes namespace filter | `.*` (all) |
| `destination_service` | Destination service name filter | `.*` (all) |

## Key Metrics Used

| Metric | Description |
|--------|-------------|
| `istio_requests_total` | Total requests counter (by service, response_code, flags) |
| `istio_request_duration_milliseconds_bucket` | Request duration histogram |
| `istio_request_bytes_sum` | Request payload bytes |
| `istio_response_bytes_sum` | Response payload bytes |
| `istio_tcp_connections_opened_total` | TCP connections opened |
| `istio_tcp_sent_bytes_total` | TCP bytes sent |
| `pilot_xds_pushes` | Pilot xDS configuration push count |
| `pilot_xds_push_errors` | Pilot xDS push error count |

## References

- [Istio Prometheus Metrics](https://istio.io/latest/docs/reference/config/metrics/)
- [Istio Observability](https://istio.io/latest/docs/concepts/observability/)
- [Grafana Istio Dashboard](https://grafana.com/grafana/dashboards/7645-istio-control-plane-dashboard/)
