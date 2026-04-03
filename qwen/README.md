# Qwen Dashboard

## Details

This dashboard offers a clear view into Qwen usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging itral along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Qwen telemetry to SigNoz, follow the [Qwen observability guide](https://signoz.io/docs/qwen-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Qwen. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="560" height="173" alt="Screenshot 2026-04-01 at 11 23 30 AM" src="https://github.com/user-attachments/assets/95532737-2c69-460a-a2dd-fb53ea615bdd" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="560" height="220" alt="Screenshot 2026-04-01 at 11 23 51 AM" src="https://github.com/user-attachments/assets/df433cce-c6a7-439b-9fdf-36852d61aede" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Qwen calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="560" height="129" alt="Screenshot 2026-04-01 at 11 24 08 AM" src="https://github.com/user-attachments/assets/a78a3046-b6ee-49f3-ac35-a404c6ebbe99" />

#### Model Distribution

Qwen offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="273" height="296" alt="Screenshot 2026-04-01 at 11 24 35 AM" src="https://github.com/user-attachments/assets/2a1e3549-1ceb-443d-ae94-3579c683e2de" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="282" height="303" alt="Screenshot 2026-04-01 at 11 24 57 AM" src="https://github.com/user-attachments/assets/3342de58-21c4-4ab0-99dd-3bab1c390143" />


#### Requests Over Time

This chart captures the volume of requests sent to Qwen over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="564" height="212" alt="Screenshot 2026-04-01 at 11 25 26 AM" src="https://github.com/user-attachments/assets/e9fe51d0-0310-441c-a6af-cdf3f2a590f4" />


#### Request Duration (P95 Over Time)

How fast does Qwen respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="564" height="212" alt="Screenshot 2026-04-01 at 11 25 47 AM" src="https://github.com/user-attachments/assets/8e6692e6-905c-4407-b8b0-268a34dd5350" />


#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Qwen LLM endpoints over time.

<img width="564" height="212" alt="Screenshot 2026-04-01 at 11 26 05 AM" src="https://github.com/user-attachments/assets/39c26b3f-06a8-4616-9b6c-3862a8756472" />


#### Services and Languages Using Qwen

Qwen powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="1131" height="162" alt="Screenshot 2026-04-01 at 11 26 31 AM" src="https://github.com/user-attachments/assets/b29924ac-d238-4961-ba9b-4534264a17ea" />


#### Logs and Error Records

The Logs panel lists all Qwen service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="1131" height="260" alt="Screenshot 2026-04-01 at 11 26 54 AM" src="https://github.com/user-attachments/assets/f658e321-a7bc-4951-a1d7-4ef56fb10897" />










