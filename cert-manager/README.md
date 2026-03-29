# cert-manager Monitoring Dashboard

Comprehensive monitoring for cert-manager using native Prometheus metrics.

## Sections

| # | Section | Covers |
|---|---------|--------|
| 1 | General Overview | Ready vs not-ready certificates, expiry countdown, expiring soon count |
| 2 | Certificate Issuance | Request status by issuer, p95 issuance duration, renewal errors |
| 3 | ACME & Challenges | ACME client request rate, ACME errors by status code |
| 4 | Resource Usage | cert-manager CPU and memory per pod |
| 5 | Controller Health | Sync error rate per controller, work queue depth |

## Setup

### Enable Prometheus Metrics

cert-manager exposes Prometheus metrics on port 9402 by default. Configure your OTel collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'cert-manager'
          kubernetes_sd_configs:
            - role: pod
              namespaces:
                names: ['cert-manager']
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_app_kubernetes_io_name]
              regex: cert-manager
              action: keep
            - source_labels: [__address__]
              action: replace
              regex: (.+)(?::d+)?
              replacement: ${1}:9402
              target_label: __address__
```

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `namespace` | Kubernetes namespace where cert-manager is deployed |

## Key Metrics

| Metric | Description |
|--------|-------------|
| `certmanager_certificate_ready_status` | Certificate ready condition (True/False) |
| `certmanager_certificate_expiration_timestamp_seconds` | Certificate expiry timestamp |
| `certmanager_certificaterequest_ready_status` | Certificate request ready condition |
| `certmanager_certificate_issuance_duration_seconds` | Issuance duration histogram |
| `certmanager_controller_sync_error_count` | Controller sync error count |
| `certmanager_http_acme_client_request_count` | ACME HTTP request count |

## References

- [cert-manager Prometheus Metrics](https://cert-manager.io/docs/devops-tips/prometheus-metrics/)
- [Sample Grafana Dashboard](https://grafana.com/grafana/dashboards/11001-cert-manager)
