# Kong Gateway Dashboard - OTEL

Kong Gateway monitoring dashboard with metrics collected via OpenTelemetry.

## Metrics Ingestion

To use this dashboard, configure the OpenTelemetry collector to receive Kong Gateway metrics. Below is a sample configuration:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
  batch:
    timeout: 10s

exporters:
  otlp:
    endpoint: <your-otlp-endpoint>

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

### Kong Configuration

Enable Kong's OTEL plugin:

```bash
curl -X POST http://localhost:8001/plugins \
  -d "name=opentelemetry" \
  -d "config.endpoint=YOUR_OTEL_ENDPOINT" \
  -d "config.service.name=kong-gateway"
```

## Variables

- `kong.instance`: Kong Gateway instance name (defaults to `kong`)

## Dashboard Panels

### Overview Row
- **Total Requests**: Total number of requests processed by Kong Gateway
- **Server Errors (5xx)**: Rate of 5xx server error responses
- **Avg Proxy Latency**: Average proxy request latency in milliseconds
- **Active Connections**: Number of active connections
- **Request Size**: Total request size in bytes
- **Response Size**: Total response size in bytes

### Requests Over Time
Time series graph showing total requests over time.

### Latency Breakdown
Time series graph showing:
- **Proxy Latency**: Time spent by Kong proxying requests
- **Request Latency**: Total request latency
- **Kong Latency**: Internal Kong processing time

### Connections
Time series graph showing:
- **Active**: Currently active connections
- **Idle**: Idle connections
- **Accepted**: Total accepted connections
- **Handled**: Total handled connections

### HTTP Status Codes
Time series graph showing request distribution by status code:
- **2xx**: Success responses
- **4xx**: Client error responses
- **5xx**: Server error responses

## Screenshots

![Kong Gateway Dashboard](assets/kong-dashboard.png)
