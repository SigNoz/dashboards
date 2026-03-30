# AWS MSK Cluster Monitoring

This dashboard expects two Prometheus scrape jobs in the OpenTelemetry Collector:

- Kafka JMX metrics on port `11001`
- Node Exporter metrics on port `11002`

The dashboard filters depend on these labels being present on both jobs:

- `cluster_name`
- `instance`

## Prerequisites

- A JMX exporter is running on each MSK broker and exposing Kafka metrics on `:11001/metrics`
- A node exporter is running on each broker host and exposing infrastructure metrics on `:11002/metrics`
- All broker targets for a cluster share the same `cluster_name` label value

## OpenTelemetry Collector

Add a Prometheus receiver similar to the example below and update the broker hostnames for your environment.

```yaml
receivers:
  prometheus/aws_msk:
    config:
      scrape_configs:
        - job_name: aws-msk-jmx
          scrape_interval: 30s
          metrics_path: /metrics
          static_configs:
            - targets:
                - b-1.example.kafka.us-east-1.amazonaws.com:11001
                - b-2.example.kafka.us-east-1.amazonaws.com:11001
                - b-3.example.kafka.us-east-1.amazonaws.com:11001
              labels:
                cluster_name: prod-msk

        - job_name: aws-msk-node
          scrape_interval: 30s
          metrics_path: /metrics
          static_configs:
            - targets:
                - b-1.example.kafka.us-east-1.amazonaws.com:11002
                - b-2.example.kafka.us-east-1.amazonaws.com:11002
                - b-3.example.kafka.us-east-1.amazonaws.com:11002
              labels:
                cluster_name: prod-msk

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
      receivers: [prometheus/aws_msk]
      processors: [batch]
      exporters: [otlp]
```

## Notes

- The `broker_id` variable is populated from the `instance` label so the infrastructure and Kafka panels can use the same broker selector.
- The `consumer_group` variable reads the `consumergroup` Kafka label exposed by the JMX exporter.
- If you do not already attach `cluster_name` to the scraped metrics, add it in `static_configs.labels` as shown above.
- After the collector is reloaded, verify that SigNoz receives metrics such as `kafka_server_brokertopicmetrics_bytesin_total`, `kafka_server_replicamanager_underreplicatedpartitions`, and `node_cpu_seconds_total`.
