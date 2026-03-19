# Elasticsearch Monitoring Dashboard - Prometheus

## Overview
Monitor Elasticsearch cluster health, nodes, indices, query performance and cache.

## Metrics Ingestion
Use the Elasticsearch exporter and scrape via OpenTelemetry Collector:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: elasticsearch
          static_configs:
            - targets: ['<es-host>:9114']
```

## Variables
- `{{deployment.environment}}`: Deployment environment
- `{{cluster_name}}`: Elasticsearch cluster name
- `{{node_name}}`: Elasticsearch node name
