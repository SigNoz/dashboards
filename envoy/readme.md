# Envoy Monitoring Dashboard - OTLP

## Metrics Ingestion

### Prerequisites

- A running Kubernetes cluster (local or cloud)
- Envoy proxy deployed (standalone or as part of an Envoy Gateway / Istio setup)
- SigNoz instance (cloud or self-hosted)

### Configuring OpenTelemetry Collector to Scrape Envoy Metrics

Envoy exposes Prometheus metrics at `/stats/prometheus`. Use the OpenTelemetry Collector's Prometheus receiver to scrape these metrics and forward them to SigNoz via OTLP.

#### 1. Set up Prometheus Receiver

Add the following to your `otel-config.yaml`:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'envoy'
          scrape_interval: 15s
          metrics_path: /stats/prometheus
          static_configs:
            - targets: ['envoy.default.svc.cluster.local:9901']
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: 'envoy_.*'
              action: keep
```

> **Note:** Replace `envoy.default.svc.cluster.local:9901` with your Envoy admin endpoint. The default Envoy admin port is `9901`.

#### 2. Configure Processors

```yaml
processors:
  batch:
    timeout: 10s
    send_batch_size: 1000
  resource/env:
    attributes:
      - key: deployment.environment
        value: "production"
        action: upsert
```

#### 3. Set Up OTLP Exporter

```yaml
exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "${SIGNOZ_ACCESS_TOKEN}"
```

#### 4. Define the Metrics Pipeline

```yaml
service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [resource/env, batch]
      exporters: [otlp]
```

### Full Configuration

Below is the complete `otel-config.yaml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  prometheus:
    config:
      scrape_configs:
        - job_name: 'envoy'
          scrape_interval: 15s
          metrics_path: /stats/prometheus
          static_configs:
            - targets: ['envoy.default.svc.cluster.local:9901']
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: 'envoy_.*'
              action: keep

processors:
  batch:
    timeout: 10s
    send_batch_size: 1000
  resource/env:
    attributes:
      - key: deployment.environment
        value: "production"
        action: upsert

exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "${SIGNOZ_ACCESS_TOKEN}"

service:
  pipelines:
    metrics:
      receivers: [otlp, prometheus]
      processors: [resource/env, batch]
      exporters: [otlp]
```

> **Note:**
> - Replace `{region}` with your SigNoz Cloud region (e.g., `us`, `in`, `eu`)
> - For self-hosted SigNoz, use `localhost:4317` or the appropriate collector endpoint
> - `SIGNOZ_ACCESS_TOKEN` is only required for SigNoz Cloud

## Variables

- `{{deployment.environment}}` – Deployment environment (e.g., staging, production)
- `{{service_name}}` – Envoy service name to filter metrics
- `{{k8s_namespace_name}}` – Kubernetes namespace where Envoy is deployed
- `{{k8s_cluster_name}}` – Kubernetes cluster for multi-cluster setups

## Dashboard Sections

### General Overview

High-level overview of Envoy's health and performance.

- **Active Connections** – `envoy_http_downstream_cx_active` (Gauge, latest/sum)
- **Total Requests** – `envoy_http_downstream_rq_total` (Counter, latest/sum)
- **Uptime** – `envoy_server_uptime` (Gauge, latest/max)
- **Request Rate** – `envoy_http_downstream_rq_total` (Counter, rate/sum)

### Request Metrics

Traffic volume and request processing insights.

- **HTTP Request Count** – `envoy_http_downstream_rq_total` (rate, grouped by `envoy_http_conn_manager_prefix`)
- **Request Size (Bytes Received)** – `envoy_http_downstream_cx_rx_bytes_total` (rate/sum)
- **Response Size (Bytes Sent)** – `envoy_http_downstream_cx_tx_bytes_total` (rate/sum)

### Response Metrics

Response code distribution and success/error breakdown.

- **HTTP Response Codes** – `envoy_http_downstream_rq_xx` (rate, grouped by `envoy_response_code_class`)
- **Success vs Error Responses** – `envoy_http_downstream_rq_xx` (filtered by code class 2/4/5)

### Latency Metrics

Request processing latency analysis.

- **Average Latency** – `envoy_http_downstream_rq_time` (Histogram, avg/avg)
- **Latency Percentiles** – `envoy_http_downstream_rq_time` (P50, P95, P99)

### Error Metrics

Error tracking and failure identification.

- **Total Errors (4xx + 5xx)** – `envoy_http_downstream_rq_xx` (filtered by code class 4, 5)
- **Connection Errors** – `envoy_http_downstream_cx_destroy_remote_active_rq`
- **Protocol Errors** – `envoy_http_downstream_cx_protocol_error`
- **Request Timeouts** – `envoy_http_downstream_rq_timeout`
- **Error Rate** – `envoy_http_downstream_rq_xx` (rate, grouped by response code class)
- **Connection Errors Over Time** – Remote close and protocol errors over time

### Resource Usage

Envoy process resource consumption.

- **Memory Allocated** – `envoy_server_memory_allocated` (Gauge, avg)
- **Memory Heap Size** – `envoy_server_memory_heap_size` (Gauge, avg)

### Network I/O

Upstream network performance monitoring.

- **Upstream Network In** – `envoy_cluster_upstream_cx_rx_bytes_total` (rate/sum)
- **Upstream Network Out** – `envoy_cluster_upstream_cx_tx_bytes_total` (rate/sum)
- **Upstream Connection Rate** – `envoy_cluster_upstream_cx_total` (rate, grouped by cluster)
- **Upstream Connection Failures** – `envoy_cluster_upstream_cx_connect_fail` + `envoy_cluster_upstream_cx_connect_timeout`

### Upstream and Downstream Metrics

Service interaction and dependency visibility.

- **Upstream Request Count** – `envoy_cluster_upstream_rq_total` (rate, grouped by cluster)
- **Upstream Error Rate** – `envoy_cluster_upstream_rq_xx` (rate, filtered by 4xx/5xx)
- **Downstream Active Requests** – `envoy_http_downstream_rq_active` (avg, grouped by prefix)
