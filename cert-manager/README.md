# cert-manager Monitoring Dashboard

Monitor cert-manager certificate lifecycle using Prometheus metrics.

## Panels

| Panel | Type | Description |
|-------|------|-------------|
| Total Certificates Issued | Value | Total certificates tracked |
| Active Certificates | Value | Certificates in Ready=True state |
| Controller Sync Count | Value | Controller sync calls processed |
| Certificates Issued per Issuer | Graph | Breakdown by issuer name/kind |
| Certificate State Changes | Graph | Ready status changes per namespace |
| ACME Client Request Count | Graph | ACME HTTP request rate by status |
| Certificates Expiring Soon | Value | Certificates expiring within 7 days |
| Certificate Expiration Timeline | Graph | Days until each certificate expires |
| Time Until Next Renewal | Graph | Seconds until next scheduled renewal |
| Controller Sync Errors | Graph | Sync error rate per controller |
| ACME Request Errors | Graph | ACME 4xx/5xx error rate |
| CPU Usage | Graph | CPU usage per cert-manager pod |
| Memory Usage | Graph | Memory per cert-manager pod |
| Pod Restarts | Graph | Container restart count per pod |
| API Request Rate | Graph | K8s API request rate by method/code |
| Workqueue Depth | Graph | Controller workqueue depth |

## Variables

- `namespace` — Kubernetes namespace
- `issuer` — Certificate issuer name
- `certificate_name` — Certificate name
- `cluster` — Kubernetes cluster
- `deployment_environment` — Deployment environment

## Metrics Used

- `certmanager_certificate_ready_status` — Certificate ready state
- `certmanager_certificate_expiration_timestamp_seconds` — Expiration timestamp
- `certmanager_certificate_renewal_timestamp_seconds` — Next renewal timestamp
- `certmanager_controller_sync_call_count` — Controller sync calls
- `certmanager_controller_sync_error_count` — Controller sync errors
- `certmanager_http_acme_client_request_count` — ACME HTTP requests
- `container_cpu_usage_seconds_total` — Container CPU
- `container_memory_working_set_bytes` — Container memory
- `kube_pod_container_status_restarts_total` — Pod restarts
- `rest_client_requests_total` — K8s API client requests
- `workqueue_depth` — Controller workqueue depth

## Query Type

PromQL
