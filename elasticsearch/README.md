# Elasticsearch Monitoring Dashboard

A comprehensive SigNoz dashboard for monitoring Elasticsearch clusters, nodes, indices, and query performance using the **OpenTelemetry Elasticsearch receiver**.

## Panels

### Node Metrics
| Panel | Metric | Description |
|---|---|---|
| Node Disk Total | `elasticsearch.node.fs.disk.total` | Total disk space per node |
| Node Disk Free | `elasticsearch.node.fs.disk.free` | Free disk space per node |
| Node Disk Available | `elasticsearch.node.fs.disk.available` | Disk available to the JVM per node |
| Node CPU Usage | `elasticsearch.os.cpu.usage` | OS-level CPU usage % per node |
| JVM Heap Memory Used | `jvm.memory.heap.used` | JVM heap memory in use per node |
| JVM Non-Heap Memory Used | `jvm.memory.nonheap.used` | JVM non-heap memory in use per node |

### Cluster Health Metrics
| Panel | Metric | Description |
|---|---|---|
| Cluster Health Status | `elasticsearch.cluster.health` | Health status grouped by green/yellow/red |
| Active Shards | `elasticsearch.cluster.shards` | Number of active shards |
| Cluster Pending Tasks | `elasticsearch.cluster.pending_tasks` | Unexecuted cluster-level changes |
| Unassigned Shards | `elasticsearch.cluster.shards` | Shards not assigned to any node |
| Total Nodes | `elasticsearch.cluster.nodes` | Total nodes in the cluster |
| In-Flight Fetches | `elasticsearch.cluster.in_flight_fetch` | Ongoing shard info requests |

### Index Metrics
| Panel | Metric | Description |
|---|---|---|
| Index Document Count | `elasticsearch.index.documents` | Active documents per index |
| Index Shard Size | `elasticsearch.index.shards.size` | Estimated disk usage per index |

### Query and Request Metrics
| Panel | Metric | Description |
|---|---|---|
| Query Operations Rate | `elasticsearch.node.operations.completed` | Query ops/sec per node |
| Fetch Operations Rate | `elasticsearch.node.operations.completed` | Fetch ops/sec per node |
| Index Operations Rate | `elasticsearch.node.operations.completed` | Index ops/sec per node |
| Query Latency | `elasticsearch.node.operations.time` | Time spent on query operations |
| Fetch Latency | `elasticsearch.node.operations.time` | Time spent on fetch operations |
| Indexing Latency | `elasticsearch.node.operations.time` | Time spent on index operations |

## Prerequisites

1. **SigNoz** running (v0.30+ recommended)
2. **OpenTelemetry Collector** with the `elasticsearchreceiver` configured:

```yaml
receivers:
  elasticsearch:
    endpoint: http://localhost:9200
    collection_interval: 60s
    # username: elastic       # if authentication is enabled
    # password: changeme

service:
  pipelines:
    metrics:
      receivers: [elasticsearch]
      exporters: [otlp]
```

See the [OpenTelemetry Elasticsearch Receiver docs](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/elasticsearchreceiver) for full configuration options.

## Importing into SigNoz

1. Open SigNoz → **Dashboards** → **New Dashboard**
2. Click **Import JSON**
3. Upload or paste the contents of `elasticsearch-otlp-v1.json`
4. Click **Import**

## Template Variables

| Variable | Description |
|---|---|
| `elasticsearch.node.name` | Filter all node-level panels by specific node(s) |

## Related Issues

- Fixes [SigNoz/signoz#6010](https://github.com/SigNoz/signoz/issues/6010)
