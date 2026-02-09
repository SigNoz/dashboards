# Ollama Dashboard

## Details

This dashboard offers a clear view into Ollama usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Ollama along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.

To start sending Ollama telemetry to SigNoz, follow the [Ollama monitoring guide](https://signoz.io/docs/ollama-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Ollama. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Token Usage (Over Time)

This line shows the total tokenm usage over time per service. 


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Ollama calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Request Distribution

Ollama offers multiple open srouce models, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.



#### Requests Over Time

 This chart captures the volume of requests sent to Ollama over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.



#### Request Duration (P95 Over Time)

How fast does Ollama respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.


#### Services and Languages Using Ollama

This shows where which services are leveraging Ollama and which languages the services are being instrumented with.


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.










