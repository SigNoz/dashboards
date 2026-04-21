# GCP Cloud Load Balancer Monitoring Dashboard

Monitors Google Cloud HTTP/S Load Balancing using OpenTelemetry metrics.

## Dashboard Details

**File:** `gcp-cloud-load-balancer-otlp-v1.json`
**Format:** SigNoz v3 OTLP
**Panels:** 7 panels across 3 sections

## Sections

| Section | Panels |
|---------|--------|
| Traffic | Request count, backend request count, request bytes, response bytes |
| Latency | Total latency, backend latency (avg) |
| Response Status | Response count by HTTP status code class |

## Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Environment filter |
| `project_id` | GCP Project ID |
| `forwarding_rule_name` | Load balancer forwarding rule name |

## Metrics Covered

| Metric | Description |
|--------|-------------|
| `loadbalancing.googleapis.com/https/request_count` | Total requests (delta) |
| `loadbalancing.googleapis.com/https/backend_request_count` | Backend requests (delta) |
| `loadbalancing.googleapis.com/https/backend_request_bytes_count` | Request bytes (delta) |
| `loadbalancing.googleapis.com/https/backend_response_bytes_count` | Response bytes (delta) |
| `loadbalancing.googleapis.com/https/total_latencies` | End-to-end latency distribution (ms) |
| `loadbalancing.googleapis.com/https/backend_latencies` | Proxy-to-backend latency (ms) |
| `loadbalancing.googleapis.com/https/response_count` | Response count by status code class |

## Setup

```yaml
receivers:
  googlecloudmonitoring:
    project_id: your-gcp-project-id
    collection_interval: 60s
    metric_prefixes:
      - "loadbalancing.googleapis.com"

exporters:
  otlp:
    endpoint: "your-signoz-host:4317"
```

## Related Issues

- [SigNoz/signoz#6386](https://github.com/SigNoz/signoz/issues/6386) — GCP Cloud Load Balancer Dashboard Request
