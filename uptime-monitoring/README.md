# Uptime Monitoring Dashboard

This dashboard provides synthetic uptime and availability insights for your HTTP
endpoints, covering availability per endpoint, transport errors with their failure
text, response-content validation, HTTP status classes and codes, phase-level
latency, response size, and TLS certificate expiry.

It is built on the `httpcheck.*` metrics produced by the OpenTelemetry Collector
[httpcheck receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/httpcheckreceiver),
which probes each configured target on a fixed interval. Enable the optional
metrics (`httpcheck.dns.lookup.duration`, `httpcheck.client.connection.duration`,
`httpcheck.tls.handshake.duration`, `httpcheck.client.request.duration`,
`httpcheck.response.duration`, `httpcheck.response.size`,
`httpcheck.tls.cert_remaining`) for the latency, payload, and TLS sections, and add
`validations` to a target for the Content Validation section, which catches a 200
response carrying the wrong body.

The receiver sets no resource attributes, so add a `service.name` through the
`resource` processor to scope the dashboard with the `service.name` and `http.url`
variables.

For setup instructions and more details, please visit the [SigNoz Monitor HTTP Endpoints Documentation](https://signoz.io/docs/monitor-http-endpoints/).
