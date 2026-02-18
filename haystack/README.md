# Haystack Dashboard

## Details

This dashboard offers a clear view into Haystack usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Haystack along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Haystack telemetry to SigNoz, follow the [Haystack observability guide](https://signoz.io/docs/haystack-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Haystack. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="520" height="163" alt="Screenshot 2026-02-17 at 10 21 36 AM" src="https://github.com/user-attachments/assets/c801b0eb-bbae-4da5-92b2-15c00b95221e" />


#### Total Token Usage (Over Time)

This chart shows the total tokenm usage over time per service. 

<img width="515" height="206" alt="Screenshot 2026-02-17 at 10 21 58 AM" src="https://github.com/user-attachments/assets/a20d8bbc-ffff-4258-99cc-cbbb44096b80" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Haystack calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="515" height="118" alt="Screenshot 2026-02-17 at 10 22 13 AM" src="https://github.com/user-attachments/assets/a99dc05d-c20e-4fac-8996-b398c4419de0" />


#### Model Distribution

Haystack offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="257" height="285" alt="Screenshot 2026-02-17 at 10 22 29 AM" src="https://github.com/user-attachments/assets/c6951447-94ef-4e27-ba01-d7bb0b55b3d3" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="257" height="285" alt="Screenshot 2026-02-17 at 10 22 42 AM" src="https://github.com/user-attachments/assets/11ce53a0-1725-4aa1-8942-ff72d35f88d4" />


#### Requests Over Time

 This chart captures the volume of requests sent to Haystack over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="512" height="202" alt="Screenshot 2026-02-17 at 10 23 03 AM" src="https://github.com/user-attachments/assets/453b5262-bafd-4b85-858c-9ec51931234a" />



#### Request Duration (P95 Over Time)

How fast does Haystack respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.


<img width="478" height="202" alt="Screenshot 2026-02-17 at 10 23 38 AM" src="https://github.com/user-attachments/assets/56188f3a-9966-4c27-a9ca-ae8db5ebc0a2" />


#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Haystack LLM endpoints over time.

<img width="512" height="202" alt="Screenshot 2026-02-17 at 10 23 18 AM" src="https://github.com/user-attachments/assets/b34ef142-27aa-4ff5-b1d5-7c3c6d2829f3" />

#### Services and Languages Using Haystack

Haystack powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="514" height="168" alt="Screenshot 2026-02-17 at 10 23 55 AM" src="https://github.com/user-attachments/assets/3554388b-cf8c-4fa0-a971-6613cbe47cd0" />


#### Logs 

The Logs panel lists all Haystack service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. 

<img width="514" height="231" alt="Screenshot 2026-02-17 at 10 24 09 AM" src="https://github.com/user-attachments/assets/b3e1b844-a9ba-4b22-8091-51378c72de2f" />


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="514" height="231" alt="Screenshot 2026-02-17 at 10 24 21 AM" src="https://github.com/user-attachments/assets/ec3adfe8-1679-45a1-8c6c-17282f00eae7" />









