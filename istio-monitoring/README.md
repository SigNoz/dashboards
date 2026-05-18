# Istio Monitoring Dashboard - Prometheus

## Overview
Monitor Istio service mesh health, traffic, latency and errors.

## Metrics Ingestion
Istio exposes Prometheus metrics automatically. Scrape with OpenTelemetry Collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: istio-mesh
          kubernetes_sd_configs:
            - role: endpoints
              namespaces:
                names: ['istio-system']
```

## Variables
- `{{namespace}}`: Kubernetes namespace to filter
- `{{deployment.environment}}`: Deployment environment
