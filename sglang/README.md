# SGLang Dashboard

This dashboard tracks a self-hosted SGLang inference server: token throughput, time to first token, inter-token and end-to-end request latency, running versus queued requests, KV cache pool usage, and prefix cache hit rate.

It reads the native `sglang:*` metrics that SGLang exposes on its server endpoint (`:30000/metrics`, with the server started using `--enable-metrics`), scraped by the OpenTelemetry Collector Prometheus receiver. Metric names keep the colon, as in `sglang:gen_throughput`, and the latency panels read the `.bucket` series that the Collector splits each Prometheus histogram into.

For setup instructions and more details, please visit the [SigNoz SGLang Observability Documentation](https://signoz.io/docs/sglang-observability/).
