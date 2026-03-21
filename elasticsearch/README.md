# Elasticsearch Dashboard - Prometheus

## Overview

This dashboard provides comprehensive monitoring for Elasticsearch clusters using Prometheus metrics from the `elasticsearch_exporter`. It covers all critical aspects of Elasticsearch performance including cluster health, indexing operations, search performance, JVM metrics, and system resources.

## Prerequisites

Before using this dashboard, ensure you have:

1. **Elasticsearch cluster** running with the [`elasticsearch_exporter`](https://github.com/prometheus-community/elasticsearch_exporter)
2. **Prometheus server** configured to scrape metrics from the exporter
3. **SigNoz** instance capable of querying Prometheus metrics

## Setup

### 1. Install and Configure elasticsearch_exporter

Deploy the elasticsearch_exporter to collect metrics from your Elasticsearch cluster:

```bash
# Download and run elasticsearch_exporter
docker run --rm -d \
  --name elasticsearch-exporter \
  -p 9114:9114 \
  quay.io/prometheuscommunity/elasticsearch-exporter:latest \
  --es.uri=http://elasticsearch:9200 \
  --es.all \
  --es.indices \
  --es.indices_settings \
  --es.cluster_settings \
  --es.shards
```

### 2. Configure Prometheus

Add the following job to your `prometheus.yml` configuration:

```yaml
scrape_configs:
  - job_name: 'elasticsearch-exporter'
    static_configs:
      - targets: ['elasticsearch-exporter:9114']
    scrape_interval: 30s
    metrics_path: /metrics
```

### 3. Configure SigNoz to Query Prometheus

Ensure your SigNoz instance is configured with a Prometheus data source pointing to your Prometheus server.

## Dashboard Panels

This dashboard is organized into six main sections:

### 🏥 Cluster Health
- **Cluster Health Status**: Shows cluster status (0=green, 1=yellow, 2=red)
- **Number of Nodes**: Total nodes in the cluster
- **Pending Tasks**: Tasks waiting in the cluster queue
- **Active Shards**: Number of active primary shards
- **Relocating Shards**: Shards currently being moved
- **Unassigned Shards**: Shards without node assignment

### 📊 Index Metrics
- **Total Documents Count**: Total documents across all indices
- **Documents Indexed Rate**: Rate of new documents being indexed (docs/sec)
- **Documents Deleted Rate**: Rate of document deletions (docs/sec)
- **Store Size**: Total size of all indices in bytes

### 🔍 Search Performance
- **Search Query Rate**: Number of search queries per second
- **Search Query Latency**: Average time per search query
- **Search Fetch Rate**: Number of fetch operations per second
- **Search Fetch Latency**: Average time per fetch operation

### ⚡ Indexing Performance
- **Indexing Rate**: Rate of indexing operations per second
- **Indexing Latency**: Average time per indexing operation
- **Merge Rate**: Rate of segment merge operations
- **Refresh Rate**: Rate of index refresh operations

### ☕ JVM Metrics
- **JVM Heap Used vs Committed**: Heap memory usage and allocation
- **JVM GC Collection Time**: Garbage collection time per second
- **JVM GC Collection Count**: Number of GC collections per second
- **JVM Thread Count**: Number of active JVM threads

### 🖥️ System Resources
- **CPU Usage**: Elasticsearch process CPU utilization percentage
- **Memory Usage**: JVM memory consumption
- **Disk Usage**: Available vs total disk space for data
- **Network I/O**: Network bytes received and transmitted

## Key Metrics Used

The dashboard uses standard `elasticsearch_exporter` metrics:

| Metric Category | Prometheus Metrics |
|---|---|
| **Cluster Health** | `elasticsearch_cluster_health_*` |
| **Document Stats** | `elasticsearch_indices_docs`, `elasticsearch_indices_store_size_bytes` |
| **Search Performance** | `elasticsearch_indices_search_query_*`, `elasticsearch_indices_search_fetch_*` |
| **Indexing Performance** | `elasticsearch_indices_indexing_*`, `elasticsearch_indices_merges_*`, `elasticsearch_indices_refresh_*` |
| **JVM Metrics** | `elasticsearch_jvm_memory_*`, `elasticsearch_jvm_gc_collection_*`, `elasticsearch_jvm_threads_current` |
| **System Resources** | `elasticsearch_process_cpu_percent`, `elasticsearch_filesystem_data_*`, `elasticsearch_transport_*` |

## Alerting Recommendations

Consider setting up alerts for:

- **Cluster Health**: Status != 0 (green)
- **Unassigned Shards**: > 0 for extended periods
- **Search Latency**: > acceptable threshold for your use case
- **JVM Heap Usage**: > 85% of committed memory
- **Disk Usage**: Available space < 15% of total
- **CPU Usage**: > 80% sustained usage

## Troubleshooting

### Common Issues

1. **No data in panels**: 
   - Verify elasticsearch_exporter is running and accessible
   - Check Prometheus is scraping the exporter (check targets in Prometheus UI)
   - Ensure SigNoz can query your Prometheus instance

2. **Some metrics missing**:
   - Confirm elasticsearch_exporter is started with appropriate flags (`--es.all`, `--es.indices`, etc.)
   - Check Elasticsearch permissions for the exporter user

3. **High resource usage**:
   - Adjust scrape intervals in Prometheus configuration
   - Consider using `--es.indices_mappings=false` to reduce metric volume

### Useful Commands

```bash
# Check elasticsearch_exporter metrics
curl http://elasticsearch-exporter:9114/metrics

# Verify Elasticsearch cluster health
curl -X GET "elasticsearch:9200/_cluster/health?pretty"

# Check Prometheus targets
curl http://prometheus:9090/api/v1/targets
```

## Dashboard Import

1. Copy the `elasticsearch-prometheus-v1.json` content
2. In SigNoz, go to **Dashboards** → **Import Dashboard**
3. Paste the JSON content and import
4. The dashboard will be ready to use with your Elasticsearch metrics

## Version Information

- **Dashboard Version**: v1
- **Compatible with**: Elasticsearch 6.x, 7.x, 8.x
- **elasticsearch_exporter**: v1.1.0+
- **SigNoz**: v0.8.0+