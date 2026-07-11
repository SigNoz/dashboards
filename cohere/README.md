# Cohere Dashboard

## Details

This dashboard monitors Cohere AI operations using traces emitted by OpenTelemetry. It provides a consolidated view of request volume, errors, token usage, latency, model adoption, request types, and individual spans so teams can understand Cohere usage and investigate slow or failed operations.

The dashboard expects Cohere telemetry to use `service.name = 'cohere-otel'` and relies on OpenTelemetry span fields and attributes including `name`, `duration_nano`, `has_error`, `gen_ai.request.model`, `gen_ai.usage.prompt_tokens`, `gen_ai.usage.completion_tokens`, `llm.request.type`, and `llm.usage.total_tokens`.

## Dashboard panels

### Overview

#### Total Cohere Calls

A count of all spans emitted by the `cohere-otel` service over the selected time range. It provides a quick view of overall Cohere activity.

<img width="708" height="232" alt="01_total-cohere-calls" src="https://github.com/user-attachments/assets/07ab6b7c-1acb-448c-9891-db6ea9431f5a" />


#### Error Spans

A count of Cohere spans where `has_error = true`. Use it as an at-a-glance signal for failed Chat, Embed, Rerank, or other Cohere operations.

<img width="708" height="232" alt="02_error-spans" src="https://github.com/user-attachments/assets/1fb87a41-fbc0-4460-8231-2be152712cdb" />


#### Input Tokens

The sum of `gen_ai.usage.prompt_tokens` across Cohere spans that report prompt-token usage.

<img width="708" height="232" alt="03_input-tokens" src="https://github.com/user-attachments/assets/5579c999-7191-4b75-883a-26162af1f9b1" />


#### Output Tokens

The sum of `gen_ai.usage.completion_tokens` across Cohere spans that report completion-token usage.

<img width="708" height="232" alt="04_output-tokens" src="https://github.com/user-attachments/assets/b11d5a8a-c8f6-446e-b146-3e1a648fddc0" />

### Activity & Latency

#### Calls by Operation

Cohere call volume over time grouped by span `name`. This separates Chat, Embed, Rerank, and other instrumented operations and shows how their traffic changes.

<img width="1432" height="564" alt="05_calls-by-operation" src="https://github.com/user-attachments/assets/2fe5619b-f63c-4e5e-b410-c9f3cf0e4fac" />


#### P95 Latency by Operation

The 95th-percentile `duration_nano` over time grouped by span `name`. It highlights slow Cohere operations and tail-latency changes.

<img width="1432" height="564" alt="06_p95-latency-by-operation" src="https://github.com/user-attachments/assets/527ff732-4d4a-4faf-a566-ae415e4d2d39" />


### Model & Operation Breakdown

#### Calls by Model

A pie chart of Cohere calls grouped by `gen_ai.request.model`, showing which models account for the most traffic.

<img width="1432" height="480" alt="07_calls-by-model" src="https://github.com/user-attachments/assets/f9ea3a5d-0907-4a90-8da4-fed6752f7ab8" />


#### Calls by Request Type

A pie chart of calls grouped by `llm.request.type`, making the distribution of Chat, Embed, Rerank, and other request types easy to compare.

<img width="1432" height="480" alt="08_calls-by-request-type" src="https://github.com/user-attachments/assets/79a1f8dc-1960-4a42-a8d9-0292e5b4b67b" />


#### Operation Performance

A table grouped by span `name` with call count, average latency, and p95 latency. It provides a side-by-side performance comparison of Cohere operations.

<img width="2880" height="560" alt="09_operation-performance" src="https://github.com/user-attachments/assets/5869d63d-95e6-448c-af8a-10700c56450e" />

### Trace Details

#### Recent Cohere Spans

A list of the 20 most recent Cohere spans with service, operation, duration, error state, model, request type, total tokens, and trace ID. Use it to inspect individual calls and continue investigation in the trace view.

<img width="1432" height="728" alt="10_recent-cohere-spans" src="https://github.com/user-attachments/assets/39f5589b-4262-4542-923f-91a28ee0120a" />


#### Cohere Error Spans

A list of the 20 most recent spans where `has_error = true`, including operation, duration, status message, and trace ID. It provides a focused starting point for debugging failed Cohere requests.

<img width="1432" height="728" alt="11_cohere-error-spans" src="https://github.com/user-attachments/assets/3f5bb7c4-d1cb-49bf-9a68-eed1597f3441" />

