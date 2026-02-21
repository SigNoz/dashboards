# Kong Gateway Monitoring Dashboard

Monitor your Kong API Gateway performance using OpenTelemetry metrics with SigNoz.

## Dashboard Sections

### General Overview
- Total Requests, Active Connections, CPU Usage, Memory Usage

### Request Metrics
- Request Rate by service, Response Status Codes, Request/Response Size

### Latency Metrics
- Average Request Latency, Latency Percentiles (P50/P90/P99), Upstream Latency, Internal Latency

### Error Metrics
- Error Rate (4xx/5xx), Failed Requests by Service

### Traffic Metrics
- Incoming/Outgoing Traffic Volume

### Resource Usage
- CPU/Memory Usage Over Time

## Variables
- namespace, service, deployment.environment, cluster

## Metrics Used
kong.request.count, kong.latency.total, kong.latency.upstream, kong.latency.internal, http.server.request.size, http.server.response.size, nginx.connections_current, process.cpu.time, process.memory.usage

## References
- Kong OpenTelemetry Plugin: https://docs.konghq.com/hub/kong-inc/opentelemetry/
- Kong Grafana Dashboard: https://grafana.com/grafana/dashboards/7424-kong-official/
