# Deepseek API Dashboard

## Details

This dashboard offers a clear view into Deepseek API usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging the Deepseek API, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Deepseek’s API. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />



#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Deepseek API calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="233" height="151" alt="gemini-error-rate" src="https://github.com/user-attachments/assets/3648b04d-3370-41e0-8083-0f3fc93b54ce" />



#### Model Distribution

Deepseek offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="357" height="292" alt="Screenshot 2025-09-14 at 10 27 40 AM" src="https://github.com/user-attachments/assets/f7dea5a3-cb27-4f47-bdf3-296ab62911fa" />



#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

<img width="683" height="313" alt="gemini-token-usage" src="https://github.com/user-attachments/assets/b316a274-89f5-4452-b2e0-ea81a187a382" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Deepseek over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Latency (P95 Over Time)

How fast does Deepseek respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />

#### HTTP Request Duration (Over Time)

This panel displays a time series line chart of the average HTTP request that is being made via the LLM calls over time. This gives you insight on the network speed for the actual outbound http request to the Google API network. 

<img width="598" height="176" alt="Screenshot 2025-09-09 at 12 00 27 PM" src="https://github.com/user-attachments/assets/ef061331-0b4b-4e25-a50b-fe0c8a771045" />

#### Services and Languages Using Deepseek

Deepseek powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="701" height="114" alt="Screenshot 2025-09-14 at 10 34 23 AM" src="https://github.com/user-attachments/assets/8662107f-4844-4733-a219-818744848624" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="820" height="309" alt="Screenshot 2025-09-14 at 10 34 44 AM" src="https://github.com/user-attachments/assets/df93ded3-70c0-468c-9988-1c7753b9b3b7" />


#### API Requests

This panel lists all Deepseek-related API requests captured from log attributes. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="701" height="251" alt="Screenshot 2025-09-14 at 10 30 06 AM" src="https://github.com/user-attachments/assets/6844be0d-e3be-4986-a9ca-de2ef8d8665b" />









