# Apache Tomcat Monitoring Dashboard for SigNoz

A pre-built SigNoz v5 dashboard for monitoring Apache Tomcat using OpenTelemetry JMX metrics.

## Metrics Source

This dashboard uses metrics collected by the **OpenTelemetry JMX Metric Gatherer** from the [opentelemetry-java-contrib](https://github.com/open-telemetry/opentelemetry-java-contrib/tree/main/jmx-metrics) project, with the `tomcat` and `jvm` target systems enabled.

### Tomcat Metrics

| Metric | Type | Unit | Description |
|--------|------|------|-------------|
| `tomcat.sessions` | Gauge | sessions | Number of active sessions |
| `tomcat.errors` | Counter | errors | Number of errors encountered |
| `tomcat.request_count` | Counter | requests | Total number of requests |
| `tomcat.max_time` | Gauge | ms | Maximum time to process a request |
| `tomcat.processing_time` | Counter | ms | Total processing time |
| `tomcat.traffic` | Counter | bytes | Bytes transmitted and received (label: `direction`) |
| `tomcat.threads` | Gauge | threads | Thread count by state (label: `state`) |

### JVM Metrics

| Metric | Type | Unit | Description |
|--------|------|------|-------------|
| `jvm.memory.heap` | Gauge | bytes | Current heap memory usage |
| `jvm.memory.nonheap` | Gauge | bytes | Current non-heap memory usage |
| `jvm.threads.count` | Gauge | threads | Number of JVM threads |
| `jvm.gc.collections.count` | Counter | collections | Total GC collection count |
| `jvm.gc.collections.elapsed` | Counter | ms | Accumulated GC elapsed time |
| `jvm.classes.loaded` | Gauge | classes | Number of loaded classes |

## Prerequisites

1. **SigNoz** instance (self-hosted or cloud)
2. **OpenTelemetry Collector** with the JMX receiver configured
3. **Apache Tomcat** with JMX remote access enabled

## Setup Instructions

### Step 1: Enable JMX on Tomcat

Add these JVM arguments to your Tomcat startup (e.g., in `setenv.sh` or `CATALINA_OPTS`):

```bash
export CATALINA_OPTS="$CATALINA_OPTS \
  -Dcom.sun.management.jmxremote \
  -Dcom.sun.management.jmxremote.port=9999 \
  -Dcom.sun.management.jmxremote.ssl=false \
  -Dcom.sun.management.jmxremote.authenticate=false \
  -Djava.rmi.server.hostname=localhost"
```

For production, enable authentication and SSL.

### Step 2: Configure the OpenTelemetry Collector

Add the JMX receiver to your `otel-collector-config.yaml`:

```yaml
receivers:
  jmx:
    jar_path: /opt/opentelemetry-jmx-metrics.jar
    endpoint: localhost:9999
    target_system: tomcat,jvm
    collection_interval: 10s

exporters:
  otlp:
    endpoint: "<signoz-otel-collector>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [jmx]
      exporters: [otlp]
```

Download the JMX metrics JAR from the [opentelemetry-java-contrib releases](https://github.com/open-telemetry/opentelemetry-java-contrib/releases) page (look for `opentelemetry-jmx-metrics-*.jar`).

### Step 3: Import the Dashboard

1. Open SigNoz UI
2. Go to **Dashboards** > **New Dashboard** > **Import JSON**
3. Upload `tomcat-otlp-v1.json`
4. The dashboard will appear as "Apache Tomcat"

## Dashboard Sections

| Section | Widgets | Description |
|---------|---------|-------------|
| JVM Metrics | 4 | Heap/non-heap memory, JVM thread count, GC duration |
| Request Metrics | 4 | Request rate, error rate, processing time, max request time |
| Thread Pool Metrics | 2 | Current vs busy threads, thread pool utilization % |
| Session Metrics | 3 | Active sessions (value + graph), GC collections rate |
| Network Metrics | 2 | Bytes received/sent rates by connector |

## Key Labels

- `proto_handler` - Tomcat connector protocol handler (e.g., `"http-nio-8080"`)
- `direction` - Traffic direction: `sent` or `received`
- `state` - Thread state: `busy` or `idle`

## Troubleshooting

- **No data appearing**: Verify JMX connectivity with `jconsole` first, then check the OTel collector logs.
- **Missing Tomcat metrics**: Ensure `target_system` includes `tomcat` (not just `jvm`).
- **Missing JVM metrics**: Ensure `target_system` includes `jvm`.
- **Partial data**: Some metrics require active traffic. Send test requests to populate request/error counters.
