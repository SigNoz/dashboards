# Daytona Dashboard

This dashboard provides detailed insights into your Daytona sandboxes, monitoring key metrics for per-sandbox CPU, memory and disk, organization quota consumption by region and sandbox class, toolbox API activity, and SDK control-plane latency and failures.

The resource, quota and toolbox panels are built on telemetry Daytona sends itself. Enable it from the OpenTelemetry section of the Daytona dashboard, and keep `*.daytona.io` reachable from your sandboxes, or the per-sandbox panels stay empty.

The SDK Control Plane panels are separate. They need tracing enabled in your own application, with `DaytonaConfig(otel_enabled=True)` or `DAYTONA_OTEL_ENABLED=true`, plus the standard OTLP endpoint and header environment variables. Without that, those five panels stay empty even when everything else is reporting.

For setup instructions and more details, please visit the [SigNoz Daytona Monitoring Documentation](https://signoz.io/docs/daytona-monitoring/).
