# ASP.NET Metrics Dashboard for SigNoz

Pre-built SigNoz dashboard for monitoring ASP.NET applications instrumented with OpenTelemetry .NET.

## Sections

- **Application Performance** -- CPU usage, memory usage, and HTTP request rate.
- **Request and Response** -- Request latency, 5xx error rate, and active in-flight requests.
- **Process Metrics** -- Thread count, .NET GC collection rate by generation, and GC heap size.

## Metrics Used

| Metric | Type | Panel |
|--------|------|-------|
| `process.cpu.utilization` | Gauge | CPU Usage |
| `process.memory.usage` | Gauge | Memory Usage |
| `http.server.request.duration` | Sum | Request Rate, Latency, Error Rate |
| `http.server.active_requests` | Gauge | Active Requests |
| `process.thread.count` | Gauge | Thread Count |
| `process.runtime.dotnet.gc.collections.count` | Sum | GC Collection Count |
| `process.runtime.dotnet.gc.heap.size` | Gauge | Process Memory (GC Heap) |

## Variables

- `deployment.environment` -- Filter by deployment environment.
- `service.name` -- Filter by service name.

## Installation

Import `aspnet-otlp-v1.json` via the SigNoz dashboard import UI or place it in SigNoz's dashboard provisioning directory.
