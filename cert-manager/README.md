# cert-manager Dashboard - Prometheus

## Metrics Ingestion

### cert-manager Prometheus Metrics

cert-manager exposes Prometheus metrics natively at the `/metrics` endpoint on port 9402. These metrics cover certificate status, controller sync operations, ACME client activity, and more.

### Configure OpenTelemetry Collector

1. Add a prometheus receiver to the `receivers:` section:

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
              - cert-manager.cert-manager.svc:9402
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
              - cert-manager.cert-manager.svc:9402

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

## Dashboard Panels

### Variables

- `{{namespace}}`: Kubernetes namespace where cert-manager or certificates are deployed, default `cert-manager`
- `{{controller}}`: cert-manager controller name

### Sections

- General Overview
  - Total Certificates - `certmanager_certificate_ready_status`
  - Certificates Ready - `certmanager_certificate_ready_status{condition="True"}`
  - Certificates Not Ready - `certmanager_certificate_ready_status{condition="False"}`
  - Soonest Cert Expiry - `certmanager_certificate_expiration_timestamp_seconds`
- Certificate Details
  - Certificate Expiry Timeline - `certmanager_certificate_expiration_timestamp_seconds`
  - Certificate Ready Status - `certmanager_certificate_ready_status`
- Controller Performance
  - Controller Sync Rate - `certmanager_controller_sync_call_count`
  - Controller Sync Errors - `certmanager_controller_sync_error_count`
- ACME Client
  - ACME HTTP Requests/sec - `certmanager_http_acme_client_request_count`
  - ACME Request Duration - `certmanager_http_acme_client_request_duration_seconds`
- Resource Usage
  - CPU Usage - `container_cpu_usage_seconds_total`
  - Memory Usage - `container_memory_usage_bytes`
