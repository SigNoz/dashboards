# StackGres PostgreSQL Dashboard - Prometheus

Health and capacity of a [StackGres](https://stackgres.io) SGCluster: Patroni HA and replication, connections and PgBouncer pooling, load and contention, I/O and cache, WAL and archiving, vacuum and growth, and the Kubernetes resources of the cluster pods.

## Metrics Ingestion

The dashboard reads the Prometheus metrics each SGCluster pod already exposes:

- `pg_*` and `pgbouncer_*` from the postgres_exporter sidecar;
- `patroni_*` from the Patroni REST API `/metrics` endpoint;
- `k8s.pod.*` and `k8s.volume.*` from the [`kubeletstats` receiver](https://signoz.io/docs/infrastructure-monitoring/k8s-metrics/) (k8s-infra chart).

Scrape the SGCluster pods with the OpenTelemetry Collector Prometheus receiver and add the `cluster` and `deployment_environment` attributes the dashboard filters on. Check the exporter and Patroni ports in your StackGres version (see the [StackGres monitoring docs](https://stackgres.io/doc/latest/administration/monitoring/)).

```yaml
receivers:
  prometheus/stackgres:
    config:
      scrape_configs:
        - job_name: stackgres
          scrape_interval: 30s
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            # Keep the SGCluster pods only.
            - source_labels: [__meta_kubernetes_pod_label_app]
              regex: StackGresCluster
              action: keep
            - source_labels: [__meta_kubernetes_pod_name]
              target_label: pod
          # Then point the job at the exporter and Patroni metrics ports.

processors:
  resource/stackgres:
    attributes:
      - key: cluster # must match k8s.cluster.name for the Kubernetes panels
        value: <k8s-cluster-name>
        action: upsert
      - key: deployment_environment
        value: <environment>
        action: upsert

service:
  pipelines:
    metrics/stackgres:
      receivers: [prometheus/stackgres]
      processors: [resource/stackgres, batch]
      exporters: [otlp]
```

## Variables

- `{{cluster}}`: Kubernetes cluster (`cluster` label, matched against `k8s.cluster.name` in the Kubernetes panels)
- `{{deployment_environment}}`: Deployment environment
- `{{namespace}}`: `namespace` resource attribute of the StackGres metrics
- `{{pod}}`: SGCluster pods
- `{{datname}}`: Databases

## Dashboard Panels

- **Health & HA (Patroni)**: at-a-glance values for replica lag, connection peak, archive age, failovers in range, PostgreSQL up, Patroni leaders (exactly 1 expected), PgBouncer queue and longest transaction, plus replica lag in seconds over time.
- **Connections & Pool (PgBouncer)**: connection saturation per pod, connections by state, PgBouncer active and waiting clients, longest pool wait.
- **Load & Contention**: transactions per second, rollback rate, longest transaction, queries waiting on locks, deadlocks and recovery conflicts, locks by mode.
- **I/O & Cache** (collapsed): cache hit ratio, temporary file bytes, writes per second, blocks read from disk vs cache.
- **WAL, Archiver & Replication**: WAL size, age of the last archive, replica lag in bytes, replication slot retained WAL, archiver failures.
- **Vacuum, Wraparound & Growth** (collapsed): XID age against `autovacuum_freeze_max_age`, dead tuples per table, size per database, sequential scans per table.
- **Kubernetes Resources**: CPU, memory, PVC usage and network I/O of the SGCluster pods.

Thresholds and panel descriptions explain what each signal means and when to act.
