# Google Gemini Dashboard

## Details

This dashboard offers a clear view into Google Gemini API usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging the Gemini API, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Gemini’s API. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Gemini API calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

#### Model Distribution

Gemini offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Gemini over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

#### Latency (P95 Over Time)

How fast does Gemini respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

#### Services and Languages Using Gemini

Gemini powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.







