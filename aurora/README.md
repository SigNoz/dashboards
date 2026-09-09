# Amazon Aurora Dashboards

These dashboards monitor Amazon Aurora clusters across capacity, replica lag, memory, transactions, storage I/O, and engine internals.

Aurora needs two sources, so there are two dashboards per engine. CloudWatch reports what the cluster and its instances are doing. The database engine reports what the queries are doing. Neither covers the other, so run both.

| Dashboard | File | Source | Docs |
| --- | --- | --- | --- |
| Aurora PostgreSQL (CloudWatch) | `postgresql/overview.json` | `AWS/RDS` via the Prometheus CloudWatch Exporter | [Page](https://signoz.io/docs/dashboards/dashboard-templates/aurora-postgresql-cloudwatch/) |
| Aurora PostgreSQL (Engine Metrics) | `postgresql/db-metrics.json` | `postgresql` receiver | [Page](https://signoz.io/docs/dashboards/dashboard-templates/aurora-postgresql-engine-metrics/) |
| Aurora MySQL (CloudWatch) | `mysql/overview.json` | `AWS/RDS` via the Prometheus CloudWatch Exporter | [Page](https://signoz.io/docs/dashboards/dashboard-templates/aurora-mysql-cloudwatch/) |
| Aurora MySQL (Engine Metrics) | `mysql/db-metrics.json` | `mysql` receiver | [Page](https://signoz.io/docs/dashboards/dashboard-templates/aurora-mysql-engine-metrics/) |

Instance panels group by `DBInstanceIdentifier`, so the writer and each reader appear as separate series. Storage volume and serverless capacity are cluster-scoped and exist only under `DBClusterIdentifier`.

Replication metrics do not work on Aurora. It replicates through its shared storage volume, so `pg_stat_replication` and `SHOW REPLICA STATUS` both return no rows. Use Aurora Replica Lag on the CloudWatch dashboards instead. Several standard Amazon RDS metrics are also absent on Aurora, including `FreeStorageSpace`, `ReplicaLag`, and `BurstBalance`.

For setup instructions covering both collection paths, please visit the [SigNoz Amazon Aurora Integration Documentation](https://signoz.io/docs/integrations/aws-rds-aurora/).

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).
