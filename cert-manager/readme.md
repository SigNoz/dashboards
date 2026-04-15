# Cert-Manager Monitoring Dashboard - Prometheus

## Metrics Ingestion

Configure the OpenTelemetry Collector to scrape cert-manager Prometheus metrics endpoints.

### otel-config.yaml

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'cert-manager'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
              regex: cert-manager
              action: keep
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
          metrics_path: /metrics
          scheme: http

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

- `namespace`: Kubernetes namespace where cert-manager is deployed
- `deployment_environment`: Deployment environment (e.g., production, staging)
- `issuer_name`: Certificate issuer name (e.g., letsencrypt-prod, vault)

## Dashboard Panels

### General Overview
- **Total Certificates Issued**: Total number of certificates successfully issued
- **Active Certificates**: Current number of active (non-expired) certificates
- **Certificate Requests**: Rate of certificate signing requests processed
- **Cert-Manager Uptime**: Uptime of cert-manager since last restart

### Certificate Issuance
- **Certificates Issued by Issuer**: Number of certificates issued per issuer
- **Certificate Issuance Rate**: Rate of certificate issuance over time
- **Issuance Success Rate**: Percentage of successful certificate issuances by condition

### Certificate Renewal
- **Certificates Pending Renewal**: Number of certificates approaching expiration
- **Renewal Success Rate**: Rate of certificate renewals over time
- **Time to Certificate Expiry**: Time remaining until certificates expire

### Error Metrics
- **Certificate Issuance Errors**: Number of errors during certificate issuance
- **Renewal Errors**: Number of errors during certificate renewal
- **API Server Errors**: Errors related to Kubernetes API server communication

### Resource Usage
- **CPU Usage**: CPU usage by cert-manager pods
- **Memory Usage**: Memory consumption of cert-manager pods
- **Pod Restarts**: Number of cert-manager pod restarts
