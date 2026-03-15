# Elasticsearch Monitoring Dashboard

## Metrics Ingestion

### Elasticsearch Receiver
This dashboard uses metrics from the [OpenTelemetry Elasticsearch receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/elasticsearchreceiver), which collects metrics from Elasticsearch's node stats, cluster health, and index stats APIs.

### Configure OpenTelemetry Collector

1. Add the Elasticsearch receiver to the `receivers:` section:

```yaml
  elasticsearch:
    endpoint: http://localhost:9200
    collection_interval: 60s
    # Optional: authentication
    # username: elastic
    # password: changeme
```

2. Complete Configuration Example

Below is a complete `otel-config.yaml` example:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  hostmetrics:
    collection_interval: 60s
    scrapers:
      cpu: {}
      disk: {}
      load: {}
      filesystem: {}
      memory: {}
      network: {}
      paging: {}
      process:
        mute_process_name_error: true
        mute_process_exe_error: true
        mute_process_io_error: true
      processes: {}
  elasticsearch:
    endpoint: http://localhost:9200
    collection_interval: 60s
    # Uncomment for authentication:
    # username: elastic
    # password: changeme

processors:
  batch:
    send_batch_size: 1000
    timeout: 10s
  resourcedetection:
    detectors: [env, system]
    timeout: 2s
    system:
      hostname_sources: [os]
  resource/env:
    attributes:
    - key: deployment.environment
      value: staging
      action: upsert

extensions:
  health_check: {}
  zpages: {}

exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "your-ingestion-key"
  logging:
    verbosity: normal

service:
  telemetry:
    metrics:
      address: 0.0.0.0:8888
  extensions: [health_check, zpages]
  pipelines:
    metrics:
      receivers: [otlp, elasticsearch]
      processors: [resource/env, batch]
      exporters: [otlp]
    metrics/internal:
      receivers: [hostmetrics]
      processors: [resource/env, resourcedetection, batch]
      exporters: [otlp]
    traces:
      receivers: [otlp]
      processors: [resource/env, batch]
      exporters: [otlp]
    logs:
      receivers: [otlp]
      processors: [resource/env, batch]
      exporters: [otlp]
```

## Variables

- `{{deployment.environment}}`: Deployment environment (e.g., production, staging)
- `{{elasticsearch.node.name}}`: Elasticsearch node name
- `{{elasticsearch.cluster.name}}`: Elasticsearch cluster name

## Sections

- Node Metrics
  - Node Disk Usage — `elasticsearch.node.fs.disk.total`
  - Node Disk Free — `elasticsearch.node.fs.disk.free`
  - Node Disk Available — `elasticsearch.node.fs.disk.available`
  - Node CPU Usage — `elasticsearch.os.cpu.usage`
  - Node JVM Memory Usage — `jvm.memory.heap.used`, `jvm.memory.nonheap.used`
  - Node Heap Memory Usage — `jvm.memory.heap.used`, `jvm.memory.heap.max`
- Cluster Health Metrics
  - Cluster Health Status — `elasticsearch.cluster.health`
  - Cluster Active Shards — `elasticsearch.cluster.shards` (active)
  - Cluster Pending Tasks — `elasticsearch.cluster.pending_tasks`
  - Cluster Unassigned Shards — `elasticsearch.cluster.shards` (unassigned)
- Index Metrics
  - Index Document Count — `elasticsearch.index.documents`
  - Index Disk Usage — `elasticsearch.index.shards.size`
  - Index Search Query Count — `elasticsearch.index.operations.completed` (query)
  - Index Search Query Time — `elasticsearch.index.operations.time` (query)
- Query and Request Metrics
  - Search Request Rate — `elasticsearch.node.operations.completed` (query)
  - Query Latency — `elasticsearch.node.operations.time` / `elasticsearch.node.operations.completed`
  - Indexing Request Rate — `elasticsearch.node.operations.completed` (index)
  - Fetch Request Rate — `elasticsearch.node.operations.completed` (fetch)
- Cache Metrics
  - Cache Evictions — `elasticsearch.node.cache.evictions`
  - Cache Hit Count — `elasticsearch.node.cache.count` (hit)
  - Cache Miss Count — `elasticsearch.node.cache.count` (miss)
  - Cache Memory Usage — `elasticsearch.node.cache.memory.usage`

## References

- [OTel Elasticsearch Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/elasticsearchreceiver)
- [Available Metrics (metadata.yaml)](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/elasticsearchreceiver/metadata.yaml)
- [Elasticsearch Node Stats API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html)
- [Elasticsearch Cluster Health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html)
