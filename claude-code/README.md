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
<img src="https://github.com/user-attachments/assets/0c0a140f-4a3d-4e82-a02e-363fb617e34a" width="500">




### Sessions and Conversations

This panel tracks how many CLI sessions and conversations are happening. Sessions show how often developers are turning to Claude, while conversations capture depth of interaction. Together, they reveal adoption and engagement.
![claude-sessions-convos](https://github.com/user-attachments/assets/b4d4456f-c0d8-484c-8a89-26f3a0226b63)




### Total Cost (USD)

Claude Code usage comes with a cost. This panel translates token consumption into actual dollars spent. It’s a quick way to validate ROI, spot runaway usage early, and ensure your AI assistant remains a cost-effective part of the toolchain.
![claude-cost](https://github.com/user-attachments/assets/a1defb1d-cdff-4d07-92b1-546c5b3bcf7d)



### Command Duration (P95)

How long do Claude-assisted commands actually take? This chart tracks the 95th percentile duration, helping you catch slowdowns, spikes, or performance regressions. Developers want Claude to be fast—this view keeps latency in check.
![claude-cmd-dur](https://github.com/user-attachments/assets/74a32597-9f2c-487e-a3dc-147a1b0a6cc0)



### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.
![claude-token-usg-over-time](https://github.com/user-attachments/assets/6bef9f83-68c0-43d4-a401-decd0f8e7381)



### Success Rate of Requests

Not every request to Claude is successful. This panel highlights how often requests succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.
![claude-sucess-rate](https://github.com/user-attachments/assets/bf72af3d-6bbd-4551-87d6-4093cd1a9bdc)



### Terminal Type

Claude Code is flexible, but developers use it differently depending on environment. This pie chart shows where developers are working—VS Code, Apple Terminal, or elsewhere. Great for understanding adoption across dev setups.
![claude-term-type](https://github.com/user-attachments/assets/17ebf616-3967-4e52-a9f6-5502add4e33b)



### Requests per User

Usage isn’t always evenly distributed. This table breaks down requests by user, making it clear who’s leaning on Claude heavily and who’s barely touching it. Perfect for identifying champions, training needs, or power users.
![claude-users-reqs](https://github.com/user-attachments/assets/9d9d1717-4a4c-498e-98cd-da3d4c4b7a44)



### Model Distribution

Claude ships with multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It’s a handy way to track preferences and see if newer models are gaining traction.
![claude-model-distr](https://github.com/user-attachments/assets/fb6f7e2e-fe0c-40cd-9e5e-592bb5946648)



### Tool Types

Claude can call on different tools—like `Read`, `Edit`, `LS`, `TodoWrite`, `Bash`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting Claude with.
![claude-tool-type](https://github.com/user-attachments/assets/daea8a7b-1030-45fb-baf2-a6cc7c5fdda3)



### User Decisions

AI suggestions only matter if developers use them. This panel tracks accept vs. reject decisions, showing how much developers trust Claude’s output. High acceptance is a sign of quality; high rejection is a signal to dig deeper.
![claude-user-decisions](https://github.com/user-attachments/assets/44050ec6-6361-4aa7-a6a7-38c652ea530a)




### Quota Usage (5-Hour Rolling Window)

Claude Code subscriptions often come with rolling quotas that reset every 5 hours. This panel tracks how much of that rolling limit has been used based on your specific subscription plan, giving you an early warning system before developers hit hard caps. Instead of being caught off guard by usage rejections, teams can proactively manage consumption and adjust workflows as they approach the threshold.
![claude-quota-usg](https://github.com/user-attachments/assets/3e16de44-6958-4e9d-a54e-186f98ba9c27)
