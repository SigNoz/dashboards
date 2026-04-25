# ASP.NET Core — Prometheus (OpenTelemetry)

Comprehensive monitoring dashboard for ASP.NET Core applications instrumented with the [OpenTelemetry .NET](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation) automatic instrumentation SDK, scraping metrics via Prometheus.

## Dashboard Sections

### 1. General Overview
High-level KPIs at a glance:
- **Request Rate** — total req/s across all routes
- **P99 Latency** — tail latency (99th percentile)
- **P50 Latency** — median latency
- **Error Rate (5xx)** — percentage of server error responses
- **Active Requests** — in-flight HTTP requests right now
- **Active Kestrel Connections** — open TCP connections to the server

### 2. HTTP Server Metrics
Time-series panels for request throughput and latency distribution:
- Request rate over time (by service)
- Request latency percentiles: P50 / P90 / P99
- Requests broken down by HTTP status code (stacked)
- Error rate by service — 4xx vs 5xx side-by-side

### 3. Request & Response Details
Per-route breakdown and payload size analysis:
- Request rate by route (identify hot paths)
- P99 latency by route (find slow endpoints)
- Request body size percentiles (P50, P99)
- Response body size percentiles (P50, P99)

### 4. Kestrel Server
Low-level ASP.NET Core server metrics:
- Active connections over time
- Queued connections and queued thread-pool requests
- Rejected connections rate (max-connections backpressure)
- Connection duration percentiles (P50, P99)

### 5. .NET Runtime — Garbage Collector
GC health and memory pressure indicators:
- GC heap size by generation (gen0, gen1, gen2, LOH)
- GC collection rate by generation
- GC pause duration (P99) — directly affects request latency
- Thread pool worker thread count and queue length

### 6. Process Metrics
OS-level process resource usage:
- CPU time rate by mode (user vs system)
- Working set / RSS memory
- Process thread count
- Virtual memory size

## Metrics Source

All metrics come from the [OpenTelemetry .NET automatic instrumentation](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation) with the Prometheus exporter enabled.

Key metrics used:

| Metric | Type | Description |
|--------|------|-------------|
| `http_server_request_duration_seconds` | Histogram | HTTP request duration |
| `http_server_active_requests` | Gauge | In-flight HTTP requests |
| `http_server_request_body_size_bytes` | Histogram | Request payload size |
| `http_server_response_body_size_bytes` | Histogram | Response payload size |
| `kestrel_active_connections` | Gauge | Active TCP connections |
| `kestrel_connection_duration_seconds` | Histogram | TCP connection lifetime |
| `kestrel_rejected_connections_total` | Counter | Rejected connections |
| `kestrel_queued_connections` | Gauge | Connections awaiting accept |
| `kestrel_queued_requests` | Gauge | Requests queued in thread pool |
| `dotnet_gc_heap_size_bytes` | Gauge | GC heap size per generation |
| `dotnet_gc_collections_total` | Counter | GC collection count |
| `dotnet_gc_duration_seconds` | Histogram | GC pause duration |
| `dotnet_thread_pool_thread_count` | Gauge | Thread pool worker threads |
| `dotnet_thread_pool_queue_length` | Gauge | Work items queued |
| `process_cpu_seconds_total` | Counter | CPU time (user + system) |
| `process_working_set_bytes` | Gauge | RSS / physical memory |
| `process_num_threads` | Gauge | Total OS threads |
| `process_virtual_memory_bytes` | Gauge | Virtual memory committed |

## Setup

### 1. Add OpenTelemetry to your ASP.NET Core app

```csharp
// Program.cs
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddRuntimeInstrumentation()
        .AddProcessInstrumentation()
        .AddPrometheusExporter());

app.MapPrometheusScrapingEndpoint(); // exposes /metrics
```

Install the required NuGet packages:
```
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package OpenTelemetry.Instrumentation.Runtime
dotnet add package OpenTelemetry.Instrumentation.Process
dotnet add package OpenTelemetry.Exporter.Prometheus.AspNetCore
```

### 2. Configure the OTel Collector (or SigNoz agent) to scrape your app

```yaml
# otel-collector-config.yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: aspnet-core
          scrape_interval: 15s
          static_configs:
            - targets: ["<your-app-host>:5000"]
          # Add resource attributes as labels
          relabel_configs:
            - target_label: service_name
              replacement: "my-aspnet-service"
            - target_label: deployment_environment
              replacement: "production"
```

### 3. Import into SigNoz

1. Open SigNoz → Dashboards → **New Dashboard** → **Import JSON**
2. Upload `aspnet-prometheus-v2.json`
3. Select your `deployment.environment` and `service.name` from the top-level variable dropdowns

## Dashboard Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by environment (production, staging, etc.) |
| `service.name` | Filter by service/application name |
