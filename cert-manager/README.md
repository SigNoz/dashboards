# cert-manager Monitoring Dashboard

cert-manager monitoring dashboard for [SigNoz](https://signoz.io/). Fixes [SigNoz/signoz#6023](https://github.com/SigNoz/signoz/issues/6023).

Uses the OpenTelemetry [`prometheus`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md) receiver to scrape cert-manager's built-in metrics endpoint.

## Sections

| #   | Section               | Covers                                                         |
| --- | --------------------- | -------------------------------------------------------------- |
| 1   | General Overview      | Certificates ready/not ready, ready status, leader election    |
| 2   | Certificate Issuance  | Expiration time, requests ready, controller sync rate          |
| 3   | Certificate Renewal   | Renewal timestamp, ACME client request rate/latency            |
| 4   | Error Metrics         | ACME errors, webhook errors, work queue depth                  |
| 5   | Resource Usage        | CPU usage, memory usage, goroutines                            |
| 6   | API & Event Metrics   | K8s API request rate, webhook request rate/latency, queue processing |

## OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "cert-manager"
          scrape_interval: 30s
          static_configs:
            - targets: ["cert-manager:9402"]
          metrics_path: /metrics

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "cert-manager"
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
- `issuer` — Certificate Issuer
- `certificate_name` — Certificate Name
- `cluster` — Cluster
- `deployment.environment` — Deployment Environment
- `service.name` — Service Name

### Notes

- cert-manager exposes Prometheus metrics on port 9402 by default.
- Screenshots will be added to the `assets/` directory.
