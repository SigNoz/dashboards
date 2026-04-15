# OpenCode Dashboard

## Details

This comprehensive dashboard provides deep visibility into OpenCode usage patterns and performance metrics. It tracks everything from token consumption and costs to tool effectiveness and cache efficiency—giving teams the data they need to optimize their AI-assisted development workflows.

To start sending OpenCode telemetry to SigNoz, follow the [OpenCode monitoring guide](https://signoz.io/docs/opencode-observability/).

## Dashboard panels

### Sections

### Cost (Total)

OpenCode usage comes with a cost. This panel translates token consumption into actual dollars spent. It's a quick way to validate ROI, spot runaway usage early, and ensure your AI assistant remains a cost-effective part of the toolchain.

### Total Tokens

Tokens are the currency of AI coding assistants. This panel shows the total token consumption across all types (input, output, cache reads, and cache creation), giving you a complete picture of how much work OpenCode is doing.

### Sessions

This panel tracks how many sessions are happening. Sessions show how often developers are turning to OpenCode, revealing adoption and engagement patterns.


### Tool Calls

This panel tracks the total number of tool calls made during OpenCode sessions. It shows how actively developers are leveraging OpenCode's capabilities to interact with code, files, and development tasks.


### Tool Success

Not every tool call is successful. This panel highlights how often tool calls succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.


### Tool Calls (Distribution)

This pie chart breaks down which tools are being called most frequently. It provides visibility into the kinds of coding tasks developers are trusting OpenCode with—whether reading files, editing code, or executing commands.


### Model Distribution

OpenCode supports multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It's a handy way to track preferences and see if newer models are gaining traction.


### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.



### Cost Over Time (USD)

This panel shows cost accumulation over time, helping you track spending patterns and budget effectively. Monitor how costs trend during different development phases and identify opportunities for optimization.

### Tokens by Type

By splitting tokens by type (input tokens, output tokens, cache reads, and cache creation), this panel shows exactly how token consumption breaks down. It helps you understand efficiency patterns and cache utilization at a glance.

### Tokens by Model

This chart displays token consumption broken down by model. It reveals which models are consuming the most resources and helps you understand the cost implications of different model choices.

### Cost by Model

This panel breaks down costs by model, translating usage patterns into actual dollars spent per model. It's essential for understanding the ROI of different model tiers and making informed decisions about which models to use.



### Cache Efficiency %

This panel calculates the percentage of tokens served from cache versus fresh input tokens. High cache efficiency means lower costs and faster responses. It's a key metric for understanding how well prompt caching is working in your workflows.




### Tool Usage Frequency

OpenCode can call on different tools—like `Read`, `Glob`, `Bash`, `Write`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting OpenCode with.

