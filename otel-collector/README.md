# OpenTelemetry Collector Monitoring Dashboard

Comprehensive monitoring dashboard for the OpenTelemetry Collector's internal telemetry metrics.

## Overview

This dashboard provides full visibility into OTel Collector health and performance, covering all three signal types (traces, metrics, logs) across the complete pipeline.

## Sections

| Section | Panels | Description |
|---------|--------|-------------|
| **Overview** | 8 | Uptime, memory RSS, heap allocation, CPU usage |
| **Receivers** | 18 | Accepted/refused data points per receiver and transport |
| **Processors** | 22 | Accepted/refused/dropped data, batch send size histograms |
| **Exporters** | 21 | Sent/failed data, queue size and utilization |
| **Runtime** | 8 | Heap, RSS, total alloc rate, CPU over time |
| **HTTP Server** | 12 | Request duration percentiles, content length, status codes |

**Total: 98 panels**

## Metrics Covered

- **Receiver metrics**: `otelcol_receiver_accepted_*`, `otelcol_receiver_refused_*`
- **Processor metrics**: `otelcol_processor_accepted_*`, `otelcol_processor_refused_*`, `otelcol_processor_dropped_*`, `otelcol_processor_batch_*`
- **Exporter metrics**: `otelcol_exporter_sent_*`, `otelcol_exporter_failed_*`, `otelcol_exporter_queue_*`, `otelcol_exporter_enqueue_failed_*`
- **Process metrics**: `otelcol_process_uptime`, `otelcol_process_runtime_*`, `otelcol_process_cpu_seconds`, `otelcol_process_memory_rss`
- **HTTP metrics**: `http_server_request_content_length`, `http_server_response_content_length`, `http_server_duration`

## Variables

- **collector_name**: Filter by `service.instance.id` to monitor specific collector instances

## Prerequisites

The OTel Collector must have internal telemetry enabled. This is the default configuration. Metrics are exposed via the Collector's own telemetry pipeline.

See: [OTel Collector Internal Telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)
