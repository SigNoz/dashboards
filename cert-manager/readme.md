# Cert-Manager Dashboard - Prometheus

## Metrics Ingestion

### Cert-Manager Metrics
Cert-Manager exposes Prometheus metrics natively on port `9402` at the `/metrics` endpoint. These metrics cover certificate lifecycle, issuance, renewal, ACME client activity, and controller performance.

Key metric families:
- `certmanager_certificate_ready_status` - Certificate readiness state
- `certmanager_certificate_expiration_timestamp_seconds` - Certificate expiration timestamps
- `certmanager_certificate_renewal_timestamp_seconds` - Certificate renewal timestamps
- `certmanager_http_acme_client_request_count` - ACME HTTP client request counts
- `certmanager_controller_sync_call_count` - Controller sync/reconciliation counts
- `process_cpu_seconds_total` / `process_resident_memory_bytes` - Process resource metrics

Reference: [cert-manager Prometheus Metrics Documentation](https://cert-manager.io/docs/devops-tips/prometheus-metrics/)

### Configure OpenTelemetry Collector

1. Add prometheus receiver to the `receivers:` section:

```yaml
  prometheus:
    config:
      global:
        scrape_interval: 60s
      scrape_configs:
        - job_name: cert-manager
          metrics_path: /metrics
          scheme: http
          static_configs:
            - targets:
              - cert-manager.cert-manager.svc.cluster.local:9402
```

2. Complete Configuration Example

Below is a complete `otel-config.yaml` example:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  hostmetrics:
    collection_interval: 60s
    scrapers:
      cpu: {}
      disk: {}
      load: {}
      filesystem: {}
      memory: {}
      network: {}
      paging: {}
      process:
        mute_process_name_error: true
        mute_process_exe_error: true
        mute_process_io_error: true
      processes: {}
  prometheus:
    config:
      global:
        scrape_interval: 60s
      scrape_configs:
        - job_name: otel-collector-binary
          static_configs:
            - targets:
              - localhost:8888
        - job_name: cert-manager
          metrics_path: /metrics
          scheme: http
          static_configs:
            - targets:
              - cert-manager.cert-manager.svc.cluster.local:9402

processors:
  batch:
    send_batch_size: 1000
    timeout: 10s
  resourcedetection:
    detectors: [env, system]
    timeout: 2s
    system:
      hostname_sources: [os]
  resource/env:
    attributes:
    - key: deployment.environment
      value: production
      action: upsert

extensions:
  health_check: {}
  zpages: {}

exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "your-ingestion-key"
  logging:
    verbosity: normal

service:
  telemetry:
    metrics:
      address: 0.0.0.0:8888
  extensions: [health_check, zpages]
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [resource/env, batch]
      exporters: [otlp]
    metrics/internal:
      receivers: [prometheus, hostmetrics]
      processors: [resource/env, resourcedetection, batch]
      exporters: [otlp]
    traces:
      receivers: [otlp]
      processors: [resource/env, batch]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [resource/env, batch]
      exporters: [otlp]
```

> **Note**: If cert-manager is deployed in a different namespace or with a different service name, update the target address accordingly. For Kubernetes ServiceMonitor-based setups, ensure the OpenTelemetry Collector can reach cert-manager's metrics endpoint.

## Variables

- `{{namespace}}` - Kubernetes namespace where certificates are deployed
- `{{issuer}}` - Certificate issuer name for filtering by issuer
- `{{certificate_name}}` - Certificate name for filtering specific certificates
- `{{cluster}}` - Kubernetes cluster name for multi-cluster environments
- `{{deployment.environment}}` - Deployment environment (e.g., staging, production)

## Dashboard Panels

### General Overview
- **Total Certificates** - Total number of certificates tracked by cert-manager
  `certmanager_certificate_ready_status`
- **Active Certificates (Ready)** - Certificates currently in Ready state
  `certmanager_certificate_ready_status` (condition=True)
- **Certificate Requests** - Total ACME HTTP client requests
  `certmanager_http_acme_client_request_count`
- **Uptime** - Cert-manager process uptime
  `process_start_time_seconds`

![General Overview](assets/general-overview.png)

### Certificate Issuance
- **Certificates Issued per Issuer** - Ready certificates grouped by issuer
  `certmanager_certificate_ready_status` grouped by `issuer_name`
- **Issuance Rate** - Rate of ACME client requests over time
  `certmanager_http_acme_client_request_count` (rate)
- **Issuance Success Rate** - Percentage of certificates in Ready state
  `certmanager_certificate_ready_status` (formula: Ready / Total * 100)

![Certificate Issuance](assets/certificate-issuance.png)

### Certificate Renewal
- **Days Until Certificate Expiration** - Time remaining before certificate expiry
  `certmanager_certificate_expiration_timestamp_seconds`
- **Renewal Success Rate** - Percentage of successfully renewed certificates
  `certmanager_certificate_ready_status`
- **Days Until Renewal** - Time remaining before scheduled renewal
  `certmanager_certificate_renewal_timestamp_seconds`

![Certificate Renewal](assets/certificate-renewal.png)

### Error Metrics
- **Certificate Issuance Errors** - Certificates with Ready condition = False
  `certmanager_certificate_ready_status` (condition=False)
- **Renewal Errors by Issuer** - Failed certificates grouped by issuer
  `certmanager_certificate_ready_status` (condition=False, grouped by issuer_name)
- **API Server Errors** - ACME requests with 4xx/5xx status codes
  `certmanager_http_acme_client_request_count` (status >= 400)

![Error Metrics](assets/error-metrics.png)

### Resource Usage
- **CPU Usage** - CPU time consumed by cert-manager process
  `process_cpu_seconds_total`
- **Memory Usage** - Resident memory used by cert-manager
  `process_resident_memory_bytes`
- **Pod Restarts** - Container restart count for cert-manager pods
  `kube_pod_container_status_restarts_total`

![Resource Usage](assets/resource-usage.png)

### API and Event Metrics
- **API Request Rate** - Rate of ACME HTTP requests by method
  `certmanager_http_acme_client_request_count` (rate, grouped by method)
- **Event Processing Rate** - Controller sync call rate by controller
  `certmanager_controller_sync_call_count` (rate, grouped by controller)
- **Failed API Requests** - Rate of failed ACME requests by method and status
  `certmanager_http_acme_client_request_count` (rate, status=4xx/5xx)

![API and Event Metrics](assets/api-event-metrics.png)

> **Note**: Screenshots will be added after importing the dashboard into SigNoz. Placeholder image references are included above for the expected screenshot locations in the `assets/` directory.
