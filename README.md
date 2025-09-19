> [!Note]
> **Dashboard Migration Status**: Due to the migration of metric names and attributes, the following dashboards may not work properly and are currently being updated:
> - Temporal
> - KEDA
> - Jenkins
> - Hadoop
>
> We are actively working on updating these dashboards to be compatible with the new metric structure.

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
Checkout list of all dashboards [here](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates)

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
