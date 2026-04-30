# Istio Monitoring Dashboard - Prometheus

## Metrics Ingestion

Configure the OpenTelemetry Collector to scrape Istio Prometheus metrics endpoints.

### otel-config.yaml

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'istio'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_istio]
              regex: pilot
              action: keep
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
          metrics_path: /stats/prometheus
          scheme: http
        - job_name: 'envoy-sidecar'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_istio]
              regex: sidecar-injector
              action: keep
          metrics_path: /stats/prometheus

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]

exporters:
  otlp:
    endpoint: "signoz-otel-collector:4317"
    tls:
      insecure: true
```

## Variables

- `namespace`: Kubernetes namespace where Istio is deployed
- `deployment_environment`: Deployment environment
- `service_name`: Service name within the mesh
- `cluster`: Kubernetes cluster name

## Dashboard Panels

### General Overview
- **Total Requests**: Total requests processed by the service mesh
- **Request Rate**: Requests per second
- **Average Latency**: Average request latency in milliseconds
- **Error Rate**: Percentage of failed requests

### Traffic Management
- **Request Distribution by Destination**: Requests across destination services
- **Request Distribution by Response Code**: Requests grouped by HTTP response code
- **Outlier Detection Ejections**: Circuit breaker ejection events
- **Retries and Timeouts**: Retry attempts and timeout occurrences

### Performance Metrics
- **Request Latency (p50, p95, p99)**: Latency percentiles
- **Throughput**: Requests per unit of time
- **Service Response Times by Destination**: Response times per service
- **Bytes Sent and Received**: Data volume transferred

### Error Metrics
- **HTTP Error Rates (4xx, 5xx)**: HTTP errors across services
- **gRPC Error Rates**: gRPC error rates in service communications
- **Failed Requests by Service**: Failed requests per service
- **Connection Failures**: Connection error count

### Resource Usage
- **CPU Usage (Control Plane)**: CPU for Istio control plane
- **Memory Usage (Control Plane)**: Memory for Istio control plane
- **Pod Restarts**: Istio pod restart count
- **Sidecar Proxy CPU**: Envoy sidecar resource consumption

### Control Plane Metrics
- **Pilot Configuration Pushes**: Configuration pushes by type
- **Pilot Proxy Push Errors**: Proxy push errors
- **Pilot Connected Proxies**: Currently connected proxies
- **Citadel Certificate Issuance**: Certificates issued for mTLS

### Security Metrics
- **Mutual TLS Sessions**: mTLS connection count
- **Authorization Policy Denials**: Policy denials
- **Certificate Expiry Time**: Certificate expiration status
