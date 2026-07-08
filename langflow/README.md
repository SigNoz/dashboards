# Langflow Dashboard

## Details

This dashboard monitors Langflow flows and agents with an emphasis on LLM usage: token consumption (input/output/total), per-model breakdown, LLM call latency, tool calls, agent/flow runs, errors, and recent LLM calls. It is built on the `gen_ai.*` OpenTelemetry span attributes exported by Langflow's built-in Traceloop tracer, so teams can see how much LLM work their flows are doing, which models dominate, where latency lives, and whether runs are failing.

## Dashboard panels

### Sections

#### Total LLM Tokens

A single-value view of `gen_ai.usage.total_tokens` summed across all LLM calls over the selected time range. It's a quick pulse on overall LLM consumption.

#### LLM Calls

A count of LLM call spans (spans carrying `gen_ai.request.model`). Shows how many model invocations flows are making.

#### Input Tokens

Sum of `gen_ai.usage.input_tokens` (prompt tokens) across all calls.

#### Output Tokens

Sum of `gen_ai.usage.output_tokens` (completion tokens) across all calls.

#### Avg Tokens / Call

Average `gen_ai.usage.total_tokens` per LLM call. Useful for spotting shifts in prompt/response size.

#### Agent / Flow Runs

Count of agent invocations (`invoke_agent LangGraph` root spans). Reflects how many flows or agents were run.

#### Tool Calls

Count of tool executions (`execute_tool` spans). Shows how much tool activity the agents are driving.

#### Errors

Count of spans with an error status in Langflow. A threshold turns the tile red when one or more errors are present, giving an at-a-glance health signal.

#### Token Usage Over Time by Model

Total tokens over time, split by `gen_ai.request.model`. Reveals how consumption is distributed across models and how it trends.

#### Input vs Output Tokens Over Time

Prompt vs completion token volume over time. Separates the two sides of token usage to show where cost is concentrated.

#### LLM Calls Over Time by Model

Number of LLM calls over time, split by model. Shows call-volume trends and which models drive the traffic.

#### LLM Call Latency (p50 / p95 / p99)

Latency percentiles for LLM call spans. Surfaces both typical performance and tail latency that affects worst-case experience.

#### Per-Model Usage Breakdown

A table of calls, input/output/total tokens, and average latency per model, sorted by total tokens. Gives a full side-by-side comparison across models.

#### Tokens by Model

A pie chart showing each model's share of total tokens. Complements the trend graphs with a clear share-of-usage view.

#### Tool Calls by Tool

Count of tool executions grouped by tool span name. Identifies which tools are used most.

#### Agent / Flow Runs Over Time

Agent invocations (`invoke_agent LangGraph`) over time. Shows run-volume patterns and traffic peaks.

#### Agent Run Latency (p95)

95th-percentile latency of agent invocation spans. Tracks how long end-to-end agent runs take under load.

#### Recent LLM Calls

A list of the most recent LLM call spans with span name, model, input/output/total tokens, and duration. Useful for spot-checking individual calls and jumping into traces.
