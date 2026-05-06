# Istio Service Mesh Monitoring Dashboard - Prometheus

SigNoz dashboard for monitoring Istio service mesh using Prometheus metrics. Covers request traffic, latency percentiles, error analysis, and TCP connection metrics across all services in the mesh.

## Prerequisites

- Kubernetes cluster with [Istio](https://istio.io/latest/docs/setup/install/) installed
- Istio telemetry v2 enabled (default in Istio 1.7+), which exposes Prometheus metrics via Envoy sidecar proxies
- SigNoz configured to scrape Prometheus metrics from the Istio mesh

## Metrics Used

| Metric | Description |
|--------|-------------|
| `istio_requests_total` | Total HTTP requests (labels: `source_workload`, `destination_service_name`, `response_code`, `reporter`) |
| `istio_request_duration_milliseconds_bucket` | Request duration histogram (used for P50/P95/P99) |
| `istio_request_bytes_sum` / `istio_request_bytes_count` | Request body size |
| `istio_response_bytes_sum` | Response body size |
| `istio_tcp_connections_opened_total` | TCP connections opened |
| `istio_tcp_connections_closed_total` | TCP connections closed |
| `istio_tcp_received_bytes_total` | TCP bytes received |
| `istio_tcp_sent_bytes_total` | TCP bytes sent |

## Dashboard Panels

### Overview
- **Total Requests** — cumulative request count across the mesh
- **Global Request Rate** — requests per second (all services combined)
- **5xx Error Rate** — percentage of server-side errors
- **P99 Latency** — 99th percentile latency across all services
- **Success Rate** — percentage of 2xx responses
- **Active Services** — count of distinct destination services receiving traffic
- **Outbound Request Rate** — RPS from source reporter perspective

### Traffic Analysis
- **Request Rate by Destination Service** — per-service RPS over time
- **Response Code Distribution** — stacked breakdown by HTTP status code
- **Average Request Size** — mean inbound payload size per service
- **Average Response Size** — mean outbound payload size per service

### Latency
- **P50 / P95 / P99 Latency by Service** — per-service percentile latency graphs
- **Latency Percentile Comparison** — P50, P95, P99 overlay on a single panel

### TCP Connections
- **Active TCP Connections** — open minus closed connections per service
- **TCP Bytes Received / Sent** — throughput breakdown per service
- **TCP Connection Rate** — rate of new connections opened vs closed
- **TCP Throughput** — combined received + sent bytes per second

### Error Analysis
- **4xx Error Rate by Service** — client error rate per service
- **5xx Error Rate by Service** — server error rate per service
- **Error Rate % by Destination** — combined 4xx+5xx percentage per service
- **Top Error Sources** — top 10 source workloads generating errors

## Setup: Scraping Istio Metrics in SigNoz

### 1. Verify Istio Metrics Are Exposed

Istio exposes Prometheus metrics on port `15090` (`/stats/prometheus`) of each Envoy sidecar. Confirm:

```bash
kubectl exec -n <namespace> <pod-name> -c istio-proxy -- curl -s localhost:15090/stats/prometheus | grep istio_requests_total | head -5
```

### 2. Configure OpenTelemetry Collector to Scrape Istio

Deploy an OTel Collector with a Prometheus receiver targeting the Istio mesh:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-istio
  namespace: istio-system
data:
  config.yaml: |
    receivers:
      prometheus:
        config:
          scrape_configs:
            - job_name: istio-mesh
              kubernetes_sd_configs:
                - role: pod
              relabel_configs:
                - source_labels: [__meta_kubernetes_pod_container_name]
                  action: keep
                  regex: istio-proxy
                - source_labels: [__address__]
                  action: replace
                  regex: ([^:]+)(?::\d+)?
                  replacement: $1:15090
                  target_label: __address__
                - action: labelmap
                  regex: __meta_kubernetes_pod_label_(.+)
                - source_labels: [__meta_kubernetes_namespace]
                  target_label: namespace
                - source_labels: [__meta_kubernetes_pod_name]
                  target_label: pod

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
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector-istio
  namespace: istio-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: otel-collector-istio
  template:
    metadata:
      labels:
        app: otel-collector-istio
    spec:
      serviceAccountName: otel-collector-istio
      containers:
      - name: otel-collector
        image: otel/opentelemetry-collector-contrib:0.144.0
        args: ["--config=/conf/config.yaml"]
        volumeMounts:
        - name: config
          mountPath: /conf
      volumes:
      - name: config
        configMap:
          name: otel-collector-istio
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-collector-istio
  namespace: istio-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-collector-istio
rules:
- apiGroups: [""]
  resources: [nodes, nodes/metrics, services, endpoints, pods]
  verbs: [get, list, watch]
- nonResourceURLs: [/metrics]
  verbs: [get]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-collector-istio
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: otel-collector-istio
subjects:
- kind: ServiceAccount
  name: otel-collector-istio
  namespace: istio-system
```

Replace `<region>` and `<your-ingestion-key>` with your SigNoz Cloud values from the [SigNoz ingestion settings](https://signoz.io/docs/ingestion/signoz-cloud/keys/).

### 3. Import the Dashboard

1. Open SigNoz and navigate to **Dashboards**
2. Click **New Dashboard** → **Import JSON**
3. Upload `istio-prometheus-v1.json`

## Notes

- All panels use `reporter="destination"` by default, which reflects metrics from the receiving service's sidecar. This avoids double-counting.
- TCP panels (`istio_tcp_*`) only populate if you have TCP services in your mesh alongside HTTP services.
- Latency percentiles require the `istio_request_duration_milliseconds_bucket` histogram; confirm it is present in your Prometheus output before using the Latency panels.
