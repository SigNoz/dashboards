# Karpenter Dashboard

This dashboard provides detailed insights into Karpenter, the Kubernetes node autoprovisioner, monitoring key metrics for fleet size and utilization, provisioning and scheduling latency, voluntary disruption and consolidation, cloud provider health, Spot interruption handling, and NodePool capacity against configured limits.

It is built on the native `karpenter_*` metrics that the Karpenter controller exposes on its metrics endpoint (`:8080/metrics`), scraped via the OpenTelemetry Collector Prometheus receiver.

For setup instructions and more details, please visit the [SigNoz Karpenter Integration Documentation](https://signoz.io/docs/metrics-management/opentelemetry-karpenter-metrics/).
