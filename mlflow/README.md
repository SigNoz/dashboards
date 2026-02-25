# MLflow Monitoring Dashboard

## Details

This dashboard provides comprehensive observability into your MLflow-tracked AI workflows by helping you monitor, debug, and ensure your AI models are production-ready by surfacing key metrics such as token usage, model distribution, latency trends and error rates. 

To start sending MLflow telemetry to SigNoz, follow the [MLflow observability guide](https://signoz.io/docs/mlflow-monitoring/).

## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

For LLM models tracked in MLflow, this panel monitors token consumption for input and output tokens.

<img width="463" height="140" alt="Screenshot 2026-02-25 at 12 18 39 PM" src="https://github.com/user-attachments/assets/967aee32-26cd-4eb6-bc93-8dbedab91fec" />

#### Total Token Usage (Over Time)

This line chart displays total token usage over time per service.

<img width="463" height="176" alt="Screenshot 2026-02-25 at 12 19 20 PM" src="https://github.com/user-attachments/assets/4920273e-d3bd-4f8b-b8c7-be64e82096e3" />


#### Total Error Rate

Not every request makes it through successfully. This panel tracks the percentage of AI calls that return errors. 

<img width="463" height="105" alt="Screenshot 2026-02-25 at 12 18 58 PM" src="https://github.com/user-attachments/assets/3f33d8fc-245a-42a5-af16-3f7612be203c" />


#### Model Distribution

This panel reveals which models are being called most often helping you track preferences, measure adoption of newer releases, and align usage with performance or cost goals.

<img width="231" height="254" alt="Screenshot 2026-02-25 at 12 19 40 PM" src="https://github.com/user-attachments/assets/bfeaacee-64b8-4768-bb39-5f67138c3726" />


#### Token Distribution By Model

This breakdown reveals how token usage is spread across different model variants, helping you identify which models drive the most consumption and optimize your workload distribution for cost and performance.

<img width="231" height="254" alt="Screenshot 2026-02-25 at 12 19 59 PM" src="https://github.com/user-attachments/assets/9fe4c1d5-8f3f-482e-aa1f-bcd7207134c8" />


#### Requests Over Time

This chart captures the volume of requests sent via MLflow over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="457" height="179" alt="Screenshot 2026-02-25 at 12 20 17 PM" src="https://github.com/user-attachments/assets/09cbb5c2-1f12-4aa2-842d-499414a42bcd" />


#### Request Duration (P95 Over Time)

How fast do your AI requests respond under load? This panel measures the 95th percentile duration of requests over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="457" height="179" alt="Screenshot 2026-02-25 at 12 20 31 PM" src="https://github.com/user-attachments/assets/1e7e568d-acc5-4cdf-ad22-04d5c6ccb4eb" />


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="461" height="174" alt="Screenshot 2026-02-25 at 12 21 01 PM" src="https://github.com/user-attachments/assets/1d0be805-e7e1-4fd6-938a-ba4a6a82e8a3" />








