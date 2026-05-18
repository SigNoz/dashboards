# CloudNativePG Dashboard

This dashboard provides monitoring for [CloudNativePG](https://cloudnative-pg.io/) PostgreSQL clusters running on Kubernetes.

## Panels

### Health
- **Instance Status** — Instance up status (1=up, 0=down) per CNPG instance
- **Uptime (seconds)** — Time since each PostgreSQL instance started

### Connections
- **Connections by State** — Active connections grouped by state (active, idle, idle in transaction, etc.)
- **Max Connections** — Maximum allowed connections per instance

### Database
- **Database Size (bytes)** — Total database size per database and instance
- **Transactions Committed** — Committed transactions per second (rate)

### Replication
- **Replication Lag (seconds)** — Replication delay between primary and replicas
- **Replication Lag (bytes)** — Replication delay in bytes

### WAL Archiving
- **WAL Archived (rate)** — WAL files successfully archived per second
- **WAL Archive Failures (rate)** — Failed WAL archive attempts per second

### Resources
- **CPU Usage (cores)** — Container CPU usage rate
- **Memory Working Set (bytes)** — Container memory usage

### Checkpoints
- **Checkpoint Buffers Written** — Buffers written during checkpoints
- **Checkpoint Write Time (ms)** — Time spent writing checkpoint data

### Operations
- **Deadlocks** — Deadlocks detected per database
- **Tuple Operations (rate)** — Tuples returned/fetched/inserted/updated/deleted

### Locks & Temp
- **Active Locks** — Number of locks by mode
- **Temp Bytes Written (rate)** — Temporary data written to disk

## Variables

| Variable | Description |
|----------|-------------|
| `cnpg_cluster` | CloudNativePG cluster name |
| `cnpg_instance` | CloudNativePG instance name |
| `k8s.node.name` | Kubernetes node name |

## Metrics Source

This dashboard uses metrics from the CloudNativePG metrics exporter. Key metrics:

- `cnpg_collector_up` — Instance health
- `cnpg_collector_pg_postmaster_uptime_seconds` — Instance uptime
- `cnpg_collector_pg_stat_activity_count` — Connection counts
- `cnpg_collector_pg_database_size_bytes` — Database sizes
- `cnpg_collector_pg_replication_lag_seconds` — Replication lag
- `cnpg_collector_pg_stat_archiver_archived_count` — WAL archiver stats
- `cnpg_collector_pg_stat_database_*` — Per-database statistics
- `cnpg_collector_pg_stat_bgwriter_*` — Background writer stats
- `container_cpu_usage_seconds_total` — Container CPU (Kubernetes)
- `container_memory_working_set_bytes` — Container memory (Kubernetes)

## References

- [CloudNativePG Documentation](https://cloudnative-pg.io/documentation/)
- [CNPG Grafana Dashboard](https://github.com/cloudnative-pg/grafana-dashboards)
- [SigNoz Issue #7875](https://github.com/SigNoz/signoz/issues/7875)
