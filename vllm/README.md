# vLLM Dashboard

This dashboard tracks a self-hosted vLLM inference server: token throughput, time to first token, inter-token and end-to-end request latency, queue time, running versus waiting requests, KV cache usage, prefix cache hit rate, and preemptions.

It reads the native `vllm:*` metrics that vLLM exposes at `/metrics` on the same port as its OpenAI-compatible API, scraped by the OpenTelemetry Collector Prometheus receiver. Metric names keep the colon, as in `vllm:generation_tokens_total`, and the latency panels read the `.bucket` series that the Collector splits each Prometheus histogram into. vLLM ships no throughput gauge and no prefix cache hit-rate metric, so the throughput panels apply a rate to the token counters and the hit rate is a formula over `vllm:prefix_cache_hits_total` and `vllm:prefix_cache_queries_total`.

For setup instructions and more details, please visit the [SigNoz vLLM Observability Documentation](https://signoz.io/docs/vllm-observability/).
