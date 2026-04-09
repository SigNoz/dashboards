# GCP Cloud Functions Monitoring Dashboard

Comprehensive GCP Cloud Functions monitoring dashboard for [SigNoz](https://signoz.io/) using Google Cloud Monitoring metrics.

## Sections

| #   | Section      | Covers                                                     |
| --- | ------------ | ---------------------------------------------------------- |
| 1   | Overview     | Active functions, total invocations, errors, execution time |
| 2   | Invocations  | Rate by function, by status, errors, timeouts, triggers    |
| 3   | Latency      | Execution time p50/p95/p99, by function                    |
| 4   | Resources    | Memory, instances, network egress, CPU                     |
| 5   | Connections  | Outgoing and database connections                          |
| 6   | Billing      | Billable execution time, network egress                    |

## Metrics Ingestion

### Using OpenTelemetry Collector with Google Cloud Monitoring Receiver

```yaml
receivers:
  googlecloudmonitoring:
    project_id: "your-gcp-project"
    collection_interval: 60s
    metrics_list:
      - metric_name: "cloudfunctions.googleapis.com/function/execution_count"
      - metric_name: "cloudfunctions.googleapis.com/function/execution_times"
      - metric_name: "cloudfunctions.googleapis.com/function/active_instances"
      - metric_name: "cloudfunctions.googleapis.com/function/user_memory_bytes"
      - metric_name: "cloudfunctions.googleapis.com/function/network_egress_bytes_count"
      - metric_name: "cloudfunctions.googleapis.com/function/cpu_utilizations"

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "gcp-cloud-functions"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring]
      processors: [batch, resource]
      exporters: [otlp]
```

## Variables

- `{{gcp_project}}`: GCP project ID for filtering metrics
- `{{function_name}}`: Cloud Function name for filtering
