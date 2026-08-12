# GitHub Copilot Dashboard

Detail page: https://signoz.io/docs/dashboards/dashboard-templates/github-copilot-dashboard/

Setup guide: https://signoz.io/docs/github-copilot-monitoring/

## Details

This dashboard monitors GitHub Copilot Chat in VS Code using the OpenTelemetry traces the Copilot Chat extension exports natively. No instrumentation library is involved: Copilot ships its own OTLP exporter, so turning on a handful of `github.copilot.chat.otel.*` settings sends agent turns, model calls, tool executions, and workspace indexing straight to SigNoz.

Every panel keys off the GenAI semantic-convention attributes Copilot emits: `gen_ai.operation.name` (`invoke_agent`, `chat`, `execute_tool`, `embeddings`), `gen_ai.response.model`, `gen_ai.usage.*`, `gen_ai.tool.name`, `gen_ai.agent.name`, and `gen_ai.conversation.id`. Use the `Service` picker at the top to scope the dashboard to one or more Copilot rollouts.

Token panels are deliberately scoped to `gen_ai.operation.name = 'chat'`. The `invoke_agent` span carries a roll-up of its children's token counts, so summing across every span would roughly double count. Copilot also emits no `gen_ai.usage.total_tokens`, which is why the total is computed as input plus output.

## Dashboard panels

### Sections

#### Total Tokens

Input plus output tokens across Copilot model calls. Copilot emits no total_tokens attribute, so this sums the two components, scoped to chat spans to avoid double counting the invoke_agent roll-up.

<img width="721" height="238" alt="github-copilot-total-tokens" src="./images/github-copilot-panel-01.webp" />

#### Model Calls

Number of chat completions requested from the model.

<img width="722" height="238" alt="github-copilot-model-calls" src="./images/github-copilot-panel-02.webp" />

#### Tool Calls

Number of tools the agent executed, such as read_file, grep_search or an MCP tool.

<img width="722" height="238" alt="github-copilot-tool-calls" src="./images/github-copilot-panel-03.webp" />

#### Conversations

Distinct chat conversations, counted on gen_ai.conversation.id.

<img width="721" height="238" alt="github-copilot-conversations" src="./images/github-copilot-panel-04.webp" />

#### Prompt Cache Hit Rate

Share of input tokens served from the prompt cache. Cached input is billed at a large discount, so this is the single biggest lever on Copilot cost.

<img width="721" height="239" alt="github-copilot-prompt-cache-hit-rate" src="./images/github-copilot-panel-05.webp" />

#### Cached Input Tokens

Input tokens read from the prompt cache rather than reprocessed.

<img width="722" height="239" alt="github-copilot-cached-input-tokens" src="./images/github-copilot-panel-06.webp" />

#### Reasoning Tokens

Output tokens spent on internal reasoning by reasoning-capable models. Billed as output but never shown in the chat.

<img width="722" height="239" alt="github-copilot-reasoning-tokens" src="./images/github-copilot-panel-07.webp" />

#### Avg Input Tokens per Call

Average prompt size per model call. Rising values mean the agent is carrying more context into each turn.

<img width="721" height="239" alt="github-copilot-avg-input-tokens-per-call" src="./images/github-copilot-panel-08.webp" />

#### Token Usage Over Time

Input, output, cached-input and reasoning tokens over time. Cached input is a subset of input, not an additional charge.

<img width="1921" height="556" alt="github-copilot-token-usage-over-time" src="./images/github-copilot-panel-09.webp" />

#### Tokens by Model

Which model is consuming the token budget. Copilot routes different tasks to different models, so this rarely matches the call-count split.

<img width="962" height="556" alt="github-copilot-tokens-by-model" src="./images/github-copilot-panel-10.webp" />

#### Model Calls Over Time

Chat completions per model over time. Useful for spotting when Copilot silently switches you to a different model.

<img width="1441" height="557" alt="github-copilot-model-calls-over-time" src="./images/github-copilot-panel-11.webp" />

#### Finish Reasons

How model responses terminated. A rising share of length means answers are being truncated by the token limit; tool_calls means the model handed control back to the agent.

<img width="1442" height="557" alt="github-copilot-finish-reasons" src="./images/github-copilot-panel-12.webp" />

#### Model Call Latency

End-to-end duration of chat completion spans, p50 through p99.

<img width="1441" height="556" alt="github-copilot-model-call-latency" src="./images/github-copilot-panel-13.webp" />

#### Time to First Chunk

Seconds until the first streamed token arrives. This is what the developer actually perceives as Copilot being slow, independent of total response length.

<img width="1442" height="556" alt="github-copilot-time-to-first-chunk" src="./images/github-copilot-panel-14.webp" />

#### Tool Calls by Name

Which tools the agent actually reaches for. Shows what kind of work Copilot is trusted with.

<img width="1441" height="557" alt="github-copilot-tool-calls-by-name" src="./images/github-copilot-panel-15.webp" />

#### MCP vs Built-in Tools

Split of tool calls between MCP server tools (names prefixed mcp_) and Copilot's built-in tools. Shows whether your MCP servers are earning their place in the tool list.

<img width="1442" height="557" alt="github-copilot-mcp-vs-built-in-tools" src="./images/github-copilot-panel-16.webp" />

#### Tool Latency (p95)

Slowest tools by p95 execution time. Long-running terminal commands and remote MCP calls dominate here and directly stall the agent.

<img width="1441" height="556" alt="github-copilot-tool-latency-p95" src="./images/github-copilot-panel-17.webp" />

#### Activity by Operation

Breakdown of Copilot spans across chat, execute_tool, invoke_agent and embeddings.

<img width="1442" height="556" alt="github-copilot-activity-by-operation" src="./images/github-copilot-panel-18.webp" />

#### Activity by Agent

Which internal Copilot agents are running. Background agents such as title generation and summarizeVirtualTools spend real tokens without any visible chat turn.

<img width="1441" height="557" alt="github-copilot-activity-by-agent" src="./images/github-copilot-panel-19.webp" />

#### Errors Over Time

Copilot spans with an error status, most often a tool that failed rather than the model itself.

<img width="1442" height="557" alt="github-copilot-errors-over-time" src="./images/github-copilot-panel-20.webp" />

#### Recent Errors

Individual failing spans with their status message. Click through to the full trace to see the conversation turn that produced the failure.

<img width="2882" height="635" alt="github-copilot-recent-errors" src="./images/github-copilot-panel-21.webp" />
