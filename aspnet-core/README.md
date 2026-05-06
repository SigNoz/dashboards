# ASP.NET Core Dashboard - Prometheus

Monitors ASP.NET Core applications using Prometheus metrics exposed via the `prometheus-net` or built-in OpenTelemetry Prometheus exporter. Covers HTTP request throughput and latency, exception tracking, memory/GC, thread pool health, and Kestrel connection metrics.

## Metrics Ingestion

### 1. Expose Prometheus metrics from your app

Add the `prometheus-net.AspNetCore` NuGet package and wire it up in `Program.cs`:

```csharp
using Prometheus;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics => metrics.AddAspNetCoreInstrumentation()
                                   .AddRuntimeInstrumentation()
                                   .AddPrometheusExporter());

var app = builder.Build();
app.MapPrometheusScrapingEndpoint(); // exposes /metrics
app.Run();
```

Or with the legacy `prometheus-net` approach:

```csharp
app.UseHttpMetrics();
app.MapMetrics(); // /metrics
```

### 2. Scrape with OpenTelemetry Collector

Add a Prometheus receiver in your `otel-config.yaml` and forward to SigNoz:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: aspnetcore
          scrape_interval: 15s
          static_configs:
            - targets: ["localhost:5000"]

exporters:
  otlp:
    endpoint: "<your-signoz-host>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Variables

This dashboard has no variables — it shows all ASP.NET Core instances together. To filter by service, add a `job` variable using the label values of the `http_server_request_duration_seconds_count` metric.

## Dashboard Panels

### Overview
| Panel | Metric | Type |
|---|---|---|
| Active Requests | `http_server_active_requests` | Value |
| Request Rate | `http_server_request_duration_seconds_count` | Graph |
| Error Rate (5xx) | `http_server_request_duration_seconds_count{http_response_status_code=~"5.."}` | Graph |
| Average Request Duration | `http_server_request_duration_seconds_sum/count` | Value |

### HTTP Requests
| Panel | Metric | Type |
|---|---|---|
| Request Rate by Endpoint | `http_server_request_duration_seconds_count` by `http_route` | Graph |
| P99 Duration by Endpoint | `http_server_request_duration_seconds_bucket` histogram_quantile(0.99) | Graph |
| P95 Duration by Endpoint | `http_server_request_duration_seconds_bucket` histogram_quantile(0.95) | Graph |
| Requests by Status Code | `http_server_request_duration_seconds_count` by `http_response_status_code` | Graph (stacked) |

### Exceptions
| Panel | Metric | Type |
|---|---|---|
| Exception Rate | `aspnetcore_diagnostics_exceptions_total` | Graph |
| Exceptions by Type | `aspnetcore_diagnostics_exceptions_total` by `exception_type` | Graph |

### Memory
| Panel | Metric | Type |
|---|---|---|
| Process Working Set | `process_working_set_bytes` | Graph |
| GC Heap Size | `dotnet_gc_heap_size_bytes` | Graph |
| GC Collections Rate | `dotnet_gc_collections_total` | Graph |

### Threading
| Panel | Metric | Type |
|---|---|---|
| Thread Pool Threads | `dotnet_threadpool_threads` | Graph |
| Thread Pool Queue Length | `dotnet_threadpool_queue_length` | Graph |

### Kestrel
| Panel | Metric | Type |
|---|---|---|
| Active Connections | `kestrel_active_connections` | Graph |
| Connection Duration (P95) | `kestrel_connection_duration_seconds_bucket` histogram_quantile(0.95) | Graph |
| Queued Requests | `kestrel_queued_requests` | Graph |

## Minimum .NET / SDK versions

- .NET 8+ for `http_server_*` semantic convention metrics (OpenTelemetry)
- `prometheus-net` 8+ for `kestrel_*` and `dotnet_*` metrics
- For .NET 6/7, some metric names may differ — check your exporter docs
