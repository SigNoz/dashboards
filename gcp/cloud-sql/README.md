# GCP Cloud SQL Monitoring Dashboard

This dashboard provides comprehensive monitoring for Google Cloud Platform Cloud SQL instances. It covers both PostgreSQL and MySQL engine variants using OpenTelemetry metrics exported from GCP.

## Overview

The dashboard includes 5 sections and 15 metric panels:

| Section | Panels | Description |
|---------|--------|-------------|
| Overview | CPU, Memory, Disk Utilization, Disk Bytes | Instance-level resource consumption |
| Network | Bytes Received, Bytes Sent, Active Connections | Network throughput and connection monitoring |
| PostgreSQL Metrics | Backends, Blocks Read, Cache Hits, Transactions | PostgreSQL-specific performance indicators |
| MySQL Metrics | Queries/sec, InnoDB Pages, Replication Lag | MySQL-specific performance indicators |
| Replication | Replica Byte Lag | Cross-engine replication health |

## Prerequisites

### 1. Enable GCP Cloud SQL Export

Export Cloud SQL metrics to Google Cloud Monitoring (formerly Stackdriver), then forward them to your OpenTelemetry collector using the [GoogleCloud exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/googlecloudexporter) or the [GCP receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/googlecloudmonitoringreceiver).

### 2. OTel Collector Configuration

Configure the GCP receiver in your `otel-collector-config.yaml`:

```yaml
receivers:
  googlecloudmonitoring:
    project_id: your-gcp-project-id
    collection_interval: 60s
    metric_prefixes:
      - "cloudsql.googleapis.com"

processors:
  resourcedetection:
    detectors: [gcp]
  batch:
    timeout: 30s

exporters:
  otlp:
    endpoint: "your-signoz-host:4317"

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring]
      processors: [resourcedetection, batch]
      exporters: [otlp]
```

## Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by environment (production, staging, etc.) |
| `project_id` | GCP Project ID |
| `database_id` | Cloud SQL instance identifier (format: `project:region:instance`) |

## Metrics Covered

### Overview Metrics

| Metric | Description |
|--------|-------------|
| `cloudsql.googleapis.com/database/cpu/utilization` | CPU utilization fraction (0.0–1.0) |
| `cloudsql.googleapis.com/database/memory/utilization` | Memory utilization fraction (0.0–1.0) |
| `cloudsql.googleapis.com/database/disk/utilization` | Disk quota utilization fraction (0.0–1.0) |
| `cloudsql.googleapis.com/database/disk/bytes_used` | Disk space used in bytes |

### Network Metrics

| Metric | Description |
|--------|-------------|
| `cloudsql.googleapis.com/database/network/received_bytes_count` | Delta bytes received per interval |
| `cloudsql.googleapis.com/database/network/sent_bytes_count` | Delta bytes sent per interval |
| `cloudsql.googleapis.com/database/network/connections` | Number of active connections |

### PostgreSQL-Specific Metrics

| Metric | Description |
|--------|-------------|
| `cloudsql.googleapis.com/database/postgresql/num_backends` | Active backend connections |
| `cloudsql.googleapis.com/database/postgresql/blks_read_count` | Disk blocks read (delta) |
| `cloudsql.googleapis.com/database/postgresql/blks_hit_count` | Buffer cache hits (delta) |
| `cloudsql.googleapis.com/database/postgresql/transaction_count` | Committed transactions (delta) |

### MySQL-Specific Metrics

| Metric | Description |
|--------|-------------|
| `cloudsql.googleapis.com/database/mysql/queries` | Statement executions (delta) |
| `cloudsql.googleapis.com/database/mysql/innodb_pages_read` | InnoDB pages read (delta) |
| `cloudsql.googleapis.com/database/mysql/replication/seconds_behind_master` | Seconds replica is behind primary |

### Replication

| Metric | Description |
|--------|-------------|
| `cloudsql.googleapis.com/database/replication/replica_byte_lag` | Byte lag of read replica behind primary |

## Import Instructions

1. Open SigNoz UI and navigate to **Dashboards**
2. Click **New Dashboard** → **Import JSON**
3. Upload `gcp-cloud-sql-otlp-v1.json`
4. Set the `project_id` and `database_id` variables to match your GCP environment

## Related Dashboards

- [GCP Compute Engine](../compute-engine/) — VM instance metrics
- [PostgreSQL](../../postgresql/) — Self-hosted PostgreSQL metrics
- [MySQL](../../mysql/) — Self-hosted MySQL metrics (if available)
