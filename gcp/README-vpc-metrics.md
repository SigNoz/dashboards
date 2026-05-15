# GCP VPC Metrics Dashboard

Comprehensive monitoring for Google Cloud VPC networking infrastructure via Google Cloud Monitoring (Stackdriver) exporter.

## Sections & Panels (36 panels)

### Overview (4 panels)
- Firewall Dropped Packets / Bytes
- Firewall Allowed Connections
- Firewall Hit Count

### VPC Flow Logs & Traffic (6 panels)
- Sent / Received Bytes by Subnet
- Sent / Received Packets by Subnet
- RTT Latencies
- Inbound vs Outbound Traffic Rate

### Cloud NAT (8 panels)
- NAT Sent / Received Bytes
- NAT Sent / Received Packets
- NAT Dropped Sent / Received Packets
- NAT Port Allocation
- NAT Open Connections

### VPC Peering (4 panels)
- Peering Sent / Received Bytes
- Peering Sent / Received Packets

### Cloud Interconnect (4 panels)
- Interconnect Sent / Received Bytes
- Interconnect Link Capacity
- Interconnect Receive Power (dBm)

### Load Balancer (6 panels)
- LB Request Count
- LB Total Latency
- LB Backend Request / Response Bytes
- LB 4xx/5xx Error Rate
- LB Backend Latency

### DNS (2 panels)
- DNS Query Count
- DNS Query Latency

### Subnet Utilization (2 panels)
- Subnet IP Utilization
- Subnet Instances Count

## Variables
| Variable | Description |
|----------|-------------|
| `project_id` | GCP Project ID |
| `network_name` | VPC Network Name (multi-select) |

## Data Source
Google Cloud Monitoring metrics via Prometheus exporter (`networking.googleapis.com/*`).
