# Istio Service Mesh Monitoring Dashboard

Istio service mesh monitoring dashboard for [SigNoz](https://signoz.io/). Fixes [SigNoz/signoz#6025](https://github.com/SigNoz/signoz/issues/6025).

Uses the OpenTelemetry [`prometheus`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md) receiver to scrape Envoy sidecar proxies and the Istiod control plane.

## Sections

| #   | Section              | Covers                                                              |
| --- | -------------------- | ------------------------------------------------------------------- |
| 1   | General Overview     | Total request rate, success rate, connected proxies, rate by service |
| 2   | Traffic Management   | Request rate by source/destination, volume by method, TCP connections |
| 3   | Performance Metrics  | Request duration P50/P95, request/response size                     |
| 4   | Error Metrics        | 5xx/4xx error rates, gRPC error rate, TCP errors                    |
| 5   | Resource Usage       | TCP bytes received/sent, active upstream connections                |
| 6   | Control Plane Metrics | XDS pushes, proxy convergence time, connected proxies, push errors |
| 7   | Data Plane Metrics   | Request rate by response flag, upstream connection pool, duration by source, TCP throughput |
| 8   | Security Metrics     | mTLS/non-mTLS request rate, certificate signing requests, auth failures |

## OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "envoy-stats"
          scrape_interval: 30s
          metrics_path: /stats/prometheus
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_container_port_number]
              action: keep
              regex: "15090"
        - job_name: "istiod"
          scrape_interval: 30s
          static_configs:
            - targets: ["istiod.istio-system:15014"]

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "istio"
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
- `deployment.environment` — Deployment Environment
- `service.name` — Service Name
- `cluster` — Cluster

### Notes

- Envoy sidecars expose Prometheus metrics on port 15090 at `/stats/prometheus`.
- Istiod exposes control plane metrics on port 15014.
- Screenshots will be added to the `assets/` directory.
