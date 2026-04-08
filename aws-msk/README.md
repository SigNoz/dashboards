# AWS MSK Cluster Monitoring Dashboard

AWS Managed Streaming for Apache Kafka (MSK) monitoring dashboard for [SigNoz](https://signoz.io/). Fixes [SigNoz/signoz#6036](https://github.com/SigNoz/signoz/issues/6036).

Uses the OpenTelemetry [`prometheus`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md) receiver to scrape JMX Exporter metrics and the [`awscloudwatch`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/awscloudwatchreceiver/README.md) receiver for CloudWatch metrics.

## Sections

| #   | Section                | Covers                                                       |
| --- | ---------------------- | ------------------------------------------------------------ |
| 1   | Broker Overview        | Active controller, offline partitions, under-replicated, min ISR |
| 2   | Topic Metrics          | Messages in rate, bytes in/out rate                          |
| 3   | Partition Metrics      | Partition count by topic, log segment count, log size        |
| 4   | Consumer Metrics       | Consumer group lag, fetch request rate, produce request rate  |
| 5   | AWS CloudWatch Metrics | CPU utilization, memory usage, disk usage, network in/out    |

## OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: "msk-jmx"
          scrape_interval: 30s
          static_configs:
            - targets: ["<broker-1>:11001", "<broker-2>:11001"]
  awscloudwatch:
    region: "<aws-region>"
    poll_interval: 60s
    metrics:
      named:
        - namespace: "AWS/Kafka"
          metric_name:
            - "CpuUser"
            - "MemoryUsed"
            - "KafkaDataLogsDiskUsed"
            - "NetworkRxPackets"
            - "NetworkTxPackets"
          dimensions:
            - name: "Cluster Name"
              value: "<cluster-name>"

processors:
  batch:
    timeout: 10s
  resource:
    attributes:
      - key: service.name
        value: "aws-msk"
        action: insert

exporters:
  otlp:
    endpoint: "ingest.<region>.signoz.cloud:443"
    headers:
      signoz-ingestion-key: "<your-ingestion-key>"

service:
  pipelines:
    metrics:
      receivers: [prometheus, awscloudwatch]
      processors: [batch, resource]
      exporters: [otlp]
```

## Dashboard Variables

- `deployment.environment` — Deployment Environment
- `cluster_name` — MSK Cluster Name
- `broker_id` — Broker ID
- `topic` — Topic
- `consumer_group` — Consumer Group
- `service.name` — Service Name

### Notes

- MSK with open monitoring enabled exposes JMX metrics via port 11001.
- CloudWatch metrics require appropriate IAM permissions for the OTel Collector.
- Screenshots will be added to the `assets/` directory.
