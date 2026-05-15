# Redis Monitoring Dashboard - Prometheus

Comprehensive Redis monitoring dashboard for [SigNoz](https://signoz.io/) using Prometheus metrics from [redis_exporter](https://github.com/oliver006/redis_exporter).

## Sections

| #   | Section       | Covers                                                        |
| --- | ------------- | ------------------------------------------------------------- |
| 1   | Overview      | Up status, connected clients, memory used, uptime             |
| 2   | Memory        | Usage over time, fragmentation ratio, RSS, dataset, evictions |
| 3   | Performance   | Commands/sec, ops/sec, hit rate, latency, slowlog             |
| 4   | Connections   | Connected/blocked clients, received/rejected connections      |
| 5   | Persistence   | RDB save status, changes since save, AOF rewrite, AOF size    |
| 6   | Replication   | Role, connected replicas, replication offset, replica lag     |
| 7   | Keyspace      | Total keys, expiring keys, expiry rate, eviction rate         |
| 8   | Network       | Input/output bytes, pub/sub channels and patterns             |
| 9   | CPU           | System and user CPU usage                                     |

## Metrics Ingestion

### Using OpenTelemetry Collector with Prometheus Receiver

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "redis"
          scrape_interval: 15s
          static_configs:
            - targets: ["redis-exporter:9121"]
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: "redis_.*"
              action: keep

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "redis"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch, resource]
      exporters: [otlp]
```

### Redis Exporter Setup

```bash
docker run -d --name redis-exporter \
  -p 9121:9121 \
  -e REDIS_ADDR=redis://your-redis-host:6379 \
  oliver006/redis_exporter:latest
```

## Variables

- `{{redis_instance}}`: Redis instance address for filtering metrics

## Dashboard Panels (47 total)

- **8 value panels** — instant metrics (up status, clients, memory, uptime, RDB status, role, replicas)
- **30 time series panels** — trends over time for all key Redis metrics
- **9 section headers** — organized into logical monitoring categories
