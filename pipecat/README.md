# Pipecat Dashboard

## Details

This dashboard offers a clear view into Pipecat usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging Pipecat along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of Pipecat LLM calls. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of Pipecat calls that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="350" height="211" alt="Screenshot 2025-11-06 at 1 23 22 PM" src="https://github.com/user-attachments/assets/5519d275-deff-45ae-9330-875dd887a9cd" />

#### LLM Model Distribution

Pipecat voice agents support multiple model variants, each optimized for different tasks. This panel reveals which models are being called most often—helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="351" height="437" alt="Screenshot 2025-11-18 at 10 42 43 AM" src="https://github.com/user-attachments/assets/6019b109-2fd3-4d65-92cb-a404337f7e82" />

#### STT Model Distribution

Speech-to-text (STT) models convert user voice input into text that the voice agent can process. This panel shows the distribution of STT models being used across your Pipecat applications, helping you understand which speech recognition providers are most popular and track the adoption of different STT services for various use cases.

<img width="347" height="286" alt="Screenshot 2025-12-02 at 10 24 40 AM" src="https://github.com/user-attachments/assets/8167373d-022b-4604-9512-b12d56c690df" />


#### TTS Model Distribution

Text-to-speech (TTS) models transform the agent's text responses into natural-sounding voice output. This panel displays which TTS models and voices are being utilized most frequently, enabling you to monitor voice synthesis preferences, evaluate the adoption of different voice providers, and optimize for quality and cost considerations.

<img width="347" height="286" alt="Screenshot 2025-12-02 at 10 24 56 AM" src="https://github.com/user-attachments/assets/806fd363-0e05-452f-b280-cc1169e0ce2e" />


#### Conversations Over Time

This chart captures the volume of conversations with Pipecat voice agents over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="570" height="213" alt="Screenshot 2025-11-28 at 6 11 24 PM" src="https://github.com/user-attachments/assets/c3f0f34c-2d58-4f4d-bf37-30653cb207ed" />


#### Agent Turn Latency(Over Time)

This panel tracks the average time it takes the agent to complete its turn turn over time. Monitoring turn latency helps identify performance bottlenecks in the voice agent pipeline, detect degradation trends, and ensure smooth, responsive conversational experiences.

<img width="572" height="230" alt="Screenshot 2025-12-02 at 10 25 25 AM" src="https://github.com/user-attachments/assets/5a81ade5-e40e-4929-bd6d-5da555eaaa04" />

#### HTTP Request Duration (Over Time)

This panel displays a time series line chart of the average HTTP request that is being made via the LLM calls over time. This gives you insight on the network speed for the actual outbound http request to the API network. 

<img width="598" height="176" alt="Screenshot 2025-09-09 at 12 00 27 PM" src="https://github.com/user-attachments/assets/ef061331-0b4b-4e25-a50b-fe0c8a771045" />

#### Services and Languages Using Pipecat

Pipecat powers a variety of applications across different services and programming languages. This breakdown shows where the API is being adopted—making it easier to understand usage patterns across your stack and identify opportunities for optimization.

<img width="700" height="118" alt="Screenshot 2025-12-02 at 10 26 24 AM" src="https://github.com/user-attachments/assets/18266764-e089-4402-bfb0-a4242063a7fb" />

#### Error Records

This table logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="584" height="206" alt="Screenshot 2025-11-06 at 1 20 55 PM" src="https://github.com/user-attachments/assets/0ac8dd8c-fecb-44ed-af6d-a98253fd6e58" />


#### Logs

This panel lists all Pipecat related logs. Teams can use this for deep troubleshooting, auditing usage patterns, and correlating issues with specific request flows. Clicking on a row links back to the corresponding log entry for full traceability.

<img width="700" height="166" alt="Screenshot 2025-12-02 at 10 27 32 AM" src="https://github.com/user-attachments/assets/f86cebab-ab59-4863-88ad-66518c5a635f" />


#### Number of Conversations Below Set Turn Threshold

This metric tracks how many conversations end before reaching a minimum number of turns, helping identify potential issues with user engagement or early drop-offs. A high count may indicate problems with the voice agent's initial responses or user experience that cause premature conversation termination.

<img width="359" height="123" alt="Screenshot 2025-11-28 at 6 08 36 PM" src="https://github.com/user-attachments/assets/b329feba-675f-4a5b-817a-cb6aacc34686" />

#### Average Number of Turns Per Conversation

This panel displays the average number of back-and-forth exchanges in each conversation. It provides insight into conversation depth and user engagement—higher averages typically indicate more complex interactions, while lower averages might suggest quick transactions or potential friction points.

<img width="349" height="132" alt="Screenshot 2025-11-28 at 6 09 30 PM" src="https://github.com/user-attachments/assets/a329bbe2-cafe-410f-8934-412d0f79b23a" />


#### List of Conversations Below Set Turn Threshold (Trace ID)

This table provides a detailed list of specific conversations that ended before meeting the turn threshold, along with their trace IDs. Teams can click through to individual traces to investigate why these conversations were shorter than expected and identify patterns or issues requiring attention.

<img width="459" height="225" alt="Screenshot 2025-12-02 at 10 28 31 AM" src="https://github.com/user-attachments/assets/893a8d9c-f460-4dd3-a373-f10e2af08fac" />



#### Average Latency of the TTS Over Time for the Voice Agent

Text-to-speech (TTS) latency directly impacts the conversational experience. This panel tracks the average TTS response time over time, helping you monitor voice synthesis performance, detect degradation, and ensure the voice agent maintains natural, responsive interactions.

<img width="571" height="274" alt="Screenshot 2025-11-28 at 6 09 58 PM" src="https://github.com/user-attachments/assets/93958337-94d6-42d8-bfe6-e91c9ebfa87e" />

#### Average Latency of the STT Over Time for the Voice Agent

Speech-to-text (STT) latency directly impacts the conversational experience. This panel tracks the average STT response time over time, helping you monitor voice synthesis performance, detect degradation, and ensure the voice agent maintains natural, responsive interactions.

<img width="575" height="267" alt="Screenshot 2025-12-02 at 10 29 08 AM" src="https://github.com/user-attachments/assets/e3fc1e62-9961-448a-bd51-fe73787a3101" />

