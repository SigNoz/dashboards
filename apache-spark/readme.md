# Apache Spark Monitoring Dashboard (Prometheus)

A comprehensive SigNoz dashboard for monitoring Apache Spark clusters using Prometheus metrics exported via the JMX Exporter or the native Spark Prometheus metrics sink.

## Overview

This dashboard provides full observability into Apache Spark workloads — from cluster-level job and stage health down to per-executor CPU, memory, shuffle I/O, structured streaming latency, and JVM internals. It is designed for production Spark deployments where you need fast triage of performance issues, resource bottlenecks, and streaming pipeline delays.

## Metrics Source

Metrics are scraped from one of two sources:

1. **JMX Exporter** — attach the Prometheus JMX Exporter as a Java agent to Spark driver and executor JVMs. Exposes `spark_driver_*` and `spark_executor_*` metrics.
2. **Spark Prometheus Sink** — configure `spark.metrics.conf` to use the built-in Prometheus servlet sink. Available from Spark 3.0+.

Both sources expose compatible metric names used in this dashboard.

## Sections

| Section | Panel Count | Description |
|---|---|---|
| Cluster Overview | 6 | Active/all jobs, running/waiting/failed stages, total active tasks |
| Job & Stage Metrics | 6 | Time-series for jobs, stages, events, and listener bus queue size |
| Executor Performance | 9 | Task completion/failure rates, CPU time, run time, active tasks by executor |
| Executor Memory & Disk | 5 | Memory used/max/utilization %, disk used, input bytes rate per executor |
| Shuffle Operations | 5 | Shuffle read/write rate by executor, totals, and read vs write comparison |
| Driver Block Manager | 5 | Driver-side block manager memory (used/max/remaining) and disk usage |
| Structured Streaming | 10 | Processing/scheduling/total delay, batch counts, record throughput |
| JVM & System | 8 | Heap memory, GC pause rate and duration, CPU usage, live threads |

## Variables

| Variable | Description | Default |
|---|---|---|
| `namespace` | Kubernetes or deployment namespace label | (all) |
| `job` | Prometheus scrape job label for Spark targets | `spark` |
| `app_name` | Spark application name label (`spark.app.name`) | (all) |

## Key Metrics Monitored

| Metric | Type | Description |
|---|---|---|
| `spark_driver_DAGScheduler_job_activeJobs` | Gauge | Active Spark jobs |
| `spark_driver_DAGScheduler_stage_runningStages` | Gauge | Currently running stages |
| `spark_driver_DAGScheduler_stage_failedStages` | Gauge | Failed stages |
| `spark_executor_activeTasks` | Gauge | Active tasks per executor |
| `spark_executor_completedTasks_total` | Counter | Completed tasks (rate) |
| `spark_executor_failedTasks_total` | Counter | Failed tasks (rate) |
| `spark_executor_cpuTime_total` | Counter | CPU time consumed (ns) |
| `spark_executor_memoryUsed_bytes` | Gauge | Executor memory used |
| `spark_executor_maxMemory_bytes` | Gauge | Executor max memory |
| `spark_executor_diskUsed_bytes` | Gauge | Executor disk used |
| `spark_executor_totalShuffleRead_total` | Counter | Shuffle read bytes |
| `spark_executor_totalShuffleWrite_total` | Counter | Shuffle write bytes |
| `spark_driver_BlockManager_memory_memUsed_MB` | Gauge | Driver block manager memory used |
| `spark_streaming_lastCompletedBatch_processingDelay` | Gauge | Streaming processing delay |
| `spark_streaming_lastCompletedBatch_totalDelay` | Gauge | Streaming end-to-end delay |
| `spark_streaming_runningBatches` | Gauge | Currently running batches |
| `spark_streaming_unprocessedBatches` | Gauge | Unprocessed streaming batches |
| `jvm_memory_used_bytes` | Gauge | JVM heap/non-heap memory |
| `jvm_gc_pause_seconds_count` | Counter | GC pause count (rate) |
| `jvm_gc_pause_seconds_sum` | Counter | GC pause total duration |
| `process_cpu_usage` | Gauge | Driver process CPU usage |

## Setup

### 1. Expose Spark Metrics via Prometheus

**Option A — Spark Prometheus Sink (Spark 3.0+)**

Add to `spark-defaults.conf` or pass as `--conf` flags:

```
spark.metrics.conf.*.sink.prometheus.class=org.apache.spark.metrics.sink.PrometheusSink
spark.metrics.conf.*.sink.prometheus.path=/metrics
spark.metrics.conf.*.sink.prometheus.period=10
spark.metrics.conf.*.sink.prometheus.unit=seconds
spark.ui.prometheus.enabled=true
```

**Option B — JMX Exporter**

Add the JMX Exporter agent to your Spark driver and executor JVM args:

```
--conf spark.driver.extraJavaOptions="-javaagent:/path/to/jmx_prometheus_javaagent.jar=8090:/path/to/spark_jmx_config.yaml"
--conf spark.executor.extraJavaOptions="-javaagent:/path/to/jmx_prometheus_javaagent.jar=8091:/path/to/spark_jmx_config.yaml"
```

### 2. Configure Prometheus Scraping

```yaml
scrape_configs:
  - job_name: spark
    static_configs:
      - targets:
          - spark-driver-host:4040
          - spark-executor-host:8091
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
```

### 3. Ship Metrics to SigNoz

Use the OpenTelemetry Collector with the Prometheus receiver to scrape and forward metrics to SigNoz:

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: spark
          scrape_interval: 15s
          static_configs:
            - targets: ['spark-driver:4040']
          metric_relabel_configs:
            - source_labels: [__name__]
              regex: 'spark_.*|jvm_.*|process_.*'
              action: keep

exporters:
  otlp:
    endpoint: <signoz-otel-collector>:4317

service:
  pipelines:
    metrics:
      receivers: [prometheus]
      exporters: [otlp]
```

### 4. Import Dashboard

Upload `apache-spark-prometheus-v1.json` via the SigNoz Dashboard UI:
**Dashboards → New Dashboard → Import JSON**

Set the `namespace`, `job`, and `app_name` template variables to match your Prometheus labels.

## References

- [Apache Spark Monitoring Documentation](https://spark.apache.org/docs/latest/monitoring.html)
- [Spark Prometheus Metrics Sink](https://spark.apache.org/docs/latest/monitoring.html#prometheus-sink)
- [Prometheus JMX Exporter](https://github.com/prometheus/jmx_exporter)
- [SigNoz Dashboard Import](https://signoz.io/docs/userguide/dashboards/)
- [OpenTelemetry Prometheus Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/prometheusreceiver)
- [SigNoz/dashboards Repository](https://github.com/SigNoz/dashboards)
