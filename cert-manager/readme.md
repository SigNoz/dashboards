# Cert-Manager Monitoring Dashboard for SigNoz

A comprehensive SigNoz dashboard for monitoring [cert-manager](https://cert-manager.io/) deployments using OTLP metrics collected via OpenTelemetry.

## Overview

This dashboard provides visibility into certificate lifecycle management, ACME client interactions, controller performance, and process-level resource consumption. It is designed for Kubernetes clusters running cert-manager with metrics exported via the OpenTelemetry Collector.

## Dashboard Sections

### 1. General Overview
- **Total Certificates** -- Count of all Certificate resources tracked by cert-manager
- **Active Certificates** -- Certificates currently in Ready=True state
- **Certificate Requests** -- Total controller sync calls for certificate readiness reconciliation
- **Clock Time** -- Current clock time reported by the controller (confirms liveness)

### 2. Certificate Issuance
- **Certificates per Issuer** -- Distribution of certificates across issuer names
- **Issuance Rate** -- Rate of controller sync calls for certificate issuance operations
- **ACME Request Success Rate** -- Comparison of total vs successful (2xx) ACME HTTP requests

### 3. Certificate Renewal
- **Certificates Pending Renewal** -- Count of certificates with tracked renewal timestamps
- **Renewal Sync Rate** -- Controller sync rate for readiness checks (renewal processing)
- **ACME Client Request Duration** -- Average ACME HTTP request latency by method and host

### 4. Error Metrics
- **Issuance Controller Sync Rate** -- Sync call rate for issuance controllers (spikes indicate retries)
- **Trigger Controller Sync Rate** -- Sync call rate for certificate trigger operations
- **ACME Client Errors by Status** -- ACME HTTP request rate broken down by status code

### 5. Resource Usage
- **CPU Usage** -- CPU seconds consumed by the cert-manager process (rate)
- **Memory Usage** -- Resident memory usage in bytes
- **Controller Sync Activity** -- Total sync rate across all controllers (activity proxy)

### 6. API and Event Metrics
- **ACME API Request Rate** -- Outbound ACME HTTP request rate by method
- **Event Processing Rate** -- All controller sync calls (event processing throughput)
- **Failed ACME Requests** -- ACME requests broken down by status and host

## Metrics Used

| Metric | Type | Description |
|--------|------|-------------|
| `certmanager_certificate_ready_status` | Gauge | Whether a certificate is in Ready state (1 or 0) |
| `certmanager_certificate_expiration_timestamp_seconds` | Gauge | Certificate expiration Unix timestamp |
| `certmanager_certificate_renewal_timestamp_seconds` | Gauge | Certificate renewal Unix timestamp |
| `certmanager_controller_sync_call_count` | Sum | Controller reconcile/sync call counter |
| `certmanager_http_acme_client_request_count` | Sum | ACME HTTP client request counter |
| `certmanager_http_acme_client_request_duration_seconds` | Histogram | ACME HTTP client request latency |
| `certmanager_clock_time_seconds` | Gauge | Current time as seen by cert-manager |
| `process.cpu.seconds.total` | Sum | Process CPU time |
| `process.resident_memory_bytes` | Gauge | Process resident memory |

## Variables

The dashboard includes three filter variables:

- **deployment.environment** -- Filter by deployment environment
- **namespace** -- Filter by Kubernetes namespace
- **cluster** -- Filter by Kubernetes cluster

## Prerequisites

1. cert-manager installed in the Kubernetes cluster
2. OpenTelemetry Collector configured to scrape cert-manager metrics (Prometheus endpoint)
3. SigNoz backend receiving OTLP metrics from the collector

## Installation

Import the `cert-manager-otlp-v1.json` file into SigNoz:

1. Navigate to **Dashboards** in the SigNoz UI
2. Click **+ New Dashboard** then **Import JSON**
3. Upload or paste the contents of `cert-manager-otlp-v1.json`
4. Save the dashboard

## Collector Configuration

Example OpenTelemetry Collector configuration for scraping cert-manager metrics:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'cert-manager'
          kubernetes_sd_configs:
            - role: pod
          relabel_configs:
            - source_labels: [__meta_kubernetes_pod_label_app]
              regex: cert-manager
              action: keep
            - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
              regex: '9402'
              action: keep

exporters:
  otlp:
    endpoint: "<signoz-otel-collector>:4317"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```
