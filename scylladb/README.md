# ScyllaDB Dashboard - Prometheus

A node-level overview dashboard for ScyllaDB, built on the `scylla_*` metrics that
ScyllaDB exposes through its built-in Prometheus endpoint (default port `9180`).

## Metrics Ingestion

ScyllaDB serves Prometheus metrics on `:9180/metrics` by default. Point an
OpenTelemetry Collector Prometheus receiver at it and forward the result to SigNoz.

```yaml
receivers:
  prometheus/scylla:
    config:
      scrape_configs:
        - job_name: scylla
          scrape_interval: 30s
          static_configs:
            - targets: ["scylla-node-1:9180", "scylla-node-2:9180"]

processors:
  batch: {}

exporters:
  otlp:
    endpoint: "<your-signoz-collector>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus/scylla]
      processors: [batch]
      exporters: [otlp]
```

The Prometheus port can be changed (or disabled) in `scylla.yaml`:

```yaml
prometheus_port: 9180
prometheus_address: 0.0.0.0
```

Nothing in this dashboard is Scylla-specific to SigNoz — it reads the standard
`prometheus` receiver output, so any collector that lands `scylla_*` metrics in SigNoz
will populate it.

## Variables

- `{{host.name}}`: Filters every panel to one or more ScyllaDB nodes. Populated
  dynamically from the hosts that report `scylla_*` metrics.

## Dashboard Panels

| Panel | Metric | Why it matters |
| --- | --- | --- |
| CPU Utilization | `scylla_reactor_utilization` | Sustained values near 100% mean the node is CPU-bound and will start queueing requests. |
| Served Requests /s | `scylla_transport_requests_served` | Overall CQL throughput handled by each node. |
| CQL Inserts /s | `scylla_cql_inserts` | Write path throughput, including conditional inserts. |
| CQL Updates /s | `scylla_cql_updates` | Update throughput, including conditional updates. |
| CQL Deletes /s | `scylla_cql_deletes` | Delete throughput, including conditional deletes. |
| CQL Batches /s | `scylla_cql_batches` | Batch rate; large batches are a common cause of latency spikes. |
| Client Connections | `scylla_transport_cql_connections` | Open driver connections per node; uneven distribution points at driver or topology issues. |
| Cache Memory Used | `scylla_cache_bytes_used` | Row cache footprint against the configured capacity. |
| Cache Row Hits /s | `scylla_cache_row_hits` | Rows served from cache rather than disk. |
| Cache Row Misses /s | `scylla_cache_row_misses` | Rows that fell through to SSTables; rising misses drive I/O latency. |

Counter metrics are charted with a `rate` time aggregation over a 60 s step, so the
values are per-second throughput rather than ever-growing totals. Gauge metrics
(`reactor_utilization`, `cql_connections`, `cache_bytes_used`) are averaged within each
step. Series are grouped by `host.name` so a single node can be isolated in the legend.

## Known gaps

Latency panels are deliberately not included in this first version.
`scylla_storage_proxy_coordinator_read_latency` and `..._write_latency` are Prometheus
**histograms**, and reducing them correctly (quantiles over bucketed series) needs a
dedicated histogram query that this dashboard does not yet model. Charting them with a
plain `rate()` would produce a meaningless number, so they are left out rather than
shipped wrong. Adding proper p50/p99 latency panels is the natural next increment.