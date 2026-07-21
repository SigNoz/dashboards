# DSPy Dashboard

## Details

This dashboard monitors DSPy programs instrumented with `openinference-instrumentation-dspy`: module/chain/tool activity, LLM call volume and latency, per-model usage, and errors. It is built on DSPy-native OpenTelemetry span attributes (`openinference.span.kind`, `llm.model_name`), so every panel keys off the span kinds DSPy emits (CHAIN / LLM / TOOL). Use the `service_name` picker to filter to one or more DSPy services.

## Dashboard panels

### Sections

#### DSPy operations

Total instrumented DSPy spans (any span carrying `openinference.span.kind`) over the selected time range. A quick pulse on how much DSPy work is being driven.

<img width="717" height="247" alt="dspy-operations" src="./images/dspy-panel-01.webp" />


#### LLM calls

Count of `LM.__call__` spans, i.e. the actual model requests DSPy makes. Shows raw model-invocation volume.

<img width="717" height="247" alt="dspy-llm-calls" src="./images/dspy-panel-02.webp" />


#### Tool calls

Count of TOOL spans (ReAct tool invocations). Shows how much tool activity the programs are driving.

<img width="717" height="247" alt="dspy-tool-calls" src="./images/dspy-panel-03.webp" />


#### Error rate

The fraction of the selected DSPy services' spans that have an error status. An at-a-glance health signal.

<img width="717" height="247" alt="dspy-error-rate" src="./images/dspy-panel-04.webp" />


#### Avg LLM calls / program run

LLM spans divided by `dspy.program.run` root spans: the model-call fan-out per program run. Useful for spotting changes in how many model calls each run makes.

<img width="717" height="247" alt="dspy-avg-llm-calls-per-run" src="./images/dspy-panel-05.webp" />


#### LLM latency (p95)

95th-percentile duration of `LM.__call__` spans. Surfaces the tail latency that shapes worst-case experience.

<img width="717" height="247" alt="dspy-llm-latency-p95" src="./images/dspy-panel-06.webp" />


#### DSPy operations by span kind (over time)

CHAIN / LLM / TOOL activity over time. Reveals traffic patterns and which span kinds dominate.

<img width="1438" height="577" alt="dspy-operations-by-span-kind" src="./images/dspy-panel-07.webp" />


#### Span kind distribution

A pie chart showing each span kind's share of CHAIN / LLM / TOOL spans. Complements the trend graph with a clear share-of-activity view.

<img width="1438" height="491" alt="dspy-span-kind-distribution" src="./images/dspy-panel-08.webp" />


#### LLM calls by model (over time)

`LM.__call__` volume over time, grouped by `llm.model_name`. Shows which models drive the traffic and how it trends.

<img width="1438" height="577" alt="dspy-llm-calls-by-model" src="./images/dspy-panel-09.webp" />


#### LLM latency percentiles (over time)

p50 / p90 / p99 of `LM.__call__` duration. Surfaces both typical performance and tail latency over time.

<img width="1438" height="577" alt="dspy-llm-latency-percentiles" src="./images/dspy-panel-10.webp" />


#### DSPy module breakdown

A table of CHAIN spans grouped by module/operation name, with call count and average latency. Gives a side-by-side comparison across the modules in a program.

<img width="1445" height="491" alt="dspy-module-breakdown" src="./images/dspy-panel-11.webp" />


#### Model usage

A table of LLM spans grouped by model and provider. Shows how model usage is distributed across providers.

<img width="1445" height="491" alt="dspy-model-usage" src="./images/dspy-panel-12.webp" />


#### Tool usage

A table of TOOL spans grouped by tool name, with call count and average latency. Identifies which tools are used most and which are slowest.

<img width="1445" height="491" alt="dspy-tool-usage" src="./images/dspy-panel-13.webp" />


#### Recent DSPy operations

A list of the latest instrumented DSPy spans, ordered by timestamp descending. Useful for drilling into individual operations when investigating a latency spike.

<img width="2885" height="656" alt="dspy-recent-operations" src="./images/dspy-panel-14.webp" />


#### Errors

A list of recent errored spans across the selected DSPy services. Useful for jumping straight to failures when the error rate climbs.

<img width="2885" height="656" alt="dspy-errors" src="./images/dspy-panel-15.webp" />
