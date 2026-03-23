# Elasticsearch Dashboard - OTEL

## Metrics Ingestion

This dashboard uses metrics from the [OpenTelemetry Elasticsearch receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/elasticsearchreceiver).

Add the Elasticsearch receiver to your OpenTelemetry Collector configuration:

```yaml
receivers:
  elasticsearch:
    endpoint: http://localhost:9200
    collection_interval: 30s

exporters:
  otlp:
    endpoint: "<signoz-otel-collector-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [elasticsearch]
      exporters: [otlp]
```

For full configuration options, see the [receiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/elasticsearchreceiver).

## Variables

- `{{deployment.environment}}`: Deployment environment filter
- `{{elasticsearch.cluster.name}}`: Elasticsearch cluster name
- `{{elasticsearch.node.name}}`: Elasticsearch node name (multi-select)

## Dashboard Sections

### Cluster Health
Cluster-level health status, node counts, shard distribution, pending tasks, and in-flight fetches.

### Node Metrics
Per-node CPU usage, load averages, disk space (total, available, free), and open file descriptors.

### JVM Metrics
Heap and non-heap memory usage, heap utilization, garbage collection rate and duration, thread count, and loaded classes.

### Index Performance
Document counts by state, indexing/search/merge operation rates, operation latency, shard sizes, and segment counts.

### Search & Query Metrics
Search request rates (query + fetch), search operation time, node-level indexing rates, and GET operation hit/miss breakdown.

### Cache Metrics
Cache evictions by type, cache memory usage, query cache hit/miss rates at both node and index level.

### Network & Connections
HTTP connections, internal cluster TCP connections, and cluster network I/O throughput.

### Ingest Pipeline
Document ingestion rate, currently ingesting documents, and failed ingest operations.

### Thread Pools
Queued tasks, finished task rates, and thread counts by pool and state.

### Circuit Breakers
Estimated memory usage, configured memory limits, and trip counts by breaker name.

### OS & Process
OS-level memory (free vs used), JVM process CPU usage, process virtual memory, and per-node document counts.
