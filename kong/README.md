# Kong Gateway Monitoring Dashboard

Kong API Gateway monitoring dashboard for [SigNoz](https://signoz.io/). Fixes [SigNoz/signoz#6028](https://github.com/SigNoz/signoz/issues/6028).

Uses the OpenTelemetry [`prometheus`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md) receiver to scrape Kong's built-in Prometheus metrics endpoint.

## Sections

| #   | Section          | Covers                                                          |
| --- | ---------------- | --------------------------------------------------------------- |
| 1   | General Overview | Total requests, active connections, datastore reachable, target health |
| 2   | Request Metrics  | Request rate by status code/route, request/response size        |
| 3   | Latency Metrics  | Request latency, upstream latency, Kong processing latency      |
| 4   | Error Metrics    | 5xx/4xx error rates, error rate by service, unhealthy targets   |
| 5   | Traffic Metrics  | Ingress/egress bandwidth, connection states, bandwidth by service |
| 6   | Plugin Metrics   | Request rate by plugin, plugin latency impact, plugin errors    |
| 7   | Resource Usage   | Nginx worker connections, shared memory, Lua worker memory      |

## OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "kong"
          scrape_interval: 30s
          static_configs:
            - targets: ["kong:8001"]
          metrics_path: /metrics

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "kong"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch, resource]
      exporters: [otlp]
```

## Dashboard Variables

- `namespace` — Kubernetes Namespace
- `service` — Kong Service
- `deployment.environment` — Deployment Environment
- `cluster` — Cluster
- `service.name` — Service Name

### Notes

- Kong exposes Prometheus metrics on port 8001 by default. Enable the `prometheus` plugin if not already active.
- Screenshots will be added to the `assets/` directory.
