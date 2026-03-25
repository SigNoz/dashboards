# Rancher Kubernetes Control Plane Dashboard

This dashboard provides monitoring for Rancher Kubernetes Control Plane components using OpenTelemetry metrics.

## Panels

| Panel | Description | Metric |
|-------|-------------|--------|
| API Server Request Rate | Request rate across the Kubernetes API server | `apiserver_request_total` |
| API Server Request Latency (p99) | p99 latency of API server requests | `apiserver_request_duration_seconds` |
| etcd WAL Fsync Duration (p99) | p99 WAL fsync latency | `etcd_disk_wal_fsync_duration_seconds` |
| etcd Backend Commit Duration (p99) | p99 backend commit latency | `etcd_disk_backend_commit_duration_seconds` |
| Scheduler Queue Depth | Pending items in the scheduler queue | `scheduler_queue_depth` |
| Controller Manager Work Queue Depth | Pending items in controller manager work queues | `workqueue_depth` |
| Node Ready Count | Number of ready nodes by node name | `k8s.node.condition_ready` |
| Pods by Phase | Pod count grouped by phase (Running, Pending, etc.) | `k8s.pod.phase` |
| CPU Usage | Node CPU utilization | `k8s.node.cpu.utilization` |
| Memory Usage | Node memory utilization | `k8s.node.memory.utilization` |

## Variables

- `k8s.cluster.name` — Select the target Kubernetes cluster
- `k8s.namespace.name` — Filter by namespace (multi-select)

## Metrics Source

Kubernetes control plane metrics collected via the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) with the `k8s_cluster` receiver and `kubeletstats` receiver.

## Data Source

Metrics via OpenTelemetry (OTLP).

## Related

- Issue: [SigNoz/signoz#9628](https://github.com/SigNoz/signoz/issues/9628)
- Reference: [Rancher Monitoring Charts](https://github.com/rancher/charts/tree/dev-v2.12/charts/rancher-monitoring/107.2.2-rc.2%2Bup69.8.2-rancher.26/templates/grafana/dashboards-1.14)
