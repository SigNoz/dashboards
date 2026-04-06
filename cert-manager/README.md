# Cert-Manager Monitoring Dashboard - Prometheus

A comprehensive SigNoz dashboard for monitoring [cert-manager](https://cert-manager.io/) in Kubernetes clusters, built on Prometheus metrics.

## Metrics Ingestion

cert-manager exposes Prometheus metrics on port `9402` by default. To ingest these metrics into SigNoz, configure the OpenTelemetry Collector with a Prometheus receiver.

### OpenTelemetry Collector Configuration

Add the following to your `otel-collector-config.yaml`:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'cert-manager'
          scrape_interval: 30s
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
              regex: cert-manager
              action: keep
            - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_component]
              regex: controller|webhook|cainjector
              action: keep
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
              regex: '(\d+)'
              target_label: __address__
              replacement: '${1}:$${2}'
              action: replace
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod

exporters:
  otlp:
    endpoint: "<SigNoz-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

Alternatively, if cert-manager is installed with Helm, enable the ServiceMonitor:

```yaml
# values.yaml
prometheus:
  enabled: true
  servicemonitor:
    enabled: true
```

## Variables

- `{{namespace}}`: Kubernetes namespace where cert-manager components are running. Supports multi-select and "All" option.

## Dashboard Sections

### 1. Certificate Overview
High-level view of certificate health across the cluster.
- Total certificates, ready vs not-ready counts
- Certificates expiring within 24h, 7d, 30d, 90d
- Average and minimum time to expiry
- Certificate readiness over time

### 2. Certificate Details
Per-certificate granular view.
- Expiry countdown per certificate (days remaining)
- Renewal countdown per certificate (hours to next renewal)
- Expiry breakdown by namespace
- Per-certificate ready status over time
- Table view of all certificates sorted by remaining lifetime

### 3. Issuer Health
Monitoring of Issuer and ClusterIssuer resources.
- Total issuers, sync success rate, sync errors
- Issuer sync rate over time by status
- Certificates per issuer

### 4. Certificate Requests & Orders
Tracking the certificate issuance pipeline.
- CertificateRequest sync rate by issuer type (ACME, CA, SelfSigned)
- ACME Order sync rate
- Challenge sync rate
- Main certificate controller sync rates

### 5. ACME Operations
Detailed monitoring of ACME protocol interactions (Let's Encrypt, etc.).
- ACME request rate, success rate, error rate
- Average request duration
- Request rate by HTTP status code, method, path, and host
- Request duration percentiles (p50/p90/p99)
- Error breakdown by status and method

### 6. Controller Performance
Overall cert-manager controller health.
- Total sync rate, success rate, error rate
- Sync rate per controller
- Error rate per controller
- Sync duration percentiles

### 7. Work Queue Metrics
Kubernetes controller-runtime work queue monitoring.
- Queue depth, adds rate, unfinished work
- Queue depth and adds rate over time per queue
- Queue wait latency percentiles (p50/p90/p99)
- Processing duration percentiles
- Retry rates
- Longest running processor duration

### 8. Webhook Metrics
Admission webhook performance monitoring.
- Webhook request rate, success rate, average latency
- Request rate by HTTP status
- Request duration percentiles

### 9. Kubernetes API & Client Metrics
cert-manager's interaction with the Kubernetes API server.
- API request rate by verb and resource
- API request errors by status code
- API request latency percentiles
- Client-side rate limiter wait duration

### 10. Leader Election
Controller leader election status.
- Current leader status per component
- Leader election transition rate (instability detection)

### 11. Resource Usage
Go runtime and process-level metrics.
- CPU usage, RSS memory, goroutines, open file descriptors
- CPU and memory over time per pod
- Goroutines and GC pause duration over time
- File descriptor usage vs limits
- Go heap memory (alloc, inuse, sys)
- GC allocation rate
- OS thread count

### 12. Network & Miscellaneous
Auxiliary monitoring metrics.
- Process uptime
- Clock skew detection (cert-manager vs Prometheus)
- Total managed resource count
- Clock skew over time
- Component up/down status

## Key Metrics Used

| Metric | Description |
|--------|-------------|
| `certmanager_certificate_ready_status` | Certificate readiness (True/False) |
| `certmanager_certificate_expiration_timestamp_seconds` | Certificate expiry Unix timestamp |
| `certmanager_certificate_renewal_timestamp_seconds` | Next renewal Unix timestamp |
| `certmanager_controller_sync_call_count` | Controller sync operation counter |
| `certmanager_http_acme_client_request_count` | ACME HTTP request counter |
| `certmanager_http_acme_client_request_duration_seconds` | ACME HTTP request duration histogram |
| `certmanager_http_webhook_request_count` | Webhook request counter |
| `certmanager_http_webhook_request_duration_seconds` | Webhook request duration histogram |
| `certmanager_clock_time_seconds` | cert-manager internal clock |
| `workqueue_depth` | Controller work queue depth |
| `workqueue_adds_total` | Work queue add operations |
| `workqueue_queue_duration_seconds` | Time spent waiting in queue |
| `workqueue_work_duration_seconds` | Time spent processing items |
| `workqueue_retries_total` | Work queue retry counter |
| `workqueue_longest_running_processor_seconds` | Longest active processor duration |
| `rest_client_requests_total` | Kubernetes API client requests |
| `rest_client_request_duration_seconds` | Kubernetes API request latency |
| `leader_election_master_status` | Leader election status |
| `process_cpu_seconds_total` | Process CPU usage |
| `process_resident_memory_bytes` | Process RSS memory |
| `go_goroutines` | Active goroutine count |
| `go_gc_duration_seconds` | GC pause duration |
| `go_memstats_heap_alloc_bytes` | Go heap allocation |

## Requirements

- cert-manager v1.0+ (tested with v1.12+)
- Prometheus metrics endpoint enabled (default: port 9402)
- OpenTelemetry Collector with Prometheus receiver configured
- SigNoz v0.30+
