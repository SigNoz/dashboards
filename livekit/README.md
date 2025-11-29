# LiveKit Dashboard

## Details

This dashboard offers a clear view into LiveKit usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging LiveKit along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of LiveKit LLM calls. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of LiveKit calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### Model Distribution

LiveKit voice agents support multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="351" height="437" alt="Screenshot 2025-11-18 at 10 42 43 AM" src="https://github.com/user-attachments/assets/6019b109-2fd3-4d65-92cb-a404337f7e82" />

#### Requests Over Time

Every API call matters. This chart captures the volume of requests sent to LiveKit over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="708" height="281" alt="gemini-requests" src="https://github.com/user-attachments/assets/4f060da9-3297-447c-89b8-730f28e39a47" />


#### Latency (P95 Over Time)

How fast does LiveKit voice agents respond under load? This panel measures the 95th percentile latency of conversations over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="708" height="281" alt="gemini-latency" src="https://github.com/user-attachments/assets/3c909491-7dfd-4a0d-8fcb-2b88cc8ff58d" />

#### HTTP Request Duration (Over Time)

This panel displays a time series line chart of the average HTTP request that is being made via the LLM calls over time. This gives you insight on the network speed for the actual outbound http request to the API network. 

<img width="598" height="176" alt="Screenshot 2025-09-09 at 12 00 27 PM" src="https://github.com/user-attachments/assets/ef061331-0b4b-4e25-a50b-fe0c8a771045" />

#### Services and Languages Using LiveKit

LiveKit powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="696" height="115" alt="Screenshot 2025-11-25 at 12 36 14 PM" src="https://github.com/user-attachments/assets/b7c2ead8-9b72-4ae0-a2e6-dc2504074fa7" />



#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="584" height="206" alt="Screenshot 2025-11-06 at 1 20 55 PM" src="https://github.com/user-attachments/assets/0ac8dd8c-fecb-44ed-af6d-a98253fd6e58" />


#### Logs

This panel lists all LiveKit-related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="696" height="417" alt="Screenshot 2025-11-25 at 12 35 49 PM" src="https://github.com/user-attachments/assets/cf0e44a1-a3bf-4b26-ab26-36610533332c" />

#### Number of Conversations Below Set Threshold Turns

This metric tracks how many conversations end before reaching a minimum number of turns, helping identify potential issues with user engagement or early drop-offs. A high count may indicate problems with the voice agent's initial responses or user experience that cause premature conversation termination.

#### Average Number of Turns Per Conversation

This panel displays the average number of back-and-forth exchanges in each conversation. It provides insight into conversation depth and user engagement—higher averages typically indicate more complex interactions, while lower averages might suggest quick transactions or potential friction points.

#### List of Conversations Below Set Threshold Turns (Trace ID)

This table provides a detailed list of specific conversations that ended before meeting the turn threshold, along with their trace IDs. Teams can click through to individual traces to investigate why these conversations were shorter than expected and identify patterns or issues requiring attention.

#### Average Latency of the TTS Over Time for the Voice Agent

Text-to-speech (TTS) latency directly impacts the conversational experience. This panel tracks the average TTS response time over time, helping you monitor voice synthesis performance, detect degradation, and ensure the voice agent maintains natural, responsive interactions.