# cert-manager Monitoring Dashboard

A comprehensive SigNoz dashboard for monitoring cert-manager in Kubernetes environments using Prometheus metrics.

## Overview

This dashboard provides complete visibility into cert-manager operations including certificate lifecycle management, issuance and renewal processes, error monitoring, and resource usage tracking.

## Prerequisites

- cert-manager deployed in your Kubernetes cluster with Prometheus monitoring enabled
- SigNoz with Prometheus data source configured
- The following cert-manager Prometheus metrics available:
  - `certmanager_certificate_ready_status`
  - `certmanager_certificate_expiration_timestamp_seconds`
  - `certmanager_certificate_renewal_timestamp_seconds`
  - `certmanager_http_acme_client_request_count`
  - `certmanager_controller_sync_call_count`
  - `process_cpu_seconds_total`
  - `process_resident_memory_bytes`
  - `process_start_time_seconds`
  - `kube_pod_container_status_restarts_total`

## Dashboard Sections

### General Overview (4 panels)
- **Total Certificates Issued**: Total number of certificates managed by cert-manager
- **Active Certificates**: Certificates currently in Ready=True state
- **Certificate Requests**: Count of HTTP ACME client requests
- **Uptime**: cert-manager process uptime

### Certificate Issuance (3 panels)
- **Certificates Issued per Issuer**: Breakdown by issuer type (Let's Encrypt, CA, etc.)
- **Issuance Rate**: Rate of certificate issuance operations
- **Issuance Success Rate**: Success percentage for certificate issuance

### Certificate Renewal (3 panels)
- **Certificates Pending Renewal**: Certificates expiring within 30 days
- **Renewal Success Rate**: Success rate of renewal operations
- **Renewal Duration**: Time taken for certificate renewals

### Error Metrics (3 panels)
- **Certificate Issuance Errors**: Failed certificate issuance attempts
- **Renewal Errors**: Controller sync errors during renewal
- **API Server Errors**: HTTP 4xx/5xx errors from ACME API calls

### Resource Usage (3 panels)
- **CPU Usage**: CPU consumption of cert-manager process
- **Memory Usage**: Memory consumption in bytes
- **Pod Restarts**: Number of cert-manager pod restarts

### API and Event Metrics (3 panels)
- **API Request Rate**: Rate of HTTP ACME client requests
- **Event Processing Rate**: Controller sync call frequency
- **Failed API Requests**: Rate of failed API requests

## Installation

1. Import the dashboard JSON file (`cert-manager-prometheus-v1.json`) into SigNoz
2. Ensure your Prometheus data source includes cert-manager metrics
3. Verify cert-manager is running with monitoring enabled

## Configuration

### Enabling cert-manager Prometheus Metrics

Ensure cert-manager is deployed with monitoring enabled:

```yaml
# In your cert-manager values.yaml or deployment
prometheus:
  enabled: true
  servicemonitor:
    enabled: true
```

### Required RBAC

Make sure your monitoring setup has the necessary permissions to scrape cert-manager metrics:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: cert-manager-metrics
  namespace: cert-manager
  labels:
    app: cert-manager
spec:
  selector:
    app: cert-manager
  ports:
  - name: tcp-prometheus-servicemonitor
    port: 9402
    protocol: TCP
    targetPort: 9402
```

## Metrics Reference

### Core cert-manager Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `certmanager_certificate_ready_status` | Certificate ready status (0 or 1) | Gauge |
| `certmanager_certificate_expiration_timestamp_seconds` | Certificate expiration time | Gauge |
| `certmanager_certificate_renewal_timestamp_seconds` | Last renewal timestamp | Gauge |
| `certmanager_http_acme_client_request_count` | ACME client request count | Counter |
| `certmanager_http_acme_client_request_duration_seconds` | ACME request duration | Histogram |
| `certmanager_controller_sync_call_count` | Controller sync operations | Counter |

### Process Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `process_cpu_seconds_total` | CPU time consumed | Counter |
| `process_resident_memory_bytes` | Memory usage in bytes | Gauge |
| `process_start_time_seconds` | Process start time | Gauge |

### Kubernetes Metrics

| Metric | Description | Type |
|--------|-------------|------|
| `kube_pod_container_status_restarts_total` | Pod restart count | Counter |

## Alerting Recommendations

Consider setting up alerts for:

1. **Certificate Expiry**: Certificates expiring within 7 days
2. **Issuance Failures**: High rate of certificate issuance errors
3. **API Errors**: Persistent ACME API failures
4. **Memory Usage**: High memory consumption
5. **Pod Restarts**: Frequent cert-manager restarts

## Troubleshooting

### Common Issues

1. **No data showing**: Verify cert-manager metrics are being scraped by Prometheus
2. **Missing panels**: Check if all required metrics are available in your environment
3. **Incorrect values**: Ensure proper label matching in PromQL queries

### Debugging Steps

1. Check cert-manager pod logs:
   ```bash
   kubectl logs -n cert-manager deployment/cert-manager
   ```

2. Verify metrics endpoint:
   ```bash
   kubectl port-forward -n cert-manager svc/cert-manager-metrics 9402:9402
   curl http://localhost:9402/metrics
   ```

3. Check Prometheus targets:
   - Ensure cert-manager metrics endpoint is being scraped
   - Verify ServiceMonitor configuration if using Prometheus Operator

## Contributing

This dashboard is part of the SigNoz community dashboards project. For issues or improvements, please contribute to the [SigNoz dashboards repository](https://github.com/SigNoz/dashboards).

## License

This dashboard is provided under the same license as the SigNoz project.