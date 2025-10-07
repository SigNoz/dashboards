# Crew AI Dashboard

## Details

This dashboard offers a clear view into Deepseek API usage and performance. It highlights key metrics such as token consumption, model distribution, error rates, request volumes, and latency trends. Teams can also track which services and languages are leveraging the Deepseek API, along with detailed records of errors, to better understand adoption patterns and optimize reliability and efficiency.


## Dashboard panels

### Sections

#### Total Token Usage (Input & Output)

Tokens are the foundation of any LLM related framework. By splitting input tokens (user prompts) and output tokens (model responses), this panel shows exactly how much work the system is doing. Over time, you can monitor efficiency, spot growth in adoption, and balance consumption across workloads.

<img width="470" height="151" alt="gemini-io-token-count" src="https://github.com/user-attachments/assets/1f13435e-e926-4c70-9e13-804f10f6fc48" />

#### Average Duration of Crew

This panel displays the average total execution time for each Crew run — from the moment a crew starts processing to when it completes all assigned tasks. Monitoring this metric helps teams understand how long workflows typically take, spot inefficiencies, and evaluate the impact of optimizations or configuration changes over time.

<img width="225" height="116" alt="Screenshot 2025-10-07 at 12 19 58 PM" src="https://github.com/user-attachments/assets/bc3016a8-cf5a-430d-baf2-c8104658c72d" />

#### Token Usage Over Time

Instead of a static snapshot, this time series shows token consumption trends. Are developers ramping up during peak cycles? Is there a steady baseline of activity? This view makes it easy to spot both healthy adoption curves and unusual spikes.

<img width="683" height="313" alt="gemini-token-usage" src="https://github.com/user-attachments/assets/b316a274-89f5-4452-b2e0-ea81a187a382" />

#### Duration Over Time (Per Agent)

This panel shows how the execution time of a specific agent changes over time. It helps identify performance trends, slowdowns, or improvements for the selected agent in the dashboard variable.

<img width="690" height="278" alt="Screenshot 2025-10-07 at 12 22 30 PM" src="https://github.com/user-attachments/assets/938617ad-14ac-45a5-a9aa-63b89e271e2e" />

#### Duration Over Time (Per Tool)

This panel tracks the execution time of a specific tool over time, based on the selected dashboard variable. It helps reveal performance patterns, inefficiencies, or changes in tool responsiveness across runs.

<img width="679" height="278" alt="Screenshot 2025-10-07 at 12 24 42 PM" src="https://github.com/user-attachments/assets/b803625e-4ad8-4ec8-a110-3f5466b84115" />

#### Agents and Tasks

This panel lists all Agent and Task spans within the Crew execution. Each entry links directly to its corresponding trace span, allowing quick navigation and detailed inspection of execution flow.

<img width="698" height="588" alt="Screenshot 2025-10-07 at 12 25 17 PM" src="https://github.com/user-attachments/assets/4d9dae4f-14e4-4298-9914-e0fab5542891" />

#### Tasks Per Agent

This table shows the number of tasks executed by each agent. It provides a clear view of workload distribution across agents, helping identify which agents handle the most activity or may require optimization.

<img width="698" height="152" alt="Screenshot 2025-10-07 at 12 27 25 PM" src="https://github.com/user-attachments/assets/24d3325d-d5f2-4832-8edf-439cb1270bc6" />

#### Average Time Per Agent

This table displays the average task execution time for each agent. It helps compare agent efficiency and identify where performance improvements or load balancing may be needed.

<img width="698" height="152" alt="Screenshot 2025-10-07 at 12 28 29 PM" src="https://github.com/user-attachments/assets/17fa63fc-033f-4e99-b00f-968aa7b16de4" />

#### Average Time Per Tool

This table shows the average execution time for each tool. It highlights which tools perform efficiently and which may need optimization or investigation for latency issues.

<img width="698" height="205" alt="Screenshot 2025-10-07 at 12 36 26 PM" src="https://github.com/user-attachments/assets/b33a5035-3e86-4d8a-9d24-39e66294e80e" />






