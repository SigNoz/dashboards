# Kong Gateway Monitoring Dashboard 🚀

A clinical-grade monitoring dashboard for **Kong Gateway** using Prometheus metrics. Formatted for **SigNoz v5** with 7 architectural sections for deep observability.

![Kong Masterpiece Overview](assets/overview.png)

## 🏛️ Sections

1. **General Overview**: High-level RPS, Success Rate, and Bandwidth.
2. **Latency Analysis**: P99 performance and distribution buckets.
3. **Traffic Segmentation**: Per Service, Route, and Consumer (Auth).
4. **Error Distribution**: HTTP status code breakdowns.
5. **Plugin Performance**: Latency overhead per active plugin.
6. **System Resources**: CPU and Memory consumption.
7. **Connection State**: Healthy vs Unhealthy upstream targets.

## 🛠️ Prerequisites

- **Kong Prometheus Plugin**: Must be enabled on the Kong Gateway.
- **SigNoz v5.x**: Required for dynamic variable support and advanced widgets.

## 🔧 Setup

1. **Enable Plugin**: `curl -X POST http://localhost:8001/plugins --data "name=prometheus"`
2. **Expose Metrics**: Ensure metrics are scraped by your Prometheus instance/SigNoz collector.
3. **Import JSON**: Import `kong-prometheus-v1.json` into your SigNoz dashboard.

## 🖇️ Metadata
- **Related Issue**: Closes [SigNoz/signoz#6028](https://github.com/SigNoz/signoz/issues/6028)
- **Author**: AntiGravity Masterpiece Standard
