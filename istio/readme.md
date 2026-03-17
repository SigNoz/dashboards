# Istio Monitoring Dashboard

## Metrics Ingestion

### Istio Metrics
Istio exports Prometheus metrics from both the control plane (istiod) and data plane (Envoy sidecar proxies). Key metric endpoints:

1. **Envoy sidecar proxies** expose metrics at port `15090` on `/stats/prometheus` — includes `istio_requests_total`, `istio_request_duration_milliseconds`, `istio_request_bytes`, `istio_response_bytes`, and `envoy_*` metrics.
2. **Istiod (Pilot)** exposes metrics at port `15014` on `/metrics` — includes `pilot_*`, `citadel_*`, and `process_*` metrics.

### Configure OpenTelemetry Collector

1. Add prometheus receiver to the `receivers:` section:

```yaml
  prometheus:
    config:
      global:
        scrape_interval: 60s
      scrape_configs:
        - job_name: istio-envoy
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_container_port_number]
              regex: "15090"
              action: keep
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
        - job_name: istiod
          metrics_path: /metrics
          kubernetes_sd_configs:
            - role: endpoints
              namespaces:
                names:
                  - istio-system
          relabel_configs:
            - source_labels: [__meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
              regex: istiod;http-monitoring
              action: keep
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
        - job_name: istio-envoy
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_container_port_number]
              regex: "15090"
              action: keep
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
        - job_name: istiod
          metrics_path: /metrics
          kubernetes_sd_configs:
            - role: endpoints
              namespaces:
                names:
                  - istio-system
          relabel_configs:
            - source_labels: [__meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
              regex: istiod;http-monitoring
              action: keep

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
      value: staging
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

## Variables

- `{{namespace}}`: Kubernetes namespace where Istio is deployed
- `{{deployment_environment}}`: Deployment environment (e.g., production, staging)
- `{{service_name}}`: Destination service name within the mesh
- `{{cluster}}`: Kubernetes cluster for multi-cluster setups

## Sections

- General Overview
  - Total Requests — `istio_requests_total`
  - Request Rate — `istio_requests_total`
  - Average Latency — `istio_request_duration_milliseconds_sum` / `istio_request_duration_milliseconds_count`
  - Error Rate — `istio_requests_total` (5xx / total)
- Traffic Management
  - Request Distribution — `istio_requests_total` by `destination_service_name`
  - Load Balancing Efficiency — `istio_requests_total` by `destination_workload`
  - Circuit Breaker Events — `envoy_cluster_circuit_breakers_default_cx_open`
  - Retries and Timeouts — `envoy_cluster_upstream_rq_retry`, `envoy_cluster_upstream_rq_timeout`
- Performance Metrics
  - Request Latency P50 — `istio_request_duration_milliseconds_bucket` (p50)
  - Request Latency P95 / P99 — `istio_request_duration_milliseconds_bucket` (p95, p99)
  - Throughput — `istio_requests_total` by `destination_service_name`
  - Service Response Times — `istio_request_duration_milliseconds_sum`
- Error Metrics
  - HTTP Error Rates — `istio_requests_total` (4xx, 5xx)
  - gRPC Error Rates — `istio_requests_total` (grpc errors)
  - Failed Requests by Service — `istio_requests_total` (5xx by service)
  - TLS Handshake Failures — `envoy_cluster_ssl_handshake`
- Resource Usage
  - CPU Usage — `process_cpu_seconds_total`
  - Memory Usage — `process_resident_memory_bytes`
  - TCP Connections — `istio_tcp_connections_opened_total`, `istio_tcp_connections_closed_total`
- Control Plane Metrics
  - Pilot xDS Pushes — `pilot_xds_pushes`
  - Pilot Proxy Convergence Time — `pilot_proxy_convergence_time_bucket`
  - Pilot Connected Endpoints — `pilot_xds`
  - Citadel Certificate Issuance — `citadel_server_csr_count`
- Data Plane Metrics
  - Active Connections — `envoy_cluster_upstream_cx_active`
  - Inbound vs Outbound Traffic — `istio_request_bytes_sum`
  - Proxy Response Size — `istio_response_bytes_sum`
  - Connection Errors — `envoy_cluster_upstream_cx_connect_fail`
- Security Metrics
  - Mutual TLS Usage — `istio_requests_total` by `connection_security_policy`
  - Authorization Policy Enforcement — `istio_requests_total` (allowed vs denied)
  - Certificate Expirations — `citadel_server_csr_count`, `citadel_server_success_cert_issuance_count`
  - Security Policy Violations — `istio_requests_total` (403 by source/destination)

## References

- [Istio Standard Metrics](https://istio.io/latest/docs/reference/config/metrics/)
- [Istio Observability](https://istio.io/latest/docs/tasks/observability/metrics/)
- [Grafana Dashboard #7645](https://grafana.com/grafana/dashboards/7645)
