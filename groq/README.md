# Groq Dashboard

## Details

This dashboard offers a clear view into Groq usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Groq along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Groq telemetry to SigNoz, follow the [Groq observability guide](https://signoz.io/docs/groq-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Groq. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="692" height="224" alt="Screenshot 2026-01-20 at 10 47 39 AM" src="https://github.com/user-attachments/assets/c46df55f-51a4-42ac-82d6-1a58937a4bcf" />


#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="510" height="199" alt="Screenshot 2026-01-20 at 10 42 45 AM" src="https://github.com/user-attachments/assets/a850609c-255b-44ae-9c3e-9b07e0f8bbb4" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Groq calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="510" height="113" alt="Screenshot 2026-01-20 at 10 43 05 AM" src="https://github.com/user-attachments/assets/22015e2b-2de5-4f47-bbce-6ade1bd221b6" />

#### Model Distribution

Groq offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="345" height="379" alt="Screenshot 2026-01-20 at 10 44 08 AM" src="https://github.com/user-attachments/assets/905f97bc-6ef6-4d39-8bf6-daf4a3048624" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="345" height="379" alt="Screenshot 2026-01-20 at 10 43 46 AM" src="https://github.com/user-attachments/assets/fa746578-3d4b-44c0-acc0-5efa0feb3408" />


#### Requests Over Time

 This chart captures the volume of requests sent to Groq over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="497" height="195" alt="Screenshot 2026-01-20 at 10 44 42 AM" src="https://github.com/user-attachments/assets/3bed3776-6f1e-49de-bdbe-caabcbe08171" />


#### Request Duration (P95 Over Time)

How fast does Groq respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="472" height="195" alt="Screenshot 2026-01-20 at 10 45 07 AM" src="https://github.com/user-attachments/assets/0925a95b-039f-4145-b799-d8d08b9804dc" />


#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Groq LLM endpoints over time.

<img width="501" height="196" alt="Screenshot 2026-01-20 at 10 45 22 AM" src="https://github.com/user-attachments/assets/c9457c6e-b765-4dfe-9a8f-c5dccc00ad1d" />


#### Services and Languages Using Groq

Groq powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="501" height="140" alt="Screenshot 2026-01-20 at 10 45 36 AM" src="https://github.com/user-attachments/assets/4f168b7a-5e0a-4912-9900-632169811e43" />


#### Logs and Error Records

The Logs panel lists all Groq service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="696" height="254" alt="Screenshot 2026-01-20 at 10 47 09 AM" src="https://github.com/user-attachments/assets/217e2227-0ce1-472b-a630-9cff02d74548" />

<img width="696" height="419" alt="Screenshot 2026-01-20 at 10 46 18 AM" src="https://github.com/user-attachments/assets/c87837e4-1f27-4514-bb98-2d47a01bb3f8" />








