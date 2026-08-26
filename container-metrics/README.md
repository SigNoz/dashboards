# Container Metrics Dashboards

This directory contains SigNoz dashboard templates for container metrics, one per container runtime.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Container Metrics (Docker)

**File:** `docker/container-metrics-by-host.json`

**Tags:** `container`

**Filter variables:** `host.name`

**Receiver:** [`docker_stats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/dockerstatsreceiver/README.md). For setup instructions, see the [SigNoz Docker Integration Documentation](https://signoz.io/docs/metrics-management/docker-container-metrics/).

**Panels:**

- Container CPU Percent
- Container Memory percent
- Mem usage / Mem limit
- Network Bytes received
- Network Bytes sent
- Packets dropped
- Block IO

## Container Metrics (Podman)

**File:** `podman/podman-metrics-by-host.json`

**Tags:** `container`, `podman`, `metrics`, `podmanreceiver`

**Filter variables:** `host.name`, `container.name`

**Receiver:** [`podman_stats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/podmanreceiver/README.md). For setup instructions, see the [SigNoz Podman Integration Documentation](https://signoz.io/docs/metrics-management/opentelemetry-podman-metrics/).

Every panel filters on `container.runtime = 'podman'`, so the dashboard stays correct on hosts that run both Podman and Docker.

**Panels:**

Overview

- Containers Reporting
- Avg CPU %
- Avg Memory %
- Total Memory Used
- Containers (table: host, image, CPU %, memory %, memory used)

CPU

- CPU Percent
- CPU Cores Used
- System CPU Cores Used

Memory

- Memory Percent
- Memory Usage
- Memory Usage vs Limit
- Memory Share by Container

Network

- Network Bytes Received
- Network Bytes Sent

Block I/O

- Block I/O Read
- Block I/O Write

**Notes:**

- The `podman_stats` receiver reports only running containers, so a stopped container disappears from every panel.
- The receiver does not emit `container.cpu.utilization` or the `*_dropped` packet counters used by the Docker dashboard, so those panels have no Podman equivalent.
- `container.cpu.usage.percpu` appears in the receiver documentation but is not emitted by default, so no panel uses it.
