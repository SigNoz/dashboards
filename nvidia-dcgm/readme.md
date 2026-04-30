# NVIDIA DCGM Exporter Monitoring Dashboard

Pre-built SigNoz dashboard for monitoring NVIDIA GPUs using [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) metrics via Prometheus.

## Metrics Ingestion

DCGM Exporter exposes GPU metrics on `:9400/metrics`. Configure the OpenTelemetry Collector to scrape these:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'dcgm-exporter'
          scrape_interval: 15s
          static_configs:
            - targets: ['<dcgm-exporter-host>:9400']

exporters:
  otlp:
    endpoint: "<signoz-otel-collector>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Dashboard Panels

| Section | Panel | Metric |
|---------|-------|--------|
| Temperature | GPU Temperature | `DCGM_FI_DEV_GPU_TEMP` |
| Temperature | GPU Avg. Temp | `DCGM_FI_DEV_GPU_TEMP` |
| Power | GPU Power Usage | `DCGM_FI_DEV_POWER_USAGE` |
| Power | GPU Power Total | `DCGM_FI_DEV_POWER_USAGE` |
| Clock | GPU SM Clocks | `DCGM_FI_DEV_SM_CLOCK` |
| Utilization | GPU Utilization | `DCGM_FI_DEV_GPU_UTIL` |
| Memory | GPU Framebuffer Mem Used | `DCGM_FI_DEV_FB_USED` |
| Compute | Tensor Core Utilization | `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE` |

## Variables

- `gpu` — Filter by GPU UUID or index
- `instance` — Filter by host instance
- `job` — Filter by scrape job name

## Prerequisites

- NVIDIA GPU with DCGM driver installed
- [dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter) running
- OpenTelemetry Collector configured to scrape DCGM metrics
- SigNoz instance
