# BEAM / Erlang VM Dashboards

Two dashboards for monitoring the BEAM Erlang/Elixir runtime. Both are generic — they work with any BEAM project (Elixir or Erlang) that exposes metrics via [`prometheus_ex`](https://hex.pm/packages/prometheus_ex). Import each JSON file directly into SigNoz.

**Template variables (shared):** `environment` · `k8s_cluster` · `k8s_pod` — all multi-select, scoped to metrics dimensions.

---

## BEAM / Erlang VM - Overview

**File:** `BEAM-ErlangVM-Overview.json`  
**Tags:** `beam` `erlang` `elixir` `overview`

First stop for on-call triage. Shows the key runtime health indicators at a glance — saturation ratios, memory pressure, scheduler backlog, and GC activity.

| Section                     | Panels                                                                                                              |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Stats **                  | Process Utilization %, Port Utilization %, Atom Utilization %, ETS Tables, Schedulers Online, Total Memory          |
| **Memory**                  | Total Memory, Memory Breakdown (stacked: Processes / System / Atom / Binary / ETS / Code), Binary Memory (off-heap) |
| **Schedulers & Run Queues** | Run Queue Length, Dirty CPU / IO Run Queues, Process Utilization % (per pod), Live Processes                        |
| **GC & Reductions**         | GC Rate, GC Bytes Reclaimed, Context Switch Rate, Reductions Rate                                                   |

Stat panels include warning (>70%) and critical (>85%) thresholds. Process/Port/Atom utilization exceeding 85% indicates imminent node exhaustion.

---

## BEAM / Erlang VM - Deep Dive

**File:** `BEAM-ErlangVM-DeepDive.json`  
**Tags:** `beam` `erlang` `elixir` `debug`

Per-subsystem breakdown for root-cause investigation. Use this after the Overview flags an anomaly. Covers memory allocator internals, MSACC scheduler microstate accounting, Erlang distribution link health, and Mnesia.

| Section                               | Panels                                                                                                                                                                  |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Process, Port & Atom Saturation**   | Process Count vs Limit, Process Utilization %, Port Count vs Limit, Port Utilization %, Atom Count vs Limit, Atom Utilization %                                         |
| **Memory Detail**                     | Process Heap Memory, System Memory, Atom Memory, Binary Memory (off-heap), ETS Memory, Code Memory                                                                      |
| **ETS Tables**                        | ETS Table Count, ETS Table Limit, ETS Utilization %, DETS (Disk ETS) Table Count                                                                                        |
| **MSACC Scheduler Microstate**        | aux / check_io / emulator / gc, port / nif / bif / send, sleep, alloc / other / timers                                                                                  |
| **GC & I/O**                          | GC Count Rate, GC Bytes Reclaimed Rate, GC Words Reclaimed Rate, I/O Bytes In/Out Rate, Context Switches Rate, Reductions Rate                                          |
| **Memory Allocator Fragmentation**    | MBCS Pool Block Size & Count, SBC Block Size, MBC Fragmentation %, MBC Block vs Carrier Size                                                                            |
| **Erlang Distribution Link**          | Distribution Bytes Sent/Received Rate, Distribution Send Pending                                                                                                        |
| **Distribution Messages**             | Distribution Messages Sent/Received Rate, Distribution Packets Sent/Received Rate                                                                                       |
| **Mnesia**                            | Held Locks, Lock Queue Depth, Tx Restart/Abort/Commit/Logged/Failed Rates, Memory Usage, Unsynchronised Tables, Subscriptions, Running/Stopped DB Nodes                 |
| **Mnesia Extended**                   | Held Locks (detail), Subscriptions by Type, Transaction Health Overview, Mnesia vs VM Memory, Node Status, Unsync Tables vs Held Locks, Active Transaction Coordinators |

### Key signals to watch

- **MSACC `sleep` high** → schedulers are idle; check I/O wait or under-provisioned concurrency.
- **MSACC `nif` high** → long-running NIFs blocking schedulers.
- **Binary Memory monotonically growing** → binary leak (processes holding large off-heap binary references).
- **MBC Fragmentation % rising** → memory allocator fragmentation; consider allocator tuning or restart.
- **Distribution Send Pending > 0 sustained** → backpressure on an Erlang cluster link.
- **Mnesia Unsynchronised Tables > 0** → partitioned or lagging replica; check node connectivity.

---

## Prerequisites

- Metrics exported via [`prometheus_ex`](https://hex.pm/packages/prometheus_ex) (or compatible exporter).
- Metrics must be ingested into SigNoz with the resource attributes `deployment.environment`, `k8s.cluster.name`, and `k8s.pod.name` populated for the template variable filters to work.
