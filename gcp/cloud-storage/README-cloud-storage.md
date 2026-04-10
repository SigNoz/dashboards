# GCP Cloud Storage Dashboard - OTLP

## Data Ingestion

### Integrate GCP Cloud Storage with OpenTelemetry Collector

To collect GCP Cloud Storage metrics via the OpenTelemetry Collector, you need to configure the `googlecloudmonitoring` receiver to scrape Cloud Storage metrics and export them to SigNoz.

#### Prerequisites

1. A GCP project with Cloud Storage buckets configured.
2. A service account with the `roles/monitoring.viewer` IAM role.
3. OpenTelemetry Collector installed and running.

#### OpenTelemetry Collector Configuration

Add the following to your OpenTelemetry Collector configuration:

```yaml
receivers:
  googlecloudmonitoring:
    collection_interval: 60s
    project_id: "<your-gcp-project-id>"
    metrics_list:
      - metric_name: "storage.googleapis.com/storage/total_bytes"
      - metric_name: "storage.googleapis.com/storage/object_count"
      - metric_name: "storage.googleapis.com/storage/total_byte_seconds"
      - metric_name: "storage.googleapis.com/api/request_count"
      - metric_name: "storage.googleapis.com/api/received_bytes_count"
      - metric_name: "storage.googleapis.com/api/sent_bytes_count"
      - metric_name: "storage.googleapis.com/network/received_bytes_count"
      - metric_name: "storage.googleapis.com/network/sent_bytes_count"
      - metric_name: "storage.googleapis.com/replication/object_count"
      - metric_name: "storage.googleapis.com/replication/bytes_to_replicate"

exporters:
  otlp:
    endpoint: "<signoz-otel-collector-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring]
      exporters: [otlp]
```

Replace `<your-gcp-project-id>` with your GCP project ID and `<signoz-otel-collector-endpoint>` with the address of your SigNoz OTel Collector.

## Dashboard Panels

## Variables

- `{{deployment.environment}}`: The deployment environment for the service.
- `{{project_id}}`: GCP Project ID.
- `{{bucket_name}}`: GCP Cloud Storage bucket name.

### Sections

- Overview
  - Total Storage Bytes - `storage.googleapis.com/storage/total_bytes`
  - Total Object Count - `storage.googleapis.com/storage/object_count`
  - Total Byte Seconds by Storage Class - `storage.googleapis.com/storage/total_byte_seconds`
- Storage Metrics
  - Total Bytes by Bucket - `storage.googleapis.com/storage/total_bytes`
  - Object Count by Bucket - `storage.googleapis.com/storage/object_count`
- API Metrics
  - API Request Count by Method - `storage.googleapis.com/api/request_count`
  - API Request Count by Response Code - `storage.googleapis.com/api/request_count`
  - API Received Bytes - `storage.googleapis.com/api/received_bytes_count`
  - API Sent Bytes - `storage.googleapis.com/api/sent_bytes_count`
- Network Metrics
  - Network Received Bytes - `storage.googleapis.com/network/received_bytes_count`
  - Network Sent Bytes - `storage.googleapis.com/network/sent_bytes_count`
- Replication Metrics
  - Replication Object Count - `storage.googleapis.com/replication/object_count`
  - Bytes Pending Replication - `storage.googleapis.com/replication/bytes_to_replicate`
