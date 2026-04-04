# ASP.NET Core Metrics Dashboard - OTLP

## Metrics Ingestion

This dashboard uses metrics from the OpenTelemetry .NET SDK automatic instrumentation. To collect ASP.NET Core metrics, configure your OpenTelemetry Collector with the OTLP receiver:

### otel-config.yaml

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  otlp:
    endpoint: "<signoz-endpoint>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [otlp]
      exporters: [otlp]
```

### ASP.NET Core Application Setup

Add the following NuGet packages to your application:

```bash
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Process
dotnet add package OpenTelemetry.Instrumentation.Runtime
```

Configure OpenTelemetry in `Program.cs`:

```csharp
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics =>
    {
        metrics
            .AddAspNetCoreInstrumentation()
            .AddProcessInstrumentation()
            .AddRuntimeInstrumentation()
            .AddOtlpExporter(opts =>
            {
                opts.Endpoint = new Uri("http://<otel-collector>:4317");
            });
    });
```

Set the service name and deployment environment via environment variables:

```bash
export OTEL_SERVICE_NAME=my-aspnetcore-app
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production
```

## Variables

- `{{service_name}}`: The name of the ASP.NET Core service (from `service.name` resource attribute)
- `{{deployment_environment}}`: Deployment environment (from `deployment.environment` resource attribute)

## Dashboard Panels

### Section: Application Performance

| Panel | Metric | Description |
|-------|--------|-------------|
| CPU Usage | `process.cpu.time` | Rate of CPU time consumed by the application process |
| Memory Usage | `process.memory.usage` | Current memory consumption in bytes |
| Request Rate | `http.server.request.duration` | Incoming HTTP request rate per second, grouped by service |
| Request Latency P95 | `http.server.request.duration` | 95th percentile request latency in nanoseconds |
| Error Rate (%) | `http.server.request.duration` | Percentage of requests returning HTTP 4xx/5xx status codes |

### Section: Request and Response

| Panel | Metric | Description |
|-------|--------|-------------|
| Active Requests | `http.server.active_requests` | Number of HTTP requests currently being processed |
| HTTP Request Rate by Status Code | `http.server.request.duration` | Request rate broken down by HTTP response status code |
| Request Duration by Route (P95) | `http.server.request.duration` | 95th percentile latency per HTTP route |

### Section: Process Metrics

| Panel | Metric | Description |
|-------|--------|-------------|
| GC Collections Count | `process.runtime.dotnet.gc.collections.count` | Garbage collection count by generation (gen0, gen1, gen2) |
| GC Heap Size | `process.runtime.dotnet.gc.heap.size` | Managed heap size in bytes |
| Thread Pool Threads | `process.runtime.dotnet.thread_pool.threads.count` | Number of active thread pool threads |
| Thread Pool Queue Length | `process.runtime.dotnet.thread_pool.queue.length` | Items queued for thread pool processing |
| Exception Count | `process.runtime.dotnet.exceptions.count` | Total .NET exceptions thrown |

### Section: Kestrel Server

| Panel | Metric | Description |
|-------|--------|-------------|
| Kestrel Active Connections | `kestrel.active_connections` | Active connections to the Kestrel web server |
| Kestrel Queue Length | `kestrel.queued_connections` | Connections queued waiting to be processed |
| Kestrel Request Duration (P95) | `kestrel.request.duration` | 95th percentile Kestrel request processing time |

## References

- [OpenTelemetry .NET Metrics Instrumentation](https://opentelemetry.io/docs/zero-code/net/instrumentations/#metrics-instrumentations)
- [OpenTelemetry .NET Runtime Instrumentation](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.Runtime)
- [OpenTelemetry .NET Process Instrumentation](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.Process)
