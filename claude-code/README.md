# Claude Code Dashboard

## Details

This comprehensive dashboard provides deep visibility into Claude Code usage patterns and performance metrics. It tracks everything from token consumption and costs to user adoption and tool effectiveness—giving teams the data they need to optimize their AI-assisted development workflows.

 Control what gets sent to SigNoz using these guides:
- Metrics: https://signoz.io/docs/userguide/drop-metrics/
- Logs: https://signoz.io/docs/logs-management/guides/drop-logs/
- Traces: https://signoz.io/docs/traces-management/guides/drop-spans/

## Dashboard panels

### Sections

### Total Token Usage (Input & Output)

Tokens are the currency of AI coding assistants. By splitting input tokens (developer prompts) and output tokens (Claude’s responses), this panel shows exactly how much work Claude is doing. Over time, you can see whether usage is ramping up, stable, or dropping off—and keep an eye on efficiency.

<img src="https://github.com/user-attachments/assets/0c0a140f-4a3d-4e82-a02e-363fb617e34a" width="400">




### Sessions and Conversations

This panel tracks how many CLI sessions and conversations are happening. Sessions show how often developers are turning to Claude, while conversations capture depth of interaction. Together, they reveal adoption and engagement.

<img src="https://github.com/user-attachments/assets/b4d4456f-c0d8-484c-8a89-26f3a0226b63" width="400" alt="claude-sessions-convos">




### Total Cost (USD)

Claude Code usage comes with a cost. This panel translates token consumption into actual dollars spent. It’s a quick way to validate ROI, spot runaway usage early, and ensure your AI assistant remains a cost-effective part of the toolchain.

<img src="https://github.com/user-attachments/assets/a1defb1d-cdff-4d07-92b1-546c5b3bcf7d" width="400" alt="claude-cost">



### Command Duration (P95)

How long do Claude-assisted commands actually take? This chart tracks the 95th percentile duration, helping you catch slowdowns, spikes, or performance regressions. Developers want Claude to be fast—this view keeps latency in check.

<img src="https://github.com/user-attachments/assets/74a32597-9f2c-487e-a3dc-147a1b0a6cc0" width="400" alt="claude-cmd-dur">



### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.

<img src="https://github.com/user-attachments/assets/6bef9f83-68c0-43d4-a401-decd0f8e7381" width="400" alt="claude-token-usg-over-time">



### Success Rate of Requests

Not every request to Claude is successful. This panel highlights how often requests succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.

<img src="https://github.com/user-attachments/assets/bf72af3d-6bbd-4551-87d6-4093cd1a9bdc" width="400" alt="claude-sucess-rate">



### Terminal Type

Claude Code is flexible, but developers use it differently depending on environment. This pie chart shows where developers are working—VS Code, Apple Terminal, or elsewhere. Great for understanding adoption across dev setups.

<img src="https://github.com/user-attachments/assets/17ebf616-3967-4e52-a9f6-5502add4e33b" width="400" alt="claude-term-type">



### Requests per User

Usage isn’t always evenly distributed. This table breaks down requests by user, making it clear who’s leaning on Claude heavily and who’s barely touching it. Perfect for identifying champions, training needs, or power users.

<img src="https://github.com/user-attachments/assets/9d9d1717-4a4c-498e-98cd-da3d4c4b7a44" width="400" alt="claude-users-reqs">



### Model Distribution

Claude ships with multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It’s a handy way to track preferences and see if newer models are gaining traction.

<img src="https://github.com/user-attachments/assets/fb6f7e2e-fe0c-40cd-9e5e-592bb5946648" width="400" alt="claude-model-distr">



### Tool Types

Claude can call on different tools—like `Read`, `Edit`, `LS`, `TodoWrite`, `Bash`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting Claude with.

<img src="https://github.com/user-attachments/assets/daea8a7b-1030-45fb-baf2-a6cc7c5fdda3" width="400" alt="claude-tool-type">



### User Decisions

AI suggestions only matter if developers use them. This panel tracks accept vs. reject decisions, showing how much developers trust Claude’s output. High acceptance is a sign of quality; high rejection is a signal to dig deeper.

<img src="https://github.com/user-attachments/assets/44050ec6-6361-4aa7-a6a7-38c652ea530a" width="400" alt="claude-user-decisions">




### Quota Usage (5-Hour Rolling Window)

Claude Code subscriptions often come with rolling quotas that reset every 5 hours. This panel tracks how much of that rolling limit has been used based on your specific subscription plan, giving you an early warning system before developers hit hard caps. Instead of being caught off guard by usage rejections, teams can proactively manage consumption and adjust workflows as they approach the threshold.

<img src="https://github.com/user-attachments/assets/3e16de44-6958-4e9d-a54e-186f98ba9c27" width="400" alt="claude-quota-usg">
