# Inkeep Dashboard

## Details

This dashboard offers a clear view into Inkeep usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Inkeep along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Inkeep telemetry to SigNoz, follow the [Inkeep monitoring guide](https://signoz.io/docs/inkeep-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Inkeep. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Inkeep calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="348" height="158" alt="Screenshot 2025-12-17 at 1 53 52 PM" src="https://github.com/user-attachments/assets/c5f95168-0621-4165-871f-e1498c49af83" />

#### Model Distribution

Inkeep offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="348" height="375" alt="Screenshot 2025-12-17 at 1 54 26 PM" src="https://github.com/user-attachments/assets/4438b990-b99d-4cd3-87ab-55363c9b0ca9" />

#### Agent Distribution

This panel shows the distribution of various agents being used within Inkeep, helping you understand which agents are most active and how adoption is spread across different agent types in your implementation.

<img width="348" height="375" alt="Screenshot 2025-12-17 at 1 54 56 PM" src="https://github.com/user-attachments/assets/2d385b05-13af-40e2-8908-770436994725" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Inkeep over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Agent Duration (P95 Over Time)

How fast does Inkeep respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="701" height="365" alt="Screenshot 2025-12-17 at 1 56 15 PM" src="https://github.com/user-attachments/assets/9c8ef8da-c570-41b7-9016-55c6f4272b0f" />


#### Agents

This panel lists all agents called within the Inkeep execution. Each entry contains the agent name along with number of requests made to that tool and the average latency for the duration of the agent.

<img width="580" height="220" alt="Screenshot 2025-12-17 at 1 55 28 PM" src="https://github.com/user-attachments/assets/129ed7b1-e213-41e1-8e7f-5a0fe3051759" />











