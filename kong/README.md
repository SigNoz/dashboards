# Kong Gateway Dashboard

Monitor your Kong API Gateway with this dashboard. Shows requests, latency, errors, and resource usage.

## What's Included

- Total request counter
- Active connections
- Request rate over time
- HTTP status code breakdown
- Latency tracking (average and percentiles)
- Error rate percentage
- Network bandwidth (in/out)
- CPU and memory usage
- Pod restart count

## Setup

### 1. Enable Kong Prometheus Plugin

```bash
curl -X POST http://localhost:8001/plugins \
  --data "name=prometheus"
```

### 2. Configure Prometheus

Add this to your prometheus.yml:

```yaml
scrape_configs:
  - job_name: 'kong'
    static_configs:
      - targets: ['kong-admin:8001']
    metrics_path: '/metrics'
```

### 3. Import Dashboard

1. Open SigNoz
2. Go to Dashboards
3. Click Import
4. Upload overview.json
5. Select your namespace

## Metrics Used

The dashboard uses these Kong metrics:

- `kong_http_requests_total` - Total HTTP requests
- `kong_http_status` - Response status codes
- `kong_latency_ms` - Request latency
- `kong_bandwidth_bytes` - Traffic volume
- `kong_nginx_connections_active` - Active connections
- `container_cpu_usage_seconds_total` - CPU usage
- `container_memory_usage_bytes` - Memory usage
- `kube_pod_container_status_restarts_total` - Pod restarts

## Dashboard Variables

- **namespace**: Kubernetes namespace where Kong runs
- **service**: Filter by specific Kong service (optional)

## Testing

To test if metrics are working:

```bash
# Check Kong metrics endpoint
curl http://localhost:8001/metrics

# Look for these metrics:
# kong_http_requests_total
# kong_nginx_connections_active
# kong_latency_ms
```

## References

- Kong Prometheus Plugin: https://docs.konghq.com/hub/kong-inc/prometheus/
- Kong OpenTelemetry: https://docs.konghq.com/mesh/latest/guides/otel-metrics/

## Notes

Make sure your Kong instance has the Prometheus plugin enabled. The CPU and memory metrics require Kubernetes deployment.

Created for SigNoz issue #6028.
