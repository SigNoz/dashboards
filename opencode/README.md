# OpenCode Dashboard

## Details

This comprehensive dashboard provides deep visibility into OpenCode usage patterns and performance metrics. It tracks everything from token consumption and costs to tool effectiveness and cache efficiency—giving teams the data they need to optimize their AI-assisted development workflows.

To start sending OpenCode telemetry to SigNoz, follow the [OpenCode monitoring guide](https://signoz.io/docs/opencode-observability/).

## Dashboard panels

### Sections

### Cost (Total)

OpenCode usage comes with a cost. This panel translates token consumption into actual dollars spent. It's a quick way to validate ROI, spot runaway usage early, and ensure your AI assistant remains a cost-effective part of the toolchain.

<img width="160" height="192" alt="Screenshot 2026-04-15 at 11 09 06 AM" src="https://github.com/user-attachments/assets/d9830ad4-adef-4189-bd42-bc3765e23ce5" />


### Total Tokens

Tokens are the currency of AI coding assistants. This panel shows the total token consumption across all types (input, output, cache reads, and cache creation), giving you a complete picture of how much work OpenCode is doing.

<img width="161" height="192" alt="Screenshot 2026-04-15 at 11 09 23 AM" src="https://github.com/user-attachments/assets/f2125d27-7617-48a9-aa86-c467b6c9195d" />


### Sessions

This panel tracks how many sessions are happening. Sessions show how often developers are turning to OpenCode, revealing adoption and engagement patterns.

<img width="320" height="192" alt="Screenshot 2026-04-15 at 11 09 38 AM" src="https://github.com/user-attachments/assets/14a85bf4-2d88-4fca-988b-feb32ea2e916" />


### Tool Calls

This panel tracks the total number of tool calls made during OpenCode sessions. It shows how actively developers are leveraging OpenCode's capabilities to interact with code, files, and development tasks.

<img width="317" height="192" alt="Screenshot 2026-04-15 at 11 09 51 AM" src="https://github.com/user-attachments/assets/f529d43a-43ea-43b1-b946-4ea9e241a87c" />


### Tool Success

Not every tool call is successful. This panel highlights how often tool calls succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.

<img width="317" height="192" alt="Screenshot 2026-04-15 at 11 10 06 AM" src="https://github.com/user-attachments/assets/1be08859-ff6f-4d11-a0b4-665985496208" />


### Tool Calls (Distribution)

This pie chart breaks down which tools are being called most frequently. It provides visibility into the kinds of coding tasks developers are trusting OpenCode with—whether reading files, editing code, or executing commands.

<img width="317" height="192" alt="Screenshot 2026-04-15 at 11 10 22 AM" src="https://github.com/user-attachments/assets/ac7a99e3-ad54-48a9-a3f3-66b5ac643ccf" />


### Model Distribution

OpenCode supports multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It's a handy way to track preferences and see if newer models are gaining traction.

<img width="317" height="192" alt="Screenshot 2026-04-15 at 11 10 35 AM" src="https://github.com/user-attachments/assets/22d95aed-468c-4817-875b-825346a235af" />


### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.

<img width="481" height="164" alt="Screenshot 2026-04-15 at 11 10 50 AM" src="https://github.com/user-attachments/assets/46fa5605-6e15-44e3-a4d8-2e14c13223e9" />


### Cost Over Time (USD)

This panel shows cost accumulation over time, helping you track spending patterns and budget effectively. Monitor how costs trend during different development phases and identify opportunities for optimization.

<img width="481" height="181" alt="Screenshot 2026-04-15 at 11 11 07 AM" src="https://github.com/user-attachments/assets/7cd8a7e3-2bd3-4af6-8f7b-cc128bdec918" />


### Tokens by Type

By splitting tokens by type (input tokens, output tokens, cache reads, and cache creation), this panel shows exactly how token consumption breaks down. It helps you understand efficiency patterns and cache utilization at a glance.

<img width="481" height="181" alt="Screenshot 2026-04-15 at 11 11 22 AM" src="https://github.com/user-attachments/assets/c1334b66-e172-4e20-b3b5-d64b44fdfae9" />


### Tokens by Model

This chart displays token consumption broken down by model. It reveals which models are consuming the most resources and helps you understand the cost implications of different model choices.

<img width="481" height="181" alt="Screenshot 2026-04-15 at 11 11 45 AM" src="https://github.com/user-attachments/assets/792af385-4f34-4cea-ac22-ce441b294022" />


### Cost by Model

This panel breaks down costs by model, translating usage patterns into actual dollars spent per model. It's essential for understanding the ROI of different model tiers and making informed decisions about which models to use.

<img width="481" height="225" alt="Screenshot 2026-04-15 at 11 11 58 AM" src="https://github.com/user-attachments/assets/85206108-ede4-4157-bdd9-f78c7a8aab2b" />


### Cache Efficiency %

This panel calculates the percentage of tokens served from cache versus fresh input tokens. High cache efficiency means lower costs and faster responses. It's a key metric for understanding how well prompt caching is working in your workflows.

<img width="481" height="225" alt="Screenshot 2026-04-15 at 11 12 13 AM" src="https://github.com/user-attachments/assets/95c24c0b-d7b6-496c-aa4d-b7826d400467" />

### Tool Usage Frequency

OpenCode can call on different tools—like `Read`, `Glob`, `Bash`, `Write`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting OpenCode with.

<img width="481" height="225" alt="Screenshot 2026-04-15 at 11 12 31 AM" src="https://github.com/user-attachments/assets/8e1a19cb-dcda-401b-91d9-fbbd3030ce82" />

