# Elasticsearch Monitoring Dashboard for SigNoz

Pre-built SigNoz dashboard for monitoring Elasticsearch clusters using OpenTelemetry Collector metrics (elasticsearch receiver from opentelemetry-collector-contrib).

## Sections

- **Node Metrics** -- CPU operations time rate, cache memory usage, disk available/total, JVM heap used/max
- **Cluster Health** -- Cluster health status, shards by state, relocating shards, pending tasks
- **Index Performance** -- Indexing rate, index operations rate, document count, refresh and flush rate
- **Search & Query Performance** -- Search rate, search latency (avg ms/op via formula), query cache memory, fetch/get rate

## Metrics Used

All metrics come from the OpenTelemetry Collector `elasticsearch` receiver:

| Metric | Type | Description |
|--------|------|-------------|
| `elasticsearch.node.operations.completed` | Sum | Completed operations by type (index, search, get, delete, refresh, flush) |
| `elasticsearch.node.operations.time` | Sum | Time spent on operations by type |
| `elasticsearch.cluster.health` | Gauge | Cluster health status (0=green, 1=yellow, 2=red) |
| `elasticsearch.cluster.shards` | Gauge | Shard counts by state |
| `elasticsearch.node.fs.disk.available` | Gauge | Available disk space per node |
| `elasticsearch.node.fs.disk.total` | Gauge | Total disk space per node |
| `elasticsearch.cluster.pending_tasks` | Gauge | Pending cluster tasks |
| `elasticsearch.node.cache.memory.usage` | Gauge | Cache memory by cache name |
| `elasticsearch.node.documents` | Gauge | Document count per node |
| `elasticsearch.index.operations.completed` | Sum | Index-level operation counts |
| `jvm.memory.heap.used` | Gauge | JVM heap memory used |
| `jvm.memory.heap.max` | Gauge | JVM heap memory maximum |

## Installation

Import `elasticsearch-otlp-v1.json` into SigNoz via Settings > Dashboards > Import JSON.

## Variable

The dashboard includes a `deployment.environment` variable for filtering by environment.
