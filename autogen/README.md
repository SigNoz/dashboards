# Autogen Dashboard

## Details

This dashboard offers a clear view into Autogen usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Autogen along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Autogen calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="233" height="151" alt="gemini-error-rate" src="https://github.com/user-attachments/assets/3648b04d-3370-41e0-8083-0f3fc93b54ce" />


#### Model Distribution

Autogen offers multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="352" height="287" alt="Screenshot 2025-11-06 at 1 22 15 PM" src="https://github.com/user-attachments/assets/5db019d4-a015-44fd-ae75-2b5c248e22db" />


#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to Autogen over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Latency (P95 Over Time)

How fast does Autogen respond under load? This panel measures the 95th percentile latency of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />

#### HTTP Request Duration (Over Time)

This panel displays a time series line chart of the average HTTP request that is being made via the LLM calls over time. This gives you insight on the network speed for the actual outbound http request to the API network. 

<img width="598" height="176" alt="Screenshot 2025-09-09 at 12 00 27 PM" src="https://github.com/user-attachments/assets/ef061331-0b4b-4e25-a50b-fe0c8a771045" />


#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="584" height="206" alt="Screenshot 2025-11-06 at 1 20 55 PM" src="https://github.com/user-attachments/assets/0ac8dd8c-fecb-44ed-af6d-a98253fd6e58" />


#### Logs

This panel lists all Autogen-related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="822" height="318" alt="Screenshot 2025-11-06 at 1 20 33 PM" src="https://github.com/user-attachments/assets/49a86de7-1722-4ead-91c1-a787d0ae5841" />


#### Agents

This panel lists all Agents used within the Autogen execution. Each entry contains the agent name along with number of requests made via that agent and the average latency. 

<img width="821" height="153" alt="Screenshot 2025-11-06 at 1 19 27 PM" src="https://github.com/user-attachments/assets/b6dbbace-b1d0-4a79-ab77-b176bf2107e1" />

#### Tools

This panel lists all tools called within the Autogen execution. Each entry contains the tool name along with number of requests made to that tool and the average latency. 

<img width="821" height="153" alt="Screenshot 2025-11-06 at 1 19 49 PM" src="https://github.com/user-attachments/assets/515c67fa-7366-421b-9f51-3ed70003612f" />







