# n8n Cloud Dashboard

## Details

This dashboard offers a clear view into n8n cloud usage and performance. It highlights key metrics such as workflow error rates, node error rates, execution volumes, and latency trends. Teams can track node type distributions, workflow execution patterns, and detailed error records to better understand adoption patterns and optimize reliability and efficiency.

To start sending n8n telemetry to SigNoz, follow the [n8n observability guide](https://signoz.io/docs/n8n-monitoring/).

## Dashboard panels

### Sections

#### Workflow Error Rate

Not every workflow makes it through successfully. This panel tracks the percentage of n8n workflows that return errors. It’s a quick way to identify reliability issues and ensure your applications maintain a smooth, dependable experience.

<img width="507" height="123" alt="Screenshot 2026-03-30 at 11 01 12 AM" src="https://github.com/user-attachments/assets/cd44511f-39b7-43d1-b9ca-2688dae13525" />

#### Node Error Rate

Individual nodes within workflows can fail independently. This panel calculates the percentage of node executions that encounter errors, helping you pinpoint which specific operations or integrations are causing issues. 

<img width="507" height="123" alt="Screenshot 2026-03-30 at 11 01 25 AM" src="https://github.com/user-attachments/assets/6e17b793-81d1-422b-a557-504b3618aba3" />

#### Requests Over Time

This chart captures the volume of executions in n8n over time, letting you see demand patterns, identify high-traffic windows, and plan infrastructure or cost controls accordingly.

<img width="507" height="185" alt="Screenshot 2026-03-30 at 11 02 05 AM" src="https://github.com/user-attachments/assets/d5966d71-a0a9-48a4-abb0-4e7c0432672a" />


#### Request Duration (P95 Over Time)

How fast does n8n respond under load? This panel measures the 95th percentile duration of worfklow executions over time, surfacing potential slowdowns, spikes, or regressions. By keeping an eye on responsiveness, teams can ensure a consistent developer and user experience.

<img width="507" height="177" alt="Screenshot 2026-03-30 at 11 01 46 AM" src="https://github.com/user-attachments/assets/f8eb921c-568a-4132-abca-c4c4633ef946" />


#### Error Records

This Errors panel logs all recorded errors and when clicking on an individual record, you are sent to the trace where the error originated.

<img width="507" height="230" alt="Screenshot 2026-03-30 at 11 02 25 AM" src="https://github.com/user-attachments/assets/cc3d0116-be58-4d55-81c3-3c671592a295" />


#### Nodes

Understanding which node types are most frequently used and how they perform is essential for optimization. This table displays all called node types alongside their execution counts and average durations. 

<img width="526" height="180" alt="Screenshot 2026-03-30 at 11 02 46 AM" src="https://github.com/user-attachments/assets/d6ab7dd6-0131-40c8-a8fd-09eb62dd2cc0" />

#### Workflows

Get a comprehensive view of all workflow executions in this detailed table. It shows each workflow's name, unique ID, execution status (success or error), and execution duration. 

<img width="1023" height="308" alt="Screenshot 2026-03-30 at 11 03 07 AM" src="https://github.com/user-attachments/assets/b4bbf91b-b634-4208-86d5-b4173cc9e4ce" />

#### Workflows Success/Error

Shows a pie chart of total workflows that ended in success vs error.

<img width="212" height="234" alt="Screenshot 2026-03-30 at 11 04 07 AM" src="https://github.com/user-attachments/assets/79c8a9aa-ef44-455f-b1d7-55aa22c813f0" />

#### Nodes Success/Error

Shows a pie chart of total node executions within workflows that ended in success vs error.

<img width="220" height="234" alt="Screenshot 2026-03-30 at 11 04 58 AM" src="https://github.com/user-attachments/assets/e30355ce-8e42-4890-a3d1-701bad74f88d" />











