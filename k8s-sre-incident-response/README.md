# K8s SRE — Incident Response Dashboard

> Built for the SRE who gets paged at 2am, not for the engineer browsing infra metrics at 2pm.

## The problem with standard K8s dashboards

Most Kubernetes dashboards show you *everything* — CPU trends, network bytes, disk IOPS across every node. That's great for capacity planning.

During an active incident, it's noise.

This dashboard gives you **8 signals** that answer one question: **what is broken right now, and why?**

Built from real on-call experience running Kubernetes at scale in a high-traffic banking environment — where a missed signal meant a real customer impact.

---

## What's included

| Panel | Signal | Why it matters in an incident |
|---|---|---|
| Pod Restart Rate | graph | First sign of crash loops or OOMKills — spikes before alerts fire |
| Node CPU Pressure | gauge | Above 80% = scheduling risk; above 90% = imminent degradation |
| Node Memory Pressure | gauge | OOM kill risk; above 85% = pods are at risk |
| Pending Pods | stat | Any non-zero = scheduling failure — resource starvation or taint mismatch |
| Container Restarts / OOMKills | stat | Memory limit breaches hiding behind auto-restarts |
| p99 Latency (SLI) | graph | Your primary SLI — sustained breach = SLO violation |
| 5XX Error Rate | graph | Error budget consumption in real time — correlate with latency |
| PVC Usage | table | Silent incidents: a PVC at 80% becomes a P1 crash in 24-48h |

---

## Thresholds (opinionated, adjust to your SLOs)

| Signal | Warning | Critical |
|---|---|---|
| Node CPU | 80% | 90% |
| Node Memory | 85% | 95% |
| Pending Pods | 1 | 5 |
| Container Restarts | 1 | 3 |

---

## Data source requirements

- OpenTelemetry Collector with **Kubernetes receiver** enabled
- Kubelet metrics scraping enabled
- APM instrumentation via OpenTelemetry SDK (for p99 latency and error rate panels)

---

## Import instructions

1. Go to **SigNoz → Dashboards → New Dashboard → Import JSON**
2. Upload `k8s-sre-incident-response.json`
3. Select your **cluster** and **namespace** from the variable dropdowns
4. Set your SLO threshold line on the p99 latency panel

---

## Triage runbook (use this during an incident)

```
1. Check Pending Pods → 0 is good, any value = scheduling issue
2. Check Pod Restart Rate → spike = crash loop, check OOMKill count
3. Check Node CPU/Memory → if both high, you have resource starvation
4. Check p99 Latency → breaching SLO threshold? = user-facing impact
5. Check 5XX Error Rate → correlates with latency? = downstream failure
6. Check PVC Usage → any at 80%+? = proactive fix needed NOW
```

---

## Author

**Shobhit Verma** — Lead SRE | AWS | Dynatrace | Kubernetes | AI Automation

- GitHub: [@infrawithshobhit](https://github.com/infrawithshobhit)
- LinkedIn: [linkedin.com/in/vershobhit](https://linkedin.com/in/vershobhit)
- Content: [@TheJugaadSRE](https://instagram.com/thejugaadsre)

15+ years in platform and reliability engineering. This dashboard reflects real patterns from operating high-traffic systems where on-call response time directly impacts customer experience.

---

*If this saved you time in an incident, star the repo and share it with your team.*
