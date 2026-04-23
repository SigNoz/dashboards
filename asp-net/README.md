# ASP.NET Metrics Dashboard - Prometheus

Comprehensive ASP.NET application monitoring dashboard covering request performance, response metrics, connection stats, runtime diagnostics, and outgoing HTTP call tracking.

## Prerequisites

- ASP.NET application instrumented with [OpenTelemetry .NET](https://opentelemetry.io/docs/zero-code/net/instrumentations/)
- Prometheus metrics endpoint exposed (via OpenTelemetry or `dotnet-monitor`)
- SigNoz collector running and accessible

### 1. Deploy OpenTelemetry Collector with Prometheus Receiver

Deploy the OTel Collector to scrape ASP.NET Prometheus metrics and forward them to SigNoz:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: default
data:
  config.yaml: |
    receivers:
      prometheus:
        config:
          scrape_configs:
            - job_name: 'aspnet-app'
              kubernetes_sd_configs:
                - role: pod
              relabel_configs:
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
                  action: keep
                  regex: "true"
                - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
                  action: replace
                  target_label: __address__
                  regex: (.+)
                  replacement: ${1}:9464

    processors:
      batch:
        timeout: 10s
        send_batch_size: 1024

    exporters:
      otlp:
        endpoint: "ingest.<region>.signoz.cloud:443"
        tls:
          insecure: false
        headers:
          signoz-ingestion-key: "<your-ingestion-key>"

    service:
      pipelines:
        metrics:
          receivers: [prometheus]
          processors: [batch]
          exporters: [otlp]
```

Replace the following:

- `<region>`: Your SigNoz Cloud [region](https://signoz.io/docs/ingestion/signoz-cloud/overview/#endpoint)
- `<your-ingestion-key>`: Your [ingestion key](https://signoz.io/docs/ingestion/signoz-cloud/keys/)

### 2. Enable OpenTelemetry Instrumentation in ASP.NET

Add the OpenTelemetry NuGet packages and configure metrics export:

```csharp
builder.Services.AddOpenTelemetry()
    .WithMetrics(metrics =>
    {
        metrics.AddAspNetCoreInstrumentation()
               .AddHttpClientInstrumentation()
               .AddRuntimeInstrumentation()
               .AddProcessInstrumentation()
               .AddPrometheusExporter();
    });

app.MapPrometheusScrapingEndpoint();
```

## Dashboard Sections

| Section | Panels | Description |
| --- | --- | --- |
| **Application Performance** | CPU Usage, Memory Usage, Request Rate, Active Requests, Avg Latency, Error Rate | High-level application health |
| **Request and Response** | Response Status Codes, Latency Percentiles (P50/P95/P99), Latency by Route, Request Rate by Method | Detailed request/response analysis |
| **Connection Metrics** | Active Connections (Kestrel), Connection Rate, Active Connections Over Time | Kestrel server connection tracking |
| **Process Metrics** | CPU Usage Over Time, Memory Usage Over Time, GC Collections by Generation, GC Heap Size & Thread Pool | .NET runtime diagnostics |
| **Outgoing HTTP Calls** | Outgoing HTTP Request Rate, Outgoing HTTP Latency, Outgoing HTTP Errors | External dependency call monitoring |

## Dashboard Variables

| Variable                  | Description              |
| ------------------------- | ------------------------ |
| `$namespace`              | Kubernetes namespace     |
| `$service.name`           | Service name             |
| `$deployment_environment` | Deployment environment   |

## Metrics Reference

This dashboard uses standard [ASP.NET OpenTelemetry metrics](https://opentelemetry.io/docs/zero-code/net/instrumentations/#metrics-instrumentations):

- `http_server_request_duration_seconds` -- Request duration histogram (sum, count, bucket)
- `http_server_active_requests` -- Currently active HTTP requests
- `kestrel_connections` -- Total Kestrel connections
- `kestrel_active_connections` -- Active Kestrel connections
- `process_cpu_seconds_total` -- Process CPU usage
- `process_resident_memory_bytes` -- Process memory usage
- `dotnet_gc_collections_total` -- GC collection count by generation
- `dotnet_gc_heap_size_bytes` -- GC managed heap size
- `dotnet_threadpool_threads_count` -- Thread pool thread count
- `http_client_request_duration_seconds` -- Outgoing HTTP client request duration (sum, count)

## Screenshot

<!-- Dashboard screenshot placeholder -->
![ASP.NET Dashboard](assets/asp-net-dashboard-preview.png)
