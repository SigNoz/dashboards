# SigNoz MCP Server Dashboard

## Details

This dashboard provides operational visibility into the SigNoz MCP server. It tracks tool-call volume and error rates, MCP (JSON-RPC) method usage, and `execute_tool` span latency—broken down per tool—so teams can quickly see how the server is being used, which tools are slow or failing, and whether the overall service is healthy. 

## Dashboard panels

### Sections

#### Total Tool Calls

A single-value view of the total number of tool calls handled by the MCP server over the selected time range. It's a quick pulse on overall traffic and adoption.

#### MCP Spans Error Rate

A single-value summary of the percentage of MCP spans that resulted in an error. It gives an at-a-glance signal of service health—low and stable is good, sudden spikes warrant investigation.

#### Tool calls / sec by tool

Per-tool call rate, stacked to show the traffic mix across all tools. This reveals which tools are driving load and how usage is distributed.

#### Tool calls by error flag

Tool calls split by `mcp.tool.is_error` (true = errored). This separates healthy calls from failures, making it easy to spot when errors start climbing relative to total volume.

#### execute_tool span latency

p50 / p95 / p99 of `execute_tool` span duration. Excludes the SSE long-poll `GET /mcp`. Tracking these percentiles surfaces both typical performance and tail latency that affects the worst-case user experience.

#### MCP method calls / sec

Per-method JSON-RPC call rate (`initialize`, `ping`, `tools/list`, `resources/list`, `prompts/list`, …). This shows how clients are interacting with the protocol and which methods dominate traffic.

#### execute_tool p95 latency by tool

p95 of `execute_tool` span duration broken down by tool (`gen_ai.tool.name`). This identifies exactly which tool is slow, so optimization effort can be targeted.

#### execute_tool error rate % by tool

Per-tool error rate %: `execute_tool` spans with `has_error=true` over total, grouped by tool (`gen_ai.tool.name`). This pinpoints which specific tools are failing rather than just the aggregate rate.

#### Total Tool Calls (by tool)

A pie chart breakdown of total tool calls by tool. It complements the rate graphs with a clear share-of-usage view across the full time range.
