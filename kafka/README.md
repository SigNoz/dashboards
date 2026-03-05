# Kafka Server Monitoring Dashboard

## Overview
This dashboard provides Kafka server monitoring using OpenTelemetry (`kafkametricsreceiver`) metrics. It is designed to help track Kafka broker health, consumer group behavior, and topic/partition status across clusters and environments.

## Dashboard Sections
The dashboard is organized into four sections:

1. Broker
   - Monitors broker count and controller status to verify cluster availability and leadership health.
2. Consumer
   - Tracks consumer group lag, lag sum, member counts, and offsets to detect stalled or delayed consumption.
3. Topic
   - Shows topic-level partition counts and retention-related metrics for topic configuration and capacity visibility.
4. Partition
   - Surfaces partition offsets and replication health (replicas and in-sync replicas) to identify partition-level risks.

## Variables
The dashboard supports the following variables for filtering and drill-down:

- `deployment.environment`
- `kafka.cluster.alias`

## Setup Requirements
To use this dashboard, ensure Kafka metrics are collected and exported via OpenTelemetry with:

- `kafkametricsreceiver`
