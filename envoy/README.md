# Envoy Proxy Monitoring Dashboard for SigNoz

SigNoz dashboard monitoring Envoy proxy traffic, performance, errors, backends, and resources.

## Prerequisites

- Envoy proxy with [OpenTelemetry stats sink](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/stat_sinks/open_telemetry_stat_sink) configured
- SigNoz collector running and accessible

### 1. Deploy OpenTelemetry Collector

Deploy the OTel Collector in your Kubernetes cluster to forward metrics to SigNoz Cloud:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: default
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317

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
          receivers: [otlp]
          processors: [batch]
          exporters: [otlp]
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      containers:
      - name: otel-collector
        image: otel/opentelemetry-collector-contrib:0.144.0
        args:
          - "--config=/conf/config.yaml"
        volumeMounts:
        - name: config
          mountPath: /conf
        ports:
        - containerPort: 4317  # OTLP gRPC
          name: otlp-grpc
      volumes:
      - name: config
        configMap:
          name: otel-collector-config
---
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
  namespace: default
spec:
  selector:
    app: otel-collector
  ports:
  - name: otlp-grpc
    port: 4317
    targetPort: 4317
```

Replace the following:

- `<region>`: Your SigNoz Cloud [region](https://signoz.io/docs/ingestion/signoz-cloud/overview/#endpoint)
- `<your-ingestion-key>`: Your [ingestion key](https://signoz.io/docs/ingestion/signoz-cloud/keys/).

## Envoy Configuration

Add OpenTelemetry stats sink to your Envoy config:

```yaml
stats_sinks:
  - name: envoy.stat_sinks.open_telemetry
    typed_config:
      "@type": type.googleapis.com/envoy.extensions.stat_sinks.open_telemetry.v3.SinkConfig
      grpc_service:
        envoy_grpc:
          cluster_name: opentelemetry_collector
      emit_tags_as_attributes: true
      report_histograms_as_deltas: true

stats_config:
  stats_tags:
    - tag_name: service.name
      fixed_value: envoy-proxy-k8s
    - tag_name: namespace
      fixed_value: default
    - tag_name: deployment_environment
      fixed_value: production
    - tag_name: cluster
      fixed_value: k8s-cluster

clusters:
  - name: opentelemetry_collector
    type: STRICT_DNS
    lb_policy: ROUND_ROBIN
    typed_extension_protocol_options:
      envoy.extensions.upstreams.http.v3.HttpProtocolOptions:
        "@type": type.googleapis.com/envoy.extensions.upstreams.http.v3.HttpProtocolOptions
        explicit_http_config:
          http2_protocol_options: {}
    load_assignment:
      cluster_name: opentelemetry_collector
      endpoints:
        - lb_endpoints:
            - endpoint:
                address:
                  socket_address:
                    address: <your-collector-address>
                    port_value: 4317
```

## Key Settings

- `emit_tags_as_attributes: true` - Exposes Envoy labels as filterable attributes
- `report_histograms_as_deltas: true` - Required for P50/P95/P99 latency metrics
- `stats_tags` - Becomes dashboard variables (`$service.name`, `$namespace`, etc.)

## Dashboard Variables

| Variable                  | Maps to Envoy Tag        |
| ------------------------- | ------------------------ |
| `$service.name`           | `service.name`           |
| `$namespace`              | `namespace`              |
| `$cluster`                | `cluster`                |
| `$deployment_environment` | `deployment_environment` |
