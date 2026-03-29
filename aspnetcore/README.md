# ASP.NET Core Metrics Dashboard

Comprehensive monitoring for ASP.NET Core applications using OpenTelemetry OTLP instrumentation.

## Sections

| # | Section | Covers |
|---|---------|--------|
| 1 | Application Performance | HTTP request rate, active connections, p95 latency, error rate (4xx/5xx) |
| 2 | Process Metrics | CPU time, memory (RSS), GC collections per generation, GC heap size |
| 3 | Thread Pool & Connections | Thread pool threads/queue, Kestrel queued connections, exception rate |
| 4 | Routing & Middleware | Route match attempts by status, active requests |

## Setup

### OpenTelemetry Collector Configuration

Enable the ASP.NET Core auto-instrumentation in your application:

```xml
<!-- .csproj -->
<PackageReference Include="OpenTelemetry.Instrumentation.AspNetCore" Version="*" />
<PackageReference Include="OpenTelemetry.Instrumentation.Process" Version="*" />
<PackageReference Include="OpenTelemetry.Instrumentation.Runtime" Version="*" />
```

```csharp
// Program.cs
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddProcessInstrumentation()
        .AddRuntimeInstrumentation()
        .AddOtlpExporter(opts => opts.Endpoint = new Uri("http://localhost:4317")));
```

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `service_name` | Name of the ASP.NET Core service |
| `deployment_environment` | Deployment environment (production, staging, etc.) |

## Key Metrics Used

| Metric | Source | Description |
|--------|--------|-------------|
| `http.server.request.duration` | AspNetCore instrumentation | HTTP request duration histogram |
| `aspnetcore.server.active_requests` | AspNetCore instrumentation | Active HTTP requests |
| `aspnetcore.routing.match_attempts` | AspNetCore instrumentation | Routing attempts by status |
| `kestrel.active_connections` | Kestrel instrumentation | Active Kestrel connections |
| `kestrel.queued_connections` | Kestrel instrumentation | Queued Kestrel connections |
| `process.cpu.time` | Process instrumentation | CPU time by state |
| `process.memory.usage` | Process instrumentation | Physical memory (RSS) |
| `process.runtime.dotnet.gc.collections.count` | Runtime instrumentation | GC collections per generation |
| `process.runtime.dotnet.gc.heap.size` | Runtime instrumentation | GC heap size per generation |
| `process.runtime.dotnet.thread_pool.threads.count` | Runtime instrumentation | Thread pool thread count |
| `process.runtime.dotnet.thread_pool.queue.length` | Runtime instrumentation | Thread pool queue depth |
| `process.runtime.dotnet.exceptions.count` | Runtime instrumentation | Exception rate |

## References

- [OTel ASP.NET Core Instrumentation](https://opentelemetry.io/docs/zero-code/net/instrumentations/#metrics-instrumentations)
- [Grafana Reference Dashboard](https://grafana.com/grafana/dashboards/17706-asp-net-otel-metrics/)
- [Process Instrumentation Metrics](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/blob/main/src/OpenTelemetry.Instrumentation.Process/README.md)
