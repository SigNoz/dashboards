# Keycloak Monitoring Dashboard (Prometheus)

Comprehensive monitoring dashboard for Keycloak Identity and Access Management servers using Prometheus metrics.

## Overview

This dashboard provides full observability into Keycloak instances including authentication flows, token operations, JVM health, HTTP performance, and database connection pool status.

## Metrics Source

**Data Source**: Prometheus  
**Exporter**: Keycloak built-in Micrometer/Quarkus metrics endpoint (`/metrics`)

## Sections

| Section | Panels | Description |
|---------|--------|-------------|
| General Overview | 4 | Server uptime, CPU usage, thread count |
| HTTP Requests | 8 | Request rates, error rates, latency percentiles, breakdown by URI/method |
| Authentication | 9 | Login success/failure rates, registrations, provider/client breakdown |
| Token Operations | 7 | Token refresh, code-to-token exchanges, client credential flows |
| JVM Memory | 7 | Heap/non-heap usage, GC pause metrics, memory pool breakdown |
| JVM Threads | 5 | Thread count, state distribution, peak/daemon threads |
| Database Connection Pool | 5 | Active/idle/pending connections, pool utilization |
| System Resources | 3 | CPU usage trends, uptime |

**Total: 56 panels (8 sections, 18 value panels, 30 graphs)**

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `namespace` | Kubernetes namespace filter | - |
| `job` | Prometheus job name | keycloak |
| `instance` | Instance filter | - |

## Key Metrics Monitored

### Authentication
- `keycloak_logins` / `keycloak_login_errors` — Login success and failure rates by realm, provider, and client
- `keycloak_registrations` / `keycloak_registrations_errors` — User registration metrics
- `keycloak_refresh_tokens` / `keycloak_refresh_tokens_errors` — Token refresh operations
- `keycloak_code_to_tokens` / `keycloak_code_to_token_errors` — Authorization code exchanges
- `keycloak_client_logins` / `keycloak_client_login_errors` — Client credential flows

### HTTP Performance
- `keycloak_request_duration_seconds_count` — Request throughput by status, method, URI
- `keycloak_request_duration_seconds_sum` — Request latency analysis

### JVM & System
- `jvm_memory_used_bytes` / `jvm_memory_max_bytes` — Memory utilization
- `jvm_gc_pause_seconds_count` / `jvm_gc_pause_seconds_sum` — Garbage collection impact
- `jvm_threads_live_threads` / `jvm_threads_states_threads` — Thread pool health
- `process_cpu_usage` / `system_cpu_usage` — CPU utilization
- `vendor_statistics_active_count` / `vendor_statistics_idle_count` — DB connection pool

## Setup

1. Enable Keycloak metrics endpoint (enabled by default in Keycloak 17+ / Quarkus distribution)
2. Configure Prometheus to scrape the `/metrics` endpoint
3. Configure OpenTelemetry Collector with Prometheus receiver to forward metrics to SigNoz
4. Import this dashboard into SigNoz

## References

- [Keycloak Server Administration Guide — Metrics](https://www.keycloak.org/server/configuration-metrics)
- [Grafana Dashboard #10441](https://grafana.com/grafana/dashboards/10441-keycloak-metrics-dashboard/)
