# AWS RDS Dashboards

This directory contains SigNoz dashboard templates for AWS RDS monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Dashboards

| File | Dashboard | Panels |
| --- | --- | --- |
| `mysql/db-metrics.json` | MySQL | 16 |
| `mysql/overview.json` | AWS RDS MySQL | 16 |
| `postgresql/db-metrics-overview.json` | Postgres overview | 11 |
| `postgresql/overview.json` | AWS RDS Postgres | 17 |

## MySQL

**File:** `mysql/db-metrics.json`

**Tags:** `mysql`

**Filter variables:** `mysql.instance.endpoint`

**Sections:** Buffer pool, Table, Resources

**Panels:**

- Buffer pool usage by status
- Buffer pool pages by kind
- Data pages by status
- Total buffer pool page flushes
- count of table I/O wait events
- count of table I/O wait events
- Count by handlers
- MySQL locks
- InnoDB log operations
- Connection/Errors
- Open resources count
- Count of operations
- Row locks
- Thread type count
- Row operations
- Prepared statement count

## AWS RDS MySQL

**File:** `mysql/overview.json`

**Tags:** `aws`, `rds`, `mysql`

**Filter variables:** `dbinstance_identifier`

**Panels:**

- DatabaseConnections
- CPUUtilization
- FreeableMemory
- ReadLatency
- ReadThroughput
- ReadIOPS
- FreeStorageSpace
- WriteThroughput
- WriteIOPS
- Network transmit/receive
- DiskQueueDepth
- EBSByteBalance%
- EBSIOBalance%
- BinLogDiskUsage
- WriteLatency
- SwapUsage

## Postgres overview

**File:** `postgresql/db-metrics-overview.json`

This dashboard provides a high-level overview of your PostgreSQL databases. It includes replication, locks, and throughput etc...

**Tags:** `postgres`, `database`

**Filter variables:** `table_name`, `db_name`

**Sections:** Operations, Locks, Connections, Stats

**Panels:**

- Inserts
- Updates
- Deleted
- Heap updates
- Operation by database
- Locks by lock mode
- Deadlocks count
- Connections per db
- Dead rows
- Index scans by index
- Table stats

## AWS RDS Postgres

**File:** `postgresql/overview.json`

**Tags:** `aws`, `rds`, `postgres`

**Filter variables:** `dbinstance_identifier`

**Panels:**

- DatabaseConnections
- CPUUtilization
- FreeableMemory
- ReadLatency
- ReadThroughput
- ReadIOPS
- FreeStorageSpace
- WriteThroughput
- WriteIOPS
- Network transmit/receive
- DiskQueueDepth
- EBSByteBalance%
- EBSIOBalance%
- WriteLatency
- SwapUsage
- CheckpointLag
- ReplicaLag
