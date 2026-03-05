# Elasticsearch Monitoring Dashboard

## Overview
This dashboard provides observability for Elasticsearch using OpenTelemetry (OTel) metrics. It focuses on Elasticsearch node behavior, overall cluster health, index performance, query/request activity, and cache efficiency.

## Dashboard Sections
1. **Node**
   Tracks per-node resource and runtime metrics such as disk usage, disk free/available space, CPU usage, and JVM/heap memory utilization.
2. **Cluster Health**
   Surfaces cluster-wide operational signals including health status, active shards, pending tasks, and unassigned shards.
3. **Index**
   Monitors index-level performance, including document count, shard/index disk usage, search query volume, and query time.
4. **Query/Request**
   Covers request throughput and responsiveness with search request rate and query latency metrics.
5. **Cache**
   Tracks cache effectiveness and churn via evictions, hit count, and miss count.

## Variables
The dashboard supports the following filter variables:
- `deployment.environment`
- `elasticsearch.node.name`
- `elasticsearch.cluster.name`

## Setup Requirements
To populate this dashboard, configure OpenTelemetry collection for Elasticsearch metrics using the `elasticsearchreceiver` in your OTel Collector pipeline.
