# Meter Dashboard


## Dashboard Page  
https://signoz.io/docs/dashboards/dashboard-templates/cost-meter/


## Overview

The Meter Dashboard delivers comprehensive, actionable insights into the ingestion of logs, spans, and metrics. It empowers teams to optimize resource usage, control costs, and make informed decisions for project or organizational budgeting.

## Dashboard Panels

### Sections

#### Total Usage

This section presents aggregated data on the total volume of logs (by size), spans (by size), and metric datapoints ingested into the platform. Usage can be broken down or filtered by service and environment using dashboard variables, enabling targeted analysis and reporting.

### Logs

Provides both cumulative and time-series visualizations of log ingestion, segmented by `service.name` and `deployment.environment` within the selected time frame. This section enables users to track overall log volume as well as identify trends and anomalies in log generation over time, both in terms of data size and entry count.

### Traces

Offers a comprehensive view of span ingestion, displaying both the cumulative total and time-series breakdowns by `service.name` and `deployment.environment`. Users can monitor the volume and count of spans, identify usage spikes, and observe trends over time.

### Metrics

Delivers cumulative and time-series analyses of metric datapoint ingestion, grouped by `service.name` and `deployment.environment`. This section helps visualize usage patterns, identify areas of growth or concern, and monitor the total count of metric datapoints across defined periods.
