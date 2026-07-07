# JVM Dashboard

JVM Runtime metrics for service

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## JVM Metrics

**File:** `jvm-metrics-by-service.json`

**Tags:** `jvm`, `runtime`

**Filter variables:** `deployment.environment`, `service.name`

**Sections:** JVM Memory, JVM GC, JVM Threads, JVM Classes, JVM CPU

**Panels:**

- GC Major & Minor Collection Count
- Non-Heap Usage
- Heap Usage
- GC Major & Minor Collection Time (p90)
- Blocked threads
- Timed waiting threads
- Runnable threads
- Live threads
- Daemon threads
- Classed loaded
- GC - p90 Duration
- Old gen size
- Eden size
- Survivor size
- GC - Duration
- Classed loaded
- CPU Count
- CPU Time
- CPU Recent Utilization
