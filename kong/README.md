# Kong Gateway Monitoring Dashboard

This dashboard provides comprehensive monitoring for Kong Gateway using Prometheus metrics exported by Kong.

## Overview

Kong Gateway is a lightweight, fast, and flexible cloud-native API gateway. This dashboard helps you monitor the health, performance, and usage of your Kong Gateway instances in real-time.

## Prerequisites

- Kong Gateway with Prometheus plugin enabled
- SigNoz for metrics collection and visualization
- Kong Gateway configured to expose Prometheus metrics (typically on `/metrics` endpoint)

## Metrics Monitored

This dashboard tracks the following key Kong Gateway metrics:

1. **kong_http_requests_total** - Total number of HTTP requests processed
2. **kong_request_latency_ms** - Request latency in milliseconds
3. **kong_bandwidth_bytes** - Total bandwidth consumed (ingress/egress)
4. **kong_nginx_connections_total** - NGINX connection states
5. **kong_upstream_latency_ms** - Latency to upstream services

## Dashboard Panels

### Summary Panels (Top Row)
1. **Total HTTP Requests** - Cumulative count of all HTTP requests
2. **Avg Request Latency** - Average request processing time
3. **Total Bandwidth** - Total data transferred
4. **Active Connections** - Current active NGINX connections

### Detailed Panels
5. **Request Rate by Status Code** - HTTP request rate grouped by response status codes (2xx, 3xx, 4xx, 5xx)
6. **Request Latency Percentiles** - P50, P95, and P99 latency distributions
7. **Bandwidth Usage Over Time** - Ingress and egress bandwidth trends
8. **NGINX Connection States** - Active, reading, writing, and waiting connections
9. **Upstream Service Latency** - Latency to backend services, grouped by service name
10. **Requests Per Service** - Request rate distribution across Kong services

## Setup Instructions

### 1. Enable Kong Prometheus Plugin

Enable the Prometheus plugin globally or per service:

```bash
# Enable globally
curl -X POST http://localhost:8001/plugins \
  --data "name=prometheus"

# Or enable for specific service
curl -X POST http://localhost:8001/services/{service}/plugins \
  --data "name=prometheus"
```

### 2. Configure Prometheus Scraping

Add Kong as a scrape target in your Prometheus configuration:

```yaml
scrape_configs:
  - job_name: 'kong'
    static_configs:
      - targets: ['kong:8001']  # Adjust to your Kong admin API address
    metrics_path: '/metrics'
```

### 3. Import Dashboard to SigNoz

1. Navigate to SigNoz Dashboards
2. Click "Import Dashboard"
3. Upload the `kong.json` file
4. The dashboard will be available immediately

## Key Insights

- **Performance Monitoring**: Track request latency percentiles to identify slow requests
- **Traffic Analysis**: Monitor request rates and bandwidth to understand usage patterns
- **Error Detection**: Quickly spot 4xx and 5xx errors through status code breakdowns
- **Capacity Planning**: Use connection and latency metrics to determine scaling needs
- **Service Health**: Monitor upstream latency to identify backend service issues

## Customization

The dashboard includes a `service` variable filter that allows you to:
- Filter metrics by specific Kong service
- View metrics across all services (default)
- Focus on individual service performance

## Troubleshooting

### No Data Appearing

1. Verify Prometheus plugin is enabled: `curl http://localhost:8001/plugins | grep prometheus`
2. Check metrics endpoint is accessible: `curl http://localhost:8001/metrics`
3. Confirm Prometheus is scraping Kong successfully
4. Verify SigNoz is receiving metrics from Prometheus

### Incomplete Metrics

Some metrics may not appear if:
- Kong hasn't processed any requests yet
- Specific plugins (like rate-limiting) aren't configured
- Upstream services aren't defined

## Resources

- [Kong Gateway Documentation](https://docs.konghq.com/gateway/latest/)
- [Kong Prometheus Plugin](https://docs.konghq.com/hub/kong-inc/prometheus/)
- [SigNoz Documentation](https://signoz.io/docs/)

## Contributing

Feel free to enhance this dashboard by adding more panels or metrics. Some suggestions:
- Plugin-specific metrics (rate limiting, authentication)
- Database connection pool metrics
- Cache hit/miss rates
- Custom plugin metrics

## License

This dashboard configuration is provided as-is for use with SigNoz and Kong Gateway.
