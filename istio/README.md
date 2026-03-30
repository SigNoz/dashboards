# Istio Service Mesh Dashboard - Prometheus

## Metrics Ingestion

This dashboard expects Istio metrics collected from Envoy sidecars or gateways via Prometheus and forwarded to SigNoz. The queries are built on Istio Prometheus metrics such as `istio_requests_total`, `istio_request_duration_milliseconds`, `istio_request_bytes`, `istio_response_bytes`, and the `istio_tcp_*` family.

A minimal OpenTelemetry Collector configuration can scrape Istio proxy metrics and forward them to SigNoz:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: istio-sidecars
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_container_name]
              action: keep
              regex: istio-proxy
            - source_labels: [__meta_kubernetes_pod_ip]
              target_label: __address__
              replacement: $1:15090

processors:
  batch:
    timeout: 10s
    send_batch_size: 1000

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      signoz-access-token: "<your-ingestion-key>"

service:
  pipelines:
    metrics/internal:
      receivers: [prometheus]
      processors: [batch]
      exporters: [otlp]
```

Replace the following:

- `<region>`: Your SigNoz Cloud region.
- `<your-ingestion-key>`: Your SigNoz ingestion key.

If you already run Prometheus in-cluster, you can keep Istio scraping there and point the OpenTelemetry Collector to the Prometheus endpoint instead. The important requirement is that the `istio_*` metrics and labels used by this dashboard reach SigNoz.

## Variables

- `{{namespace}}`: Destination workload namespace.
- `{{service_name}}`: Destination service short name from `destination_service_name`.
- `{{destination_service}}`: Full destination service label, typically the service FQDN.
- `{{source_workload}}`: Source workload sending traffic to the selected destination service.

This dashboard filters on `reporter = destination` to avoid double-counting the same traffic from both source and destination telemetry.

## Dashboard Panels

### Traffic Overview

- **Request Rate**: Request throughput from `istio_requests_total`.
- **Request Duration P50 / P90 / P99**: Service latency percentiles from `istio_request_duration_milliseconds`.
- **Request Size**: Average request payload size from `istio_request_bytes`.
- **Response Size**: Average response payload size from `istio_response_bytes`.

### Error Analysis

- **4xx Request Rate**: 4xx responses per second from `istio_requests_total`.
- **5xx Request Rate**: 5xx responses per second from `istio_requests_total`.
- **Error Rate by Response Code**: Error traffic grouped by `response_code`.
- **Top Error Services**: Namespace-level error rate grouped by `destination_service_name`.

### Service Performance

- **Latency by Destination Service**: P90 latency grouped by `destination_service_name`.
- **Throughput by Source Workload**: Request rate grouped by `source_workload`.
- **Throughput by Destination Service**: Request rate grouped by `destination_service_name`.

### TCP Metrics

- **TCP Bytes Sent**: Rate of `istio_tcp_sent_bytes_total`.
- **TCP Bytes Received**: Rate of `istio_tcp_received_bytes_total`.
- **TCP Connections Opened**: Rate of `istio_tcp_connections_opened_total`.
- **TCP Connections Closed**: Rate of `istio_tcp_connections_closed_total`.

### Security

- **Traffic by Security Policy**: Request rate grouped by `connection_security_policy`.
- **mTLS Traffic Share**: Percentage of traffic with `connection_security_policy = mutual_tls`.
- **Plaintext Traffic Share**: Percentage of traffic where mTLS is not in use.

## Screenshots

The `assets/` directory is included as a placeholder for screenshots before opening the upstream pull request.

Suggested filenames:

- `assets/traffic-overview.png`
- `assets/error-analysis.png`
- `assets/service-performance.png`
- `assets/tcp-metrics.png`
- `assets/security.png`
