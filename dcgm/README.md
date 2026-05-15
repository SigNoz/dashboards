# NVIDIA DCGM Exporter Dashboard

Monitoring dashboard for NVIDIA GPUs using the [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) with SigNoz.

## Panels

| Panel | Metric | Description |
|-------|--------|-------------|
| GPU Utilization | `DCGM_FI_DEV_GPU_UTIL` | GPU utilization percentage |
| GPU Memory Used | `DCGM_FI_DEV_FB_USED` | Framebuffer memory used (MB) |
| GPU Temperature | `DCGM_FI_DEV_GPU_TEMP` | GPU temperature (°C) |
| GPU Power Draw | `DCGM_FI_DEV_POWER_USAGE` | GPU power consumption (W) |
| PCIe TX Throughput | `DCGM_FI_DEV_PCIE_TX_THRU` | PCIe transmit throughput |
| PCIe RX Throughput | `DCGM_FI_DEV_PCIE_RX_THRU` | PCIe receive throughput |
| SM Occupancy | `DCGM_FI_PROF_SM_OCCUPANCY` | Streaming multiprocessor occupancy (%) |
| XID Errors | `DCGM_FI_DEV_XID_ERRORS` | XID error count |

## Variables

- **gpu** — Filter by GPU identifier
- **k8s.node.name** — Filter by Kubernetes node

## Data Ingestion

### Prerequisites

1. Deploy [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) on GPU nodes
2. Configure OpenTelemetry Collector to scrape DCGM metrics

### OTel Collector Config

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'dcgm-exporter'
          scrape_interval: 15s
          static_configs:
            - targets: ['dcgm-exporter:9400']

processors:
  resource/env:
    attributes:
      - key: deployment.environment
        value: prod
        action: upsert
  batch: {}

exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    tls:
      insecure: false
    headers:
      "signoz-access-token": "<SIGNOZ_INGESTION_KEY>"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [resource/env, batch]
      exporters: [otlp]
```

## Import

Import `dcgm-otlp-v1.json` via **Dashboards → Import** in SigNoz.
