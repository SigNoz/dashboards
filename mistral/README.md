# Mistral AI Dashboard

## Details

This dashboard offers a clear view into Mistral AI usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging itral along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Mistral telemetry to SigNoz, follow the [Mistral observability guide](https://signoz.io/docs/mistral-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Mistral. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="535" height="159" alt="Screenshot 2026-03-16 at 11 48 56 AM" src="https://github.com/user-attachments/assets/78a06849-64d7-4730-b86b-13903aee3ceb" />


#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="535" height="198" alt="Screenshot 2026-03-16 at 11 49 09 AM" src="https://github.com/user-attachments/assets/1258a098-46e4-45a2-b1aa-83909995a2b4" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Mistral calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="535" height="114" alt="Screenshot 2026-03-16 at 11 49 23 AM" src="https://github.com/user-attachments/assets/1df38ea9-2e31-42d5-9c11-04b94a2f2661" />


#### Model Distribution

Mistral offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="258" height="285" alt="Screenshot 2026-03-16 at 11 49 40 AM" src="https://github.com/user-attachments/assets/7c38a8f8-c3fe-4b28-b930-be6ea8dbe61b" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="258" height="285" alt="Screenshot 2026-03-16 at 11 49 52 AM" src="https://github.com/user-attachments/assets/d4e5b29c-1577-4794-9422-e90221b35c6b" />


#### Requests Over Time

This chart captures the volume of requests sent to Mistral over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="536" height="201" alt="Screenshot 2026-03-16 at 11 50 11 AM" src="https://github.com/user-attachments/assets/98ec5b49-1667-41bc-a8d5-8de6e85c00a0" />


#### Request Duration (P95 Over Time)

How fast does Mistral respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="536" height="201" alt="Screenshot 2026-03-16 at 11 50 24 AM" src="https://github.com/user-attachments/assets/956c1cd0-8889-4b29-a818-33804642640d" />


#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Mistral LLM endpoints over time.

<img width="536" height="201" alt="Screenshot 2026-03-16 at 11 50 38 AM" src="https://github.com/user-attachments/assets/32dc9a6a-967b-4007-bad9-d8fcd9cb47aa" />


#### Services and Languages Using Mistral

Mistral powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="536" height="176" alt="Screenshot 2026-03-16 at 11 50 53 AM" src="https://github.com/user-attachments/assets/4fb8c917-49d2-415c-afea-8749e9c7ba57" />


#### Logs and Error Records

The Logs panel lists all Mistral service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="536" height="199" alt="Screenshot 2026-03-16 at 11 51 12 AM" src="https://github.com/user-attachments/assets/d47402d3-2918-4942-b3fb-6c83f8fd2f76" />

<img width="536" height="242" alt="Screenshot 2026-03-16 at 11 51 23 AM" src="https://github.com/user-attachments/assets/ea3dbb60-28cb-45f2-803b-eaaceebe8e6e" />










