# Istio Service Mesh Dashboard - Prometheus

SigNoz dashboard for monitoring Istio service mesh traffic, latency, error rates, and control plane (Istiod) health using Prometheus metrics.

## Prerequisites

- Kubernetes cluster with Istio installed (v1.13+)
- Istio telemetry v2 enabled (default since Istio 1.7)
- SigNoz with Prometheus remote write configured, or OpenTelemetry Collector forwarding Prometheus metrics to SigNoz

## Metrics Ingestion

Istio exposes Prometheus metrics from the Envoy sidecar proxies and Istiod. To forward them to SigNoz, use the OpenTelemetry Collector with the `prometheus` receiver pointing at the Istio Prometheus instance, or scrape the sidecars directly.

### Option 1: Scrape Istio's Prometheus via OTel Collector

Deploy an OTel Collector that scrapes the existing Istio Prometheus and forwards to SigNoz:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: istio-system
data:
  config.yaml: |
    receivers:
      prometheus:
        config:
          scrape_configs:
            - job_name: 'istio-mesh'
              kubernetes_sd_configs:
                - role: pod
                  namespaces:
                    names: []
              relabel_configs:
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
                  action: keep
                  regex: 'true'
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
                  action: replace
                  target_label: __metrics_path__
                  regex: (.+)
                - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
                  action: replace
                  regex: ([^:]+)(?::\d+)?;(\d+)
                  replacement: $1:$2
                  target_label: __address__
            - job_name: 'istiod'
              kubernetes_sd_configs:
                - role: endpoints
                  namespaces:
                    names:
                      - istio-system
              relabel_configs:
                - source_labels: [__meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
                  action: keep
                  regex: istiod;http-monitoring

    processors:
      batch:
        timeout: 10s
        send_batch_size: 1024

    exporters:
      otlp:
        endpoint: "ingest.<region>.signoz.cloud:443"
        tls:
          insecure: false
        headers:
          signoz-ingestion-key: "<your-ingestion-key>"

    service:
      pipelines:
        metrics:
          receivers: [prometheus]
          processors: [batch]
          exporters: [otlp]
```

Replace:
- `<region>`: Your SigNoz Cloud [region](https://signoz.io/docs/ingestion/signoz-cloud/overview/#endpoint)
- `<your-ingestion-key>`: Your [ingestion key](https://signoz.io/docs/ingestion/signoz-cloud/keys/)

### Option 2: Prometheus Remote Write to SigNoz

Configure your existing Istio Prometheus to remote-write to SigNoz:

```yaml
# In your Prometheus configuration (prometheus.yml)
remote_write:
  - url: "https://ingest.<region>.signoz.cloud/api/prometheus/remote/write"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"
    write_relabel_configs:
      - source_labels: [__name__]
        regex: "istio_.*|pilot_.*"
        action: keep
```

## Variables

| Variable | Description |
|---|---|
| `$namespace` | Kubernetes namespace to filter by (supports multi-select) |
| `$destination_service` | Destination service name to filter by (supports multi-select) |

## Dashboard Sections

### Traffic Overview
- **Incoming Request Rate (RPS)** — `istio_requests_total` rate by destination service
- **5xx Error Rate** — Ratio of 5xx responses to total requests
- **Average Request Size** — Mean request body size in bytes
- **Average Response Size** — Mean response body size in bytes

### Latency
- **Request Latency p50** — Median request latency via `istio_request_duration_milliseconds_bucket`
- **Request Latency p95** — 95th percentile request latency
- **Request Latency p99** — 99th percentile request latency
- **Latency Percentiles (All Services)** — p50/p95/p99 overlaid on one panel

### Service Mesh Traffic
- **Incoming Requests by Source Workload** — Traffic breakdown by `source_workload`
- **Outgoing Requests by Destination** — Outbound traffic from the source reporter side
- **HTTP Response Status Codes** — Distribution of all HTTP status codes
- **gRPC Response Status Codes** — gRPC-specific status code distribution

### Control Plane (Istiod / Pilot)
- **Pilot xDS Push Rate by Type** — Rate of CDS/EDS/LDS/RDS pushes from Istiod (`pilot_xds_pushes`)
- **Active xDS Connections** — Number of live Envoy proxy connections to Istiod (`pilot_xds`)
- **Pilot xDS Push Errors** — Configuration delivery failures (`pilot_xds_push_errors`)
- **Pilot Known Services** — Total services discovered by Istiod (`pilot_services`)

### TCP Traffic
- **TCP Bytes Sent** — `istio_tcp_sent_bytes_total` rate by destination service
- **TCP Bytes Received** — `istio_tcp_received_bytes_total` rate by destination service

## Key Istio Metrics Used

| Metric | Description |
|---|---|
| `istio_requests_total` | Total HTTP/gRPC requests (counter) |
| `istio_request_duration_milliseconds_bucket` | Request duration histogram |
| `istio_request_bytes_sum` / `_count` | Request body size |
| `istio_response_bytes_sum` / `_count` | Response body size |
| `istio_tcp_sent_bytes_total` | TCP bytes sent |
| `istio_tcp_received_bytes_total` | TCP bytes received |
| `pilot_xds_pushes` | xDS configuration pushes from Istiod |
| `pilot_xds` | Active xDS connections |
| `pilot_xds_push_errors` | xDS push errors |
| `pilot_services` | Services known to Istiod |
