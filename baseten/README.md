# Baseten Dashboard

## Details

This dashboard offers a clear view into Baseten usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging itral along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Baseten telemetry to SigNoz, follow the [Baseten observability guide](https://signoz.io/docs/baseten-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Baseten. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="451" height="128" alt="Screenshot 2026-04-08 at 11 01 48 AM" src="https://github.com/user-attachments/assets/370119cb-7f2d-410a-8714-0a1b7a99b6fc" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="451" height="174" alt="Screenshot 2026-04-08 at 11 02 11 AM" src="https://github.com/user-attachments/assets/4a654898-2e03-449c-91ab-8293118bf025" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Baseten calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="451" height="109" alt="Screenshot 2026-04-08 at 11 02 34 AM" src="https://github.com/user-attachments/assets/dda7caea-b18c-47b5-828b-e51a1ab7c5ca" />


#### Model Distribution

Baseten offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="220" height="239" alt="Screenshot 2026-04-08 at 11 03 12 AM" src="https://github.com/user-attachments/assets/708b23a9-1c14-4374-ad84-a8d46582e9e2" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="220" height="244" alt="Screenshot 2026-04-08 at 11 03 57 AM" src="https://github.com/user-attachments/assets/dec3813a-dff7-4782-9cad-1fd5ec329dba" />


#### Requests Over Time

This chart captures the volume of requests sent to Baseten over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="447" height="167" alt="Screenshot 2026-04-08 at 11 04 27 AM" src="https://github.com/user-attachments/assets/4894839b-cb64-4c3a-be52-b987ada87f35" />


#### Request Duration (P95 Over Time)

How fast does Baseten respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="446" height="167" alt="Screenshot 2026-04-08 at 11 05 51 AM" src="https://github.com/user-attachments/assets/213e56d8-474e-46a9-ae57-8d42c8cce6a4" />


#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Baseten LLM endpoints over time.

<img width="446" height="167" alt="Screenshot 2026-04-08 at 11 05 23 AM" src="https://github.com/user-attachments/assets/4488bcb1-ee29-4681-944d-091e5d8dfcef" />


#### Services and Languages Using Baseten

Baseten powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="908" height="140" alt="Screenshot 2026-04-08 at 11 06 23 AM" src="https://github.com/user-attachments/assets/c516885f-8100-492e-9ae0-f2bccd18303b" />


#### Logs and Error Records

The Logs panel lists all Baseten service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="908" height="210" alt="Screenshot 2026-04-08 at 11 06 47 AM" src="https://github.com/user-attachments/assets/23ccc652-2185-4f5c-946e-674f74634975" />









