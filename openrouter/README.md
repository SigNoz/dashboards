# OpenRouter Dashboard

## Details

This dashboard offers a clear view into OpenRouter usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging OpenRouter along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending OpenRouter telemetry to SigNoz, follow the [OpenRouter observability guide](https://signoz.io/docs/openrouter-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of OpenRouter. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="477" height="133" alt="Screenshot 2026-02-20 at 10 29 28 AM" src="https://github.com/user-attachments/assets/2a80ce17-159b-4c87-9a59-b55d59464953" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 

<img width="479" height="161" alt="Screenshot 2026-02-20 at 10 29 47 AM" src="https://github.com/user-attachments/assets/091e2f69-8fd3-4957-a8d7-f8b88e6865df" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of OpenRouter calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="230" height="128" alt="Screenshot 2026-02-20 at 10 30 05 AM" src="https://github.com/user-attachments/assets/90030a8e-3ddc-4aa4-812d-5ae22cf2b79e" />

#### Cache Utilization %

This panel shows the percentage of input tokens served from cache, helping you track cost savings. 

<img width="230" height="98" alt="Screenshot 2026-02-20 at 10 30 18 AM" src="https://github.com/user-attachments/assets/01db8077-a699-4b33-baf2-f395e672e636" />

#### Model Distribution

OpenRouter offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="236" height="231" alt="Screenshot 2026-02-20 at 10 30 36 AM" src="https://github.com/user-attachments/assets/e55d4966-bc58-44df-b04d-127e71bd62f8" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="236" height="231" alt="Screenshot 2026-02-20 at 10 30 48 AM" src="https://github.com/user-attachments/assets/15868d92-e09a-4259-b084-9f599515a354" />

#### Cost Distribution By Model

This panel shows the overall cost of all token usage grouped by model, allowing you to visualize which models are the most cost intensive.

<img width="236" height="231" alt="Screenshot 2026-02-20 at 10 30 59 AM" src="https://github.com/user-attachments/assets/e23dfc8f-8b91-4bc3-b9ee-4470cdcc6ff3" />

#### Requests Over Time

This chart captures the volume of requests sent to OpenRouter over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="476" height="163" alt="Screenshot 2026-02-20 at 10 31 17 AM" src="https://github.com/user-attachments/assets/d040f064-ccce-4b37-b0bb-8b121f1cd6ad" />

#### Request Duration (P95 Over Time)

How fast does OpenRouter respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="476" height="163" alt="Screenshot 2026-02-20 at 10 31 37 AM" src="https://github.com/user-attachments/assets/26f9b11b-9870-44bc-bbbd-82f86d2e91d9" />

#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="476" height="188" alt="Screenshot 2026-02-20 at 10 31 52 AM" src="https://github.com/user-attachments/assets/59acc793-c3c6-4578-894e-a2fad36148c3" />








