# ASP.NET Metrics Dashboard - OTEL

## Metrics Ingestion

This dashboard uses metrics collected via the [OpenTelemetry .NET instrumentation](https://opentelemetry.io/docs/zero-code/net/instrumentations/#metrics-instrumentations) with ASP.NET Core HTTP, .NET Runtime, and Process metrics.

### appsettings.json

```json
{
  "OpenTelemetry": {
    "Metrics": {
      "Providers": [
        "AspNetCore",
        "HttpClient",
        "Process",
        "Runtime"
      ],
      "Exporter": {
        "Otlp": {
          "Endpoint": "http://signoz-otel-collector:4317"
        }
      }
    }
  }
}
```

### Or via code:

```csharp
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddProcessInstrumentation()
        .AddRuntimeInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("http://signoz-otel-collector:4317");
        }));
```

## Variables

- `deployment_environment`: Deployment environment (e.g., production, staging)
- `service_name`: ASP.NET service name

## Dashboard Panels

### Application Performance
- **CPU Usage**: Current CPU usage of the application instance
- **Memory Usage**: Memory consumption of the ASP.NET process
- **Request Rate**: Incoming requests per second
- **Active Requests**: Active requests being processed

### Request and Response
- **Request Latency (Average)**: Average time to serve requests
- **Request Latency by Route**: Latency broken down by route
- **Error Rate (HTTP 4xx/5xx)**: Error responses by status code
- **Total Requests**: Total requests processed
- **Request Duration (p50, p95, p99)**: Request duration percentiles

### Process Metrics
- **Process CPU Utilization**: Process-level CPU utilization
- **Process Working Set Memory**: Working set memory of the process
- **GC Heap Size**: Size of the .NET GC heap
- **Thread Pool Queue Length**: Items queued in the .NET thread pool

### HTTP Connection Metrics
- **HTTP Connections Current**: Current number of HTTP connections
- **Requests by Method**: Request count by HTTP method
- **Requests by Status Code**: Request count by HTTP status code

### .NET Runtime Metrics
- **GC Collections (Gen 0/1/2)**: GC collections by generation
- **Exception Count**: Number of exceptions thrown
- **Allocation Rate**: Rate of memory allocations
- **GC Pause Duration**: Duration of GC pauses
