# DeepSeek Harness Dashboard

## Details

This dashboard offers a clear view into DeepSeek Harness (`dsh`) usage and performance. It highlights key metrics such as token spend and cache efficiency, turn and session volume, model latency and time to first token, native and MCP tool activity, and error breakdown.

To start sending DeepSeek Harness telemetry to SigNoz, follow the [DeepSeek Harness observability guide](https://signoz.io/docs/deepseek-harness-observability/).

## Dashboard panels

### Sections

### Agent Turns

Every prompt-and-response cycle the harness completed. Subagent turns are included here, because a spawned subagent opens its own root span rather than nesting under its parent; the Activity panel breaks them out separately.

<img width="479" height="158" alt="deepseek-harness-agent-turns" src="./images/deepseek-harness-panel-01.webp" />

### Sessions

Distinct sessions. Read this next to Agent Turns to tell a lot of quick one-shot invocations apart from a few long working sessions. A subagent runs under its own session id and is tied back to its parent by `dsh.session.parent_id`.

<img width="479" height="158" alt="deepseek-harness-sessions" src="./images/deepseek-harness-panel-02.webp" />

### Model Calls

One count per model call. Divided by Agent Turns, this tells you how many round trips the agent needs to finish a piece of work.

<img width="480" height="158" alt="deepseek-harness-model-calls" src="./images/deepseek-harness-panel-03.webp" />

### Tool Calls

Every tool the agent executed, native and MCP together, which is a good proxy for how much real work is being delegated to it rather than just discussed.

<img width="480" height="158" alt="deepseek-harness-tool-calls" src="./images/deepseek-harness-panel-04.webp" />

### Total Tokens

Total token spend across every model call. Scoped to `LLM` spans on purpose: the `invoke_agent` span repeats the sum of its own model calls, so an unscoped sum double counts exactly 2x.

<img width="480" height="158" alt="deepseek-harness-total-tokens" src="./images/deepseek-harness-panel-05.webp" />

### Cache Hit Rate

Share of input tokens served from cache. On a long session this climbs quickly, since each turn replays the conversation so far. Read from `AGENT` spans, because `LLM` spans omit the cache attribute rather than setting it to zero on a miss, which would drop the cold calls out of the average and read high.

<img width="479" height="158" alt="deepseek-harness-cache-hit-rate" src="./images/deepseek-harness-panel-06.webp" />

### Token Usage Over Time

Input, cached, and output tokens over time. Output stays low and flat on almost any real agent workload: most model calls are short decisions about which tool to run next, and only the final answer of a turn is long.

<img width="1921" height="476" alt="deepseek-harness-token-usage-over-time" src="./images/deepseek-harness-panel-07.webp" />

### Turn Outcomes

How turns actually finished, from `dsh.turn.end_reason`. A healthy setup is almost entirely `completed`; a rising `error` share points at the model provider rather than at tooling, since tool failures do not end a turn.

<img width="962" height="476" alt="deepseek-harness-turn-outcomes" src="./images/deepseek-harness-panel-08.webp" />

### Activity Over Time

Turns, model calls, tool calls, and subagent turns on one axis. The subagent line is worth watching on its own, because those turns are also counted in the turn total and can quietly inflate it.

<img width="1921" height="476" alt="deepseek-harness-activity-over-time" src="./images/deepseek-harness-panel-09.webp" />

### Model Finish Reasons

Why each model call stopped. `tool_calls` dominating over `stop` is the normal shape for an agent: most calls end by reaching for a tool, and only the last call of a turn ends with a finished answer. Scoped to `LLM` spans, since on `AGENT` spans the same attribute holds the turn outcome instead.

<img width="962" height="476" alt="deepseek-harness-model-finish-reasons" src="./images/deepseek-harness-panel-10.webp" />

### Model Call Latency

p95 and p99 duration of model calls. This tracks output length more than anything else, so a rising p99 usually means longer answers rather than a slower provider. Check it against Time to First Token to tell the two apart.

<img width="1441" height="476" alt="deepseek-harness-model-call-latency" src="./images/deepseek-harness-panel-11.webp" />

### Time to First Token

How long the model takes to start responding. Unlike total latency this is independent of answer length, so it is the honest measure of provider responsiveness and the one developers actually feel.

<img width="1442" height="476" alt="deepseek-harness-time-to-first-token" src="./images/deepseek-harness-panel-12.webp" />

### Token Distribution by Model

Token spend per model. Useful for tracking migration between model versions and for spotting which model is actually carrying the workload, which is rarely the one you assume.

<img width="961" height="476" alt="deepseek-harness-token-distribution-by-model" src="./images/deepseek-harness-panel-13.webp" />

### Tool Call Distribution

Which tools the agent reaches for. Tools named `mcp__<server>__<tool>` come from an MCP server, and the name is the only thing that identifies them: no attribute distinguishes an MCP tool from a native one.

<img width="962" height="476" alt="deepseek-harness-tool-call-distribution" src="./images/deepseek-harness-panel-14.webp" />

### Errors Over Time

Failed turns, model call errors, and reported tool errors together. Read the tool line with care: it only counts tools that report failure explicitly, so a shell command exiting non-zero still records a successful span and never appears here.

<img width="962" height="476" alt="deepseek-harness-errors-over-time" src="./images/deepseek-harness-panel-15.webp" />

### Session Details

Token spend and model call count per session, sorted so the expensive ones surface first. Subagent sessions appear as their own rows, identifiable by a bare UUID where a top-level session id carries a `session-` prefix.

<img width="1441" height="476" alt="deepseek-harness-session-details" src="./images/deepseek-harness-panel-16.webp" />

### Tool Performance

Call count and latency per tool. Slow tools are worth attention even when they never fail, since every second here is a second the model sits idle mid-turn and the developer sits watching.

<img width="1453" height="476" alt="deepseek-harness-tool-performance" src="./images/deepseek-harness-panel-17.webp" />
