# OpenRouter Dashboard

## Details

This dashboard offers a clear view into OpenRouter usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging OpenRouter along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending OpenRouter telemetry to SigNoz, follow the [OpenRouter observability guide](https://signoz.io/docs/openrouter-observability/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of OpenRouter. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.


#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of OpenRouter calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.


#### Cache Utilization %

This panel shows the percentage of input tokens served from cache, helping you track cost savings. 

#### Model Distribution

OpenRouter offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.


#### Cost Distribution By Model

This panel shows the overall cost of all token usage grouped by model, allowing you to visualize which models are the most cost intensive.


#### Requests Over Time

This chart captures the volume of requests sent to OpenRouter over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.


#### Request Duration (P95 Over Time)

How fast does OpenRouter respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.









