# Istio Service Mesh Dashboard for SigNoz

SigNoz dashboard for monitoring Istio service mesh using Prometheus metrics from Envoy sidecars and the Istiod control plane.

## Prerequisites

- Istio installed with default telemetry (Envoy sidecar injection enabled)
- SigNoz with OpenTelemetry Collector configured with a Prometheus receiver
- Istio metrics exposed on the standard Envoy stats port (15090)

## Setup: OTel Collector Prometheus Receiver

Add the following to your OpenTelemetry Collector configuration to scrape Istio metrics:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        # Scrape Envoy sidecar metrics from all mesh pods
        - job_name: 'istio-mesh'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
              action: keep
              regex: 'true'
            - source_labels: [__meta_kubernetes_pod_annotation_sidecar_istio_io_status]
              action: keep
              regex: '.+'
            - source_labels: [__address__]
              action: replace
              regex: '([^:]+)(?::\d+)?'
              replacement: '${1}:15090'
              target_label: __address__
            - action: labeldrop
              regex: '__meta_kubernetes_pod_label_(.+)'
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: 'istio_.*'
              action: keep

        # Scrape Istiod control plane metrics
        - job_name: 'istiod'
          kubernetes_sd_configs:
            - role: pod
              namespaces:
                names: ['istio-system']
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_app]
              action: keep
              regex: 'istiod'
            - source_labels: [__address__]
              action: replace
              regex: '([^:]+)(?::\d+)?'
              replacement: '${1}:15014'
              target_label: __address__

exporters:
  otlp:
    endpoint: "<signoz-otel-collector>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Enabling Istio Metrics

Istio emits Prometheus metrics by default. Verify with:

```bash
# Check sidecar stats
kubectl exec <pod-with-sidecar> -c istio-proxy -- curl -s localhost:15090/stats/prometheus | head -50

# Check Istiod metrics
kubectl -n istio-system port-forward svc/istiod 15014:15014
curl -s localhost:15014/metrics | grep pilot_
```

If metrics are missing, ensure the Istio `Telemetry` API is configured:

```yaml
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
```

## Importing the Dashboard

1. Open SigNoz UI
2. Go to **Dashboards** > **New Dashboard** > **Import JSON**
3. Upload or paste the contents of `istio-prometheus-v1.json`
4. Save

## Variables

| Variable | Description | Source Metric |
|---|---|---|
| `namespace` | Kubernetes namespace filter. Multi-select, defaults to all. | `istio_requests_total` label `namespace` |
| `destination_service` | Target service filter. Multi-select, defaults to all. | `istio_requests_total` label `destination_service` |
| `deployment_environment` | Environment tag from OTel resource attributes (if present). | `istio_requests_total` label `deployment.environment` |

## Panel Reference

### General Overview

| Panel | Type | Metric | Description |
|---|---|---|---|
| Total Requests | value | `istio_requests_total` | Aggregate request count across the mesh |
| Request Rate by Service | graph | `istio_requests_total` sum_rate | Requests/sec grouped by `destination_service` |
| Average Latency | graph | `istio_request_duration_milliseconds_sum` / `_count` | Mean latency via formula (duration sum rate / count rate) |
| Error Rate % | graph | `istio_requests_total` (5xx / total) | Percentage of 5xx responses using formula `A*100/B` |

### Traffic Management

| Panel | Type | Metric | Description |
|---|---|---|---|
| Request Distribution by Service | graph (stacked) | `istio_requests_total` sum_rate | Traffic share per service |
| Request Distribution by Response Code | graph (stacked) | `istio_requests_total` sum_rate | Traffic breakdown by HTTP status code |
| TCP Connections Opened | graph | `istio_tcp_connections_opened_total` sum_rate | Rate of new TCP connections |

### Performance Metrics

| Panel | Type | Metric | Description |
|---|---|---|---|
| Latency P50 | graph | `istio_request_duration_milliseconds` p50 | Median request latency |
| Latency P95 | graph | `istio_request_duration_milliseconds` p95 | 95th percentile latency |
| Latency P99 | graph | `istio_request_duration_milliseconds` p99 | 99th percentile (tail) latency |
| Throughput | graph | `istio_requests_total` sum_rate | Total requests/sec across the mesh |

### Error Metrics

| Panel | Type | Metric | Description |
|---|---|---|---|
| HTTP 5xx Error Rate by Service | graph | `istio_requests_total` (response_code 5xx) | Server error rate per destination service |
| HTTP 4xx Rate | graph | `istio_requests_total` (response_code 4xx) | Client error rate |
| gRPC Error Rate | graph | `istio_requests_total` (grpc_response_status != 0, protocol=grpc) | gRPC-specific error rate |

### Control Plane

| Panel | Type | Metric | Description |
|---|---|---|---|
| Connected Proxies | value | `pilot_xds` (Gauge, last) | Number of Envoy proxies connected to Istiod |
| Config Push Rate by Type | graph (stacked) | `pilot_xds_pushes` sum_rate | xDS push rate grouped by config type (CDS, EDS, LDS, RDS) |
| Certificate Signing Requests | graph | `citadel_server_csr_count` sum_rate | Rate of mTLS certificate requests |

## Metrics Reference

| Metric | Type | Source |
|---|---|---|
| `istio_requests_total` | Counter (Sum) | Envoy sidecar |
| `istio_request_duration_milliseconds` | Histogram | Envoy sidecar |
| `istio_request_bytes` | Histogram | Envoy sidecar |
| `istio_response_bytes` | Histogram | Envoy sidecar |
| `istio_tcp_connections_opened_total` | Counter (Sum) | Envoy sidecar |
| `istio_tcp_connections_closed_total` | Counter (Sum) | Envoy sidecar |
| `istio_tcp_sent_bytes_total` | Counter (Sum) | Envoy sidecar |
| `istio_tcp_received_bytes_total` | Counter (Sum) | Envoy sidecar |
| `pilot_xds_pushes` | Counter (Sum) | Istiod |
| `pilot_xds` | Gauge | Istiod |
| `pilot_proxy_convergence_time` | Histogram | Istiod |
| `citadel_server_csr_count` | Counter (Sum) | Istiod (Citadel) |
| `envoy_cluster_upstream_cx_active` | Gauge | Envoy sidecar |
