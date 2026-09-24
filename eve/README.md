# Eve Dashboard

## Details

This dashboard offers a clear view into agents built on eve, Vercel's agent framework. It highlights turns, conversations, and model calls, token usage per model and per agent, latency percentiles for calls and turns, tool, subagent, and provider-tool activity, turn outcomes, and errors by type.

To start sending eve telemetry to SigNoz, follow the [Eve observability guide](https://signoz.io/docs/eve-observability/).

## Dashboard panels

### Sections

### Turns

Agent turns, counted from `invoke_agent` spans. eve starts a new trace for every turn, and a subagent's turn is its own trace linked to the caller, so subagent turns count here too.

<img width="232" height="154" alt="eve-turns" src="./images/eve-panel-01.webp" />

### Conversations

Distinct sessions, from `gen_ai.conversation.id`. A subagent shares its caller's session, and `/new` in the dev TUI keeps the same id, so a long session with several topics still counts once.

<img width="232" height="154" alt="eve-conversations" src="./images/eve-panel-02.webp" />

### LLM Calls

Model calls across every agent, from `chat` spans. Read it against Turns: close to two calls per turn is normal for a tool-using agent (one call that requests tools, one that answers).

<img width="232" height="154" alt="eve-llm-calls" src="./images/eve-panel-03.webp" />

### Input Tokens

Prompt tokens, summed over `chat` spans only. eve reports the same usage on `chat`, `agent.step`, and `invoke_agent`, so a query that sums every span triples the figure. Cache reads are included in this number.

<img width="231" height="154" alt="eve-input-tokens" src="./images/eve-panel-04.webp" />

### Output Tokens

Completion tokens, summed over `chat` spans only, for the same reason as Input Tokens.

<img width="232" height="154" alt="eve-output-tokens" src="./images/eve-panel-05.webp" />

### Turn Failure Rate

Share of turns where `agent.turn.outcome` is `failed`. This reads the outcome attribute rather than span status, because a cancelled turn marks its children as errors and a failed tool call leaves the turn clean.

<img width="232" height="154" alt="eve-turn-failure-rate" src="./images/eve-panel-06.webp" />

### Token Usage Over Time

Input, output, and cache-read tokens over time. Input dominates because every step resends the conversation and tool results. Cache reads are a subset of input and cover most of it on long sessions, so a widening gap between the two lines is a caching regression worth checking.

<img width="712" height="369" alt="eve-token-usage-over-time" src="./images/eve-panel-07.webp" />

### LLM Calls by Model

Call volume per `gen_ai.response.model`, which carries the dated snapshot the provider served. A silent model upgrade shows up as a new series here.

<img width="712" height="369" alt="eve-llm-calls-by-model" src="./images/eve-panel-08.webp" />

### Tokens by Model

Calls, input, output, and cache-read tokens per served model and `gen_ai.provider.name`. The provider reads `openai.responses` for eve's `openai()` helper and `gateway` for AI Gateway model strings, which is how to spot traffic that moved to the Gateway.

<img width="712" height="369" alt="eve-tokens-by-model" src="./images/eve-panel-09.webp" />

### Tokens by Agent

Turns and tokens per agent, read from `invoke_agent` spans. Subagents appear as their own rows because their usage is reported on their own turn and is not rolled into the caller, so add a subagent's row to its caller's to get the full cost of a request.

<img width="712" height="369" alt="eve-tokens-by-agent" src="./images/eve-panel-10.webp" />

### LLM Call Latency

p50, p95, and p99 of `chat` span duration. A p99 that spikes while p50 stays flat usually means rate-limit retries on a few calls rather than a slower model.

<img width="712" height="369" alt="eve-llm-call-latency" src="./images/eve-panel-11.webp" />

### Turn Latency (p95)

p95 end-to-end turn duration per agent, including every model step, tool call, and subagent dispatch. Compare each agent to its own baseline: agents with slow tools or subagents sit well above chat-only ones.

<img width="712" height="369" alt="eve-turn-latency-p95" src="./images/eve-panel-12.webp" />

### Model Steps per Turn

Average `agent.step` spans per turn. Each tool round trip adds a step, so a line drifting upward means agents need more tool calls to answer.

<img width="712" height="369" alt="eve-model-steps-per-turn" src="./images/eve-panel-13.webp" />

### Finish Reasons

Why each model call ended. A near-even split between `tool-calls` and `stop` is the normal shape for tool-using agents. A growing `length` slice means responses are being cut off at the token limit.

<img width="712" height="369" alt="eve-finish-reasons" src="./images/eve-panel-14.webp" />

### Agents

Turns, failed turns, cancelled turns, and average latency per agent, all from `agent.turn.outcome`. Cancelled turns come from a user pressing Escape, so a high count points at slow answers rather than broken code.

<img width="712" height="369" alt="eve-agents" src="./images/eve-panel-15.webp" />

### Tools

Calls, failures, and average latency per authored tool, from `execute_tool` spans. A tool failure does not fail the turn, because the model sees the error and recovers, so this table is where a flaky backend shows up.

<img width="712" height="369" alt="eve-tools" src="./images/eve-panel-16.webp" />

### Tool Calls Over Time

Authored tool invocations per tool. A sustained climb on one tool without a matching rise in Turns is the usual early sign of an agent looping on a tool instead of answering.

<img width="712" height="369" alt="eve-tool-calls-over-time" src="./images/eve-panel-17.webp" />

### Actions by Kind

Every action the model took, from `agent.action` spans, split by `agent.action.kind` into tool calls and subagent calls. Provider-executed tools such as OpenAI `web_search` have no `execute_tool` span, so this is the only panel that counts them. Sort or page the table to reach the subagent rows.

<img width="712" height="369" alt="eve-actions-by-kind" src="./images/eve-panel-18.webp" />

### Turn Outcomes

Turns over time by outcome: completed, failed, and cancelled. Failures and cancellations should stay a thin band under completed. Model failures that exhaust their retries are what fail a turn, so a rising failed band usually traces back to rate limits or provider errors in LLM Error Rate.

<img width="712" height="369" alt="eve-turn-outcomes" src="./images/eve-panel-19.webp" />

### Errors by Type

Errored agent spans by `error.type` and operation. A model failure appears as `AI_RetryError` on both `chat` and `agent.step`, and a failed tool as `Error` on `execute_tool` plus `ACTION_RESULT_FAILED` on its `agent.action`, so read the chart per operation rather than summing it.

<img width="712" height="369" alt="eve-errors-by-type" src="./images/eve-panel-20.webp" />

### Tool Error Rate

Share of authored tool executions that threw. The agent usually recovers and still answers, which is why this rate needs its own panel.

<img width="712" height="153" alt="eve-tool-error-rate" src="./images/eve-panel-21.webp" />

### LLM Error Rate

Share of model calls that failed after retries. Cancellations are excluded: eve marks a cancelled call as `TurnCancelledError`, which would otherwise inflate this rate every time a user presses Escape.

<img width="712" height="153" alt="eve-llm-error-rate" src="./images/eve-panel-22.webp" />

### Recent Errors

The latest errored agent spans with their error class, message, and service. A failed tool shows as an `execute_tool` row followed by its `agent.action` at the same timestamp, and a model failure as a `chat` row followed by its `agent.step`.

<img width="1433" height="477" alt="eve-recent-errors" src="./images/eve-panel-23.webp" />
