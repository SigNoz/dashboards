# Cert-Manager Monitoring Dashboard - Prometheus

## Overview

This dashboard provides comprehensive monitoring for [cert-manager](https://cert-manager.io/), the Kubernetes certificate management controller. It tracks certificate lifecycle, issuance, renewal, errors, and resource usage using Prometheus metrics.

## Data Ingestion

### Configure Prometheus Scraping

Add the following scrape config to your Prometheus configuration:

```yaml
- job_name: cert-manager
  static_configs:
    - targets: ['cert-manager.cert-manager.svc.cluster.local:9402']
```

Or use a Kubernetes ServiceMonitor:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: cert-manager
  namespace: cert-manager
spec:
  selector:
    matchLabels:
      app: cert-manager
  endpoints:
    - port: http-metrics
      interval: 30s
```

## Dashboard Variables

- `{{namespace}}`: Kubernetes namespace where cert-manager is deployed (default: `cert-manager`)
- `{{issuer}}`: Filter by certificate issuer name (e.g., `letsencrypt-prod`, `vault-issuer`)
- `{{certificate_name}}`: Filter by specific certificate name

## Dashboard Sections and Panels

### General Overview
- **Total Certificates** - `certmanager_certificate_expiration_timestamp_seconds` (count)
- **Active Certificates** - `certmanager_certificate_ready_status{condition="True"}`
- **Certificate Requests** - `certmanager_certificate_sync_call_count_total`
- **Uptime** - `process_start_time_seconds`

### Certificate Issuance
- **Certificates Issued per Issuer** - grouped by `issuer_name`
- **Issuance Rate** - rate of `certmanager_certificate_sync_call_count_total`
- **Issuance Success Rate** - Ready True vs False

### Certificate Renewal
- **Certificates Pending Renewal** - certs expiring within 7 days
- **Renewal Success Rate** - ACME requests 2xx vs non-2xx
- **Renewal Duration (p99)** - `certmanager_http_acme_client_request_duration_seconds_bucket`

### Error Metrics
- **Certificate Issuance Errors** - sync vs success rate delta
- **Renewal Errors** - ACME non-2xx responses
- **API Server Errors** - `rest_client_requests_total` 4xx/5xx

### Resource Usage
- **CPU Usage** - `process_cpu_seconds_total` per pod
- **Memory Usage** - `process_resident_memory_bytes` per pod
- **Pod Restarts** - `kube_pod_container_status_restarts_total`

### API and Event Metrics
- **API Request Rate** - `rest_client_requests_total` by verb/resource
- **Event Processing Rate** - `certmanager_controller_sync_call_count_total`
- **Failed API Requests** - 4xx/5xx increases

## References

- [cert-manager Prometheus Metrics Documentation](https://cert-manager.io/docs/observability/prometheus-metrics/)
- [cert-manager Installation Guide](https://cert-manager.io/docs/installation/)
