# NGINX Dashboards

This directory contains SigNoz dashboard templates for NGINX monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Dashboards

| File | Dashboard | Panels |
| --- | --- | --- |
| `ingress-nginx-controller.json` | NGINX Ingress controller | 11 |
| `nginx-ingress-request-handling-performance.json` | Ingress Nginx - Request Handling Performance | 9 |
| `nginx.json` | NGINX (OTEL) | 10 |

## NGINX Ingress controller

**File:** `ingress-nginx-controller.json`

Ingress-nginx controller health and performance — request volume, success rate, config reloads, CPU/memory, network I/O, and latency percentiles. Filter by namespace, controller class, controller pod, and ingress.

**Tags:** `nginx`, `ingress`, `kubernetes`

**Filter variables:** `controller`, `controller_class`, `ingress`, `namespace`

**Panels:**

- Controller Request Volume
- Controller Connections
- Controller Success Rate (non-4|5xx responses)
- Config Reloads
- Last Config Failed
- Ingress Request Volume
- Ingress Success Rate (non-4|5xx responses)
- Network I/O pressure
- Average Memory Usage
- Average CPU Usage
- Ingress Percentile Response Times

## Ingress Nginx - Request Handling Performance

**File:** `nginx-ingress-request-handling-performance.json`

Ingress-nginx controller request-handling performance (nginx_ingress_controller_* metrics scraped via Prometheus → OTel). Filter by ingress.

**Tags:** `nginx`, `ingress`, `kubernetes`

**Filter variables:** `ingress`

**Panels:**

- Request Latency Percentiles
- Upstream Response Latency Percentiles
- Request Rate by Method and Path
- Median Upstream Response Time by Method and Path
- Response Error Ratio (4xx/5xx) by Method and Path
- Error Request Rate by Status (4xx/5xx)
- Average Upstream Response Time by Method and Path
- Average Upstream Response Latency
- Average Response Size by Method and Path

## NGINX (OTEL)

**File:** `nginx.json`

NGINX metrics from the OpenTelemetry nginx receiver: request throughput, accepted and handled connections, and current connections by state (active, reading, writing, waiting). Scope with the host.name and service.name variables.

**Tags:** `nginx`, `otel`, `metrics`

**Filter variables:** `host.name`, `service.name`

**Panels:**

- Requests
- Accepted conns
- Current conns
- Handled conns
- Total requests
- Active
- Accepted connections
- Handled connections
- Writing
- Waiting
