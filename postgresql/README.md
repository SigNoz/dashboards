# PostgreSQL Dashboard

This dashboard provides a high-level overview of your PostgreSQL databases. It includes replication, locks, and throughput etc...

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Postgres overview

**File:** `postgresql.json`

**Tags:** `postgres`, `database`

**Filter variables:** `host.name`, `table.name`, `db.name`

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
