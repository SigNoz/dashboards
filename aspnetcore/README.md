# ASP.NET Core Metrics Dashboard - OTLP

A comprehensive monitoring dashboard for ASP.NET Core applications using OpenTelemetry (OTLP) metrics. Covers HTTP server performance, .NET runtime internals, and Kestrel server metrics.

Uses modern .NET 9+ metric names (`dotnet.*` prefix) with backwards compatibility for .NET 8.

## Metrics Ingestion

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

Add the following NuGet packages:

```bash
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Http
dotnet add package OpenTelemetry.Instrumentation.Runtime
dotnet add package OpenTelemetry.Instrumentation.Process
```

Configure OpenTelemetry in `Program.cs`:

```csharp
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics =>
    {
        metrics
            .AddAspNetCoreInstrumentation()
            .AddHttpClientInstrumentation()
            .AddProcessInstrumentation()
            .AddRuntimeInstrumentation()
            .AddMeter("Microsoft.AspNetCore.Hosting")
            .AddMeter("Microsoft.AspNetCore.Server.Kestrel")
            .AddOtlpExporter(opts =>
            {
                opts.Endpoint = new Uri("http://<otel-collector>:4317");
            });
    });
```

Set the service name and deployment environment:

```bash
export OTEL_SERVICE_NAME=my-aspnetcore-app
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production
```

## Variables

| Variable | Description |
|----------|-------------|
| `service_name` | Filter by ASP.NET Core service (from `service.name` resource attribute) |
| `deployment_environment` | Filter by deployment environment (from `deployment.environment` resource attribute) |

## Dashboard Panels

### Section 1: Application Performance

| Panel | Metric | Description |
|-------|--------|-------------|
| CPU Usage | `dotnet.process.cpu.time` / `process.cpu.time` | CPU time consumed (supports .NET 8 and 9+) |
| Memory Usage | `dotnet.process.memory.working_set` / `process.memory.usage` | Memory consumption in bytes |
| Request Rate | `http.server.request.duration` | Incoming HTTP requests per second |
| Request Latency P95 | `http.server.request.duration` | 95th percentile request latency |
| Error Rate | `http.server.request.duration` | Requests with HTTP status >= 400 |

### Section 2: Request & Response

| Panel | Metric | Description |
|-------|--------|-------------|
| Active Requests | `http.server.active_requests` | In-flight HTTP requests |
| Request Rate by Status Code | `http.server.request.duration` | Request rate grouped by response status |
| Request Duration by Route (P95) | `http.server.request.duration` | Latency per HTTP route |

### Section 3: .NET Runtime

| Panel | Metric | Description |
|-------|--------|-------------|
| GC Collections | `dotnet.gc.collections` | Garbage collection rate by generation (gen0, gen1, gen2) |
| GC Heap Size | `dotnet.gc.last_collection.heap.size` | Heap size by generation |
| Thread Pool Threads | `dotnet.thread_pool.thread.count` | Active thread pool threads |
| Thread Pool Queue | `dotnet.thread_pool.queue.length` | Queued work items (spikes indicate saturation) |
| Exceptions | `dotnet.exceptions` | Exception rate |

### Section 4: Kestrel Server

| Panel | Metric | Description |
|-------|--------|-------------|
| Active Connections | `kestrel.active_connections` | Current TCP connections |
| Connection Duration P95 | `kestrel.connection.duration` | 95th percentile connection lifetime |
| Queued Connections | `kestrel.queued_connections` | Connections waiting to be accepted |
| Rejected Connections | `kestrel.rejected_connections` | Connections rejected (MaxConcurrentConnections exceeded) |
