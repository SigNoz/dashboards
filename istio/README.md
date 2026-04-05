# Istio Monitoring Dashboard for SigNoz

Comprehensive Istio service mesh monitoring dashboard covering traffic, performance, errors, resource usage, control plane, data plane, and security metrics.

## Prerequisites

- [Istio](https://istio.io/latest/docs/setup/install/) service mesh installed in your Kubernetes cluster
- Istio configured to expose [Prometheus metrics](https://istio.io/latest/docs/reference/config/metrics/)
- SigNoz collector running and accessible

### 1. Deploy OpenTelemetry Collector with Prometheus Receiver

Deploy the OTel Collector in your Kubernetes cluster to scrape Istio metrics and forward them to SigNoz:

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
            - job_name: 'istiod'
              kubernetes_sd_configs:
                - role: pod
              relabel_configs:
                - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_pod_label_app]
                  action: keep
                  regex: istio-system;istiod
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
                  action: replace
                  target_label: __address__
                  regex: (.+)
                  replacement: $1:15014
            - job_name: 'envoy-stats'
              metrics_path: /stats/prometheus
              kubernetes_sd_configs:
                - role: pod
              relabel_configs:
                - source_labels: [__meta_kubernetes_pod_container_name]
                  action: keep
                  regex: istio-proxy

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

Replace the following:

- `<region>`: Your SigNoz Cloud [region](https://signoz.io/docs/ingestion/signoz-cloud/overview/#endpoint)
- `<your-ingestion-key>`: Your [ingestion key](https://signoz.io/docs/ingestion/signoz-cloud/keys/)

### 2. Enable Istio Telemetry

Ensure Istio is configured to emit Prometheus metrics (enabled by default):

```yaml
apiVersion: telemetry.istio.io/v1
kind: Telemetry
metadata:
  name: mesh-default
  namespace: istio-system
spec:
  metrics:
    - providers:
        - name: prometheus
```

## Dashboard Sections

| Section | Panels | Description |
| --- | --- | --- |
| **General Overview** | Total Requests, Avg Latency, Pod Restarts, Request Rate, Error Rate | High-level service mesh health |
| **Traffic Management** | Request Distribution by Service, Retries | Traffic routing and retry behavior |
| **Performance Metrics** | Latency P50/P95/P99, Throughput | Detailed latency percentiles and throughput |
| **Error Metrics** | HTTP 4xx/5xx Errors, gRPC Errors | Error breakdown by type and protocol |
| **Resource Usage** | CPU Usage, Memory Usage | Istio sidecar and control plane resource consumption |
| **Control Plane** | Pilot xDS Pushes, Convergence Time | Istiod configuration distribution health |
| **Data Plane** | TCP Connections, TCP Traffic | Envoy sidecar network activity |
| **Security** | mTLS vs Plaintext Traffic | Connection security policy distribution |

## Dashboard Variables

| Variable                  | Description              |
| ------------------------- | ------------------------ |
| `$namespace`              | Kubernetes namespace     |
| `$service.name`           | Service name             |
| `$cluster`                | Cluster name             |
| `$deployment_environment` | Deployment environment   |

## Metrics Reference

This dashboard uses standard [Istio metrics](https://istio.io/latest/docs/reference/config/metrics/):

- `istio_requests_total` — Total request count
- `istio_request_duration_milliseconds` — Request duration histogram
- `istio_request_retries_total` — Request retry count
- `istio_tcp_connections_opened_total` / `istio_tcp_connections_closed_total` — TCP connections
- `istio_tcp_sent_bytes_total` / `istio_tcp_received_bytes_total` — TCP traffic
- `pilot_xds_pushes` — Control plane xDS push count
- `pilot_proxy_convergence_time_sum` — Proxy convergence time

## Screenshot

<!-- Dashboard screenshot placeholder -->
![Istio Dashboard](assets/istio-dashboard-preview.png)
