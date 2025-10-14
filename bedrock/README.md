# Amazon Bedrock Dashboard

## Details

This dashboard offers a clear view into Bedrock usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Bedrock, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Bedrock's API. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />



#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Bedrock calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="233" height="151" alt="gemini-error-rate" src="https://github.com/user-attachments/assets/3648b04d-3370-41e0-8083-0f3fc93b54ce" />



#### Model Distribution

Amazon Bedrock offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="364" height="379" alt="bedrock-models" src="https://github.com/user-attachments/assets/ccfce9cf-820a-4fd1-8974-e1511c4f5e0e" />




#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

<img width="473" height="212" alt="bedrock-token-usg" src="https://github.com/user-attachments/assets/db1a00a2-e751-4da5-8202-6946c8ef024f" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Bedrock over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="585" height="212" alt="bedrock-num-reqs" src="https://github.com/user-attachments/assets/2999df5d-d314-4534-8d66-f1d3999239cd" />


#### Latency (P95 Over Time)

How fast does Bedrock respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="473" height="212" alt="bedrock-latency" src="https://github.com/user-attachments/assets/fc7357bb-9c40-4cb1-823c-268010b27429" />

#### Services and Languages Using Bedrock

Bedrock powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="696" height="122" alt="bedrock-services-langs" src="https://github.com/user-attachments/assets/f4a65ca8-2f85-442c-987b-00ecb0575cd5" />

#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="812" height="301" alt="bedrock-errors" src="https://github.com/user-attachments/assets/340beb48-1421-407b-b5d6-47ba9c4dec94" />

#### Logs

This panel lists all Bedrock-related captured from logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="576" height="250" alt="bedrock-logs-panel" src="https://github.com/user-attachments/assets/339b52f7-b07d-4468-a4a4-8e20d5b7279c" />









