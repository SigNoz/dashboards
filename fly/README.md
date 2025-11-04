# Fly.io Dashboards

This directory contains dashboards for monitoring Fly.io applications using Prometheus metrics. The dashboards provide insights into CPU, memory, network, and HTTP performance for applications running on Fly.io.

## Dashboards

- **fly-prometheus-v1.json**: Comprehensive dashboard adapted from the official Fly Grafana dashboard queries. Includes panels for CPU, memory, network, TCP, and HTTP metrics.
- **fly-cpu-mem-prometheus-v1.json**: Focused dashboard for CPU and memory usage, aggregated by app, using Fly federated Prometheus metrics.

## Dashboard Panels

### fly-prometheus-v1.json

Key panels include:

- **CPU Usage**: Visualizes CPU utilization across apps and instances.
- **Memory Usage**: Tracks memory consumption and trends.
- **Network Traffic**: Monitors data transfer, TCP connections, and errors.
- **HTTP Metrics**: Shows HTTP request rates, error rates, and heatmaps for edge/app traffic.

### fly-cpu-mem-prometheus-v1.json

Key panels include:

- **CPU Utilisation**: Percentage of total CPU time by app.
- **CPU User/System**: Breakdown of user and system CPU time.
- **Memory Used (bytes/percent)**: Memory usage in bytes and as a percentage.
- **Memory Cached**: Amount of memory used for caching.

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
- [Official Fly Grafana Dashboards](https://github.com/superfly/grafana-dashboards)
