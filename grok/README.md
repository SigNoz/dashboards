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

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Grok calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Distribution

Grok offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="351" height="437" alt="Screenshot 2025-11-18 at 10 42 43 AM" src="https://github.com/user-attachments/assets/6019b109-2fd3-4d65-92cb-a404337f7e82" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

#### Cache Utilization Rate
Caching can dramatically reduce costs and latency by reusing previous responses. This chart tracks how effectively your cache is currently being utilized.

#### Cache Utilization Rate (Over Time)
This chart tracks how effectively your cache is being utilized over time.


#### Requests Over Time

 This chart captures the volume of requests sent to Grok over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Request Duration (P95 Over Time)

How fast does Grok respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />


#### Services and Languages Using Grok

Grok powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="686" height="122" alt="Screenshot 2025-12-10 at 10 41 32 AM" src="https://github.com/user-attachments/assets/5bcd4c4c-2394-4e47-ab5b-50ca8e2b0711" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="584" height="206" alt="Screenshot 2025-11-06 at 1 20 55 PM" src="https://github.com/user-attachments/assets/0ac8dd8c-fecb-44ed-af6d-a98253fd6e58" />


#### Logs

This panel lists all Grok service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="686" height="334" alt="Screenshot 2025-12-10 at 10 41 07 AM" src="https://github.com/user-attachments/assets/4266d88a-53bc-4f5d-9b7a-c6b2ca3e82e2" />











