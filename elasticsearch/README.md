# Elasticsearch Monitoring Dashboard - Prometheus

Comprehensive Elasticsearch monitoring dashboard for [SigNoz](https://signoz.io/) using Prometheus metrics from [elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter).

## Sections

| # | Section | Panels | Key Metrics |
|---|---------|--------|-------------|
| 1 | Cluster Overview | Health status, node count, active/relocating/unassigned/initializing shards, pending tasks | `elasticsearch_cluster_health_*` |
| 2 | Index Metrics | Document count, store size, deleted docs, indexing rate & latency, flush rate, merge rate | `elasticsearch_indices_*` |
| 3 | Search Metrics | Query rate & latency, fetch rate & latency, scroll ops, active queries | `elasticsearch_indices_search_*` |
| 4 | JVM Metrics | Heap/non-heap memory, GC count & time (young/old), thread count & peak | `elasticsearch_jvm_*` |
| 5 | OS & System | CPU %, memory usage, load average, open file descriptors, process CPU, filesystem available | `elasticsearch_os_*`, `elasticsearch_process_*` |
| 6 | Network & Transport | Bytes sent/received, transport connections, HTTP connections, packet rates | `elasticsearch_transport_*`, `elasticsearch_http_*` |
| 7 | Thread Pool | Active threads, queue size, rejected tasks, completed tasks, total threads, largest pool | `elasticsearch_thread_pool_*` |

## Metrics Ingestion

This dashboard uses Prometheus metrics from [elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter). Ingest them into SigNoz via the OpenTelemetry Collector Prometheus receiver.

### OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "elasticsearch"
          scrape_interval: 30s
          static_configs:
            - targets: ["elasticsearch-exporter:9114"]

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "elasticsearch"
        action: upsert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch, resource]
      exporters: [otlp]
```

### Elasticsearch Exporter Setup

Deploy `elasticsearch_exporter` alongside your Elasticsearch cluster:

```bash
docker run -d --name es-exporter \
  -p 9114:9114 \
  quay.io/prometheuscommunity/elasticsearch-exporter:latest \
  --es.uri=http://elasticsearch:9200 \
  --es.all \
  --es.indices \
  --es.shards
```

## Variables

- `{{namespace}}` - Kubernetes namespace
- `{{service.name}}` - OTel service name for the Elasticsearch exporter
- `{{cluster}}` - Cluster identifier
- `{{deployment_environment}}` - Deployment environment (e.g., production, staging)

## Dashboard Panels

### Cluster Overview
Provides a high-level view of cluster health including the green/yellow/red status indicator, total node count, shard distribution (active, relocating, unassigned, initializing), and pending cluster tasks.

### Index Metrics
Monitors index-level operations including total document count, store size in bytes, indexing throughput (ops/sec), average indexing latency, flush rate, and segment merge rate.

### Search Metrics
Tracks search performance with query rate, average query latency, fetch rate and latency, scroll operations, and currently active search queries.

### JVM Metrics
Displays JVM health including heap and non-heap memory usage vs committed/max limits, garbage collection frequency and duration broken down by young and old generation, and thread counts.

### OS & System Metrics
Monitors operating system resources: CPU utilization, memory usage, 1-minute load average, open file descriptors, process-level CPU, and available filesystem space.

### Network & Transport
Visualizes inter-node communication with transport byte rates (TX/RX), packet counts, open transport connections, and HTTP connection count.

### Thread Pool Metrics
Shows thread pool utilization including active threads, queued tasks, rejected task rate, completed task rate, total thread count, and largest pool size.
