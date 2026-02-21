# ASP.NET Metrics Dashboard
 
Monitor your ASP.NET application performance using OpenTelemetry metrics with SigNoz.
 
## Dashboard Sections
 
### Application Performance
- **CPU Usage** — Process CPU time consumed
- **Memory Usage** — Process memory consumption
- **Request Rate** — Incoming HTTP requests per second
 
### Request and Response
- **Request Latency (P50 / P90 / P99)** — Time taken to serve HTTP requests at various percentiles
- **Error Rate (4xx / 5xx)** — Rate of error responses grouped by status code
 
### Process Metrics
- **Active Requests** — Currently active HTTP requests
- **Thread Count** — Number of process threads
- **GC Collections** — .NET garbage collector collection counts by generation
 
## Variables
 
| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by environment (production, staging) |
| `service.name` | Filter by ASP.NET service name |
 
## Prerequisites
 
- ASP.NET application instrumented with OpenTelemetry .NET SDK
- Metrics exporter configured to send data to SigNoz via OTLP
- Enable ASPNETCORE, PROCESS, and NETRUNTIME instrumentations
 
## Metrics Used
 
| Metric | Source |
|--------|--------|
| `process.cpu.time` | Process instrumentation |
| `process.memory.usage` | Process instrumentation |
| `http.server.request.duration` | ASP.NET Core instrumentation |
| `http.server.active_requests` | ASP.NET Core instrumentation |
| `process.thread.count` | Process instrumentation |
| `process.runtime.dotnet.gc.collections.count` | .NET Runtime instrumentation |
 
## References
 
- [OpenTelemetry .NET Metrics Instrumentations](https://opentelemetry.io/docs/zero-code/net/instrumentations/#metrics-instrumentations)
- [Grafana ASP.NET OTEL Dashboard](https://grafana.com/grafana/dashboards/17706-asp-net-otel-metrics/)
- [SigNoz Documentation](https://signoz.io/docs/)
 
