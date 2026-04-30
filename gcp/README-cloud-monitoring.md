# GCP Cloud Monitoring Dashboard

Meta-monitoring dashboard for Google Cloud Monitoring — monitor the monitoring platform itself. Tracks uptime checks, alerting, metric ingestion, API usage, notifications, SLOs, and log-based metrics.

## Sections & Panels (28 panels)

### Uptime Checks (4 panels)
- Uptime Check Passed
- Uptime Check Latency
- Content Mismatch Events
- Time Until SSL Cert Expiry

### Alerting Policies (5 panels)
- Active Alerts per Policy
- Alert Notification Rate
- Incident Count
- Condition Evaluation Duration
- Notification Errors

### Metric Ingestion (4 panels)
- Metric Descriptor Count
- Metric Bytes Ingested
- Time Series Count (cost driver)
- Ingested Samples Rate

### Monitoring API Usage (3 panels)
- API Request Count
- API Request Latency
- API Error Rate

### Notification Channels (4 panels)
- Delivery Success Rate
- Delivery Latency
- Channel Errors
- Notifications per Channel

### Service Level Objectives (4 panels)
- SLO Compliance
- Error Budget Remaining
- Good Events Ratio
- SLO Burn Rate

### Logging Integration (2 panels)
- Log-Based Metric Entries
- Log Metric Extraction Errors

### Custom & Agent Metrics (2 panels)
- Custom Metric Descriptor Count
- Agent Metric Bytes Ingested

## Variables
| Variable | Description |
|----------|-------------|
| `project_id` | GCP Project ID |
| `service_name` | GCP Service Name (multi-select) |

## Data Source
Google Cloud Monitoring metrics via Prometheus exporter (`monitoring.googleapis.com/*`).
