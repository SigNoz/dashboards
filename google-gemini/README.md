# Google Gemini Dashboard

## Details

This dashboard offers a clear view into Google Gemini API usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging the Gemini API, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Gemini’s API. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />



#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Gemini API calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="233" height="151" alt="gemini-error-rate" src="https://github.com/user-attachments/assets/3648b04d-3370-41e0-8083-0f3fc93b54ce" />



#### Model Distribution

Gemini offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="466" height="277" alt="gemini-model-distr" src="https://github.com/user-attachments/assets/d1f90ae7-93e7-484f-88d8-d55a77d8d00e" />


#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

<img width="683" height="313" alt="gemini-token-usage" src="https://github.com/user-attachments/assets/b316a274-89f5-4452-b2e0-ea81a187a382" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Gemini over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Latency (P95 Over Time)

How fast does Gemini respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />


#### Services and Languages Using Gemini

Gemini powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="708" height="138" alt="gemini-services" src="https://github.com/user-attachments/assets/7ef5f513-3581-4966-b1a0-e37b25f801a7" />



#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="708" height="252" alt="gemini-errors" src="https://github.com/user-attachments/assets/e9a4c0c1-71f2-4cd5-b565-2a6c93afa975" />









