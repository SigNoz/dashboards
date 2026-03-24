# cert-manager Dashboard - Prometheus

## Data Ingestion

This dashboard expects cert-manager metrics scraped by Prometheus and available in SigNoz metrics storage.

### Option 1: Kubernetes Helm chart values

Enable metrics and a ServiceMonitor in cert-manager values:

```yaml
prometheus:
  enabled: true
servicemonitor:
  enabled: true
```

### Option 2: OpenTelemetry Collector Prometheus receiver

Add a Prometheus scrape job that discovers cert-manager pods/services:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: cert-manager
          kubernetes_sd_configs:
            - role: endpoints
          relabel_configs:
            - source_labels: [__meta_kubernetes_namespace]
              action: keep
              regex: cert-manager
            - source_labels: [__meta_kubernetes_service_name]
              action: keep
              regex: cert-manager

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [otlp]
```

## Variables

- {{namespace}}: Kubernetes namespace containing cert-manager and Certificate resources.
- {{issuer}}: Issuer/ClusterIssuer label to filter certificate-centric views.

## Dashboard Panels

- Certificates Ready: Total certificates in Ready=True state.
- Expiring in 7 Days: Count of certificates near expiration.
- Renewal Due: Certificates whose renewal timestamp is already reached.
- ACME Request Rate: Current request throughput to ACME endpoints.
- Certificate Ready Status: Condition split for ready status series.
- Certificate Expiration Horizon (Days): Days remaining before expiration per certificate.
- Controller Sync Calls: Controller reconciliation call rate by controller.
- ACME Client Requests by Host: ACME request rate grouped by host.
