# GCP Cloud Load Balancer Dashboard - OTLP

## Data Ingestion

### Integrate GCP Cloud Load Balancer with OpenTelemetry Collector

Follow the instructions on SigNoz's GCP Cloud Monitoring integration [docs](https://signoz.io/docs/gcp-monitoring/cloud-monitoring/) to configure the OpenTelemetry Collector to fetch GCP Cloud Load Balancer metrics.

The collector should be configured to scrape `loadbalancing.googleapis.com` metrics from the GCP Monitoring API.

## Dashboard panels

## Variables

- `{{deployment.environment}}`: The deployment environment for the service.
- `{{project_id}}`: GCP Project ID.
- `{{url_map_name}}`: URL Map name for the load balancer.
- `{{backend_target_name}}`: Backend service name.

### Sections

- Overview
  - Total Request Count - `loadbalancing_googleapis_com_https_request_count`
  - Total Request Bytes - `loadbalancing_googleapis_com_https_request_bytes_count`
  - Total Response Bytes - `loadbalancing_googleapis_com_https_response_bytes_count`
- Request Traffic
  - Request Count by URL Map - `loadbalancing_googleapis_com_https_request_count`
  - Request Bytes by Backend - `loadbalancing_googleapis_com_https_request_bytes_count`
  - Response Bytes by Backend - `loadbalancing_googleapis_com_https_response_bytes_count`
- Latency
  - Total Latency - `loadbalancing_googleapis_com_https_total_latencies`
  - Backend Latency - `loadbalancing_googleapis_com_https_backend_latencies`
  - Frontend TCP RTT - `loadbalancing_googleapis_com_https_frontend_tcp_rtt`
- Backend Health
  - Backend Connections - `loadbalancing_googleapis_com_https_backend_connections`
  - Backend Request Count - `loadbalancing_googleapis_com_https_backend_request_count`
  - Regional Proxy Latency - `loadbalancing_googleapis_com_https_external_regional_proxy_latencies`
- Errors
  - Internal Error Count - `loadbalancing_googleapis_com_https_internal_error_count`
  - External Error Count - `loadbalancing_googleapis_com_https_external_error_count`
- SSL/TCP Proxy
  - Open Connections - `loadbalancing_googleapis_com_tcp_ssl_proxy_open_connections`
  - New Connections - `loadbalancing_googleapis_com_tcp_ssl_proxy_new_connections`
