# AWS ECS Infra Metrics Dashboards

This directory contains SigNoz dashboard templates for AWS ECS Infra Metrics monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Dashboards

| File | Dashboard | Panels |
| --- | --- | --- |
| `container-metrics.json` | Container Metrics - ECS | 10 |
| `instance-metrics.json` | Instance Metrics - ECS | 15 |

## Container Metrics - ECS

**File:** `container-metrics.json`

Container Metrics Dashboard of ECS using sidecar

**Tags:** `ecs`, `ec2`, `sidecar`

**Filter variables:** `ServiceName`, `ClusterName`

**Panels:**

- CPU Usage
- Network IO (receive)
- Network IO (transmit)
- Memory usage
- CPU Reserved
- CPU Usage
- Memory usage
- Memory reserved
- Storage read bytes
- Storage write bytes

## Instance Metrics - ECS

**File:** `instance-metrics.json`

Instance Metrics Dashboard of ECS EC2

**Tags:** `ecs`, `daemon`, `ec2`

**Filter variables:** `AutoScalingGroupName`, `ClusterName`, `InstanceId`

**Panels:**

- Memory Usage
- CPU Usage
- Disk IO
- File System Usage
- File System Usage
- Memory Utilization
- File System Utilization
- CPU Utilization
- Disk IO (read)
- Network IO
- Disk IO (write)
- Memory Limit
- CPU Limit
- Filesystem Capacity
- Network Interface IO
