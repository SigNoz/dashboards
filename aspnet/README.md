# ASP.NET Metrics Dashboard

Monitor ASP.NET application performance using OpenTelemetry (OTLP) metrics.

## Panels

| Panel | Type | Description |
|-------|------|-------------|
| Request Rate | Graph | HTTP requests per second by route |
| Average Response Time | Graph | Average request duration by route |
| Active Requests | Value | Currently active HTTP requests |
| Error Rate (5xx) | Graph | Rate of 5xx error responses |
| GC Collections | Graph | .NET garbage collection rate by generation |
| Thread Pool Size | Graph | Active thread pool thread count |
| Memory Usage (GC Heap) | Graph | Managed heap size in bytes |
| CPU Utilization | Graph | Process CPU utilization (0-100%) |

## Variables

- `namespace` — Kubernetes namespace
- `deployment_environment` — Deployment environment
- `service_name` — Application service name
- `cluster` — Kubernetes cluster

## Metrics Used

All metrics follow [OpenTelemetry .NET semantic conventions](https://opentelemetry.io/docs/specs/semconv/dotnet/):

- `http.server.request.duration` (Histogram) — HTTP request duration
- `http.server.active_requests` (UpDownCounter) — Active request count
- `process.runtime.dotnet.gc.collections.count` (Sum) — GC collections
- `process.runtime.dotnet.thread_pool.threads.count` (Gauge) — Thread pool threads
- `process.runtime.dotnet.gc.heap.size` (Gauge) — GC heap size
- `process.cpu.utilization` (Gauge) — CPU utilization

## Query Type

Builder (OTLP metrics)
