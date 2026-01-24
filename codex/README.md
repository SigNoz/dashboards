# OpenAI Codex Dashboard

## Details

This comprehensive dashboard provides deep visibility into OpenAI Codex usage patterns and performance metrics. It tracks everything from token consumption and costs to user adoption and tool effectiveness, giving teams the data they need to optimize their AI-assisted development workflows.

To start sending OpenAI Codex telemetry to SigNoz, follow the [Codex monitoring guide](https://signoz.io/docs/codex-monitoring/).

## Dashboard panels

### Sections

### Total Token Usage (Input & Output)

Tokens are the currency of AI coding assistants. By splitting input tokens (developer prompts) and output tokens (Codex’s responses), this panel shows exactly how much work Codex is doing. Over time, you can see whether usage is ramping up, stable, or dropping off—and keep an eye on efficiency.

<img width="468" height="109" alt="Screenshot 2026-01-23 at 9 02 16 AM" src="https://github.com/user-attachments/assets/f422add3-f649-4a9a-935e-4e24d84fb1d6" />


### Cached Tokens

Cached tokens show how much of the prompt or context was served from cache instead of recomputed. Higher cached usage usually means faster responses and lower costs.

<img width="229" height="101" alt="Screenshot 2026-01-23 at 9 02 37 AM" src="https://github.com/user-attachments/assets/568e5ad5-6ae6-4ce0-aab4-1f68a033c837" />


### Cache Utlization Rate

This measures the percentage of total tokens that were cached. It’s a quick health check for whether caching is working as expected and improving efficiency.

<img width="229" height="101" alt="Screenshot 2026-01-23 at 9 02 54 AM" src="https://github.com/user-attachments/assets/88462691-b6ab-40f3-ac55-ceb53607c48b" />


### Sessions and Model Calls

This panel tracks how many conversations and model calls are happening. Conversations show how often developers are turning to Codex, while model calls capture depth of interaction. Together, they reveal adoption and engagement.


<img width="460" height="101" alt="Screenshot 2026-01-23 at 9 03 17 AM" src="https://github.com/user-attachments/assets/05066450-ad90-4b3a-a3f9-9cc2cdf994bc" />


### Command Duration (P95)

How long do Codex-assisted commands actually take? This chart tracks the 95th percentile duration, helping you catch slowdowns, spikes, or performance regressions. Developers want Codex to be fast—this view keeps latency in check.

<img width="700" height="322" alt="Screenshot 2026-01-23 at 9 09 16 AM" src="https://github.com/user-attachments/assets/4bb03789-e6f2-4ed6-8669-ccfe7d10ae39" />



### Token Usage Over Time

Instead of looking at total tokens in a snapshot, this time series shows usage trends. Are developers spiking usage during sprints? Is there a steady upward adoption curve? This view is perfect for spotting both growth and anomalies.

<img width="687" height="313" alt="Screenshot 2026-01-23 at 9 04 09 AM" src="https://github.com/user-attachments/assets/bd8193eb-8bc1-4ce9-8721-7165d3df3998" />


### Number of Conversations Over Time

This trend line shows how many conversations are happening over time. It helps you see adoption growth, seasonal spikes, or drop-offs.

<img width="687" height="313" alt="Screenshot 2026-01-23 at 9 04 42 AM" src="https://github.com/user-attachments/assets/1457d4e5-84dc-40a4-a4db-60f94ec2d589" />


### Success Rate of Requests

Not every request to Codex is successful. This panel highlights how often requests succeed vs. fail, helping you spot reliability issues—whether from the model, connectivity, or developer inputs. A healthy success rate means smooth workflows.

<img width="340" height="322" alt="Screenshot 2026-01-23 at 9 05 02 AM" src="https://github.com/user-attachments/assets/4d3e0901-09d8-4dd1-a0cd-34f3ab8a2abe" />



### Terminal Type

OpenAI Codex is flexible, but developers use it differently depending on environment. This pie chart shows where developers are working—VS Code, Apple Terminal, or elsewhere. Great for understanding adoption across dev setups.

<img width="344" height="322" alt="Screenshot 2026-01-23 at 9 05 26 AM" src="https://github.com/user-attachments/assets/5d7d2fe4-e807-4716-b185-e5251a313743" />



### Requests per User

Usage isn’t always evenly distributed. This chart breaks down requests by user, making it clear who’s leaning on Codex heavily and who’s barely touching it. Perfect for identifying champions, training needs, or power users.

<img width="329" height="322" alt="user-distr-codex" src="https://github.com/user-attachments/assets/9f720080-75ee-46f2-81d0-09d295acae3f" />


### Model Distribution

Codex ships with multiple models, and not all usage is equal. This panel shows which models developers are actually calling. It’s a handy way to track preferences and see if newer models are gaining traction.

<img width="344" height="322" alt="Screenshot 2026-01-23 at 9 06 27 AM" src="https://github.com/user-attachments/assets/cf1f2805-509f-47ef-b07f-19997cd7cb89" />


### Token Distribution By Model

This panel breaks down token usage by model, not just request counts. It shows which models consume the most tokens and drive the majority of cost.

<img width="344" height="322" alt="Screenshot 2026-01-23 at 9 06 45 AM" src="https://github.com/user-attachments/assets/67deeb3a-9fb1-44cd-acf3-fc00ddce6d2f" />


### Tool Types

Codex can call on different tools—like `shell_comman`, `apply_patch`, and more. This breakdown shows which tools are most frequently used, shining a light on the kinds of coding tasks developers are trusting Codex with.

<img width="344" height="322" alt="Screenshot 2026-01-23 at 9 07 02 AM" src="https://github.com/user-attachments/assets/00b7216e-f859-4062-a964-8cc13ea892d2" />



### User Decisions

AI suggestions only matter if developers use them. This panel tracks accept vs. reject decisions, showing how much developers trust Codex’s output. High acceptance is a sign of quality; high rejection is a signal to dig deeper.

<img width="344" height="322" alt="Screenshot 2026-01-23 at 9 07 18 AM" src="https://github.com/user-attachments/assets/b82c49d8-6812-4256-8207-5af44007940d" />

