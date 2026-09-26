# Tomcat Dashboard

This dashboard provides insights into your Apache Tomcat instances: request throughput, errors, processing time, connector threads, active sessions, and network traffic.

It is built on the metrics collected by the [OpenTelemetry Collector's JMX receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/jmxreceiver) with `target_system: tomcat`, which reads Tomcat's `GlobalRequestProcessor`, `ThreadPool` and `Manager` MBeans.

## Metrics ingestion

Enable JMX on Tomcat, for example via `CATALINA_OPTS`:

```bash
CATALINA_OPTS="-Dcom.sun.management.jmxremote \
  -Dcom.sun.management.jmxremote.port=9010 \
  -Dcom.sun.management.jmxremote.rmi.port=9010 \
  -Dcom.sun.management.jmxremote.local.only=false \
  -Dcom.sun.management.jmxremote.authenticate=false \
  -Dcom.sun.management.jmxremote.ssl=false"
```

Then point the collector's JMX receiver at it:

```yaml
receivers:
  jmx:
    jar_path: /opt/opentelemetry-java-contrib-jmx-metrics.jar
    endpoint: <tomcat-host>:9010
    target_system: tomcat
    collection_interval: 10s
    resource_attributes:
      service.name: <your-tomcat-service-name>

exporters:
  otlp:
    endpoint: ingest.<region>.signoz.cloud:443
    headers:
      signoz-ingestion-key: <your-ingestion-key>

service:
  pipelines:
    metrics:
      receivers: [jmx]
      exporters: [otlp]
```

## Variables

- `$service_name`: Tomcat instance, from the `service.name` resource attribute.
- `$proto_handler`: Tomcat connector / protocol handler (for example `"http-nio-8080"`), from the `proto_handler` attribute.

## Dashboard panels

### Overview

- **Active Sessions** (`tomcat.sessions`)
- **Requests / sec** (rate of `tomcat.request_count`)
- **Errors / sec** (rate of `tomcat.errors`)
- **Busy Threads** (`tomcat.threads`, `state=busy`)

### Requests and Errors

- **Request Rate by Protocol Handler** (`tomcat.request_count`, grouped by `proto_handler`)
- **Error Rate by Protocol Handler** (`tomcat.errors`, grouped by `proto_handler`)
- **Error Ratio** (`tomcat.errors` over `tomcat.request_count`)

### Latency

- **Average Processing Time** (`tomcat.processing_time` over `tomcat.request_count`)
- **Slowest Request** (`tomcat.max_time`)

### Threads and Sessions

- **Threads by State** (`tomcat.threads`, `state=busy|idle`)
- **Active Sessions Over Time** (`tomcat.sessions`)

### Network Traffic

- **Traffic Sent and Received** (`tomcat.traffic`, `direction=sent|received`)
