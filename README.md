
> :warning: **Migration Notice**: These dashboards are currently being updated for compatibility with non-normalized metrics. If your system still uses normalized metrics, please use the legacy dashboards available in the [legacy branch](https://github.com/SigNoz/dashboards/tree/legacy-underscore-metrics).

> :note: **Migration Notice**: If you're using SigNoz cloud, your account has already been migrated to use non-normalized metrics.

# SigNoz Dashboards

Welcome to the **SigNoz Dashboards** repository! This repository hosts a collection of pre-built SigNoz dashboard templates in JSON format, designed to monitor popular services like MySQL, MongoDB, APM, JVM, and more. These dashboards allow you to quickly set up visualizations for your application's metrics and performance.

## Table of Contents

- [Overview](#overview)
- [Available Dashboards](#available-dashboards)
- [Request New Dashboard Template](#request-new-dashboard-template)
- [Adding New Dashboards](#adding-new-dashboards)
- [Dashboard Naming Convention](#dashboard-naming-convention)
- [Contributing](#contributing)
- [License](#license)

## Overview

SigNoz is an open-source observability platform that helps you monitor and analyze the performance of your services in real-time. This repository contains ready-to-use dashboard templates in JSON format that can be imported into SigNoz to visualize key metrics and performance indicators for various services.

Each dashboard is built for specific services and data sources like OpenTelemetry (OTLP) and Prometheus. Users can import and modify these dashboards or create new ones based on their needs.

## Available Dashboards

Below is a list of available dashboard templates in this repository:

- [**Hostmetrics Dashboard**](https://github.com/SigNoz/dashboards/tree/main/hostmetrics): Monitors general host metrics, including CPU, memory, and disk usage.
- [**Kubernetes Infra Dashboard**](https://github.com/SigNoz/dashboards/tree/main/k8s-infra-metrics): Visualizes metrics related to Kubernetes infrastructure.
- [**Key Operations Dashboard**](https://github.com/SigNoz/dashboards/tree/main/key-operations): Tracks key operations within an application, focusing on performance and reliability.
- [**Apache Web Server Dashboard**](https://github.com/SigNoz/dashboards/tree/main/apache-web-server): Monitors Apache web server metrics like request rates and active connections.
- [**APM Dashboard**](https://github.com/SigNoz/dashboards/tree/main/apm): Visualizes application performance metrics, including latency, throughput, and error rates.
- [**Docker Container Metrics Dashboard**](https://github.com/SigNoz/dashboards/tree/main/container-metrics): Tracks metrics related to Docker containers, such as CPU and memory usage.
- [**CouchDB Dashboard**](https://github.com/SigNoz/dashboards/tree/main/couchdb): Monitors CouchDB-specific metrics, such as document read/write rates.
- [**ECS Infrastructure Metrics Dashboard**](https://github.com/SigNoz/dashboards/tree/main/ecs-infra-metrics): Visualizes metrics for Amazon ECS infrastructure.
- [**Flask Monitoring Dashboard**](https://github.com/SigNoz/dashboards/tree/main/flask-monitoring): Monitors performance metrics for Flask applications.
- [**HAProxy Dashboard**](https://github.com/SigNoz/dashboards/tree/main/haproxy): Monitors HAProxy metrics such as request rates and active sessions.
- [**Jenkins Dashboard**](https://github.com/SigNoz/dashboards/tree/main/jenkins): Tracks Jenkins metrics, including job success rates and queue times.
- [**JMX Dashboard**](https://github.com/SigNoz/dashboards/tree/main/jmx): Monitors Java Management Extensions (JMX) metrics.
- [**JVM Dashboard**](https://github.com/SigNoz/dashboards/tree/main/jvm): Tracks JVM metrics, including heap usage, garbage collection, and thread counts.
- [**Memcached Dashboard**](https://github.com/SigNoz/dashboards/tree/main/memcached): Visualizes Memcached-specific metrics, such as cache hit/miss rates.
- [**MongoDB Dashboard**](https://github.com/SigNoz/dashboards/tree/main/mongodb): Monitors MongoDB operations, memory usage, and performance metrics.
- [**MySQL Dashboard**](https://github.com/SigNoz/dashboards/tree/main/mysql): Tracks MySQL metrics, including queries per second and connection errors.
- [**Nginx Dashboard**](https://github.com/SigNoz/dashboards/tree/main/nginx): Monitors Nginx web server metrics, including request rates and active connections.
- [**Nomad Dashboard**](https://github.com/SigNoz/dashboards/tree/main/nomad): Visualizes metrics for HashiCorp Nomad.
- [**PostgreSQL Dashboard**](https://github.com/SigNoz/dashboards/tree/main/postgresql): Monitors PostgreSQL performance metrics.
- [**RabbitMQ Dashboard**](https://github.com/SigNoz/dashboards/tree/main/rabbitmq): Tracks RabbitMQ metrics like queue sizes and message throughput.
- [**Temporal.io Dashboard**](https://github.com/SigNoz/dashboards/tree/main/temporal.io): Monitors Temporal.io workflow metrics.
- [**LLM Observability Dashboard**](https://github.com/SigNoz/dashboards/tree/main/llm-observability): Visualizes metrics for monitoring large language models.
- [**SigNoz Ingestion Analysis**](https://github.com/SigNoz/dashboards/tree/main/signoz-ingestion-analysis): Visualizes the volume the metrics, traces and logs ingested into SigNoz. Useful for cost optimization.
- [**KEDA Dashboard**](https://github.com/SigNoz/dashboards/tree/main/keda): Monitors metrics for KEDA, a Kubernetes-based event-driven autoscaling component.

More services will be added in the future!

## Request New Dashboard Template

Before requesting a new dashboard, please check if a similar request has already been made by searching through the open issues here: [Existing Dashboard Requests](https://github.com/SigNoz/signoz/issues?q=is%3Aopen+is%3Aissue+label%3Adashboard-template).

If no similar request exists, you can create a new issue using the following link: [Request a New Dashboard](https://github.com/SigNoz/signoz/issues/new?assignees=&labels=dashboard-template&projects=&template=request_dashboard.md&title=).

Please make sure to provide the necessary details when submitting your request to ensure that it can be addressed appropriately.

## Adding New Dashboards

To add a new dashboard template for any service, follow the contribution guidelines in the [Contributing Guide](CONTRIBUTING.md). In brief:

1. Create a dashboard JSON file following the [Dashboard Naming Convention](#dashboard-naming-convention).
2. Add a README file explaining the dashboard, the metrics ingested, and the configurations needed.
3. Include screenshots of the dashboard in the `assets/` directory.
4. Submit a pull request for review.

## Dashboard Naming Convention

Dashboard JSON files should follow this naming convention:

```
name-of-dashboard-source-version.json
```

- **name-of-dashboard**: The name of the service being monitored (e.g., `mysql-dashboard`).
- **source**: Data source, such as `otlp` or `prometheus`.
- **version**: Start with `v1` for the initial version and increment with future versions (e.g., `v2`, `v3`).

Example: `mysql-dashboard-otlp-v1.json`

## Contributing

We welcome contributions! If you want to contribute new dashboard templates or enhance existing ones, please refer to our [Contributing Guide](CONTRIBUTING.md) for details on how to get started. Be sure to follow the naming conventions and guidelines outlined in the guide.

Your contributions will help the SigNoz community grow and make monitoring easier for everyone.

## License

This repository is licensed under the Apache 2.0 License. By contributing to this repository, you agree that your contributions will also be licensed under the same.

[![License](https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)
