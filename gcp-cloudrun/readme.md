# GCP Cloud Run Dashboard - OTLP

## Overview

This dashboard provides comprehensive monitoring for Google Cloud Run services using OpenTelemetry (OTLP) metrics collected from Google Cloud Monitoring. It covers request traffic, latency, container lifecycle, resource utilization, and billing.

## Metrics Ingestion

To ingest GCP Cloud Run metrics into SigNoz, configure the Google Cloud Monitoring receiver in your OpenTelemetry Collector:

```yaml
receivers:
  googlecloudmonitoring:
    collection_interval: 60s
    project_id: "your-gcp-project-id"
    metrics_list:
      - run.googleapis.com/request_count
      - run.googleapis.com/request_latencies
      - run.googleapis.com/container/instance_count
      - run.googleapis.com/container/cpu/utilization
      - run.googleapis.com/container/memory/utilization
      - run.googleapis.com/container/billable_instance_time
      - run.googleapis.com/container/startup_latencies

service:
  pipelines:
    metrics:
      receivers: [googlecloudmonitoring]
      exporters: [otlp]
```

Ensure GCP credentials are configured via `GOOGLE_APPLICATION_CREDENTIALS` environment variable or Workload Identity.

## Variables

- `{{service_name}}`: Cloud Run service name — filters all panels by the selected service.

## Dashboard Sections and Panels

### Overview

| Panel | Metric | Description |
|-------|--------|-------------|
| Total Requests | `run.googleapis.com/request_count` | Current request rate (requests/sec) |
| Active Instances | `run.googleapis.com/container/instance_count` | Number of active container instances |
| CPU Utilization | `run.googleapis.com/container/cpu/utilization` | Current CPU utilization percentage |
| Memory Utilization | `run.googleapis.com/container/memory/utilization` | Current memory utilization percentage |

### Request Metrics

| Panel | Metric | Description |
|-------|--------|-------------|
| Request Rate | `run.googleapis.com/request_count` | Requests per second, grouped by response code |
| Request Latency | `run.googleapis.com/request_latencies` | Request latency over time |
| Error Rate | `run.googleapis.com/request_count` | 5xx error rate |

### Container Metrics

| Panel | Metric | Description |
|-------|--------|-------------|
| Container Instance Count | `run.googleapis.com/container/instance_count` | Active instances over time |
| Container Startup Latency | `run.googleapis.com/container/startup_latencies` | Cold start / container startup time |

### Resource Utilization

| Panel | Metric | Description |
|-------|--------|-------------|
| CPU Utilization | `run.googleapis.com/container/cpu/utilization` | CPU usage over time |
| Memory Utilization | `run.googleapis.com/container/memory/utilization` | Memory usage over time |

### Billing & Cost

| Panel | Metric | Description |
|-------|--------|-------------|
| Billable Instance Time | `run.googleapis.com/container/billable_instance_time` | Billable seconds consumed |

## References

- [GCP Cloud Run Metrics Documentation](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-run)
- [SigNoz Dashboard Templates](https://signoz.io/docs/dashboards/dashboard-templates/overview/)
- [Issue #6388](https://github.com/SigNoz/signoz/issues/6388)
