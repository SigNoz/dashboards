# xAi Grok Dashboard

## Details

This dashboard offers a clear view into xAi Grok usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Grok along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Grok telemetry to SigNoz, follow the [Grok monitoring guide](https://signoz.io/docs/grok-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Grok. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="678" height="270" alt="Screenshot 2025-12-30 at 10 53 11 AM" src="https://github.com/user-attachments/assets/d8692f2d-73cd-48eb-9a10-a9cf4f409395" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Grok calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Distribution

Grok offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="335" height="370" alt="Screenshot 2025-12-30 at 10 51 35 AM" src="https://github.com/user-attachments/assets/584eeed9-7d5e-4e1c-956d-7da6bd7556a5" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="335" height="377" alt="Screenshot 2025-12-30 at 10 51 57 AM" src="https://github.com/user-attachments/assets/870e90a8-3fa9-43d9-863f-246addfcf8b4" />


#### Cache Utilization Rate
Caching can dramatically reduce costs and latency by reusing previous responses. This chart tracks how effectively your cache is currently being utilized.

<img width="335" height="150" alt="Screenshot 2025-12-30 at 10 52 14 AM" src="https://github.com/user-attachments/assets/1e2170dd-5135-43de-8819-8a9c9b385c8e" />


#### Cache Utilization Rate (Over Time)
This chart tracks how effectively your cache is being utilized over time.

<img width="678" height="210" alt="Screenshot 2025-12-30 at 10 52 33 AM" src="https://github.com/user-attachments/assets/990b4e18-33cd-460b-abe1-dcffea091900" />


#### Requests Over Time

 This chart captures the volume of requests sent to Grok over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="678" height="270" alt="Screenshot 2025-12-30 at 10 53 50 AM" src="https://github.com/user-attachments/assets/6fca0b3a-32bc-446d-9c2c-80c8a5d8da4a" />


#### Request Duration (P95 Over Time)

How fast does Grok respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="678" height="270" alt="Screenshot 2025-12-30 at 10 54 10 AM" src="https://github.com/user-attachments/assets/4cd92d52-6c97-4109-9f3e-07500cd84e5a" />



#### Services and Languages Using Grok

Grok powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="678" height="199" alt="Screenshot 2025-12-30 at 10 54 26 AM" src="https://github.com/user-attachments/assets/7ee926d9-5a82-40b2-9275-41f84d720025" />


#### Logs and Error Records

The Logs panel lists all Grok service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










