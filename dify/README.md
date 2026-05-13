# Dify Dashboard

## Details

This comprehensive dashboard provides deep visibility into the langgenius/dify service. It covers RED metrics (Rate, Errors, Duration), HTTP endpoint performance, LLM/GenAI activity (token usage, model latency, providers), workflow & app activity, and Postgres/Redis dependencies. It gives teams the data they need to monitor and optimize their Dify deployments.

To start sending Dify telemetry to SigNoz, follow the [Dify monitoring guide](https://signoz.io/docs/dify-observability/).

## Dashboard panels

### Sections

### Request Rate (spans/min)

Total spans per minute for langgenius/dify, representing the overall traffic level. Use this panel to gauge how busy the service is at any point in time and spot sudden spikes or drops in activity.

<img width="220" height="74" alt="Screenshot 2026-05-12 at 8 15 29 PM" src="https://github.com/user-attachments/assets/ad047800-6cf4-441d-be91-0dd5af969410" />


### Error Spans

Count of error spans in the time range. This panel helps you quickly detect when something is going wrong in the service, making it a key signal for on-call alerting and incident triage.

<img width="220" height="74" alt="Screenshot 2026-05-12 at 8 15 43 PM" src="https://github.com/user-attachments/assets/034b0dfc-54e0-49b9-bf95-32575bfb0d5a" />


### p95 Latency (root spans)

p95 latency for root HTTP request spans. This gives you a realistic picture of what most users experience in terms of response time, filtering out outliers while still catching degraded performance.

<img width="220" height="74" alt="Screenshot 2026-05-12 at 8 15 57 PM" src="https://github.com/user-attachments/assets/6eaa250d-21ff-4973-b971-fa7c9230c9a4" />


### Total LLM Tokens

Sum of total tokens consumed (input + output) across all LLM spans. Tokens represent the work being done by language models, and tracking this total helps you understand usage volume and anticipate costs.

<img width="220" height="74" alt="Screenshot 2026-05-12 at 8 16 09 PM" src="https://github.com/user-attachments/assets/615b3643-7634-42b2-ada8-96bc41670076" />


### Requests by Operation

Spans grouped by operation name, showing the traffic shape across different endpoints. Use this table to understand which operations are most heavily used and where load is concentrated.

<img width="437" height="129" alt="Screenshot 2026-05-12 at 8 16 26 PM" src="https://github.com/user-attachments/assets/7757927e-461e-40ba-a57a-1107315f5d6c" />

### p95 Latency by Operation

p95 span duration per operation, making it easy to spot which endpoints are slow. This table makes it easy to prioritize performance investigations based on where latency is highest.

<img width="437" height="129" alt="Screenshot 2026-05-12 at 8 16 46 PM" src="https://github.com/user-attachments/assets/00667bc0-8718-48a2-83bb-1ac619a6f08a" />

### LLM p95 Latency by Model

p95 latency of LLM/chat operations broken down by model. Different models have different performance characteristics; this panel helps you compare them and detect when a particular model is underperforming.

<img width="444" height="159" alt="Screenshot 2026-05-12 at 8 17 07 PM" src="https://github.com/user-attachments/assets/b9d8d285-5adf-4202-a527-8bc168cbb9e0" />


### LLM Calls by Model

Number of LLM invocations per model over time. This bar chart reveals which models are being used most and how usage patterns shift over time, supporting both capacity planning and model adoption tracking.

<img width="445" height="161" alt="Screenshot 2026-05-12 at 8 19 39 PM" src="https://github.com/user-attachments/assets/62e1c468-7c58-40c2-8b7d-dcc21b4c9466" />


### Token Usage: Input vs Output (by model)

Input and output tokens consumed per model, useful for cost tracking. By splitting token usage by direction and model, you can identify which models and workflows are the most resource-intensive.

<img width="447" height="146" alt="Screenshot 2026-05-12 at 8 20 03 PM" src="https://github.com/user-attachments/assets/a6a0c73b-d5ae-4bac-a836-6e81d3445445" />


### Activity by Dify App

Spans grouped by `dify.app_id` to show which apps are most active. This table helps you understand how usage is distributed across the applications built on your Dify deployment.

<img width="449" height="150" alt="Screenshot 2026-05-12 at 8 20 24 PM" src="https://github.com/user-attachments/assets/ce8d764d-849a-4934-befa-867518a93b27" />


### Streaming vs Non-Streaming Requests

Distribution of the `dify.streaming` attribute showing how many requests use streaming. This pie chart reveals user and application preferences and can inform infrastructure decisions around connection handling.

<img width="246" height="125" alt="Screenshot 2026-05-12 at 8 23 11 PM" src="https://github.com/user-attachments/assets/84579232-c4d0-4a47-b583-e743fb9c6018" />


### Postgres Query p95 Latency

p95 latency for Postgres operations from the Dify service, broken down by operation type. Database latency is a common source of application slowdowns, and this panel makes it easy to catch regression early.

<img width="246" height="125" alt="Screenshot 2026-05-12 at 8 23 23 PM" src="https://github.com/user-attachments/assets/76ccc461-91f8-464c-85ed-cffad1e01bbb" />


### Redis Operations by Type

Count of Redis operations by name, revealing cache and queue usage patterns. Monitoring Redis activity helps you understand caching effectiveness and detect unexpected spikes in queue depth or cache misses.

<img width="246" height="125" alt="Screenshot 2026-05-12 at 8 23 37 PM" src="https://github.com/user-attachments/assets/a6166ee9-ce62-413d-b7c6-cbbcc8dca1a8" />


### Slowest Endpoints (by p95)

Table of the slowest HTTP endpoints ranked by p95 latency, along with call count. This view is ideal for prioritizing optimization work by surfacing the endpoints that are both slow and frequently called.

<img width="746" height="104" alt="Screenshot 2026-05-12 at 8 24 02 PM" src="https://github.com/user-attachments/assets/bb0a2998-02e5-401e-8161-b5ddd9be2a78" />

