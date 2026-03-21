# Kong Gateway Dashboard - Prometheus

## Overview

This dashboard provides comprehensive monitoring for Kong Gateway using Prometheus metrics. It covers all critical aspects of Kong Gateway performance including general overview, request metrics, latency analysis, error tracking, upstream health, and plugin performance.

## Prerequisites

Before using this dashboard, ensure you have:

1. **Kong Gateway** running with Prometheus metrics enabled
2. **Prometheus server** configured to scrape metrics from Kong
3. **SigNoz** instance capable of querying Prometheus metrics

## Setup

### 1. Enable Prometheus Plugin in Kong

First, enable the Prometheus plugin in Kong to expose metrics:

```bash
# Enable globally for all services
curl -X POST http://kong-admin:8001/plugins \
    --data "name=prometheus"

# Or enable for a specific service
curl -X POST http://kong-admin:8001/services/{service}/plugins \
    --data "name=prometheus"
```

### 2. Configure Prometheus

Add the following job to your `prometheus.yml` configuration:

```yaml
scrape_configs:
  - job_name: 'kong'
    static_configs:
      - targets: ['kong:8001']  # Kong Admin API port
    scrape_interval: 30s
    metrics_path: /metrics
```

### 3. Configure SigNoz to Query Prometheus

Ensure your SigNoz instance is configured with a Prometheus data source pointing to your Prometheus server.

## Dashboard Panels

This dashboard is organized into six main sections:

### 🏥 General Overview (5 panels)
- **Total Requests**: Total HTTP requests processed (`kong_http_requests_total`)
- **Active Connections**: Current active connections (`kong_nginx_connections_total{state="active"}`)
- **Uptime**: Kong Gateway uptime (`time() - process_start_time_seconds`)
- **CPU Usage**: Kong process CPU utilization (`rate(process_cpu_seconds_total[5m]) * 100`)
- **Memory Usage**: Kong process memory consumption (`process_resident_memory_bytes`)

### 📊 Request Metrics (4 panels)
- **Request Rate**: Requests per second (`rate(kong_http_requests_total[5m])`)
- **Response Status Codes**: Status code distribution (2xx, 4xx, 5xx)
- **Request Size**: Average request size in bytes
- **Response Size**: Average response size in bytes

### ⚡ Latency Metrics (3 panels)
- **Average Request Latency**: Mean request processing time
- **Request Latency Percentiles**: P50, P90, P99 latency distribution
- **Upstream Latency**: Backend service response times

### 🚨 Error Metrics (3+ panels)
- **Total Errors**: Count of 4xx and 5xx responses
- **Error Rate**: Percentage of failed requests
- **Error Codes Distribution**: Breakdown by specific error codes
- **Datastore Status**: Kong database connectivity status

### 🎯 Upstream Health (3+ panels)
- **Upstream Success Rate**: Percentage of successful upstream requests
- **Active Upstreams**: Number of available upstream services
- **Upstream Response Time**: Backend service performance
- **Nginx Connections**: Connection state breakdown

### 🔌 Plugin/Route Metrics (3+ panels)
- **Requests per Route/Service**: Traffic distribution across routes
- **Bandwidth Usage**: Network I/O (ingress/egress)
- **Plugin Execution Time**: Plugin processing overhead

## Key Metrics Used

The dashboard uses standard Kong Prometheus metrics:

| Metric Category | Prometheus Metrics |
|---|---|
| **HTTP Requests** | `kong_http_requests_total` |
| **Request Latency** | `kong_request_latency_ms_bucket/sum/count` |
| **Upstream Latency** | `kong_upstream_latency_ms_bucket/sum/count` |
| **Request/Response Size** | `kong_request_size_bytes_*`, `kong_response_size_bytes_*` |
| **Nginx Connections** | `kong_nginx_connections_total` |
| **Bandwidth** | `kong_bandwidth_bytes` |
| **System Resources** | `process_cpu_seconds_total`, `process_resident_memory_bytes` |
| **Datastore Health** | `kong_datastore_reachable` |

## Alerting Recommendations

Consider setting up alerts for:

- **High Error Rate**: Error rate > 5%
- **High Latency**: P99 latency > 1000ms
- **Datastore Unreachable**: `kong_datastore_reachable` = 0
- **High CPU Usage**: CPU usage > 80%
- **High Memory Usage**: Memory usage > 2GB
- **Upstream Failures**: Success rate < 95%

## Troubleshooting

### Common Issues

1. **No data in panels**: 
   - Verify Kong Prometheus plugin is enabled
   - Check Prometheus is scraping Kong metrics (check targets in Prometheus UI)
   - Ensure SigNoz can query your Prometheus instance

2. **Missing specific metrics**:
   - Confirm Kong version supports the required metrics
   - Check Kong configuration for metric collection

3. **High resource usage**:
   - Consider adjusting Prometheus scrape intervals
   - Review Kong worker processes and resource allocation

### Useful Commands

```bash
# Check Kong Prometheus metrics endpoint
curl http://kong:8001/metrics

# Verify Kong admin API is accessible
curl http://kong:8001/status

# Check Prometheus targets
curl http://prometheus:9090/api/v1/targets

# Kong configuration check
kong config -c /etc/kong/kong.conf
```

## Kong Configuration

Ensure your Kong configuration includes:

```yaml
# kong.conf
admin_listen = 0.0.0.0:8001
proxy_listen = 0.0.0.0:8000

# Enable metrics collection
nginx_worker_processes = auto
mem_cache_size = 128m
```

## Version Information

- **Dashboard Version**: v1
- **Compatible with**: Kong Gateway 2.x, 3.x
- **Kong Prometheus Plugin**: 2.0.0+
- **SigNoz**: v0.8.0+

## Dashboard Import

1. Copy the `kong-prometheus-v1.json` content
2. In SigNoz, go to **Dashboards** → **Import Dashboard**
3. Paste the JSON content and import
4. The dashboard will be ready to use with your Kong metrics

## Performance Considerations

- **Metric Cardinality**: Be mindful of high-cardinality labels like route names
- **Scrape Frequency**: Balance between data granularity and resource usage
- **Retention**: Configure appropriate metric retention policies in Prometheus

## Advanced Monitoring

For enhanced monitoring, consider:

- **Custom Plugins**: Developing Kong plugins for application-specific metrics
- **Distributed Tracing**: Integrating with OpenTelemetry for request tracing
- **Log Aggregation**: Combining metrics with Kong access logs
- **Health Checks**: Implementing upstream health check monitoring