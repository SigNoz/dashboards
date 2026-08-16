# Grok Build Dashboard

## Details

This comprehensive dashboard provides deep visibility into Grok Build usage patterns and performance metrics. It tracks everything from token consumption and model mix to tool effectiveness, error categories, and startup latency, giving teams the data they need to optimize their AI-assisted development workflows.

Grok Build exports metrics natively, so no instrumentation library is required. Enable it with `GROK_EXTERNAL_OTEL=1` plus an OTLP exporter, and use `http/protobuf` as the protocol.

## Dashboard panels

### Sections

### Total Tokens

Tokens are the currency of AI coding assistants. This panel adds every token type together, giving you a complete picture of how much work Grok is doing and whether usage is ramping up, holding steady, or tailing off.

<img width="721" height="238" alt="grok-build-total-tokens" src="./images/grok-build-panel-01.webp" />

### Sessions

How many times Grok Build was started. Sessions show how often developers are turning to the agent, revealing adoption and engagement patterns across the team.

<img width="722" height="238" alt="grok-build-sessions" src="./images/grok-build-panel-02.webp" />

### Turns

Every prompt-and-response cycle the agent completed. Read this alongside Sessions to tell a lot of quick one-off invocations apart from a few long working sessions.

<img width="722" height="238" alt="grok-build-turns" src="./images/grok-build-panel-03.webp" />

### Errors

Total errors across every category. The panel turns amber as soon as one is recorded, since a healthy setup should sit at zero.

<img width="721" height="238" alt="grok-build-errors" src="./images/grok-build-panel-04.webp" />

### Token Usage Over Time

Token consumption split by type over time. Grok reports four types: input, output, cache reads, and reasoning. Reasoning tokens are broken out separately rather than folded into output, so you can see how much of your spend goes on thinking the user never sees.

<img width="1441" height="557" alt="grok-build-token-usage-over-time" src="./images/grok-build-panel-05.webp" />

### Tokens by Type

The same four types as a share of the total. Input tokens dominate on almost any real workload, and a high cache read share means prompt caching is working. A falling share usually means sessions are being restarted rather than continued.

<img width="1442" height="557" alt="grok-build-tokens-by-type" src="./images/grok-build-panel-06.webp" />

### Tokens by Model

Token spend per model. Useful for tracking migration between model versions and for spotting which model is actually carrying the workload, which is rarely the one you assume.

<img width="1441" height="556" alt="grok-build-tokens-by-model" src="./images/grok-build-panel-07.webp" />

### Tool Calls by Tool

Grok's agent does more than talk. This counts every tool it executed, from reading a file to running a terminal command to spawning a subagent, which is a good proxy for how much real work is being delegated to it.

<img width="1453" height="556" alt="grok-build-tool-calls-by-tool" src="./images/grok-build-panel-08.webp" />

### Tool Outcomes

Success against error across all tool calls. Tool failures are usually environmental rather than model problems: a missing file, a command that exits non-zero, a denied permission.

<img width="1441" height="557" alt="grok-build-tool-outcomes" src="./images/grok-build-panel-09.webp" />

### Turns Over Time by Outcome

Turn volume split by completed, cancelled, and error. Cancellations are worth watching on their own, since they usually mean a developer stopped the agent mid-answer rather than anything failing.

<img width="1442" height="557" alt="grok-build-turns-over-time-by-outcome" src="./images/grok-build-panel-10.webp" />

### Errors by Category

Errors over time, grouped by category. Note that rate limit covers both the per-minute request ceiling and full quota exhaustion, so check the status code on the api_error event to tell them apart.

<img width="1441" height="556" alt="grok-build-errors-by-category" src="./images/grok-build-panel-11.webp" />

### Startup Duration p95

How long Grok takes from process start to a usable session. This includes a deliberate wait while the CLI fetches fleet policy, which is bounded and never exceeds 30 seconds.

<img width="1442" height="556" alt="grok-build-startup-duration-p95" src="./images/grok-build-panel-12.webp" />

### Startup Phase Duration p95

The same startup cost broken down by step, which is what you need to make it faster. Filter on a successful outcome before comparing percentiles, since truncated samples from timeouts will skew the result.

<img width="2894" height="557" alt="grok-build-startup-phase-duration-p95" src="./images/grok-build-panel-13.webp" />
