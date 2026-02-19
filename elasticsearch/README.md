# Elasticsearch Monitoring Dashboard

The Elasticsearch Monitoring dashboard provides comprehensive visibility into Elasticsearch cluster health, performance metrics, and resource utilization using Prometheus metrics exported by Elasticsearch.

## Dashboard Panels

### Health & Status
- **Cluster Health Status**: Real-time cluster health indicator (green/yellow/red status with color-coded thresholds)
- **Total Documents**: Total number of documents across all indices in the cluster

### Performance Metrics
- **Search Query Rate**: Current search query throughput across the cluster
- **Search Query Rate by Node**: Search query rate broken down by individual nodes

### Resource Utilization
- **CPU Usage**: Current OS-level CPU utilization percentage with threshold alerts
- **CPU Usage by Node**: CPU usage trends over time for each node
- **JVM Memory Usage**: Java Virtual Machine memory consumption by memory pool (heap/non-heap)
- **Network Transport RX Rate**: Network bytes received rate for inter-node communication

## Metrics Used

This dashboard leverages the following Elasticsearch Prometheus metrics:

- `elasticsearch_cluster_health_status` - Cluster health status (0=green, 1=yellow, 2=red)
- `elasticsearch_indices_docs_count` - Total number of documents across all indices
- `elasticsearch_jvm_memory_used_bytes` - JVM memory usage in bytes
- `elasticsearch_os_cpu_percent` - OS-level CPU utilization percentage
- `elasticsearch_indices_search_query_total` - Total number of search queries executed
- `elasticsearch_transport_rx_size_in_bytes` - Network transport bytes received

## Prerequisites

To use this dashboard, you need to:

1. Have Elasticsearch running with Prometheus exporter enabled
2. Configure SigNoz to scrape Elasticsearch Prometheus metrics endpoint (typically `:9114/metrics`)
3. Ensure the metrics listed above are being collected

## Learn more

- [Elasticsearch Prometheus Exporter](https://github.com/prometheus-community/elasticsearch_exporter)
- [Monitoring Elasticsearch with Prometheus](https://www.elastic.co/guide/en/elasticsearch/reference/current/es-monitoring-exporters.html)
- [SigNoz Documentation](https://signoz.io/docs/)
