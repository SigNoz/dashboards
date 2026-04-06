# Elasticsearch Monitoring Dashboard

Elasticsearch monitoring dashboard for [SigNoz Cloud](https://signoz.io/), uses the OpenTelemetry [`elasticsearch`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/elasticsearchreceiver/documentation.md) receiver.

## Sections

| #   | Section         | Covers                                                  |
| --- | --------------- | ------------------------------------------------------- |
| 1   | Cluster Health  | Health status, shards, pending tasks, node count        |
| 2   | Node Metrics    | CPU, disk, HTTP connections, open files                 |
| 3   | Index Metrics   | Docs, store size, segments, operations, merges          |
| 4   | Search & Query  | Query rate, avg latency, scroll/suggest, cache hit/miss |
| 5   | JVM & GC        | GC count/time, thread count, classes loaded             |
| 6   | Cache           | Cache memory, evictions, query cache size               |
| 7   | Circuit Breaker | Estimated vs limit per breaker, tripped count           |
| 8   | Thread Pool     | Threads, queued tasks                                   |

## OTel Collector Config

```yaml
receivers:
  elasticsearch:
    endpoint: "http://elasticsearch:9200"
    collection_interval: 30s
    nodes: ["_all"]
    skip_cluster_metrics: false
    metrics:
      elasticsearch.node.operations.get.completed:
        enabled: true
      elasticsearch.node.operations.get.time:
        enabled: true
      elasticsearch.index.cache.evictions:
        enabled: true
      elasticsearch.index.cache.memory.usage:
        enabled: true
      jvm.memory.heap.utilization:
        enabled: true
      elasticsearch.node.cache.size:
        enabled: true

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "elasticsearch"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [elasticsearch]
      processors: [batch, resource]
      exporters: [otlp]
```

## Dashboard Variables

- `service.name` — OTel service name
- `elasticsearch.cluster.name` — filter by cluster name
- `elasticsearch.node.name` — filter by node name

### Notes

- Optional metrics above must be explicitly enabled in the receiver config.
