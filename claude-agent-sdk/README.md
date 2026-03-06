# Claude Agent SDK Dashboard

## Details

This dashboard offers a clear view into the Claude Agent SDK usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Claude Agent SDK along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.
claude-agent
To start sending Claude Agent SDK telemetry to SigNoz, follow the [Claude Agent SDK monitoring guide](https://signoz.io/docs/claude-agent-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Claude Agent SDK. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="526" height="157" alt="Screenshot 2026-03-06 at 11 14 00 AM" src="https://github.com/user-attachments/assets/09db6664-48c8-4915-9d5e-e7aecb58a170" />


#### Total Token Usage (Over Time)

This line shows the total token usage over time per service. 

<img width="531" height="211" alt="Screenshot 2026-03-06 at 11 21 02 AM" src="https://github.com/user-attachments/assets/c395ec10-b309-4a50-8de8-0971f426cabb" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Claude Agent SDK calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="526" height="120" alt="Screenshot 2026-03-06 at 11 14 20 AM" src="https://github.com/user-attachments/assets/fe341c6e-69c6-45ed-9000-5ce1cf129385" />

#### Model Distribution

Claude Agent SDK offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="259" height="281" alt="Screenshot 2026-03-06 at 11 15 10 AM" src="https://github.com/user-attachments/assets/0e7a96f9-0b16-4a8c-b05a-f4e59274b970" />

#### Token Distribution by Model

This panel shows the token usage distribution by model within Claude Agent SDK.

<img width="259" height="285" alt="Screenshot 2026-03-06 at 11 15 32 AM" src="https://github.com/user-attachments/assets/41c5a63f-1586-42b9-9978-7c7acde3a0f8" />

#### Cost Distribution By Model

This panel shows the cost distribution by model within Claude Agent SDK.

<img width="259" height="287" alt="Screenshot 2026-03-06 at 11 16 52 AM" src="https://github.com/user-attachments/assets/60c16fd0-52b9-41c4-affd-e01a52037028" />

#### Cost Distribution By Service

This panel shows the cost distribution by services using Claude Agent SDK.

<img width="271" height="287" alt="Screenshot 2026-03-06 at 11 17 18 AM" src="https://github.com/user-attachments/assets/3dfc7712-5bb3-43dc-b44d-aabd657fc333" />

#### Tool Call Distribution

This panel shows the distribution of various tool calls being used within Claude Agent SDK.

<img width="519" height="203" alt="Screenshot 2026-03-06 at 11 18 07 AM" src="https://github.com/user-attachments/assets/6a1f205a-9731-48ea-8faa-b1948823ad71" />

#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Claude Agent SDK over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="519" height="203" alt="Screenshot 2026-03-06 at 11 18 28 AM" src="https://github.com/user-attachments/assets/b911aa65-3e3e-408b-9200-49fac5a8504a" />

#### Request Duration (P95 Over Time)

How fast does Claude Agent SDK respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

#### Services and Languages Using Claude Agent SDK

Claude Agent SDK powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="529" height="181" alt="Screenshot 2026-03-06 at 11 19 40 AM" src="https://github.com/user-attachments/assets/2dc319ec-ec35-49b7-aa25-14260ea4e2ee" />


#### Logs and Error Records

The Logs panel lists all Claude Agent SDK service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. The Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="531" height="444" alt="Screenshot 2026-03-06 at 11 20 29 AM" src="https://github.com/user-attachments/assets/aa7e52a6-2518-4113-aac8-a791918c87b7" />









