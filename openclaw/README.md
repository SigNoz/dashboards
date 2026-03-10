# OpenClaw Dashboard

## Details

This dashboard offers a clear view into OpenClaw usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. 

To start sending OpenClaw telemetry to SigNoz, follow the [OpenClaw observability guide](https://signoz.io/docs/openclaw-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of OpenClaw. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="658" height="106" alt="Screenshot 2026-03-10 at 12 01 03 PM" src="https://github.com/user-attachments/assets/bf3fe10f-5b10-44e8-844a-2a429d7005a1" />


#### Total Token Usage (Over Time)

This line shows the total token usage over time per model. 

<img width="492" height="170" alt="Screenshot 2026-03-10 at 12 01 41 PM" src="https://github.com/user-attachments/assets/b9e0ec39-99c6-42db-b243-809f16460652" />

#### Cache Read & Write Util %

Shows the percentage of tokens served from cache versus newly written, helping you understand cache efficiency and potential cost savings from prompt caching.

<img width="685" height="310" alt="Screenshot 2026-03-10 at 12 02 01 PM" src="https://github.com/user-attachments/assets/3be65ede-e4e6-493c-a504-1820377827ae" />


#### Input vs Output Token Rate

Displays the ratio between input tokens and output tokens over time, revealing how wordy model responses are relative to user prompts.

<img width="507" height="212" alt="Screenshot 2026-03-10 at 12 02 23 PM" src="https://github.com/user-attachments/assets/9ae1daa2-bb7b-433e-b110-26e47cc6bec4" />


#### Token Type Breaktdown by Model

Breaks down cache reads, cache writes, input tokens, and output tokens for each model to show detailed consumption patterns across token types.

<img width="507" height="241" alt="Screenshot 2026-03-10 at 12 02 46 PM" src="https://github.com/user-attachments/assets/8ca59c9b-1b3c-4956-aa07-6de5dc111d3e" />


#### Request Model Distribution

OpenClaw supports multiple LLM models, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="330" height="214" alt="Screenshot 2026-03-10 at 12 03 01 PM" src="https://github.com/user-attachments/assets/d246b79d-f163-45b3-828e-8d74cbb79ac6" />

#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="330" height="214" alt="Screenshot 2026-03-10 at 12 03 12 PM" src="https://github.com/user-attachments/assets/e779716a-3a8c-423a-bc8d-4c7404dc4e26" />

#### Requests Over Time

This chart captures the volume of requests/messages sent to OpenClaw over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="495" height="244" alt="Screenshot 2026-03-10 at 12 03 30 PM" src="https://github.com/user-attachments/assets/35004147-342c-442f-876f-ae27f7bf58a3" />


#### Message Processing Latency (Over Time)

Tracks how long OpenClaw takes to process messages over time, helping you identify performance bottlenecks and ensure responsive user experiences.

<img width="494" height="205" alt="Screenshot 2026-03-10 at 12 03 51 PM" src="https://github.com/user-attachments/assets/15f4d16b-aab0-455d-96ad-2b1bb0475dae" />


#### Messages Outcome by Channel

This dashboard tracks the volume of successfully completed messages processed by OpenClaw over time, broken down by channel. It's useful for monitoring message throughput and comparing channel activity to spot traffic patterns or drops in processing.

<img width="504" height="215" alt="Screenshot 2026-03-10 at 12 04 11 PM" src="https://github.com/user-attachments/assets/17998987-f5af-4f76-acaa-8945e45e7829" />


#### Queue Wait By Lane

This dashboard tracks the 95th percentile queue wait time across different processing lanes, measuring how long tasks sit in queue before being picked up. It helps identify latency spikes or backpressure building up in OpenClaw's internal queues.

<img width="508" height="215" alt="Screenshot 2026-03-10 at 12 04 29 PM" src="https://github.com/user-attachments/assets/abe065a5-8793-4fd6-9cae-f6f360d13a38" />


#### Message Queue Rate

This dashboard tracks the rate at which incoming messages are being queued for dispatch, broken down by channel. It helps monitor inbound message load and identify surges or drop-offs in traffic hitting OpenClaw's dispatch system.

<img width="508" height="215" alt="Screenshot 2026-03-10 at 12 04 44 PM" src="https://github.com/user-attachments/assets/3b1756c6-e3d0-45cb-b92b-4b1ce51d5b66" />


#### Queue Depth By Lane

This dashboard tracks the number of items sitting in each processing lane's queue at any given time, indicating how backed up each lane is. 

<img width="508" height="207" alt="Screenshot 2026-03-10 at 12 05 18 PM" src="https://github.com/user-attachments/assets/25c6c840-e6d0-46da-95c8-4fb746fe1896" />


#### Session State Transition

This dashboard tracks the rate of session lifecycle state transitions to show how actively OpenClaw sessions are moving through their processing stages.

<img width="508" height="211" alt="Screenshot 2026-03-10 at 12 04 59 PM" src="https://github.com/user-attachments/assets/3c354d5f-e86c-43fb-99dd-faaffcdfb90f" />














