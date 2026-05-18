# ASP.NET Dashboard - OTLP

## Metrics Ingestion

To ingest ASP.NET metrics, use the [OpenTelemetry .NET Automatic Instrumentation](https://opentelemetry.io/docs/zero-code/dotnet/instrumentations/):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

service:
  pipelines:
    metrics:
      receivers: [otlp]
      exporters: [signoz]
```

Set the following environment variables on your ASP.NET application:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://<signoz-collector>:4317
export OTEL_SERVICE_NAME=my-aspnet-app
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production
```

## Variables

- `{{deployment_environment}}`: Deployment environment (e.g., production, staging)
- `{{service_name}}`: Name of the ASP.NET service

## Dashboard Panels

### Application Performance
- **CPU Usage** (Value + Graph): Current and historical CPU usage of the ASP.NET application process
- **Memory Usage** (Value + Graph): Memory consumption of the ASP.NET application process
- **Request Rate** (Value): Incoming requests per second

### Request and Response
- **Request Latency** (Graph): p50, p95, and p99 percentile request latencies
- **Error Rate** (Value + Graph): HTTP 4xx and 5xx error responses per second
- **Active Requests** (Value + Graph): Number of active requests being processed

### Process Metrics
- **Thread Count** (Value + Graph): Number of threads in the process
- **GC Collections** (Graph): Garbage collection count by generation (Gen 0, Gen 1, Gen 2)
- **GC Heap Size** (Graph): Managed heap size by generation
