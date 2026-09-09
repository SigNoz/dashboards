# Modal Dashboard

This dashboard provides detailed insights into your Modal workspace, monitoring key metrics for input throughput and success rate, cold start and queue wait, execution time, container backlog and churn, per-function CPU and memory, and GPU saturation.

It is built on the native `modal.*` metrics that Modal pushes to your OTLP endpoint through its workspace-level OpenTelemetry integration, which covers every Function and every Sandbox without any code changes.

For setup instructions and more details, please visit the [SigNoz Modal Integration Documentation](https://signoz.io/docs/integrations/modal/).
