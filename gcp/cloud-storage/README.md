# GCP Cloud Storage Monitoring Dashboard

This dashboard monitors Google Cloud Storage (GCS) bucket activity using OpenTelemetry metrics from the GCP monitoring receiver.

## Dashboard Details

**File:** `gcp-cloud-storage-otlp-v1.json`
**Format:** SigNoz v3 OTLP
**Panels:** 5 panels across 3 sections

## Sections

| Section | Panels |
|---------|--------|
| Storage | Total bytes stored, Object count |
| Requests | API request count by method/response code |
| Network | Bytes received, Bytes sent |

## Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by environment |
| `project_id` | GCP Project ID |
| `bucket_name` | GCS Bucket name to monitor |

## Metrics Covered

| Metric | Description |
|--------|-------------|
| `storage.googleapis.com/storage/total_bytes` | Total bytes stored in bucket |
| `storage.googleapis.com/storage/object_count` | Total objects in bucket |
| `storage.googleapis.com/storage/api/request_count` | API requests (delta) |
| `storage.googleapis.com/storage/network/received_bytes_count` | Bytes received (delta) |
| `storage.googleapis.com/storage/network/sent_bytes_count` | Bytes sent (delta) |

## Setup

Configure the GCP monitoring receiver in your OTel collector:

```yaml
receivers:
  googlecloudmonitoring:
    project_id: your-gcp-project-id
    collection_interval: 60s
    metric_prefixes:
      - "storage.googleapis.com"

exporters:
  otlp:
    endpoint: "your-signoz-host:4317"

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring]
      exporters: [otlp]
```

## Related Issues

- [SigNoz/signoz#6385](https://github.com/SigNoz/signoz/issues/6385) — GCP Cloud Storage Dashboard Request
