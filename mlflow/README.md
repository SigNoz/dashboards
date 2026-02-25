# MLflow Monitoring Dashboard

## Details

This dashboard provides comprehensive observability into your MLflow-tracked AI workflows by helping you monitor, debug, and ensure your AI models are production-ready by surfacing key metrics such as token usage, model distribution, latency trends and error rates. 

To start sending MLflow telemetry to SigNoz, follow the [MLflow observability guide](https://signoz.io/docs/mlflow-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

For LLM models tracked in MLflow, this panel monitors token consumption for input and output tokens.


#### Total Token Usage (Over Time)

This line chart displays total token usage over time per service.


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of AI calls that return errors. 

#### Model Distribution

This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.


#### Requests Over Time

This chart captures the volume of requests sent via MLflow over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.


#### Request Duration (P95 Over Time)

How fast do your AI requests respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.









