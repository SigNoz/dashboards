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



### Sessions and Conversations

This panel tracks how many CLI sessions and conversations are happening. Sessions show how often developers are turning to Claude, while conversations capture depth of interaction. Together, they reveal adoption and engagement.




### Total Cost (USD)

Claude Code usage comes with a cost. This panel translates token consumption into actual dollars spent. It’s a quick way to validate ROI, spot runaway usage early, and ensure your AI assistant remains a cost-effective part of the toolchain.



### Command Duration (P95)

How long do Claude-assisted commands actually take? This chart tracks the 95th percentile duration, helping you catch slowdowns, spikes, or performance regressions. Developers want Claude to be fast—this view keeps latency in check.



### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.



### Success Rate of Requests

Not every request to Claude is successful. This panel highlights how often requests succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.



### Terminal Type

Claude Code is flexible, but developers use it differently depending on environment. This pie chart shows where developers are working—VS Code, Apple Terminal, or elsewhere. Great for understanding adoption across dev setups.



### Requests per User

Usage isn’t always evenly distributed. This table breaks down requests by user, making it clear who’s leaning on Claude heavily and who’s barely touching it. Perfect for identifying champions, training needs, or power users.



### Model Distribution

Claude ships with multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It’s a handy way to track preferences and see if newer models are gaining traction.



### Tool Types

Claude can call on different tools—like `Read`, `Edit`, `LS`, `TodoWrite`, `Bash`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting Claude with.



### User Decisions

AI suggestions only matter if developers use them. This panel tracks accept vs. reject decisions, showing how much developers trust Claude’s output. High acceptance is a sign of quality; high rejection is a signal to dig deeper.



### Quota Usage (5-Hour Rolling Window)

Claude Code subscriptions often come with rolling quotas that reset every 5 hours. This panel tracks how much of that rolling limit has been used based on your specific subscription plan, giving you an early warning system before developers hit hard caps. Instead of being caught off guard by usage rejections, teams can proactively manage consumption and adjust workflows as they approach the threshold.
