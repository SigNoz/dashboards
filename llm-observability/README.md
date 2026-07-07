# LLM Observability Dashboards

This directory contains SigNoz dashboard templates for LLM Observability monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Dashboards

| File | Dashboard | Panels |
| --- | --- | --- |
| `sample-chatpdf-cost-dashboard.json` | SigNoz ChatPDF Cost Dashboard | 3 |
| `sample-chatpdf-performance-metrics.json` | SigNoz Chat PDF Performance Metrics | 4 |

## SigNoz ChatPDF Cost Dashboard

**File:** `sample-chatpdf-cost-dashboard.json`

**Filter variables:** `serviceName`

**Panels:**

- Top 10 User Token Consumption
- Estimated Costs (Last 1 Day) GPT-4
- Cost Over Time

## SigNoz Chat PDF Performance Metrics

**File:** `sample-chatpdf-performance-metrics.json`

**Tags:** `langchain`

**Filter variables:** `userNames`

**Panels:**

- Latency
- Token Throughput
- Total LLM Calls
- Model vs Total Tokens
