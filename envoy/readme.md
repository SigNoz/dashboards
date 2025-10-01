# Envoy Dashboard - OTLP

## Metrics Ingestion

To emit OpenTelemetry metrics from Envoy you must enable the [OpenTelemetry stat sink](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/stat_sinks/open_telemetry_stat_sink). A minimal static bootstrap example that ships metrics to an OpenTelemetry Collector running at `otel-collector:4317` looks like this:

```yaml
stats_sinks:
  - name: envoy.stat_sinks.open_telemetry
    typed_config:
      "@type": type.googleapis.com/envoy.extensions.stat_sinks.open_telemetry.v3.SinkConfig
      grpc_service:
        envoy_grpc:
          cluster_name: otel-collector
static_resources:
  clusters:
    - name: otel-collector
      type: STRICT_DNS
      connect_timeout: 1s
      load_assignment:
        cluster_name: otel-collector
        endpoints:
          - lb_endpoints:
              - endpoint:
                  address:
                    socket_address:
                      address: otel-collector
                      port_value: 4317
```

On the SigNoz side you only need an OTLP receiver. The snippet below extends the default SigNoz Collector configuration to fan-in Envoy metrics:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317

processors:
  batch: {}

exporters:
  clickhouse: {}

service:
  pipelines:
    metrics/standard:
      receivers: [otlp]
      processors: [batch]
      exporters: [clickhouse]
```

Envoy’s stat names (for example `downstream_cx_active`, `downstream_rq_time`, `upstream_rq_total`, etc.) become OpenTelemetry metrics prefixed with the component that reported them, such as `envoy_http_downstream_cx_active` or `envoy_cluster_upstream_rq_total`. Refer to the [HTTP connection manager](https://www.envoyproxy.io/docs/envoy/latest/_sources/configuration/http/http_conn_man/stats.rst.txt) and [cluster manager](https://www.envoyproxy.io/docs/envoy/latest/_sources/configuration/upstream/cluster_manager/cluster_stats.rst.txt) statistics tables for the full catalogue.

## Variables

The dashboard exposes four resource-scoped variables so that the same template works across multi-tenant environments:

- `namespace`: Kubernetes namespace (maps to `k8s.namespace.name`).
- `deployment.environment`: Logical environment tag (`deployment.environment`).
- `service.name`: OpenTelemetry service name reported by Envoy.
- `cluster`: Cluster identifier (for example `prod-eu` or `staging`).

Set each variable to `.*` to view aggregate metrics across all values or narrow the scope with an exact match/regex.

## Sections & Panels

### General Overview
- **Active Connections** – `sum(envoy_http_downstream_cx_active)`
- **Total Requests** – `sum(envoy_http_downstream_rq_total)`
- **Request Rate** – `sum(rate(envoy_http_downstream_rq_total[5m]))` grouped by `envoy_http_conn_manager_prefix`
- **Uptime** – `max(envoy_server_uptime)`

### Request Metrics
- **HTTP Request Throughput** – `sum(rate(envoy_http_downstream_rq_total[5m]))`
- **Ingress Bytes** – `sum(rate(envoy_http_downstream_cx_rx_bytes_total[5m]))`
- **Average Response Size** – `sum(rate(envoy_http_downstream_cx_tx_bytes_total[5m])) / sum(rate(envoy_http_downstream_rq_total[5m]))`

### Response Metrics
- **Response Code Class Breakdown** – `sum(rate(envoy_http_downstream_rq_xx[5m]))` by `envoy_response_code_class`
- **Average Response Time per Listener** – `sum(rate(envoy_http_downstream_rq_time_sum[5m])) / sum(rate(envoy_http_downstream_rq_time_count[5m]))`
- **Latency Histogram (LE buckets)** – `sum(rate(envoy_http_downstream_rq_time_bucket[5m]))` by `le`

### Latency Metrics
- **Overall Mean Latency** – same ratio of `_sum` to `_count`
- **P95 Latency by Listener** – `histogram_quantile(0.95, rate(envoy_http_downstream_rq_time_bucket[5m]))`
- **Downstream Distribution** – pie chart of `rate(envoy_http_downstream_rq_total[5m])` grouped by `envoy_http_conn_manager_prefix`

### Error Metrics
- **Total 4xx/5xx Errors** – `sum(envoy_http_downstream_rq_xx{envoy_response_code_class=~"4|5"})`
- **Error Rate by Class** – `sum(rate(envoy_http_downstream_rq_xx{envoy_response_code_class=~"4|5"}[5m]))`

### Resource Usage
- **CPU Seconds / s** – `rate(process_cpu_seconds_total[5m])`
- **Allocated Memory** – `max(envoy_server_memory_allocated)`
- **Disk I/O Bytes / s** – host metrics `container_fs_reads_bytes_total` + `container_fs_writes_bytes_total` (scope to Envoy workload)

### Network I/O
- **Upstream Throughput** – `rate(envoy_cluster_upstream_cx_tx_bytes_total[5m]) + rate(envoy_cluster_upstream_cx_rx_bytes_total[5m])`
- **Connection Establish Rate** – `sum(rate(envoy_cluster_upstream_cx_total[5m]))`
- **Rejected Connections** – `rate(envoy_cluster_upstream_cx_connect_fail[5m]) + rate(envoy_cluster_upstream_cx_connect_timeout[5m])`

### Upstream & Downstream
- **Upstream Request Volume** – `sum(rate(envoy_cluster_upstream_rq_total[5m]))` by `envoy_cluster_name`
- **Upstream Error Rate** – `sum(rate(envoy_cluster_upstream_rq_xx{envoy_response_code_class=~"4|5"}[5m]))` by `envoy_cluster_name`
- **Downstream Distribution** – mirrored pie/table from latency section

> Note:    All queries automatically inherit the four dashboard variables so the template can be dropped into any SigNoz tenant without manual rewiring.




