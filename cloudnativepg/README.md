# CloudNativePG Dashboard - Prometheus

Comprehensive monitoring dashboard for [CloudNativePG](https://cloudnative-pg.io/) (CNPG) PostgreSQL clusters running on Kubernetes. This dashboard provides visibility into cluster health, replication, WAL archiving, database activity, storage, checkpoints, buffer cache, locks, backups, PgBouncer connection pooling, and Kubernetes resource usage.

## Metrics Ingestion

CloudNativePG exposes Prometheus metrics natively via its built-in monitoring exporter. To collect these metrics in SigNoz, configure the OpenTelemetry Collector with a Prometheus receiver.

### 1. Enable Monitoring in CloudNativePG

Ensure your CNPG `Cluster` resource has monitoring enabled:

```yaml
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: my-cluster
  namespace: cnpg-system
spec:
  instances: 3
  monitoring:
    enablePodMonitor: true
    customQueriesConfigMap:
      - name: cnpg-default-monitoring
        key: queries
```

### 2. Configure OpenTelemetry Collector

Add the following receiver to your `otel-collector-config.yaml`:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'cloudnativepg'
          scrape_interval: 30s
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_cnpg_io_cluster]
              action: keep
              regex: .+
            - source_labels: [__meta_kubernetes_namespace]
              target_label: namespace
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
            - source_labels: [__meta_kubernetes_pod_label_cnpg_io_cluster]
              target_label: cluster
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
              action: replace
              target_label: __address__
              regex: (.+)
              replacement: ${1}:9187

exporters:
  otlp:
    endpoint: "<signoz-otel-collector-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

Replace `<signoz-otel-collector-endpoint>` with your SigNoz OTel Collector address (e.g., `signoz-otel-collector.signoz.svc.cluster.local`).

### 3. PgBouncer Metrics (Optional)

If you use PgBouncer with CNPG, enable it in your cluster spec:

```yaml
spec:
  monitoring:
    enablePodMonitor: true
  postgresql:
    pg_hba:
      - host all all 0.0.0.0/0 md5
  managed:
    roles: []
  # PgBouncer pooler
---
apiVersion: postgresql.cnpg.io/v1
kind: Pooler
metadata:
  name: my-cluster-pooler
spec:
  cluster:
    name: my-cluster
  instances: 2
  type: rw
  pgbouncer:
    poolMode: transaction
    monitoring:
      enablePodMonitor: true
```

### 4. Kubernetes Resource Metrics (Optional)

For CPU, memory, and PVC metrics panels, ensure you have the following collectors configured:

```yaml
receivers:
  kubeletstats:
    collection_interval: 30s
    auth_type: serviceAccount
    endpoint: "https://${K8S_NODE_NAME}:10250"
    insecure_skip_verify: true
    metric_groups:
      - container
      - pod
      - volume
```

## Variables

- `{{namespace}}` - Kubernetes namespace where CloudNativePG clusters are deployed
- `{{cluster}}` - CloudNativePG cluster name (maps to the `cnpg.io/cluster` label)
- `{{instance}}` - CloudNativePG pod/instance name (supports multi-select)

## Dashboard Panels

### Cluster Overview
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Total Instances | Value | Total CNPG instances | `cnpg_collector_up` |
| Ready Instances | Value | Instances that are up and serving | `cnpg_collector_up == 1` |
| Not Ready Instances | Value | Instances that are down (threshold alert if > 0) | `cnpg_collector_up == 0` |
| Current Primary | Value | Identifies the current primary instance | `cnpg_pg_replication_in_recovery == 0` |
| Collector Up Status | Graph | Instance availability over time | `cnpg_collector_up` |
| Instance Roles | Graph | Primary vs replica role per instance | `cnpg_pg_replication_in_recovery` |
| PostgreSQL Up | Graph | PostgreSQL postmaster availability | `cnpg_pg_postmaster_start_time` |
| Switchover Count | Value | Failover/switchover events in last hour | `changes(cnpg_pg_replication_in_recovery[1h])` |

