# ASP.NET Core Dashboard - Prometheus

Monitors ASP.NET Core applications that expose Prometheus metrics via the `prometheus-net` middleware. Covers HTTP traffic, Kestrel web server, .NET runtime (GC and thread pool), and process-level resource usage.

## Metrics Ingestion

Add the `prometheus-net.AspNetCore` NuGet package and register the middleware in your app:

```csharp
// Program.cs (.NET 6+)
builder.Services.AddHttpMetrics();
// ...
app.UseHttpMetrics();
app.MapMetrics(); // exposes /metrics endpoint
```

Configure the OpenTelemetry Collector to scrape the `/metrics` endpoint:

```yaml
# otel-collector-config.yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: aspnet-core
          scrape_interval: 15s
          static_configs:
            - targets: ['<your-app-host>:<port>']

exporters:
  otlp:
    endpoint: '<signoz-collector-endpoint>:4317'

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Variables

- `{{job}}`: Prometheus `job` label — matches the `job_name` in your scrape config
- `{{instance}}`: Application instance (`host:port`), supports multi-select

## Dashboard Panels

### HTTP Traffic

| Panel | Metric | Description |
|---|---|---|
| Request Rate | `http_requests_received_total` | Requests per second (stat) |
| 5xx Error Rate | `http_requests_received_total{code=~"5.."}` | Fraction of server errors (stat) |
| Latency p50 | `http_request_duration_seconds_bucket` | Median latency (stat) |
| Latency p99 | `http_request_duration_seconds_bucket` | 99th percentile latency (stat) |
| Request Rate by Route | `http_requests_received_total` | Time-series broken down by method/route/code |
| Request Latency Percentiles | `http_request_duration_seconds_bucket` | p50/p90/p95/p99 over time |
| Requests by Status Code Class | `http_requests_received_total` | Stacked 2xx/3xx/4xx/5xx |
| Latency by Route (p50/p99) | `http_request_duration_seconds_bucket` | Per-route latency comparison |

### Kestrel

| Panel | Metric | Description |
|---|---|---|
| Active Connections | `kestrel_active_connections` | Concurrent open connections |
| Queued Connections | `kestrel_queued_connections` | Connections waiting in accept queue |
| Rejected Connections/s | `kestrel_rejected_connections_total` | Connection limit violations |
| Connection Duration (p50/p99) | `kestrel_connection_duration_seconds_bucket` | Connection lifetime percentiles |

### .NET Runtime

| Panel | Metric | Description |
|---|---|---|
| GC Collections/s by Generation | `dotnet_collection_count_total` | Gen0/Gen1/Gen2 GC frequency |
| Managed Heap Size | `dotnet_total_memory_bytes` | Total GC heap in bytes |
| Thread Pool Queue Depth | `dotnet_threadpool_queue_length` | Work items waiting for a thread |
| Thread Pool Threads & Completed Items | `dotnet_threadpool_num_threads`, `dotnet_threadpool_completed_items_total` | Active threads and throughput |

### Process Resources

| Panel | Metric | Description |
|---|---|---|
| Process CPU Usage | `process_cpu_seconds_total` | CPU seconds consumed per second |
| Process Memory Usage | `process_working_set_bytes`, `process_private_memory_bytes` | RSS and private memory |
