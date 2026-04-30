# Tomcat Dashboard - OTLP

This dashboard provides monitoring for Apache Tomcat application servers using OpenTelemetry JMX Receiver.

## Metrics Ingestion

Configure the OpenTelemetry JMX Receiver to collect Tomcat metrics. Add the following to your OpenTelemetry Collector configuration:

```yaml
receivers:
  jmx:
    jar_path: /opt/opentelemetry-java-contrib-jmx-metrics.jar
    endpoint: localhost:7199
    target_system: tomcat,jvm
    collection_interval: 60s
    username: admin
    password: admin
```

Ensure the JMX metrics JAR is downloaded from the [OpenTelemetry Java Contrib](https://github.com/open-telemetry/opentelemetry-java-contrib/releases) repository.

### Required Metrics

| Metric Name | Type | Description |
|---|---|---|
| `tomcat.threads.current` | Gauge | Current thread count |
| `tomcat.threads.busy` | Gauge | Busy thread count |
| `tomcat.threads.max_config` | Gauge | Maximum configured threads |
| `tomcat.request_count` | Sum | Total request count |
| `tomcat.error_count` | Sum | Total error count |
| `tomcat.processing_time` | Sum | Total processing time (ns) |
| `tomcat.sessions.active` | Gauge | Active session count |
| `tomcat.sessions.created` | Sum | Total sessions created |
| `tomcat.sessions.expired` | Sum | Total sessions expired |
| `tomcat.sessions.rejected` | Sum | Total sessions rejected |
| `jvm.memory.heap.used` | Gauge | JVM heap memory used (bytes) |
| `jvm.memory.heap.max` | Gauge | JVM heap memory max (bytes) |

## Variables

| Variable | Description |
|---|---|
| `host.name` | List of hosts sending Tomcat metrics |

## Dashboard Panels

### Section 1: Tomcat Thread Pool
- **Active Threads** — Current number of threads (`tomcat.threads.current`)
- **Busy Threads** — Number of busy threads (`tomcat.threads.busy`)
- **Max Threads** — Maximum configured threads (`tomcat.threads.max_config`)

### Section 2: Request Metrics
- **Request Rate** — Rate of requests per second (`tomcat.request_count`)
- **Error Rate** — Rate of errors per second (`tomcat.error_count`)
- **Processing Time Rate** — Rate of processing time (`tomcat.processing_time`, ns)

### Section 3: Session Metrics
- **Active Sessions** — Number of active sessions (`tomcat.sessions.active`)
- **Created Sessions** — Rate of sessions created (`tomcat.sessions.created`)
- **Expired Sessions** — Rate of sessions expired (`tomcat.sessions.expired`)
- **Rejected Sessions** — Rate of sessions rejected (`tomcat.sessions.rejected`)

### Section 4: JVM Memory
- **JVM Heap Used** — Heap memory currently used (`jvm.memory.heap.used`)
- **JVM Heap Max** — Heap memory max available (`jvm.memory.heap.max`)
