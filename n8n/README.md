# n8n Cloud Dashboard

## Details

This dashboard offers a clear view into n8n cloud usage and performance. It highlights key metrics such as workflow error rates, node error rates, execution volumes, and latency trends. Teams can track node type distributions, workflow execution patterns, and detailed error records to better understand adoption patterns and optimize reliability and efficiency.

To start sending n8n telemetry to SigNoz, follow the [n8n observability guide](https://signoz.io/docs/n8n-monitoring/).

## Dashboard panels

### Sections

#### Workflow Error Rate

Not every workflow makes it through successfully. This panel tracks the percentage of n8n workflows that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.


#### Node Error Rate

Individual nodes within workflows can fail independently. This panel calculates the percentage of node executions that encounter errors, helping you pinpoint which specific operations or integrations are causing issues. 


#### Requests Over Time

This chart captures the volume of executions in n8n over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.



#### Request Duration (P95 Over Time)

How fast does n8n respond under load? This panel measures the 95th percentile duration of worfklow executions over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.



#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.


#### Nodes

Understanding which node types are most frequently used and how they perform is essential for optimization. This table displays all called node types alongside their execution counts and average durations. 


#### Workflows

Get a comprehensive view of all workflow executions in this detailed table. It shows each workflow's name, unique ID, execution status (success or error), and execution duration. 