### Replication & WAL
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Replication Lag (bytes) | Graph | Byte lag between primary and replicas | `cnpg_pg_replication_lag` |
| Replication Lag (seconds) | Graph | Write, flush, and replay lag in seconds | `cnpg_pg_replication_replay_lag_seconds`, `write_lag`, `flush_lag` |
| WAL Sent vs Received | Graph | LSN positions for sent/written/replayed WAL | `cnpg_pg_replication_sent_lsn`, `write_lsn`, `replay_lsn` |
| WAL Archiving Rate | Graph | Archive success/failure rate | `cnpg_pg_stat_archiver_archived_count`, `failed_count` |
| WAL Files Archived | Graph | Cumulative archived WAL files | `cnpg_pg_stat_archiver_archived_count` |
| WAL Archiving Failures | Graph | Cumulative failed archival attempts | `cnpg_pg_stat_archiver_failed_count` |
| Seconds Since Last Archival | Graph | Time since last successful archival | `cnpg_pg_stat_archiver_last_archived_time` |
| Current WAL LSN | Graph | Current and insert WAL positions | `cnpg_pg_wal_current_lsn`, `insert_lsn` |
| Streaming Replication Connected | Graph | Active streaming replication connections | `cnpg_pg_replication_streaming_replicas` |
| Replication Slots | Graph | Active and inactive replication slots | `cnpg_pg_replication_slots_active`, `inactive` |

### Database Activity
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Active Connections | Graph | Currently active connections | `cnpg_pg_stat_activity_connections{state="active"}` |
| Connections by State | Graph | Stacked view of all connection states | `cnpg_pg_stat_activity_connections` |
| Max Connections | Graph | Max allowed vs current connections | `cnpg_pg_settings_setting{name="max_connections"}` |
| Transactions Per Second | Graph | Commit and rollback rates | `cnpg_pg_stat_database_xact_commit`, `xact_rollback` |
| Transactions Committed | Graph | Cumulative committed transactions | `cnpg_pg_stat_database_xact_commit` |
| Transactions Rolled Back | Graph | Cumulative rolled-back transactions | `cnpg_pg_stat_database_xact_rollback` |
| Waiting Connections | Graph | Connections waiting for locks | `cnpg_pg_stat_activity_connections{state="waiting"}` |
| Idle in Transaction | Graph | Idle-in-transaction connections | `cnpg_pg_stat_activity_connections{state="idle in transaction"}` |

### Database Size & Storage
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Database Size | Graph | Size per database per instance | `cnpg_pg_database_size_bytes` |
| Database Size Growth Rate | Graph | Rate of size growth per hour | `deriv(cnpg_pg_database_size_bytes[1h])` |
| Total Database Size | Value | Sum of all databases per instance | `sum(cnpg_pg_database_size_bytes)` |
| Table Bloat Estimate | Graph | Dead-to-live tuple ratio per table | `n_dead_tup / (n_live_tup + 1)` |
| Disk Usage by Tablespace | Graph | Size per tablespace | `cnpg_pg_tablespace_size_bytes` |
| Temporary File Size | Graph | Temp file bytes per database | `cnpg_pg_stat_database_temp_bytes` |
| Temporary Files Created Rate | Graph | Rate of temp file creation | `cnpg_pg_stat_database_temp_files` |

### Checkpoint & Maintenance
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Checkpoints Requested vs Timed | Graph | Forced vs scheduled checkpoints | `cnpg_pg_stat_bgwriter_checkpoints_timed`, `checkpoints_req` |
| Checkpoint Write Time | Graph | Milliseconds spent writing in checkpoints | `cnpg_pg_stat_bgwriter_checkpoint_write_time` |
| Checkpoint Sync Time | Graph | Milliseconds spent syncing in checkpoints | `cnpg_pg_stat_bgwriter_checkpoint_sync_time` |
| Buffers Written by Checkpoint | Graph | Buffers written by checkpoint, backend, bgwriter | `buffers_checkpoint`, `buffers_backend`, `buffers_clean` |
| Autovacuum Workers Active | Graph | Currently running autovacuum workers | `cnpg_pg_stat_activity_connections{backend_type="autovacuum worker"}` |
| Dead Tuples by Table | Graph | Top 10 tables by dead tuple count | `cnpg_pg_stat_user_tables_n_dead_tup` |
| Last Autovacuum Time | Graph | Seconds since last autovacuum per table | `cnpg_pg_stat_user_tables_last_autovacuum` |
| Last Autoanalyze Time | Graph | Seconds since last autoanalyze per table | `cnpg_pg_stat_user_tables_last_autoanalyze` |

### Buffer Cache & I/O Performance
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Cache Hit Ratio | Graph | Buffer cache hit % (target: >99%) | `blks_hit / (blks_hit + blks_read)` |
| Blocks Read vs Hit | Graph | Disk reads vs buffer hits rate | `cnpg_pg_stat_database_blks_read`, `blks_hit` |
| Backend Buffers Written | Graph | Buffers written directly by backends | `cnpg_pg_stat_bgwriter_buffers_backend` |
| Backend Fsync Count | Graph | Fsyncs by backends (should be 0) | `cnpg_pg_stat_bgwriter_buffers_backend_fsync` |
| Rows Fetched Rate | Graph | Rows returned by queries | `cnpg_pg_stat_database_tup_fetched` |
| Rows Inserted Rate | Graph | Row insert rate per database | `cnpg_pg_stat_database_tup_inserted` |
| Rows Updated Rate | Graph | Row update rate per database | `cnpg_pg_stat_database_tup_updated` |
| Rows Deleted Rate | Graph | Row delete rate per database | `cnpg_pg_stat_database_tup_deleted` |

