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

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Distribution

Inkeep offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="351" height="437" alt="Screenshot 2025-11-18 at 10 42 43 AM" src="https://github.com/user-attachments/assets/6019b109-2fd3-4d65-92cb-a404337f7e82" />

#### Agent Distribution

This panel shows the distribution of various agents being used within Inkeep, helping you understand which agents are most active and how adoption is spread across different agent types in your implementation.

<img width="461" height="382" alt="Screenshot 2025-12-10 at 10 41 58 AM" src="https://github.com/user-attachments/assets/c5c6128f-d53d-4caa-9fd6-a45ae7ec4c0c" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Inkeep over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Agent Duration (P95 Over Time)

How fast does Inkeep respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="584" height="206" alt="Screenshot 2025-11-06 at 1 20 55 PM" src="https://github.com/user-attachments/assets/0ac8dd8c-fecb-44ed-af6d-a98253fd6e58" />


#### Logs

This panel lists all related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Additionally, custom logs can be added to your application which will show up here. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="686" height="334" alt="Screenshot 2025-12-10 at 10 41 07 AM" src="https://github.com/user-attachments/assets/4266d88a-53bc-4f5d-9b7a-c6b2ca3e82e2" />


#### Agents

This panel lists all agents called within the Inkeep execution. Each entry contains the agent name along with number of requests made to that tool and the average latency for the duration of the agent.

<img width="690" height="158" alt="Screenshot 2025-12-10 at 10 40 23 AM" src="https://github.com/user-attachments/assets/cf2b6b4d-5af7-4ddd-8179-69a938504290" />










