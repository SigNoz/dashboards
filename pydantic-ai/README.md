# Pydantic AI Dashboard

## Details

This dashboard offers a clear view into Pydantic AI usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Pydantic AI, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Pydantic AI. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Pydantic AI calls that return errors. It's a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="233" height="151" alt="gemini-error-rate" src="https://github.com/user-attachments/assets/3648b04d-3370-41e0-8083-0f3fc93b54ce" />


#### Model Distribution

Pydantic AI offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="322" height="266" alt="Screenshot 2025-10-16 at 12 20 27 PM" src="https://github.com/user-attachments/assets/af09af43-d88c-4a0c-b8b8-0c2a4a4ce90d" />


#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

<img width="683" height="313" alt="gemini-token-usage" src="https://github.com/user-attachments/assets/b316a274-89f5-4452-b2e0-ea81a187a382" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Pydantic AI over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Latency (P95 Over Time)

How fast does Pydantic AI respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />

#### HTTP Request Duration (Over Time)

This panel displays a time series line chart of the average HTTP request that is being made via the LLM calls over time. This gives you insight on the network speed for the actual outbound http request to the API network. 

<img width="598" height="176" alt="Screenshot 2025-09-09 at 12 00 27 PM" src="https://github.com/user-attachments/assets/ef061331-0b4b-4e25-a50b-fe0c8a771045" />

#### Services and Languages Using Pydantic AI

Pydantic AI powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="703" height="121" alt="pydantic-services-langs" src="https://github.com/user-attachments/assets/289e39bb-d7b1-40d9-a5e8-e9e68b84d6b9" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="815" height="138" alt="pydantic-errs" src="https://github.com/user-attachments/assets/7faf9d6b-1938-4974-aebe-2b91d86079c1" />


#### API Requests

This panel lists all Pydantic AI-related API requests captured from log attributes. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="695" height="252" alt="pydantic_api_reqs" src="https://github.com/user-attachments/assets/76532c68-72f0-474a-9092-f0c7f29e419b" />


#### Agents

This table shows a list of agents deployed using Pydantic along with how many times each agent was called.

<img width="695" height="159" alt="pydantic_agents" src="https://github.com/user-attachments/assets/054fa1be-9008-418d-bde6-62b17660e07c" />

#### Tools

This table shows the list of tools executed by agents/workflows in Pydantic, along with how many times each tool was executed. 

<img width="696" height="110" alt="pydantic-tools" src="https://github.com/user-attachments/assets/f0857c07-3b4d-42b0-b923-7e188a681856" />







