# Langflow Dashboard

## Details

This dashboard monitors Langflow flows and agents with an emphasis on LLM usage: token consumption (input/output/total), per-model breakdown, LLM call latency, tool calls, agent/flow runs, errors, and recent LLM calls. It is built on the `gen_ai.*` OpenTelemetry span attributes exported by Langflow's built-in Traceloop tracer, so teams can see how much LLM work their flows are doing, which models dominate, where latency lives, and whether runs are failing.

## Dashboard panels

### Sections

#### Total LLM Tokens

A single-value view of `gen_ai.usage.total_tokens` summed across all LLM calls over the selected time range. It's a quick pulse on overall LLM consumption.

<img width="386" height="124" alt="Screenshot 2026-07-08 at 12 18 08 PM" src="https://github.com/user-attachments/assets/72d3549b-64e9-4e8f-bef8-46a8f9cb8c42" />


#### LLM Calls

A count of LLM call spans (spans carrying `gen_ai.request.model`). Shows how many model invocations flows are making.

<img width="386" height="124" alt="Screenshot 2026-07-08 at 12 18 21 PM" src="https://github.com/user-attachments/assets/9678e199-bd84-4f96-8d91-f14e5889365a" />

#### Avg Tokens / Call

Average `gen_ai.usage.total_tokens` per LLM call. Useful for spotting shifts in prompt/response size.

<img width="386" height="124" alt="Screenshot 2026-07-08 at 12 19 05 PM" src="https://github.com/user-attachments/assets/a15efa1a-8961-4fba-97d6-98a13ea177cb" />


#### Agent / Flow Runs

Count of agent invocations (`invoke_agent LangGraph` root spans). Reflects how many flows or agents were run.

<img width="386" height="124" alt="Screenshot 2026-07-08 at 12 19 16 PM" src="https://github.com/user-attachments/assets/02c6bc15-b9e0-41a0-b33f-8ccec5396758" />


#### Tool Calls

Count of tool executions (`execute_tool` spans). Shows how much tool activity the agents are driving.

<img width="386" height="124" alt="Screenshot 2026-07-08 at 12 19 26 PM" src="https://github.com/user-attachments/assets/8bb55915-3188-4423-bd1f-aff9200e0678" />


#### Errors

Count of spans with an error status in Langflow. A threshold turns the tile red when one or more errors are present, giving an at-a-glance health signal.

<img width="396" height="128" alt="Screenshot 2026-07-08 at 12 19 46 PM" src="https://github.com/user-attachments/assets/83ac36b2-a2af-4cc3-9f73-202e3b6dc6fd" />


#### Token Usage Over Time by Model

Total tokens over time, split by `gen_ai.request.model`. Reveals how consumption is distributed across models and how it trends.

<img width="624" height="166" alt="Screenshot 2026-07-08 at 12 20 11 PM" src="https://github.com/user-attachments/assets/96c54698-1162-408d-93d6-00deae29e7e3" />


#### Input vs Output Tokens Over Time

Prompt vs completion token volume over time. Separates the two sides of token usage to show where cost is concentrated.

<img width="606" height="178" alt="Screenshot 2026-07-08 at 12 20 31 PM" src="https://github.com/user-attachments/assets/171b67c6-c646-4453-b695-3422f7d03153" />


#### LLM Calls Over Time by Model

Number of LLM calls over time, split by model. Shows call-volume trends and which models drive the traffic.

<img width="625" height="178" alt="Screenshot 2026-07-08 at 12 20 50 PM" src="https://github.com/user-attachments/assets/10d98b98-3268-4f0b-82df-aff23e03f92e" />


#### LLM Call Latency (p50 / p95 / p99)

Latency percentiles for LLM call spans. Surfaces both typical performance and tail latency that affects worst-case experience.

<img width="603" height="178" alt="Screenshot 2026-07-08 at 12 21 16 PM" src="https://github.com/user-attachments/assets/47c84769-8550-413b-8039-ab4cf3f0c425" />


#### Per-Model Usage Breakdown

A table of calls, input/output/total tokens, and average latency per model, sorted by total tokens. Gives a full side-by-side comparison across models.

<img width="644" height="71" alt="Screenshot 2026-07-08 at 12 21 42 PM" src="https://github.com/user-attachments/assets/dc58cfdb-2686-487a-bbe4-73e5fa31a30c" />


#### Tokens by Model

A pie chart showing each model's share of total tokens. Complements the trend graphs with a clear share-of-usage view.

<img width="569" height="235" alt="Screenshot 2026-07-08 at 12 21 59 PM" src="https://github.com/user-attachments/assets/3486ccc3-032d-4a66-816f-fb0e080f73d1" />


#### Tool Calls by Tool

Count of tool executions grouped by tool span name. Identifies which tools are used most.

<img width="565" height="235" alt="Screenshot 2026-07-08 at 12 22 13 PM" src="https://github.com/user-attachments/assets/8eb0735d-d504-4d2a-b6e9-d29e3aa92e89" />


#### Agent / Flow Runs Over Time

Agent invocations (`invoke_agent LangGraph`) over time. Shows run-volume patterns and traffic peaks.

<img width="595" height="164" alt="Screenshot 2026-07-08 at 12 22 45 PM" src="https://github.com/user-attachments/assets/d2899459-bb02-41d6-8fa9-900e7be39cf2" />


#### Agent Run Latency (p95)

95th-percentile latency of agent invocation spans. Tracks how long end-to-end agent runs take under load.

<img width="596" height="164" alt="Screenshot 2026-07-08 at 12 22 59 PM" src="https://github.com/user-attachments/assets/8981a900-6c0d-4d05-b7ed-f42dca65d3d4" />

