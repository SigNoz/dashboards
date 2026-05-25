# Hugging Face Dashboard

## Details

This dashboard offers a clear view into Hugging Face usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Hugging Face along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Hugging Face telemetry to SigNoz, follow the [Hugging Face observability guide](https://signoz.io/docs/huggingface-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Hugging Face. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="509" height="151" alt="Screenshot 2026-03-02 at 7 48 00 AM" src="https://github.com/user-attachments/assets/cabe3b94-e2ce-4f9d-83fc-b060c048eb45" />


#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="509" height="195" alt="Screenshot 2026-03-02 at 7 48 18 AM" src="https://github.com/user-attachments/assets/7be8edb9-62eb-4021-ac53-dccc2ca6da45" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Hugging Face calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="506" height="105" alt="Screenshot 2026-03-02 at 7 48 34 AM" src="https://github.com/user-attachments/assets/41e41262-987d-4e48-9079-7dbf9b819986" />


#### Model Distribution

Hugging Face offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="249" height="269" alt="Screenshot 2026-03-02 at 7 48 52 AM" src="https://github.com/user-attachments/assets/0923d6a4-d669-46a2-9b4e-6019d0388981" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="249" height="269" alt="Screenshot 2026-03-02 at 7 49 06 AM" src="https://github.com/user-attachments/assets/ad179f54-a078-4a43-b20d-98e688ed6746" />

#### Requests Over Time

 This chart captures the volume of requests sent to Hugging Face over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="507" height="191" alt="Screenshot 2026-03-02 at 7 50 03 AM" src="https://github.com/user-attachments/assets/3faef90f-11b7-4f4a-b68d-dc0d412ad9f7" />


#### Request Duration (P95 Over Time)

How fast does Hugging Face respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="476" height="191" alt="Screenshot 2026-03-02 at 7 49 33 AM" src="https://github.com/user-attachments/assets/b83551f2-de3b-4f7c-a542-0b2f1e08dae9" />

#### HTTP Request Duration (Over Time)

This chart tracks the latency of the underlying HTTP requests being made to Hugging Face LLM endpoints over time.

<img width="512" height="191" alt="Screenshot 2026-03-02 at 7 50 19 AM" src="https://github.com/user-attachments/assets/07d6a6a3-bda0-463c-b0e1-e4b1c044f106" />


#### Services and Languages Using Hugging Face

Hugging Face powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="512" height="191" alt="Screenshot 2026-03-02 at 7 50 35 AM" src="https://github.com/user-attachments/assets/1dfefcfa-4f5c-416f-ac1b-0ce15e12abac" />


#### Logs and Error Records

The Logs panel lists all Hugging Face service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="512" height="437" alt="Screenshot 2026-03-02 at 7 50 51 AM" src="https://github.com/user-attachments/assets/9a52b87c-2e5a-4d34-aa75-6136cccf20bc" />

<img width="512" height="189" alt="Screenshot 2026-03-02 at 7 51 09 AM" src="https://github.com/user-attachments/assets/71a9459b-3e99-484d-b111-f2d6d754873a" />










