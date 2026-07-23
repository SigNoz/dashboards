# OpenWebUI Dashboard

## Details

This dashboard monitors [OpenWebUI](https://docs.openwebui.com/) instrumented with OpenTelemetry: application golden signals (throughput, latency, errors), database query performance, and end-to-end LLM/GenAI observability. It combines two telemetry sources OpenWebUI can emit — the backend's **native OpenTelemetry** auto-instrumentation of FastAPI, SQLAlchemy, and HTTP clients (server spans carrying `http.route`, DB spans carrying `db.system`/`db.operation`), and **OpenLIT** GenAI instrumentation for model calls (chat spans carrying the OpenTelemetry `gen_ai.*` semantic conventions: `gen_ai.request.model`, `gen_ai.usage.input_tokens`/`output_tokens`, `gen_ai.usage.cost`). Every panel keys off these attributes and filters through the `service_name` picker, so you can scope to one or more services (for example the app service and the OpenLIT LLM service).

## Dashboard panels

### Sections

#### Total Requests

Total inbound HTTP requests (FastAPI server spans) handled by the selected OpenWebUI services over the selected time range. A quick pulse on overall traffic.

<img width="719" height="245" alt="openwebui-total-requests" src="./images/openwebui-panel-01.webp" />


#### Error Rate

The fraction of server requests that ended in an error status. An at-a-glance health signal for the application.

<img width="719" height="245" alt="openwebui-error-rate" src="./images/openwebui-panel-02.webp" />


#### Latency p95

95th-percentile request duration across all endpoints. Surfaces the tail latency that shapes worst-case experience.

<img width="719" height="245" alt="openwebui-latency-p95" src="./images/openwebui-panel-03.webp" />


#### Latency p99

99th-percentile request duration across all endpoints. The worst-case latency signal.

<img width="719" height="245" alt="openwebui-latency-p99" src="./images/openwebui-panel-04.webp" />


#### Request Rate by Endpoint

Request volume over time, split by `http.route`. Shows the traffic mix and which endpoints dominate.

<img width="1442" height="491" alt="openwebui-request-rate-by-endpoint" src="./images/openwebui-panel-05.webp" />


#### Latency Percentiles (p50 / p95 / p99)

p50 / p95 / p99 request duration over time. Typical performance and tail latency at a glance.

<img width="1442" height="491" alt="openwebui-latency-percentiles" src="./images/openwebui-panel-06.webp" />


#### Error Rate Over Time

The error fraction of server requests over time. Reveals incident windows and regressions.

<img width="1442" height="491" alt="openwebui-error-rate-over-time" src="./images/openwebui-panel-07.webp" />


#### Request Distribution by Endpoint

Share of requests per endpoint (`http.route`). A clear view of where traffic concentrates.

<img width="1457" height="491" alt="openwebui-request-distribution-by-endpoint" src="./images/openwebui-panel-08.webp" />


#### Endpoint Performance

A table of endpoints with request count and p95 / p99 latency. A side-by-side comparison to find the slow routes.

<img width="2888" height="491" alt="openwebui-endpoint-performance" src="./images/openwebui-panel-09.webp" />


#### DB Query Latency (p95 / p99)

p95 / p99 duration of database (SQLAlchemy) query spans over time. Surfaces database-driven slowness.

<img width="1442" height="492" alt="openwebui-db-query-latency" src="./images/openwebui-panel-10.webp" />


#### Database Operations

A table of database operations grouped by `db.operation`, with query count and average latency. Shows which queries run most and which are slowest.

<img width="1442" height="492" alt="openwebui-database-operations" src="./images/openwebui-panel-11.webp" />


#### LLM Requests

Count of LLM chat requests captured by the OpenLIT-instrumented `gen_ai` spans. Raw model-invocation volume.

<img width="719" height="244" alt="openwebui-llm-requests" src="./images/openwebui-panel-12.webp" />


#### Input Tokens

Total prompt/input tokens consumed across LLM calls (`gen_ai.usage.input_tokens`).

<img width="719" height="244" alt="openwebui-input-tokens" src="./images/openwebui-panel-13.webp" />


#### Output Tokens

Total completion/output tokens generated across LLM calls (`gen_ai.usage.output_tokens`).

<img width="719" height="244" alt="openwebui-output-tokens" src="./images/openwebui-panel-14.webp" />


#### Total Cost (USD)

The summed OpenLIT-computed cost of LLM calls (`gen_ai.usage.cost`) over the selected range.

<img width="734" height="244" alt="openwebui-total-cost" src="./images/openwebui-panel-15.webp" />


#### LLM Latency Percentiles (p50 / p95 / p99)

p50 / p95 / p99 duration of LLM chat spans over time. Model-call latency, both typical and tail.

<img width="1442" height="492" alt="openwebui-llm-latency-percentiles" src="./images/openwebui-panel-16.webp" />


#### Token Usage Over Time

Input vs output token volume over time. Shows demand and how prompt/response sizes trend.

<img width="1442" height="492" alt="openwebui-token-usage-over-time" src="./images/openwebui-panel-17.webp" />


#### LLM Cost Over Time (USD)

LLM spend over time. Spot cost spikes and trends before they surprise the bill.

<img width="1442" height="492" alt="openwebui-llm-cost-over-time" src="./images/openwebui-panel-18.webp" />


#### Requests by Model

Share of LLM requests per model (`gen_ai.request.model`). Shows which models carry the load.

<img width="1442" height="492" alt="openwebui-requests-by-model" src="./images/openwebui-panel-19.webp" />


#### Model Breakdown

A table of models with request count, input/output tokens, cost, and average latency. The cost and usage comparison across models.

<img width="2903" height="492" alt="openwebui-model-breakdown" src="./images/openwebui-panel-20.webp" />


#### Errors Over Time by Service

Error span count over time, grouped by service. Pinpoints which service is failing and when.

<img width="2888" height="491" alt="openwebui-errors-over-time-by-service" src="./images/openwebui-panel-21.webp" />


#### Recent Error Traces

A list of the latest errored spans across the selected services, newest first. Useful for jumping straight to failures when the error rate climbs.

<img width="1442" height="491" alt="openwebui-recent-error-traces" src="./images/openwebui-panel-22.webp" />


#### Recent Logs

A list of the most recent logs from the selected services. Quick log context to read alongside the traces.

<img width="1442" height="491" alt="openwebui-recent-logs" src="./images/openwebui-panel-23.webp" />
