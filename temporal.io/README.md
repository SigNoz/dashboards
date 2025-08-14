# Temporal.io Monitoring Dashboards

> [!Note]
> **Dashboard Migration Status**: Due to the migration of metric names and attributes, the dashboards may not work properly and are currently being updated:
> We are actively working on updating these dashboards to be compatible with the new metric structure.


Comprehensive monitoring dashboards for Temporal workflow orchestration platform, covering both cloud and SDK metrics across different programming languages.

## Dashboards

### Temporal Cloud Metrics
Monitors cloud-hosted Temporal clusters with infrastructure and service-level metrics.

### Temporal SDK Metrics - Go
Tracks performance metrics for Temporal Go SDK applications:
- **Workflow Metrics**: End-to-end latency, task execution times
- **Activity Metrics**: Schedule-to-start latency, execution latency, success rates  
- **Task Queue Metrics**: Schedule-to-start latency for workflow tasks
- **Request Metrics**: API request latencies and patterns

### Temporal SDK Metrics - TypeScript
Performance monitoring for Temporal TypeScript/Node.js SDK applications with similar metric categories as the Go dashboard.

## Key Metrics

- **Workflow End-to-End Latency**: Complete workflow execution times
- **Activity Execution Latency**: Individual activity performance
- **Schedule-to-Start Latency**: Queue wait times for tasks and activities
- **Request Latency**: API call performance
- **Success/Failure Rates**: Reliability metrics

## Usage

Import these dashboards to monitor your Temporal workflow applications and identify performance bottlenecks in workflow orchestration, activity execution, and task scheduling.