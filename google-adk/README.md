# Google ADK Dashboard

## Details

This dashboard offers a clear view into Google ADK usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, latency trends, and agent usage. Teams can also track which services and languages are leveraging Google ADK along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Google ADK telemetry to SigNoz, follow the [Google ADK monitoring guide](https://signoz.io/docs/google-adk-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Google ADK. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="704" height="277" alt="Screenshot 2026-01-05 at 10 46 44 AM" src="https://github.com/user-attachments/assets/749d4c10-f804-45cc-87f0-c3c493ec56f5" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Google ADK calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="341" height="148" alt="Screenshot 2026-01-05 at 10 47 05 AM" src="https://github.com/user-attachments/assets/b79b00b1-d889-4dd2-8a72-79ea96e23d18" />


#### Model Distribution

Google ADK offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="340" height="381" alt="Screenshot 2026-01-05 at 10 47 30 AM" src="https://github.com/user-attachments/assets/86fbdaa1-790c-4602-ad15-98488ce35940" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="349" height="393" alt="Screenshot 2026-01-05 at 10 49 52 AM" src="https://github.com/user-attachments/assets/78d6a56d-3fd2-43d5-928f-77d9e117cda1" />

#### Agent Call Distribution

This pie chart shows the distribution of total calls made by agent, to highlight which agents are being used the most by users. 


#### Number of Requests Over Time

 This chart captures the volume of requests sent to Google ADK over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.



#### Request Duration (P95 Over Time)

How fast does Google ADK respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.



#### Services and Languages Using Google ADK

Google ADK powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.



#### Logs and Error Records

The Logs panel lists all Google ADK service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










