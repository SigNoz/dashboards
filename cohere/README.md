# Cohere Dashboard

## Details

This dashboard monitors Cohere AI operations using traces emitted by OpenTelemetry. It provides a consolidated view of request volume, errors, token usage, latency, model adoption, request types, and individual spans so teams can understand Cohere usage and investigate slow or failed operations.

The dashboard expects Cohere telemetry to use `service.name = 'cohere-otel'` and relies on OpenTelemetry span fields and attributes including `name`, `duration_nano`, `has_error`, `gen_ai.request.model`, `gen_ai.usage.prompt_tokens`, `gen_ai.usage.completion_tokens`, `llm.request.type`, and `llm.usage.total_tokens`.

## Dashboard panels

### Overview

#### Total Cohere Calls

A count of all spans emitted by the `cohere-otel` service over the selected time range. It provides a quick view of overall Cohere activity.

#### Error Spans

A count of Cohere spans where `has_error = true`. Use it as an at-a-glance signal for failed Chat, Embed, Rerank, or other Cohere operations.

#### Input Tokens

The sum of `gen_ai.usage.prompt_tokens` across Cohere spans that report prompt-token usage.

#### Output Tokens

The sum of `gen_ai.usage.completion_tokens` across Cohere spans that report completion-token usage.

### Activity & Latency

#### Calls by Operation

Cohere call volume over time grouped by span `name`. This separates Chat, Embed, Rerank, and other instrumented operations and shows how their traffic changes.

#### P95 Latency by Operation

The 95th-percentile `duration_nano` over time grouped by span `name`. It highlights slow Cohere operations and tail-latency changes.

### Model & Operation Breakdown

#### Calls by Model

A pie chart of Cohere calls grouped by `gen_ai.request.model`, showing which models account for the most traffic.

#### Calls by Request Type

A pie chart of calls grouped by `llm.request.type`, making the distribution of Chat, Embed, Rerank, and other request types easy to compare.

#### Operation Performance

A table grouped by span `name` with call count, average latency, and p95 latency. It provides a side-by-side performance comparison of Cohere operations.

### Trace Details

#### Recent Cohere Spans

A list of the 20 most recent Cohere spans with service, operation, duration, error state, model, request type, total tokens, and trace ID. Use it to inspect individual calls and continue investigation in the trace view.

#### Cohere Error Spans

A list of the 20 most recent spans where `has_error = true`, including operation, duration, status message, and trace ID. It provides a focused starting point for debugging failed Cohere requests.
