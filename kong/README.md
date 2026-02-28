# Kong Monitoring Dashboard

## Overview
This dashboard provides observability for Kong Gateway using OpenTelemetry (OTel) metrics. It is designed to monitor gateway health, request performance, traffic behavior, errors, plugin activity, and runtime resource usage.

## Dashboard Sections
The dashboard is organized into seven sections:

1. **General**  
   High-level gateway status and key health indicators.
2. **Request**  
   Request volume, throughput, and request distribution trends.
3. **Latency**  
   End-to-end and upstream latency views to identify slow paths.
4. **Error**  
   Error rates and failure signals across status classes.
5. **Traffic**  
   Traffic patterns over time, including spikes and load behavior.
6. **Plugin**  
   Plugin-level metrics to understand policy and extension impact.
7. **Resource**  
   Runtime resource telemetry such as CPU/memory-related signals.

## Variables
The dashboard supports the following variables for filtering and scoping:

- `namespace`
- `service`
- `deployment.environment`
- `cluster`

## Setup Requirements
To populate this dashboard with data, Kong Gateway must have the **OpenTelemetry (OTel) plugin** enabled and configured to export metrics to your observability backend.
