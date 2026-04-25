# cert-manager Prometheus Dashboard for SigNoz

Monitor all aspects of [cert-manager](https://cert-manager.io/) certificate lifecycle from a single SigNoz dashboard.

## Overview

cert-manager automates TLS certificate management in Kubernetes. This dashboard gives you full visibility into certificate health, issuance performance, renewal scheduling, error rates, and controller activity — all from Prometheus metrics scraped via OpenTelemetry.

## Dashboard Sections

### 1. Certificate Health
- **Total Certificates** — total count across monitored namespaces
- **Ready Certificates** — count of certificates currently in `Ready=True` state
- **Not Ready Certificates** — certificates that need attention
- **Min Days to Expiry** — soonest upcoming expiry across all certs
- **Certificate Days to Expiry** — per-certificate expiry timeline graph
- **Certificate Ready Status** — readiness status over time per certificate

### 2. Certificate Issuance
- **Cert Request Rate** — current certificate request rate (req/s)
- **Avg Issuance Duration** — average time to issue a certificate
- **Certificate Request Rate by Issuer** — throughput broken down by issuer
- **Issuance Duration Percentiles (P50/P95/P99)** — latency histogram for certificate issuance
- **Certificate Existence Time** — how long each certificate has been alive (days)

### 3. Certificate Renewal
- **Certs Renewing Within 7 Days** — count of upcoming renewals
- **Min Days to Next Renewal** — soonest upcoming renewal
- **Days Until Certificate Renewal** — per-certificate renewal schedule
- **Certificate Renewal Rate by Namespace** — renewal throughput per namespace

### 4. Error Metrics
- **ClusterIssuer Sync Error Rate** — errors per second by ClusterIssuer name
- **Issuer Sync Error Rate** — errors per second by namespace-scoped Issuer
- **ACME Request Error Rate (non-2xx)** — failed ACME challenge requests
- **ACME Request Duration (P50/P95/P99)** — ACME HTTP latency percentiles

### 5. Resource Usage & Controller Performance
- **Controller Sync Call Rate** — sync operations per second by controller type
- **ACME HTTP Request Volume by Method** — total ACME traffic by HTTP method
- **Certificate Expiry & Renewal Timestamps** — raw expiry/renewal timestamps for all certs

## Prerequisites

### cert-manager Prometheus Metrics

Enable Prometheus metrics in cert-manager by adding these flags to the cert-manager controller deployment:

```yaml
args:
  - --enable-certificate-owner-ref=true
  - --metrics-listen-address=0.0.0.0:9402
```

Or if using the Helm chart:

```yaml
prometheus:
  enabled: true
  servicemonitor:
    enabled: true
```

### OpenTelemetry Collector

Configure your OTel Collector to scrape cert-manager metrics and send them to SigNoz:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: cert-manager
          scrape_interval: 30s
          static_configs:
            - targets: ['cert-manager.cert-manager.svc.cluster.local:9402']

exporters:
  otlp:
    endpoint: "your-signoz-endpoint:4317"

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Key Metrics

| Metric | Description |
|--------|-------------|
| `certmanager_certificate_expiration_timestamp_seconds` | Unix timestamp when each certificate expires |
| `certmanager_certificate_ready_status` | Certificate readiness (1 = ready, 0 = not ready) |
| `certmanager_certificate_renewal_timestamp_seconds` | Scheduled renewal timestamp |
| `certmanager_certificate_existence_time_seconds` | Age of each certificate |
| `certmanager_certificate_request_duration_seconds_bucket` | Issuance duration histogram |
| `certmanager_http_acme_client_request_count` | ACME HTTP request count by status/method |
| `certmanager_http_acme_client_request_duration_seconds_bucket` | ACME HTTP request latency histogram |
| `certmanager_controller_sync_call_count` | Controller reconciliation call count |
| `certmanager_clusterissuer_sync_error_count` | ClusterIssuer reconciliation errors |
| `certmanager_issuer_sync_error_count` | Namespace-scoped Issuer reconciliation errors |

## Importing the Dashboard

1. Open SigNoz → **Dashboards** → **New Dashboard**
2. Click **Import JSON**
3. Upload `cert-manager-prometheus-v2.json`
4. Select the `namespace` variable value (or leave as `ALL`)

## Variables

| Variable | Description |
|----------|-------------|
| `namespace` | Kubernetes namespace filter (multi-select, supports ALL) |

## Version

- Dashboard version: v4
- cert-manager compatibility: v1.x and later
- SigNoz compatibility: v0.30+
