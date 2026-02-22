# Kong Gateway Monitoring Dashboard - OTLP

## Data Ingestion

### Use prometheus receiver with OpenTelemetry Collector

Add the following code to the collector metrics section of the OpenTelemetry Collector configuration file:

```
prometheus:
  config:
    scrape_configs:
      - job_name: "kong-otel-collector"
        scrape_interval: 30s
        static_configs:
          - targets: ["<KONG_GATEWAY_ADDRESS>:8001"]

```

## Dashboard panels

## Variables

- `{{service}}`: Service created in Kong Gateway
- `{{route}}`: Route created in Kong Gateway
- `{{code}}`: Service response code

### Sections

- General Overview
![General Overview Section](assets/general.png)
  - Total Requests
- Request Metrics
![Request Metrics Section](assets/request-metrics.png)
   - Response Status Codes
- Latency Metrics
![Latency Metric Section](assets/latency-metrics.png)
  - Request Latency
  - Upstream Latency
- Error Metrics
![Error Metrics Section](assets/error-metrics.png)
  - Total Errors
- Traffic Metrics
![Traffic Metrics Section 1](assets/traffic-metrics-1.png)
![Traffic Metrics Section 2](assets/traffic-metrics-2.png)
  - Incoming Traffic Volume
  - Outgoing Traffic Volume
  - Handled Connections
  - Accepted Connections
  - Active Connections
- Resource Usage
![Request Usage Section](assets/request-usage.png)
  - Memory Usage - Kong

