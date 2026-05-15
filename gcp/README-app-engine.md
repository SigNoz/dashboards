# GCP App Engine Monitoring Dashboard - Prometheus

Comprehensive GCP App Engine monitoring dashboard for [SigNoz](https://signoz.io/) using Google Cloud Monitoring metrics via the OpenTelemetry Google Cloud exporter.

## Sections

| #   | Section             | Covers                                                    |
| --- | ------------------- | --------------------------------------------------------- |
| 1   | Overview            | Active instances, request count, error rate, response time |
| 2   | HTTP Performance    | Request rate, latency percentiles, error rates by code    |
| 3   | Instance Management | Instance count, memory/CPU per instance, startup latency  |
| 4   | Network             | Bytes sent/received, bandwidth per version                |
| 5   | Memcache            | Hit ratio, operations/sec, size, item count               |
| 6   | Task Queue          | Queue depth, execution rate, retry count, task age        |
| 7   | Costs & Quotas      | Billable instance hours, API calls by service             |

## Metrics Ingestion

### Using OpenTelemetry Collector with Google Cloud Monitoring Receiver

```yaml
receivers:
  googlecloudmonitoring:
    project_id: "your-gcp-project"
    collection_interval: 60s
    metrics_list:
      - metric_name: "appengine.googleapis.com/http/server/response_count"
      - metric_name: "appengine.googleapis.com/http/server/response_latencies"
      - metric_name: "appengine.googleapis.com/system/instance_count"
      - metric_name: "appengine.googleapis.com/system/cpu/usage"
      - metric_name: "appengine.googleapis.com/system/memory/usage"
      - metric_name: "appengine.googleapis.com/system/network/sent_bytes_count"
      - metric_name: "appengine.googleapis.com/system/network/received_bytes_count"
      - metric_name: "appengine.googleapis.com/memcache/hit_ratio"
      - metric_name: "appengine.googleapis.com/task_queue/queue_depth"

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "gcp-app-engine"
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
