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

<img width="561" height="270" alt="Screenshot 2026-02-09 at 12 15 14 PM" src="https://github.com/user-attachments/assets/a5b5ee7f-18bd-4a0b-b022-dc13d46cb9ee" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Ollama calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Request Distribution

Ollama offers multiple open srouce models, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="275" height="270" alt="Screenshot 2026-02-09 at 12 15 37 PM" src="https://github.com/user-attachments/assets/bca95982-ec30-41ee-805a-3f0286c4329a" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="275" height="270" alt="Screenshot 2026-02-09 at 12 15 51 PM" src="https://github.com/user-attachments/assets/1b81add1-e5d5-4bf8-afca-6fb004bad0dc" />


#### Requests Over Time

 This chart captures the volume of requests sent to Ollama over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="507" height="263" alt="Screenshot 2026-02-09 at 12 16 14 PM" src="https://github.com/user-attachments/assets/14453282-38bd-4c17-8b76-0c554b5f5dca" />


#### Request Duration (P95 Over Time)

How fast does Ollama respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="507" height="263" alt="Screenshot 2026-02-09 at 12 16 31 PM" src="https://github.com/user-attachments/assets/85f21ee0-49f9-4bd0-ab5a-eaf5d510d6a7" />


#### Services and Languages Using Ollama

This shows where which services are leveraging Ollama and which languages the services are being instrumented with.

<img width="566" height="219" alt="Screenshot 2026-02-09 at 12 17 01 PM" src="https://github.com/user-attachments/assets/b77684b6-8762-49c6-bbda-4fbad20208e4" />


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="557" height="251" alt="Screenshot 2026-02-09 at 12 17 20 PM" src="https://github.com/user-attachments/assets/fdba85ac-6af8-4b90-8892-9979027fce46" />









