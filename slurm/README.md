# SLURM Dashboard

This directory contains SigNoz dashboard template for SLURM monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## SLURM

**File:** `slurm.json`

**Sections:** Cluster Nodes, SLURM Jobs, Users and Accounts, CPU Cores Allocation, SLURM Scheduler Cycles, SLURM Scheduler Details, Backfilled Jobs

**Panels:**

- Nodes
- Fail / Down / Drain / Err Nodes
- RUNNING/COMPL/PEND Jobs
- FAIL/SUSP/CANC/PREEMPT/TIMEDOUT Jobs
- Pending Jobs per Partition
- Running Jobs per Account
- Pending Jobs per Account
- Running Jobs per User
- Pending Jobs per Users
- Utilized CPUs per Account
- Utilized CPUs per User
- CPU Allocation
- CPUs Allocated per Partition
- CPUs Idle per Partition
- Slurm Scheduler Threads
- Agent Queue Size
- DBD Agent Queue length
- Scheduler Cycles
- Backfill Scheduler Cycles
- Scheduler Backfill Depth Mean
- Total backfilled heterogeneous Job components
- Total Backfilled Jobs (since last slurm start)
- Total Backfilled Jobs (since last stats cycle start)
