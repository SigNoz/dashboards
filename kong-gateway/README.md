# Kong Gateway Dashboard - Prometheus

## Overview
Monitor Kong API Gateway health, performance, traffic and errors.

## Metrics Ingestion
Configure Kong with Prometheus metrics enabled and scrape with OpenTelemetry Collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: kong
          scrape_interval: 15s
          kubernetes_sd_configs:
            - role: pod
              namespaces:
                names:
                  - <kong-namespace>
          relabel_configs:
            - source_labels: [__address__]
              target_label: __address__
              replacement: $1:8100
```

## Variables
- `{{namespace}}`: Kubernetes namespace where Kong is deployed
- `{{deployment.environment}}`: Deployment environment
