# FluxCD Monitoring Dashboard

Monitors FluxCD (GitOps Toolkit) controllers. Tracks reconciliation throughput, errors, and duration (avg and P50/P95/P99 by kind, controller, and resource), controller-runtime workqueues (depth, adds, retries, queue and unfinished-work time), per-controller runtime resources (CPU, working-set memory, goroutines), and Kubernetes API client traffic (request rate by code, method, and host, plus non-2xx error rate).

For more information, please visit the [FluxCD Metrics doc](https://signoz.io/docs/metrics-management/fluxcd-metrics).
