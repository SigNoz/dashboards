# Kong Gateway Dashboard — Prometheus

Comprehensive Kong Gateway monitoring dashboard for SigNoz, built on Prometheus metrics exported by Kong's built-in Prometheus plugin.

## Metrics Ingestion

### 1. Enable Kong Prometheus Plugin

```bash
curl -X POST http://localhost:8001/plugins \
  --data "name=prometheus" \
  --data "config.per_consumer=true" \
  --data "config.latency_metrics=true" \
  --data "config.bandwidth_metrics=true" \
  --data "config.upstream_health_metrics=true"
```

### 2. OpenTelemetry Collector Configuration

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'kong'
          scrape_interval: 15s
          static_configs:
            - targets: ['kong-gateway:8001']
          metrics_path: /metrics

exporters:
  otlp:
    endpoint: "ingest.signoz.io:443"
    tls:
      insecure: false
    headers:
      "signoz-ingestion-key": "<SIGNOZ_INGESTION_KEY>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Variables

- `{{service_name}}`: Filter by Kong service name

## Dashboard Sections

### 1. Overview
Total requests, active connections, request rate, error rates (4xx/5xx)

### 2. HTTP Traffic
Requests by service, route, status code, consumer. Bandwidth ingress/egress by service.

### 3. Latency
Request latency P50/P90/P99, upstream latency, Kong processing latency, latency by service and route.

### 4. Upstream Health
Target health status, upstream connections, connection states (reading/writing/waiting/accepted/handled).

### 5. Database
Datastore reachability, query duration, cache hit/miss rates.

### 6. Nginx Internals
Worker connections, shared memory zones, worker process metrics.

### 7. Plugin Execution
Plugin execution counts by phase, plugin latency, rate limiting metrics.

## Metrics Reference

| Metric | Description |
|--------|-------------|
| `kong_http_requests_total` | Total HTTP requests |
| `kong_bandwidth_bytes` | Bandwidth by direction |
| `kong_request_latency_ms_bucket` | Request latency histogram |
| `kong_upstream_latency_ms_bucket` | Upstream latency histogram |
| `kong_kong_latency_ms_bucket` | Kong processing latency |
| `kong_nginx_connections_total` | Nginx connection states |
| `kong_datastore_reachable` | Database reachability |
| `kong_upstream_target_health` | Upstream target health |