### Locks & Conflicts
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Locks by Mode | Graph | Stacked lock count per mode | `cnpg_pg_locks_count` |
| Exclusive Locks | Graph | AccessExclusive and Exclusive locks | `cnpg_pg_locks_count{mode=~".*Exclusive.*"}` |
| Deadlocks | Graph | Deadlock detection rate | `cnpg_pg_stat_database_deadlocks` |
| Conflicts | Graph | Query cancellations from recovery conflicts | `cnpg_pg_stat_database_conflicts` |
| Waiting Queries | Graph | Queries blocked on lock waits | `cnpg_pg_stat_activity_connections{wait_event_type="Lock"}` |
| Long Running Queries | Graph | Queries running > 5 minutes | `cnpg_pg_long_running_queries` |

### Backup & Recovery
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| Last Backup Duration | Value | Duration of most recent backup | `cnpg_pg_last_backup_duration_seconds` |
| Time Since Last Backup | Graph | Seconds since last successful backup | `cnpg_pg_last_backup_timestamp` |
| Backup Size | Value | Size of most recent backup | `cnpg_pg_last_backup_size_bytes` |
| WAL Segment Size | Value | WAL segment file size | `cnpg_pg_wal_segment_size_bytes` |
| Last Backup Success | Graph | Backup success/failure status | `cnpg_pg_last_backup_success` |
| Backup History Timeline | Graph | Historical backup durations | `cnpg_pg_last_backup_duration_seconds` |

### PgBouncer Connection Pooling
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| PgBouncer Active Connections | Graph | Active server connections in pools | `cnpg_pgbouncer_pool_server_active_connections` |
| PgBouncer Client Connections | Graph | Client active and waiting connections | `cnpg_pgbouncer_pool_client_active_connections`, `waiting` |
| PgBouncer Server Idle | Graph | Idle server connections available | `cnpg_pgbouncer_pool_server_idle_connections` |
| PgBouncer Max Wait Time | Graph | Maximum client wait time for a connection | `cnpg_pgbouncer_pool_max_wait_seconds` |
| PgBouncer Total Queries | Graph | Query throughput via PgBouncer | `cnpg_pgbouncer_stats_queries_total` |
| PgBouncer Query Duration | Graph | Average query duration | `cnpg_pgbouncer_stats_query_avg_duration_seconds` |
| PgBouncer Bytes In/Out | Graph | Data throughput via PgBouncer | `cnpg_pgbouncer_stats_received_bytes_total`, `sent_bytes` |
| PgBouncer Login Connections | Graph | Connections in login phase | `cnpg_pgbouncer_pool_server_login_connections` |

### Resource Usage (Kubernetes)
| Panel | Type | Description | Key Metrics |
|-------|------|-------------|-------------|
| CPU Usage by Pod | Graph | Per-pod CPU consumption | `container_cpu_usage_seconds_total` |
| Memory Usage by Pod | Graph | Per-pod RSS memory | `container_memory_rss` |
| Memory Working Set | Graph | Working set memory (OOM trigger) | `container_memory_working_set_bytes` |
| PVC Usage | Graph | Persistent volume used bytes | `kubelet_volume_stats_used_bytes` |
| PVC Available Space | Graph | Available PVC space | `kubelet_volume_stats_available_bytes` |
| PVC Capacity | Graph | Total capacity vs used | `kubelet_volume_stats_capacity_bytes` |
| Network Receive Rate | Graph | Pod network ingress | `container_network_receive_bytes_total` |
| Network Transmit Rate | Graph | Pod network egress | `container_network_transmit_bytes_total` |

## References

- [CloudNativePG Documentation](https://cloudnative-pg.io/documentation/)
- [CloudNativePG Monitoring](https://cloudnative-pg.io/documentation/current/monitoring/)
- [CloudNativePG Grafana Dashboard](https://github.com/cloudnative-pg/grafana-dashboards)
- [CNPG Prometheus Metrics Reference](https://cloudnative-pg.io/documentation/current/metrics_reference/)
- [SigNoz Documentation](https://signoz.io/docs/)
- [OpenTelemetry Collector Prometheus Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/prometheusreceiver)
