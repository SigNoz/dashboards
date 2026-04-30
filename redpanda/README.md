# Redpanda Monitoring Dashboard - Prometheus

Comprehensive Redpanda monitoring dashboard for [SigNoz](https://signoz.io/) using native Prometheus metrics exposed by Redpanda.

## Sections

| #   | Section          | Covers                                                          |
| --- | ---------------- | --------------------------------------------------------------- |
| 1   | Cluster Overview | Brokers online, partitions, unavailable/under-replicated status |
| 2   | Throughput       | Produce/consume bytes/sec, messages/sec, latency p99            |
| 3   | Topics           | Partition counts, log sizes, leaders, replicas                  |
| 4   | Consumer Groups  | Lag, members, committed offsets, topics per group               |
| 5   | RPC & Internal   | RPC connections, request errors, Raft leadership changes        |
| 6   | Resources        | CPU, memory allocated/free, storage used/free, IO queue         |
| 7   | Schema Registry  | Request rate, errors                                            |
| 8   | Connections      | Active connections, connection rate                             |
| 9   | Storage          | Disk utilization, compaction metrics                            |

## Metrics Ingestion

Redpanda exposes Prometheus metrics natively on port 9644.

### Using OpenTelemetry Collector with Prometheus Receiver

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "redpanda"
          scrape_interval: 15s
          static_configs:
            - targets: ["redpanda-broker-1:9644", "redpanda-broker-2:9644"]
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: "redpanda_.*|vectorized_.*"
              action: keep

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "redpanda"
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

## Variables

- `{{redpanda_instance}}`: Redpanda broker instance for filtering metrics

## Dashboard Panels (49 total)

- **4 value panels** — instant cluster status metrics
- **36 time series panels** — trends for throughput, latency, resources, and more
- **9 section headers** — organized into logical monitoring categories
