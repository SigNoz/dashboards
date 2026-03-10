# OpenClaw Dashboard

## Details

This dashboard offers a clear view into OpenClaw usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. 

To start sending OpenClaw telemetry to SigNoz, follow the [OpenClaw observability guide](https://signoz.io/docs/openclaw-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of OpenClaw. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.


#### Total Token Usage (Over Time)

This line shows the total token usage over time per model. 

#### Cache Read & Write Util %

Shows the percentage of tokens served from cache versus newly written, helping you understand cache efficiency and potential cost savings from prompt caching.

#### Input vs Output Token Rate

Displays the ratio between input tokens and output tokens over time, revealing how wordy model responses are relative to user prompts.

#### Token Type Breaktdown by Model

Breaks down cache reads, cache writes, input tokens, and output tokens for each model to show detailed consumption patterns across token types.

#### Request Model Distribution

OpenClaw supports multiple LLM models, each optimized for different tasks. This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.


#### Requests Over Time

This chart captures the volume of requests/messages sent to OpenClaw over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.


#### Message Processing Latency (Over Time)

Tracks how long OpenClaw takes to process messages over time, helping you identify performance bottlenecks and ensure responsive user experiences.

#### Messages Outcome by Channel

This dashboard tracks the volume of successfully completed messages processed by OpenClaw over time, broken down by channel. It's useful for monitoring message throughput and comparing channel activity to spot traffic patterns or drops in processing.

#### Queue Wait By Lane

This dashboard tracks the 95th percentile queue wait time across different processing lanes, measuring how long tasks sit in queue before being picked up. It helps identify latency spikes or backpressure building up in OpenClaw's internal queues.

#### Message Queue Rate

This dashboard tracks the rate at which incoming messages are being queued for dispatch, broken down by channel. It helps monitor inbound message load and identify surges or drop-offs in traffic hitting OpenClaw's dispatch system.

#### Queue Depth By Lane

This dashboard tracks the number of items sitting in each processing lane's queue at any given time, indicating how backed up each lane is. 

#### Session State Transition

This dashboard tracks the rate of session lifecycle state transitions to show how actively OpenClaw sessions are moving through their processing stages.















