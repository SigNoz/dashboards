# Apache Tomcat Monitoring Dashboard

Pre-built SigNoz dashboard for monitoring Apache Tomcat servers using Prometheus JMX Exporter metrics.

## Metrics Ingestion

Tomcat metrics are exposed via the [JMX Exporter](https://github.com/prometheus/jmx_exporter) or [Tomcat Prometheus Exporter](https://github.com/nlighten/tomcat_exporter). Configure the OpenTelemetry Collector to scrape:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'tomcat'
          scrape_interval: 15s
          static_configs:
            - targets: ['<tomcat-host>:9404']

exporters:
  otlp:
    endpoint: "<signoz-otel-collector>:4317"
    tls:
      insecure: true

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

## Dashboard Sections

| Section | Panels | Key Metrics |
|---------|--------|-------------|
| Overview | 6 values | Current/busy/max threads, request rate, error rate, active sessions |
| Thread Pool | 2 | Current vs busy threads, busy vs max threads |
| Request Processing | 4 | Request rate, error rate, processing time, avg duration |
| Sessions | 4 | Active sessions, created/rejected/expired rates |
| JVM Memory | 3 | Memory used, max, pool usage |
| Garbage Collection | 2 | GC collection rate, GC time rate |
| Network I/O | 2 | Bytes sent/received rates |
| Class Loading | 3 | Currently loaded, total loaded, unloaded |

## Variables

- `instance` — Filter by Tomcat instance
- `job` — Filter by Prometheus scrape job

## Metrics Reference

- `tomcat_threads_current_total` — Current thread pool size
- `tomcat_threads_busy_total` — Busy threads in pool
- `tomcat_threads_config_max_total` — Max configured threads
- `tomcat_requestcount_total` — Total HTTP requests processed
- `tomcat_errorcount_total` — Total HTTP errors
- `tomcat_processingtime_total` — Cumulative request processing time
- `tomcat_sessions_active_current_total` — Current active sessions
- `tomcat_sessions_created_total` — Total sessions created
- `tomcat_sessions_rejected_total` — Sessions rejected (capacity)
- `tomcat_sessions_expired_total` — Sessions expired
- `tomcat_bytessent_total` — Total bytes sent
- `tomcat_bytesreceived_total` — Total bytes received
- `jvm_memory_bytes_used` — JVM heap/non-heap memory used
- `jvm_memory_bytes_max` — JVM max memory
- `jvm_gc_collection_seconds_count` — GC invocation count
- `jvm_gc_collection_seconds_sum` — Total GC time
- `jvm_classes_loaded` — Currently loaded classes
- `jvm_classes_loaded_total` — Total loaded since start
- `jvm_classes_unloaded_total` — Total unloaded since start

## Prerequisites

- Apache Tomcat server
- JMX Exporter or Tomcat Prometheus Exporter configured
- OpenTelemetry Collector scraping Tomcat metrics
- SigNoz instance
