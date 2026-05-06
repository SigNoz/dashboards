# Istio Monitoring Dashboard - Prometheus

Comprehensive Istio service mesh monitoring dashboard providing insights into traffic, performance, security, control plane, and data plane metrics.

## Dashboard Overview

This dashboard provides a complete view of your Istio service mesh health and performance across 8 key sections:

- **General Overview**: High-level metrics including total requests, request rate, average latency, and error rate
- **Traffic Management**: Request distribution, circuit breaker events, retries, timeouts, and inbound/outbound traffic
- **Performance Metrics**: Latency percentiles (p50, p95, p99), throughput, service response times, and resource utilization
- **Error Metrics**: HTTP and gRPC error rates, failed requests by service, and TLS handshake failures
- **Resource Usage**: CPU, memory, pod restarts, and disk I/O for Istio components
- **Control Plane Metrics**: Pilot configuration syncs, Mixer requests, Galley operations, and Citadel certificate issuance
- **Data Plane Metrics**: Envoy proxy metrics, traffic volume, proxy resource usage, and connection errors
- **Security Metrics**: Mutual TLS usage, authorization policy enforcement, certificate expirations, and security violations

## Metrics Ingestion

### Prerequisites

To use this dashboard, you need:

1. **Istio installed** in your Kubernetes cluster
2. **Prometheus configured** to scrape Istio metrics
3. **SigNoz OpenTelemetry Collector** configured to receive metrics from Prometheus

### Configuration

Add the following configuration to your OpenTelemetry collector to receive Istio metrics:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'istio-pilot'
          scrape_interval: 15s
          kubernetes_sd_configs:
            - role: pod
              namespaces:
                names:
                  - istio-system
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
              action: keep
              regex: true
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
              action: replace
              target_label: __metrics_path__
              regex: (.+)
            - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
              action: replace
              regex: ([^:]+)(?::\d+)?;(\d+)
              replacement: $1:$2
              target_label: __address__
            - action: labelmap
              regex: __meta_kubernetes_pod_label_(.+)
            - source_labels: [__meta_kubernetes_namespace]
              action: replace
              target_label: namespace
            - source_labels: [__meta_kubernetes_pod_name]
              action: replace
              target_label: pod

        - job_name: 'envoy-stats'
          scrape_interval: 15s
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
              action: keep
              regex: true
            - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
              action: replace
              regex: ([^:]+)(?::\d+)?;(\d+)
              replacement: $1:$2
              target_label: __address__
            - action: labelmap
              regex: __meta_kubernetes_pod_label_(.+)

processors:
  batch:
    timeout: 5s
    send_batch_size: 10000

exporters:
  signoz:
    endpoint: "http://your-signoz-collector-endpoint:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [signoz]
```

### Key Metrics Used

The dashboard uses the following Istio/Prometheus metrics:

| Metric Name | Description |
|------------|-------------|
| `istio_requests_total` | Total number of requests in the service mesh |
| `istio_request_duration_milliseconds_bucket` | Request latency histogram |
| `istio_request_bytes` | Request size in bytes |
| `istio_response_bytes` | Response size in bytes |
| `envoy_cluster_upstream_cx_total` | Total upstream connections |
| `envoy_cluster_upstream_rq_total` | Total upstream requests |
| `envoy_cluster_ssl_handshake_failure` | SSL handshake failures |
| `envoy_cluster_outlier_detection_ejections_active` | Circuit breaker events |
| `envoy_cluster_retry_success_total` | Successful retry attempts |
| `envoy_cluster_rq_timeout_total` | Request timeouts |
| `pilot_xds_pushes_total` | Pilot configuration pushes |
| `mixer_config_quads_success_total` | Mixer successful operations |
| `galley_validation_success_total` | Galley validation operations |
| `citadel_server_root_cert_expiry_timestamp` | Citadel root certificate expiry |
| `process_cpu_seconds_total` | Process CPU usage |
| `process_resident_memory_bytes` | Process memory usage |
| `kube_pod_container_status_restarts_total` | Pod restart count |
| `grpc_server_handled_total` | gRPC request count |

## Variables

- `{{namespace}}` - Kubernetes namespace where Istio is deployed (default: istio-system)
- `{{deployment.environment}}` - Deployment environment (e.g., production, staging)
- `{{service.name}}` - Service name within the mesh (multi-select)
- `{{cluster}}` - Kubernetes cluster name for multi-cluster setups

## Dashboard Panels

### General Overview

- **Total Requests**: Cumulative count of all requests processed by the mesh
- **Request Rate**: Current rate of incoming/outgoing requests per second
- **Average Latency**: Mean response time across all services
- **Error Rate**: Percentage of failed requests (4xx and 5xx)

### Traffic Management

- **Request Distribution**: Traffic volume breakdown by service
- **Circuit Breaker Events**: Active ejections due to health checks
- **Retries and Timeouts**: Retry attempts and request timeout counts
- **Inbound and Outbound Traffic**: Request volume by direction (source/destination)

### Performance Metrics

- **Request Latency Percentiles**: P50, P95, P99 latency values
- **Throughput**: Total requests processed per second
- **Service Response Times**: Individual service latency over time
- **Resource Utilization per Service**: CPU and memory usage by service

### Error Metrics

- **HTTP Error Rates**: 4xx (client) and 5xx (server) error rates
- **gRPC Error Rates**: gRPC error codes breakdown
- **Failed Requests by Service**: Table of failed requests grouped by service
- **TLS Handshake Failures**: Failed TLS negotiation attempts

### Resource Usage

- **CPU Usage**: CPU consumption for Istio control and data plane components
- **Memory Usage**: Memory usage for Istio components
- **Pod Restarts**: Restart count for Istio pods
- **Disk I/O**: Disk read/write operations

### Control Plane Metrics

- **Pilot Configuration Syncs**: Configuration push rate to proxies
- **Mixer Requests**: Policy and telemetry request rate
- **Galley Operations**: Configuration validation operations
- **Citadel Certificate Issuance**: Root certificate expiry timestamp

### Data Plane Metrics

- **Envoy Proxy Metrics**: Connection counts and request rates
- **Inbound and Outbound Traffic**: Data plane traffic by direction
- **Proxy CPU and Memory Usage**: Envoy proxy resource consumption
- **Connection Errors**: Failed connection establishment attempts

### Security Metrics

- **Mutual TLS Usage**: Connections secured with mTLS
- **Authorization Policy Enforcement**: Allowed vs denied requests
- **Certificate Expirations**: Time until certificate expiry
- **Security Policy Violations**: Authorization denials and policy violations

## Screenshots

![General Overview Section](assets/general-overview.png)
![Traffic Management Section](assets/traffic-management.png)
![Performance Metrics Section](assets/performance-metrics.png)
![Error Metrics Section](assets/error-metrics.png)
![Resource Usage Section](assets/resource-usage.png)
![Control Plane Metrics Section](assets/control-plane-metrics.png)
![Data Plane Metrics Section](assets/data-plane-metrics.png)
![Security Metrics Section](assets/security-metrics.png)

## References

- [Istio Metrics Documentation](https://istio.io/latest/docs/reference/config/metrics/)
- [Istio Observability Guide](https://istio.io/latest/docs/concepts/observability/)
- [Prometheus Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
