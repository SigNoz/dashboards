# Kubernetes System Monitoring Dashboards

This directory contains SigNoz dashboard templates for Kubernetes System Monitoring monitoring.

Browse all dashboard templates in the [SigNoz docs](https://signoz.io/docs/dashboards/dashboard-templates/overview/#available-dashboard-templates).

## Dashboards

| File | Dashboard | Panels |
| --- | --- | --- |
| `kubernetes-apiserver.json` | Kubernetes API Server | 9 |
| `kubernetes-controller-manager.json` | Kubernetes Controller Manager | 9 |
| `kubernetes-coredns.json` | Kubernetes CoreDNS | 9 |
| `kubernetes-etcd.json` | Kubernetes Etcd | 9 |
| `kubernetes-kube-proxy.json` | Kubernetes Kube Proxy | 9 |
| `kubernetes-kubelet.json` | Kubernetes Kubelet | 9 |
| `kubernetes-scheduler.json` | Kubernetes Scheduler | 9 |
| `kubernetes-system-overview.json` | Kubernetes System Overview | 16 |

## Kubernetes API Server

**File:** `kubernetes-apiserver.json`

Standard control-plane view for kube-apiserver using Prometheus/OpenTelemetry metrics.

**Tags:** `kubernetes`, `control-plane`, `apiserver`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered API Services
- API Requests / s
- Inflight Requests
- Long Running Requests
- Go Routines
- Request Rate By Verb
- Request Rate By Status Code
- Request SLI Duration (p50/p90/p99)
- Workqueue Depth

## Kubernetes Controller Manager

**File:** `kubernetes-controller-manager.json`

Standard control-plane view for kube-controller-manager workqueues, retries, and client request pressure.

**Tags:** `kubernetes`, `control-plane`, `controller-manager`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered Controller Services
- Workqueue Adds / s
- Workqueue Retries / s
- Go Routines
- Process RSS
- Workqueue Depth By Queue
- Workqueue Queue Duration (p50/p90/p99)
- Workqueue Work Duration (p50/p90/p99)
- REST Client Requests By Code

## Kubernetes CoreDNS

**File:** `kubernetes-coredns.json`

Cluster DNS view for request volume, cache efficiency signals, and request duration buckets.

**Tags:** `kubernetes`, `dns`, `coredns`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered CoreDNS Services
- DNS Requests / s
- Cache Hits / s
- Cache Misses / s
- Panics / s
- DNS Responses By Rcode
- DNS Requests By Record Type
- DNS Request Duration (p50/p90/p99)
- Go Routines By Instance

## Kubernetes Etcd

**File:** `kubernetes-etcd.json`

Standard etcd view using native etcd server metrics (leadership, proposals, client request traffic, and storage latency).

**Tags:** `kubernetes`, `control-plane`, `etcd`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered Etcd Services
- Client Requests / s
- Has Leader
- Proposals Pending
- DB Size
- Client Requests By Type
- Apply Duration (p50/p90/p99)
- Range Duration (p50/p90/p99)
- WAL Fsync Duration (p50/p90/p99)

## Kubernetes Kube Proxy

**File:** `kubernetes-kube-proxy.json`

Network-agent view for kube-proxy sync loops, network programming durations, and client request rates.

**Tags:** `kubernetes`, `node`, `kube-proxy`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered Kube-Proxy Services
- Sync Proxy Rules / s
- Network Programming / s
- Go Routines
- Process RSS
- Sync Proxy Rules Duration (p50/p90/p99)
- Network Programming Duration (p50/p90/p99)
- REST Client Requests By Code
- Last Sync Timestamp

## Kubernetes Kubelet

**File:** `kubernetes-kubelet.json`

Node-agent view for kubelet runtime operations, pod lifecycle, and storage operation latencies.

**Tags:** `kubernetes`, `node`, `kubelet`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered Kubelet Services
- Running Pods
- Running Containers
- Started Pods / s
- Go Routines
- Runtime Operations / s By Type
- Runtime Operation Duration (p50/p90/p99)
- Pod Start Duration (p50/p90/p99)
- Storage Operation Duration (p50/p90/p99)

## Kubernetes Scheduler

**File:** `kubernetes-scheduler.json`

Standard control-plane view for kube-scheduler queue pressure, scheduling throughput, and duration buckets.

**Tags:** `kubernetes`, `control-plane`, `scheduler`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- Auto-Discovered Scheduler Services
- Scheduling Attempts / s
- Pending Pods
- Go Routines
- Process RSS
- Scheduling Attempts By Result
- E2E Scheduling Duration (p50/p90/p99)
- Framework Extension p99 by extension_point
- Workqueue Depth

## Kubernetes System Overview

**File:** `kubernetes-system-overview.json`

Combined view across control-plane, node, networking, and DNS components with distro-neutral service scoping.

**Tags:** `kubernetes`, `overview`, `control-plane`, `node`, `dns`, `prometheus`

**Filter variables:** `service.name`, `k8s.cluster.name`, `deployment_environment_name`, `deployment_environment`

**Panels:**

- API Requests / s
- Scheduling Attempts / s
- Controller Workqueue Adds / s
- Etcd Client Requests / s
- Kubelet Running Pods
- Proxy Sync / s
- CoreDNS Requests / s
- Etcd Has Leader
- Component Throughput Trends
- API Request Rate By Code
- Scheduling Attempts By Result
- Controller Workqueue Depth
- Etcd Apply Duration (p50/p90/p99)
- Kubelet Runtime Ops / s By Type
- Proxy Network Programming Duration (p50/p90/p99)
- CoreDNS Responses By Rcode
