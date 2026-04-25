# Istio Service Mesh — Prometheus Dashboard for SigNoz

A comprehensive SigNoz dashboard for monitoring Istio service mesh using standard Prometheus metrics exposed by the Istio telemetry system.

## Overview

This dashboard provides full observability into your Istio-managed Kubernetes services — from high-level traffic health down to individual service latency and control plane status.

## Sections

### General Overview
High-level KPIs visible at a glance:
- **Total Requests** — cumulative request count over the selected time range
- **Request Rate (RPS)** — current requests per second across the mesh
- **Global Error Rate (%)** — percentage of 5xx responses mesh-wide
- **P99 Latency (ms)** — 99th percentile latency for all requests
- **Success Rate (%)** — inverse of the error rate
- **RPS by Response Class** — stacked breakdown of 2xx / 3xx / 4xx / 5xx

### Traffic Management
Service-level traffic visibility:
- **Request Rate by Destination Service** — inbound RPS per service
- **Active TCP Connections** — open/closed TCP connections per workload
- **TCP Bytes Sent** — outbound throughput per destination service
- **TCP Bytes Received** — inbound throughput per destination service

### Performance Metrics
Latency percentiles for SLO tracking:
- **P50 Latency by Service** — median latency
- **P95 Latency by Service** — 95th percentile latency
- **P99 Latency by Service** — tail latency (critical for SLO alerting)
- **Request Throughput by Service** — source → destination traffic matrix

### Error Metrics
Detailed error breakdown:
- **HTTP 4xx Error Rate by Service** — client-side errors
- **HTTP 5xx Error Rate by Service** — server-side errors / reliability issues
- **gRPC Error Rate by Service** — non-zero gRPC status codes
- **Failed Requests by Source Workload** — identifies which workloads generate the most errors

### Control Plane
Istiod / Pilot health:
- **Pilot XDS Push Rate** — CDS / LDS / RDS / EDS push rates
- **Envoy Proxy Config Sync** — connected proxies and push context errors
- **Pilot XDS Push Errors** — push and internal error rates
- **Pilot Config Push Latency** — P50/P95/P99 convergence time

## Variables

| Variable | Description |
|---|---|
| `namespace` | Filter all panels to one or more Kubernetes namespaces |
| `destination_service` | Scope panels to specific destination services |
| `source_workload` | Scope panels to specific source workloads |

## Metrics Used

| Metric | Description |
|---|---|
| `istio_requests_total` | Total Istio request counter (labels: source/destination service, response_code, grpc_response_status) |
| `istio_request_duration_milliseconds_bucket` | Histogram for request duration in milliseconds |
| `istio_tcp_connections_opened_total` | Total TCP connections opened |
| `istio_tcp_connections_closed_total` | Total TCP connections closed |
| `istio_tcp_sent_bytes_total` | Total TCP bytes sent |
| `istio_tcp_received_bytes_total` | Total TCP bytes received |
| `pilot_xds_pushes` | Pilot XDS push counter by type |
| `pilot_xds_push_errors` | Pilot XDS push error counter |
| `pilot_xds_internal_errors` | Pilot internal error counter |
| `pilot_xds_push_context_errors` | Push context error gauge |
| `pilot_proxy_convergence_time_bucket` | Histogram for proxy convergence latency |
| `pilot_xds` | Number of endpoints connected to Pilot |

## Prerequisites

- Istio installed with Prometheus integration enabled (`meshConfig.enablePrometheusMerge: true`)
- SigNoz deployed and configured to scrape your Prometheus endpoint
- Istio telemetry v2 (default since Istio 1.5)

## Installation

1. In SigNoz, go to **Dashboards → New Dashboard → Import JSON**
2. Paste or upload `istio-prometheus-v1.json`
3. Set the Prometheus data source
4. Use the namespace / service / workload variables to filter as needed
