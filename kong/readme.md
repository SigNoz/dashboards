# Kong Gateway Monitoring Dashboard for SigNoz

Comprehensive monitoring dashboard for Kong Gateway using OTLP metrics from the Kong OpenTelemetry plugin. Tracks request throughput, latency percentiles, error rates, connection states, traffic volume, plugin performance, and resource usage.

## Dashboard Sections

| Section | Panels | Description |
|---------|--------|-------------|
| General Overview | 5 | Total Requests, Active Connections, Accepted Connections, CPU Usage, Memory Usage |
| Request Metrics | 4 | Request Rate, Response Status Codes, Request Size, Response Size |
| Latency Metrics | 3 | Average Request Latency, Request Latency Percentiles, Upstream Latency |
| Error Metrics | 4 | Total 5xx Errors, Error Rate, Top Error Types, Failed Requests by Service |
| Traffic Metrics | 4 | Incoming Traffic Volume, Outgoing Traffic Volume, Connection Rate, Connection States |
| Plugin Metrics | 3 | Kong Processing Latency, Kong Latency Percentiles, Kong Latency by Route |
| Resource Usage | 3 | CPU Usage Over Time, Memory Usage Over Time, Active Connections Over Time |

## Metrics Reference

All metrics are collected via the Kong OpenTelemetry plugin and exported in OTLP format.

| Metric Name | Type | Unit | Description |
|-------------|------|------|-------------|
| `kong.request.count` | Sum | count | Total request count, with attributes: service, route, status_code |
| `kong.request.latency` | Histogram | ms | Total request latency (client to response) |
| `kong.upstream_latency` | Histogram | ms | Time spent waiting for upstream service response |
| `kong.kong_latency` | Histogram | ms | Kong internal processing latency (plugin execution) |
| `kong.request.size` | Histogram | bytes | Request body size |
| `kong.response.size` | Histogram | bytes | Response body size |
| `kong.connections.active` | Gauge | count | Current active client connections |
| `kong.connections.accepted` | Sum | count | Total accepted connections |
| `kong.connections.handled` | Sum | count | Total handled connections |
| `kong.connections.reading` | Gauge | count | Connections in reading state |
| `kong.connections.writing` | Gauge | count | Connections in writing state |
| `kong.connections.waiting` | Gauge | count | Connections in waiting (keep-alive) state |
| `process.cpu.seconds.total` | Sum | seconds | Total CPU seconds consumed by the Kong process |
| `process.resident_memory_bytes` | Gauge | bytes | Resident memory usage of the Kong process |

## Variables

| Variable | Description |
|----------|-------------|
| `deployment.environment` | Filter by deployment environment (e.g., production, staging) |
| `service.name` | Filter by OTel service name |
| `namespace` | Filter by Kubernetes namespace |
| `cluster` | Filter by cluster name |

## Prerequisites

1. Kong Gateway with the OpenTelemetry plugin enabled
2. An OpenTelemetry Collector receiving OTLP data from Kong
3. SigNoz configured as an OTLP exporter destination

## Kong OpenTelemetry Plugin Configuration

Enable the OTel plugin in Kong to export metrics:

```yaml
plugins:
  - name: opentelemetry
    config:
      endpoint: "http://otel-collector:4318/v1/traces"
      resource_attributes:
        service.name: "kong-gateway"
        deployment.environment: "production"
```

## OpenTelemetry Collector Configuration

Configure the OTel Collector to receive from Kong and export to SigNoz:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:
    send_batch_size: 10000
    timeout: 10s
  resourcedetection:
    detectors: [env, system]
    timeout: 5s
    override: false

exporters:
  otlp/signoz:
    endpoint: "signoz-otel-collector:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch, resourcedetection]
      exporters: [otlp/signoz]
    traces:
      receivers: [otlp]
      processors: [batch, resourcedetection]
      exporters: [otlp/signoz]
```

## Kubernetes Deployment (Helm)

If running Kong on Kubernetes via Helm, enable the OTel plugin in `values.yaml`:

```yaml
env:
  tracing_instrumentations: all
  tracing_sampling_rate: 1.0

plugins:
  configMaps:
    - name: kong-plugins
      pluginName: opentelemetry

extraObjects:
  - apiVersion: configuration.konghq.com/v1
    kind: KongClusterPlugin
    metadata:
      name: opentelemetry
      annotations:
        kubernetes.io/ingress.class: kong
      labels:
        global: "true"
    config:
      endpoint: "http://otel-collector.monitoring:4318/v1/traces"
      resource_attributes:
        service.name: "kong-gateway"
    plugin: opentelemetry
```

## Importing the Dashboard

1. Open SigNoz UI
2. Navigate to **Dashboards** > **New Dashboard** > **Import JSON**
3. Upload or paste the contents of `kong-otlp-v1.json`
4. Save the dashboard

## Troubleshooting

- **No data showing**: Verify the Kong OTel plugin is active (`curl http://kong-admin:8001/plugins`) and the collector is receiving data.
- **Missing metrics**: Some connection metrics require Kong to be compiled with the `ngx_http_stub_status_module`. Verify with `kong version -v`.
- **Variable dropdowns empty**: Ensure metric data has been flowing for at least 1 day (the variable queries use the `distributed_time_series_v4_1day` table).
