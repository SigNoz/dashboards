# OpenAI Dashboard

## Details

This dashboard offers a clear view into OpenAI usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging OpenAI along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending OpenAI telemetry to SigNoz, follow the [OpenAI monitoring guide](https://signoz.io/docs/openai-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of OpenAI. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="704" height="277" alt="Screenshot 2026-01-05 at 10 46 44 AM" src="https://github.com/user-attachments/assets/749d4c10-f804-45cc-87f0-c3c493ec56f5" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of OpenAI calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="341" height="148" alt="Screenshot 2026-01-05 at 10 47 05 AM" src="https://github.com/user-attachments/assets/b79b00b1-d889-4dd2-8a72-79ea96e23d18" />


#### Model Distribution

OpenAI offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="340" height="381" alt="Screenshot 2026-01-05 at 10 47 30 AM" src="https://github.com/user-attachments/assets/86fbdaa1-790c-4602-ad15-98488ce35940" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="349" height="393" alt="Screenshot 2026-01-05 at 10 49 52 AM" src="https://github.com/user-attachments/assets/78d6a56d-3fd2-43d5-928f-77d9e117cda1" />



#### Cache Utilization Rate
Caching can dramatically reduce costs and latency by reusing previous responses. This chart tracks how effectively your cache is currently being utilized.

<img width="335" height="150" alt="Screenshot 2025-12-30 at 10 52 14 AM" src="https://github.com/user-attachments/assets/1e2170dd-5135-43de-8819-8a9c9b385c8e" />


#### Cache Utilization Rate (Over Time)
This chart tracks how effectively your cache is being utilized over time.

<img width="678" height="210" alt="Screenshot 2025-12-30 at 10 52 33 AM" src="https://github.com/user-attachments/assets/990b4e18-33cd-460b-abe1-dcffea091900" />


#### Requests Over Time

 This chart captures the volume of requests sent to OpenAI over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="652" height="264" alt="Screenshot 2026-01-05 at 10 48 48 AM" src="https://github.com/user-attachments/assets/46167713-6c96-4489-929f-54ea3e15ada4" />


#### Request Duration (P95 Over Time)

How fast does OpenAI respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="652" height="264" alt="Screenshot 2026-01-05 at 10 48 30 AM" src="https://github.com/user-attachments/assets/e2e6d6e6-1e7f-4a67-a7eb-4582a9d57fc6" />



#### Services and Languages Using OpenAI

OpenAI powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="685" height="156" alt="Screenshot 2026-01-05 at 10 49 11 AM" src="https://github.com/user-attachments/assets/7cd9e430-9135-4dcb-abac-9a397e7bb9de" />



#### Logs and Error Records

The Logs panel lists all OpenAI service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










