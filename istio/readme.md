# Istio Service Mesh Monitoring Dashboard

SigNoz dashboard for monitoring Istio service mesh infrastructure using OTLP metrics collected from Istio and Envoy proxies via the OpenTelemetry Collector.

## Overview

This dashboard provides end-to-end visibility into Istio service mesh operations across 8 sections with 32 data panels and 4 configurable variables.

## Sections

### 1. General Overview
- **Total Requests** -- Cumulative request count across the mesh
- **Request Rate** -- Requests per second (current)
- **Average Latency** -- Mean request duration in milliseconds
- **Error Rate** -- Rate of 5xx responses per second

### 2. Traffic Management
- **Request Distribution** -- Traffic breakdown by destination workload
- **Load Balancing Efficiency** -- Active upstream connections per service
- **Circuit Breaker Events** -- Upstream connection creation rate
- **Retries and Timeouts** -- Envoy retry and timeout counts

### 3. Performance Metrics
- **Request Latency Percentiles** -- p50, p90, p99 latency distribution
- **Throughput** -- Request and response bytes per second
- **Service Response Times** -- Average duration by destination workload
- **Resource Utilization per Service** -- Request rate by source workload

### 4. Error Metrics
- **HTTP Error Rates** -- 4xx/5xx responses by code
- **gRPC Error Rates** -- gRPC request errors by response code
- **Failed Requests by Service** -- 5xx errors by destination workload
- **TLS Handshake Failures** -- TCP connection closure rate

### 5. Resource Usage
- **Envoy Memory Allocated** -- Total sidecar memory (current value)
- **Envoy Memory Over Time** -- Memory trend per service
- **TCP Bytes Sent** -- Outbound network utilization
- **TCP Bytes Received** -- Inbound network utilization

### 6. Control Plane Metrics
- **Pilot Configuration Syncs** -- xDS push rate
- **Config Convergence Time** -- p50/p99 proxy convergence latency
- **Galley Validations Passed** -- Configuration validation rate
- **Citadel Certificate Issuance** -- CSR processing rate

### 7. Data Plane Metrics
- **Envoy Proxy Connections** -- Active upstream connections
- **Inbound/Outbound Traffic** -- Bidirectional TCP byte rates
- **Proxy Memory Usage** -- Envoy memory per service over time
- **Connection Errors** -- Connection closures and retry rates

### 8. Security Metrics
- **Mutual TLS Usage** -- TCP connection establishment patterns
- **Authorization Policy Enforcement** -- 403 Forbidden response rate
- **Certificate Signing Requests** -- Citadel CSR rate
- **Security Policy Violations** -- 401/403 response rates

## Variables

| Variable | Description |
|---|---|
| `deployment.environment` | Filter by deployment environment |
| `service.name` | Filter by service name |
| `namespace` | Filter by Kubernetes namespace |
| `cluster` | Filter by Kubernetes cluster |

## Metrics Used

| Metric | Type | Source |
|---|---|---|
| `istio_requests_total` | Sum | Istio proxy |
| `istio_request_duration_milliseconds` | Histogram | Istio proxy |
| `istio_request_bytes` | Histogram | Istio proxy |
| `istio_response_bytes` | Histogram | Istio proxy |
| `istio_tcp_sent_bytes_total` | Sum | Istio proxy |
| `istio_tcp_received_bytes_total` | Sum | Istio proxy |
| `istio_tcp_connections_opened_total` | Sum | Istio proxy |
| `istio_tcp_connections_closed_total` | Sum | Istio proxy |
| `envoy_cluster_upstream_cx_active` | Gauge | Envoy |
| `envoy_cluster_upstream_cx_total` | Sum | Envoy |
| `envoy_server_memory_allocated` | Gauge | Envoy |
| `envoy_cluster_upstream_rq_retry` | Sum | Envoy |
| `envoy_cluster_upstream_rq_timeout` | Sum | Envoy |
| `pilot_xds_pushes` | Sum | Istiod |
| `pilot_proxy_convergence_time` | Histogram | Istiod |
| `citadel_server_csr_count` | Sum | Citadel |
| `galley_validation_passed` | Sum | Galley |

## Prerequisites

- Istio service mesh with telemetry v2 enabled
- OpenTelemetry Collector configured with Istio/Envoy metric receivers
- SigNoz backend receiving OTLP metrics

## Installation

Import `istio-otlp-v1.json` via the SigNoz dashboard import feature or place it in the SigNoz dashboards directory.
