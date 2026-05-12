# Dify Dashboard

## Details

This comprehensive dashboard provides deep visibility into the langgenius/dify service. It covers RED metrics (Rate, Errors, Duration), HTTP endpoint performance, LLM/GenAI activity (token usage, model latency, providers), workflow & app activity, and Postgres/Redis dependencies. It gives teams the data they need to monitor and optimize their Dify deployments.

To start sending Dify telemetry to SigNoz, follow the [Dify monitoring guide](https://signoz.io/docs/dify-observability/).

## Dashboard panels

### Sections

### Request Rate (spans/min)

Total spans per minute for langgenius/dify, representing the overall traffic level. Use this panel to gauge how busy the service is at any point in time and spot sudden spikes or drops in activity.

### Error Spans

Count of error spans in the time range. This panel helps you quickly detect when something is going wrong in the service, making it a key signal for on-call alerting and incident triage.

### p95 Latency (root spans)

p95 latency for root HTTP request spans. This gives you a realistic picture of what most users experience in terms of response time, filtering out outliers while still catching degraded performance.

### Total LLM Tokens

Sum of total tokens consumed (input + output) across all LLM spans. Tokens represent the work being done by language models, and tracking this total helps you understand usage volume and anticipate costs.

### Requests by Operation

Spans grouped by operation name, showing the traffic shape across different endpoints. Use this table to understand which operations are most heavily used and where load is concentrated.

### p95 Latency by Operation

p95 span duration per operation, making it easy to spot which endpoints are slow. This table makes it easy to prioritize performance investigations based on where latency is highest.

### LLM p95 Latency by Model

p95 latency of LLM/chat operations broken down by model. Different models have different performance characteristics; this panel helps you compare them and detect when a particular model is underperforming.

### LLM Calls by Model

Number of LLM invocations per model over time. This bar chart reveals which models are being used most and how usage patterns shift over time, supporting both capacity planning and model adoption tracking.

### Token Usage: Input vs Output (by model)

Input and output tokens consumed per model, useful for cost tracking. By splitting token usage by direction and model, you can identify which models and workflows are the most resource-intensive.

### Activity by Dify App

Spans grouped by `dify.app_id` to show which apps are most active. This table helps you understand how usage is distributed across the applications built on your Dify deployment.

### Streaming vs Non-Streaming Requests

Distribution of the `dify.streaming` attribute showing how many requests use streaming. This pie chart reveals user and application preferences and can inform infrastructure decisions around connection handling.

### Postgres Query p95 Latency

p95 latency for Postgres operations from the Dify service, broken down by operation type. Database latency is a common source of application slowdowns, and this panel makes it easy to catch regression early.

### Redis Operations by Type

Count of Redis operations by name, revealing cache and queue usage patterns. Monitoring Redis activity helps you understand caching effectiveness and detect unexpected spikes in queue depth or cache misses.

### Slowest Endpoints (by p95)

Table of the slowest HTTP endpoints ranked by p95 latency, along with call count. This view is ideal for prioritizing optimization work by surfacing the endpoints that are both slow and frequently called.
