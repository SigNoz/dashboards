# Kong API Gateway Monitoring Dashboard

Comprehensive monitoring for Kong API Gateway using the Kong Prometheus plugin.

## Sections

| # | Section | Covers |
|---|---------|--------|
| 1 | General Overview | Request rate, error rate, p99 upstream latency, p95 total latency |
| 2 | Traffic Management | Request distribution by service, bandwidth in/out, connections |
| 3 | Upstream Health | Healthy/unhealthy targets, DNS latency, circuit breaker events |
| 4 | Node & Nginx | Datastore reachability, Nginx metric errors |

## Setup

### Enable Kong Prometheus Plugin

```bash
# Enable globally
curl -X POST http://localhost:8001/plugins \
  --data "name=prometheus" \
  --data "config.per_consumer=false"
```

### OTel Collector Configuration

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'kong'
          static_configs:
            - targets: ['kong-admin:8001']
          metrics_path: '/metrics'
```

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `kong_job` | Prometheus job name for Kong (default: `kong.*`) |

## Key Metrics

| Metric | Description |
|--------|-------------|
| `kong_http_requests_total` | Total HTTP requests by service, route, code |
| `kong_latency_ms_bucket` | Request/upstream latency histogram |
| `kong_bandwidth_bytes_total` | Bandwidth by direction (ingress/egress) |
| `kong_nginx_connections_total` | Nginx connection states |
| `kong_upstream_target_health` | Upstream target health state |
| `kong_datastore_reachable` | Datastore reachability (1=up) |

## References

- [Kong Prometheus Plugin](https://docs.konghq.com/hub/kong-inc/prometheus/)
- [Kong Prometheus Metrics](https://docs.konghq.com/gateway/latest/production/monitoring/prometheus/)
