# Google ADK Dashboard

## Details

This dashboard offers a clear view into Google ADK usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, latency trends, and agent usage. Teams can also track which services and languages are leveraging Google ADK along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Google ADK telemetry to SigNoz, follow the [Google ADK monitoring guide](https://signoz.io/docs/google-adk-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Google ADK. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="469" height="111" alt="Screenshot 2026-01-16 at 9 17 39 AM" src="https://github.com/user-attachments/assets/9c89ff96-e2d2-4ee2-8fa2-2b3e0482d9da" />


#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="463" height="143" alt="Screenshot 2026-01-16 at 9 14 07 AM" src="https://github.com/user-attachments/assets/cc1b6c15-cf7d-4d0a-a74a-b430a2dd810e" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Google ADK calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="341" height="148" alt="Screenshot 2026-01-05 at 10 47 05 AM" src="https://github.com/user-attachments/assets/b79b00b1-d889-4dd2-8a72-79ea96e23d18" />


#### Model Distribution

Google ADK offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="226" height="199" alt="Screenshot 2026-01-16 at 9 14 27 AM" src="https://github.com/user-attachments/assets/8497aa77-051b-4de0-bf57-cd640e980c51" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="226" height="199" alt="Screenshot 2026-01-16 at 9 14 40 AM" src="https://github.com/user-attachments/assets/f497356b-8b5d-4a2c-8ee2-2e86b8d3103e" />


#### Agent Call Distribution

This pie chart shows the distribution of total calls made by agent, to highlight which agents are being used the most by users. 

<img width="226" height="199" alt="Screenshot 2026-01-16 at 9 14 55 AM" src="https://github.com/user-attachments/assets/d13a41a1-84b8-4345-9b06-9f84b8573200" />


#### Number of Requests Over Time

 This chart captures the volume of requests sent to Google ADK over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="461" height="142" alt="Screenshot 2026-01-16 at 9 15 10 AM" src="https://github.com/user-attachments/assets/d4ec46de-79c6-4034-8e22-5e8aaf2be418" />


#### Request Duration (P95 Over Time)

How fast does Google ADK respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="461" height="127" alt="Screenshot 2026-01-16 at 9 16 55 AM" src="https://github.com/user-attachments/assets/eede0641-ef3e-420f-a96a-4a4e1e5e4a66" />



#### Services and Languages Using Google ADK

Google ADK powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="461" height="112" alt="Screenshot 2026-01-16 at 9 15 50 AM" src="https://github.com/user-attachments/assets/2289b42f-86d6-48da-a809-683e8c814e23" />


#### Logs and Error Records

The Logs panel lists all Google ADK service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










