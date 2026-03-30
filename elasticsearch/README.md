# Elasticsearch Monitoring

This dashboard uses OpenTelemetry metrics from the `elasticsearchreceiver` and expects the receiver to send the Elasticsearch resource labels below into SigNoz:

- `elasticsearch.cluster.name`
- `elasticsearch.node.name`
- `elasticsearch.index.name`
- `thread_pool_name`
- metric attributes such as `status`, `state`, `name`, and `operation`

## Prerequisites

- Elasticsearch 7.9 or newer
- An account with the Elasticsearch `monitor` or `manage` cluster privilege when security is enabled
- A running OpenTelemetry Collector that exports metrics to SigNoz over OTLP

## OpenTelemetry Collector

Configure the Elasticsearch receiver in the Collector and point the OTLP exporter at your SigNoz deployment.

```yaml
receivers:
  elasticsearch:
    endpoint: http://localhost:9200
    username: elastic
    password: ${env:ELASTIC_PASSWORD}
    collection_interval: 30s
    nodes: ["_all"]
    indices: ["_all"]

processors:
  batch: {}

exporters:
  otlp:
    endpoint: <SIGNOZ_OTLP_ENDPOINT>
    tls:
      insecure: false

service:
  pipelines:
    metrics:
      receivers: [elasticsearch]
      processors: [batch]
      exporters: [otlp]
```

## Notes

- The search panels use `operation=query` because that is the value emitted by the OpenTelemetry Elasticsearch receiver for search work.
- The dashboard variables query `signoz_metrics.distributed_time_series_v4` and only list labels seen in the last 5 minutes of samples.
- If you scope the receiver with `nodes` or `indices`, the dashboard automatically reflects the subset of data exported to SigNoz.
- The `index_name` variable is included for dashboards and future panels that drill into index-level metrics, even though the current panel set focuses on cluster and node health.
