# Hermes Agent Dashboard

## Details

This dashboard offers comprehensive monitoring for the Hermes coding agent. It highlights key metrics such as agent sessions and turns, LLM API calls and token usage, tool-call activity, latency trends, and errors. It is built from OTel traces (service: `hermes-agent`) using `gen_ai.*` and `hermes.*` span attributes.

Panels are grouped top-to-bottom: Overview (scorecards), LLM/Model, Agent/Turns, Tool Calls, and Errors.

## Dashboard panels

### Overview

This section provides at-a-glance scorecards summarizing overall agent activity in the selected time range.

#### Agent Turns

Count of root `agent` spans, representing the number of agent turns/sessions handled by Hermes. This is the top-level measure of how much work the agent is doing.

#### LLM Turns

Count of `llm.*` wrapper spans, showing how many LLM interaction turns the agent has executed.

#### LLM API Calls

Count of individual gen_ai chat completions (spans where `llm.model_name` exists), capturing the raw volume of requests sent to model providers.

#### Tool Calls

Count of `tool.*` spans, giving a single-value view of how often the agent invokes tools.

#### Total Tokens

Sum of `gen_ai.usage.total_tokens` across all spans, showing total token consumption in the selected range.

#### Error Spans

Count of spans with `hasError = true`. A quick reliability check — any non-zero value is highlighted for immediate attention.

### LLM & Model Usage

This section breaks down model usage, token consumption, and LLM API performance.

#### LLM API Calls by Model

Hermes can call multiple LLM models, each optimized for different tasks. This panel reveals which models are being called most often, helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

#### Token Usage Over Time

Stacked token totals over time, split into input tokens, output tokens, and cache-read tokens. Over time, you can monitor efficiency, spot growth in adoption, and understand cache savings from prompt caching.

#### Total Tokens by Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

#### LLM API Call Latency (p50 / p95 / p99)

Duration percentiles of chat completion spans, helping you identify provider-side slowness and ensure responsive agent turns.

#### Cost Proxy: Input vs Output Tokens by Model

Token volume as a cost proxy, split into input and output tokens per model. No native cost attribute exists, so scale these volumes by your per-model pricing to estimate spend.

#### Responses by Finish Reason

Distribution of `llm.response.finish_reason` values across completions. A healthy system is dominated by normal stop reasons; spikes in other reasons (such as length cutoffs) signal truncated or abnormal responses.

### Agent Turns & Sessions

This section tracks agent turn activity and session behavior, showing how turns flow through the system and how they resolve.

#### Agent Turn Duration (p50 / p95)

End-to-end latency of root `agent` spans, measuring how long a full agent turn takes from start to finish.

#### Avg API Calls per Turn

Average of `hermes.turn.api_call_count` per agent turn over time. Turns requiring unusually many API calls may indicate loops or inefficient agent behavior.

#### Sessions by Kind

Session counts grouped by `hermes.session.kind`, showing how usage is distributed across different session types.

#### Agent Turns Over Time

This chart captures the volume of agent turns over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

#### Avg Tools per Turn

Average of `hermes.turn.tool_count` over time, showing how tool-heavy a typical agent turn is.

#### Turn Final Status

Distribution of `hermes.turn.final_status`, making it easy to see the share of turns that complete successfully versus those that end in other states.

### Tool Calls

This section breaks down Hermes tool usage, showing which tools are invoked most often, how they perform, and how they resolve.

#### Tool Call Latency (p95) by Type

p95 span duration grouped by tool span name, showing where tool execution time is actually spent. A tool that is called rarely but dominates this chart is a prime optimization target.

#### GenAI Tool Invocations by Name

Count of tool spans grouped by `tool.name` (model-requested tools), showing which capabilities the model relies on the most.

#### Tool Outcomes (completed vs error)

Tool spans grouped by `hermes.tool.outcome`, giving a quick view of how often tool executions succeed versus fail.

#### Tool Calls by Type

Count of `tool.*` spans grouped by operation name, showing which tool types are invoked most frequently.

#### Tool Usage Summary

Table of call count and p95 latency per tool type, sorted by call volume, combining usage and performance in a single view.

### Error Monitoring

This section surfaces failures across Hermes agent runs, helping you quickly spot error spikes, identify which operations are most affected, and drill into individual failed spans.

#### Errors Over Time

Time series of spans with `hasError = true`, broken down by span name. Watch for spikes that signal incidents or regressions.

#### Error Count by Operation

Table of errored spans grouped by span name, surfacing the operations associated with the most failures.

#### Recent Error Spans (detail)

Detailed list of the most recent errored spans with status message, tool outcome, and duration. Drill into individual failed runs for root-cause investigation.
