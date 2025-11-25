# Fly.io Dashboards

This directory contains dashboards for monitoring Fly.io applications using Prometheus metrics. The dashboards provide insights into CPU, memory, network, and HTTP performance for applications running on Fly.io.

## Dashboards

- **fly-prometheus-v1.json**: Dashboard for CPU, memory usage, data transfer, and TCP aggregated by app, using Fly federated Prometheus metrics.

## Dashboard Panels

### fly-prometheus-v1.json

Key panels include:

- **CPU Utilisation**: Percentage of total CPU time by app.
- **CPU User/System**: Breakdown of user and system CPU time.
- **Memory Used (bytes/percent)**: Memory usage in bytes and as a percentage.

## Usage

1. **Import the dashboard JSON** into your SigNoz or Grafana instance.
2. **Configure Prometheus** to scrape Fly.io metrics. Ensure your Prometheus setup has access to Fly.io's federated metrics endpoints.
3. **Adjust variables** as needed for your environment (e.g., app names, regions).

### Minimal otel-collector-config.yaml delta

Be sure to mount your fly token in to the path specified.

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        # ...your existing jobs...

        - job_name: fly-federate
          scheme: https
          metrics_path: /prometheus/your-org/federate
          params:
            match[]:
              - '{__name__=~"fly_.*"}'
          static_configs:
            - targets: ['api.fly.io']
          authorization:
            type: FlyV1
            credentials_file: /etc/otel/secret/fly_federate_token
```

## References

- [Fly.io Metrics Documentation](https://fly.io/docs/reference/metrics/)
