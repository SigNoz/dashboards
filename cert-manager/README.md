# Cert-Manager Monitoring Dashboard

## Overview
This dashboard provides a focused view of cert-manager health across your Kubernetes environment. It helps operators monitor TLS certificate lifecycle status, detect failures early, and track controller resource usage so certificate issuance and renewals stay reliable.

## Dashboard Sections
The dashboard is organized into six operational sections:

1. **General Overview**
   - High-level status of certificate inventory and readiness.
   - Fast signal for overall cert-manager health.
2. **Issuance**
   - Certificate issuance throughput and success trends.
   - Issuance distribution by issuer.
3. **Renewal**
   - Upcoming renewals, renewal success rate, and renewal timing.
   - Useful for identifying certificates at risk of expiry.
4. **Errors**
   - Issuance, renewal, and API-related error visibility.
   - Helps pinpoint reliability regressions quickly.
5. **Resource Usage**
   - cert-manager CPU, memory, and restart behavior.
   - Supports capacity planning and performance troubleshooting.
6. **API/Events**
   - API request activity and failures.
   - Event-level insight into cert-manager interactions.

## Variables
Use dashboard variables to scope metrics by environment and workload:

- `cluster`
- `namespace`
- `issuer`
- `certificate_name`
- `deployment.environment`

## Setup
This dashboard requires cert-manager metrics to be exported and available to your observability backend.

- Ensure cert-manager is exposing Prometheus-format metrics.
- Ensure Prometheus/SigNoz is scraping and storing those metrics before importing or using this dashboard.
