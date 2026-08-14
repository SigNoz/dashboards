# Grok Build Dashboard

## Details

This dashboard tracks usage and health for [Grok Build](https://github.com/xai-org/grok-build), xAI's terminal coding agent. It covers token consumption split by type and model, session and turn volume, tool activity and outcomes, error categories, and startup latency broken down by phase.

Everything here comes from the OpenTelemetry export Grok Build ships natively, so there is no instrumentation library to install. Grok emits **metrics and events only, no traces**, and every panel on this dashboard is metrics-based. All counters live under the `ai.xai.grok_code` meter scope and are monotonic delta sums, which is why the panels aggregate them with `increase` rather than `rate`.

Telemetry is off by default and requires a **double opt-in**: the `GROK_EXTERNAL_OTEL=1` master switch plus at least one exporter. Either one alone emits nothing.

```bash
export GROK_EXTERNAL_OTEL=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_ENDPOINT="https://ingest.<region>.signoz.cloud:443"
export OTEL_EXPORTER_OTLP_HEADERS="signoz-ingestion-key=<your-ingestion-key>"
grok
```

Two things are worth knowing before you wire this up.

**Use `http/protobuf`, not `grpc`.** Grok Build 1.0.3 documents gRPC as supported, but selecting it fails at export time with `gRPC protocol is not compatible with HTTP transport`. The telemetry stream still reports itself as active, so nothing surfaces in the terminal and the data silently never arrives. Check `grok --debug` for `external otel:` lines if a collector receives nothing.

**Collector auth is environment-only.** There is deliberately no headers key in `~/.grok/config.toml`, so the ingestion key has to come from `OTEL_EXPORTER_OTLP_HEADERS`. Non-secret settings can live in the config file under `[telemetry]` as `otel_*` keys.

There is no cost metric. To track spend, join `grok_code.token.usage` against your own price sheet.

## Dashboard panels

### Sections

#### Total Tokens

Tokens are the currency of an AI coding agent. This adds every token type together so you can see at a glance how much work Grok is doing and whether usage is climbing, flat, or tailing off.

<img width="721" height="238" alt="grok-build-total-tokens" src="./images/grok-build-panel-01.webp" />

#### Sessions

How many times Grok Build was started. Read this next to Turns to tell a lot of quick one-off invocations apart from a few long working sessions.

<img width="722" height="238" alt="grok-build-sessions" src="./images/grok-build-panel-02.webp" />

#### Turns

Every prompt-and-response cycle the agent completed, whether it finished, was cancelled, or errored. This is the closest thing to a request count for a coding agent.

<img width="722" height="238" alt="grok-build-turns" src="./images/grok-build-panel-03.webp" />

#### Errors

Total errors across every category. The panel turns amber as soon as one is recorded, because on a healthy setup this should sit at zero.

<img width="721" height="238" alt="grok-build-errors" src="./images/grok-build-panel-04.webp" />

#### Token Usage Over Time

Token consumption split by type. Grok reports four: `input`, `output`, `cache_read`, and `reasoning`. The reasoning split is its own dimension here rather than being folded into output, which makes it easy to see how much of your spend goes on thinking the user never sees.

<img width="1441" height="557" alt="grok-build-token-usage-over-time" src="./images/grok-build-panel-05.webp" />

#### Tokens by Type

The same four types as a share of the total. Input tokens dominate on almost any real workload, and a high `cache_read` share is the signal that prompt caching is doing its job. If that share falls, sessions are being restarted rather than continued.

<img width="1442" height="557" alt="grok-build-tokens-by-type" src="./images/grok-build-panel-06.webp" />

#### Tokens by Model

Token spend per model. Useful for tracking migration between model versions and for spotting which model is actually carrying the workload, which is rarely the one you assume.

<img width="1441" height="556" alt="grok-build-tokens-by-model" src="./images/grok-build-panel-07.webp" />

#### Tool Calls by Tool

Which tools the agent reaches for, from reading files and running shell commands to spawning subagents and searching the web. A good proxy for how much real work is being delegated rather than just discussed. Note that MCP tools collapse to `mcp_tool` and other non-built-in tools to `custom_tool` unless `OTEL_LOG_TOOL_DETAILS=1` is set.

<img width="1453" height="556" alt="grok-build-tool-calls-by-tool" src="./images/grok-build-panel-08.webp" />

#### Tool Outcomes

Success against error across every tool call. Tool failures are usually environmental rather than model problems: a missing file, a command that exits non-zero, a denied permission. A rising error share is often the first sign that the agent is working against a stale picture of the repo.

<img width="1441" height="557" alt="grok-build-tool-outcomes" src="./images/grok-build-panel-09.webp" />

#### Turns Over Time by Outcome

Turn volume split by `completed`, `cancelled`, and `error`. Cancellations are worth watching on their own, since they usually mean a developer stopped the agent mid-answer rather than anything failing.

<img width="1442" height="557" alt="grok-build-turns-over-time-by-outcome" src="./images/grok-build-panel-10.webp" />

#### Errors by Category

Errors over time, grouped by category. One caveat worth knowing: `rate_limit` covers both the per-minute request ceiling and full quota exhaustion, so the metric alone cannot tell "slow down" apart from "you are out of credit". Use the `status_code` on the `api_error` event to separate them.

<img width="1441" height="556" alt="grok-build-errors-by-category" src="./images/grok-build-panel-11.webp" />

#### Startup Duration p95

How long Grok takes from process start to a usable session. This includes a deliberate wait: the CLI holds telemetry closed until it has fetched fleet policy from xAI, since that policy can force the stream off. The wait is bounded and emission starts regardless within 30 seconds.

<img width="1442" height="556" alt="grok-build-startup-duration-p95" src="./images/grok-build-panel-12.webp" />

#### Startup Phase Duration p95

The same startup cost broken down by step, which is what you actually need to make it faster. Filter on `outcome = ok` before comparing percentiles, because truncated samples from timeouts will skew the result. Note that the step named by `stuck_in` on a timeout is often not the slowest step, since a phase that runs without pausing finishes before the timeout is recorded.

<img width="2894" height="557" alt="grok-build-startup-phase-duration-p95" src="./images/grok-build-panel-13.webp" />
