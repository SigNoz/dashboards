# Claude Agent SDK Dashboard

## Details

This dashboard offers a clear view into the Claude Agent SDK usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Claude Agent SDK along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.
claude-agent
To start sending Claude Agent SDK telemetry to SigNoz, follow the [Claude Agent SDK monitoring guide](https://signoz.io/docs/claude-agent-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Claude Agent SDK. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.


#### Total Token Usage (Over Time)

This line shows the total token usage over time per service. 


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Claude Agent SDK calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.


#### Model Distribution

Claude Agent SDK offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

#### Token Distribution by Model

This panel shows the token usage distribution by model within Claude Agent SDK.

#### Cost Distribution By Model

This panel shows the cost distribution by model within Claude Agent SDK.

#### Cost Distribution By Service

This panel shows the cost distribution by services using Claude Agent SDK.

#### Tool Call Distribution

This panel shows the distribution of various tool calls being used within Claude Agent SDK.


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Claude Agent SDK over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.



#### Request Duration (P95 Over Time)

How fast does Claude Agent SDK respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.



#### Services and Languages Using Claude Agent SDK

Claude Agent SDK powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.



#### Logs and Error Records

The Logs panel lists all Claude Agent SDK service related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability. The Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










