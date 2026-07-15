# Firecrawl Dashboard

## Details

This dashboard monitors Firecrawl SDK usage instrumented by `firecrawl-otel`: call volume, latency, error rate, credits consumed, and results returned, broken down per operation (scrape/search/map/crawl/batch_scrape). It is built on trace spans carrying the `firecrawl.*` attributes (every panel filters on `firecrawl.operation EXISTS`), so it renders for both short-lived jobs and long-running services.

## Dashboard panels

### Sections

#### Total Firecrawl Calls

A count of all Firecrawl operation spans over the selected time range. A quick pulse on how much scraping work is being driven through the SDK.

<img width="717" height="247" alt="firecrawl-total-firecrawl-calls" src="https://github.com/user-attachments/assets/d372d075-c797-4860-aaf2-9febe8631fbc" />


#### Error Rate

The share of Firecrawl calls that failed, computed as errored spans divided by all spans (`A / (A + B)` where A filters on `has_error = true` and B on `has_error = false`). Rendered as a percentage for an at-a-glance health signal.

<img width="720" height="247" alt="firecrawl-error-rate" src="https://github.com/user-attachments/assets/335c64d0-493d-46e1-bfc7-7e5dba043dea" />


#### Total Credits Used

Sum of `firecrawl.credits_used` across all calls. Tracks consumption against your Firecrawl plan.

<img width="721" height="247" alt="firecrawl-total-credits-used" src="https://github.com/user-attachments/assets/f2dd869e-cf08-4010-ad30-0f3807d8361f" />


#### Total Results Returned

Sum of `firecrawl.results` across all calls. Shows how much content the operations are actually bringing back.

<img width="1442" height="575" alt="firecrawl-results-returned-over-time" src="https://github.com/user-attachments/assets/7dbd6f18-42ce-4665-a415-39b74abe8eb9" />


#### Calls Over Time by Operation

Call count over time, split by `firecrawl.operation`. Reveals traffic patterns and which operations dominate.

<img width="1438" height="577" alt="firecrawl-calls-over-time-by-operation" src="https://github.com/user-attachments/assets/1684ddc1-c886-4106-9959-719bc25db1a6" />


#### Latency Percentiles (p50 / p95 / p99)

Duration percentiles across all Firecrawl spans. Surfaces both typical performance and the tail latency that shapes worst-case experience.

<img width="1444" height="577" alt="firecrawl-latency-percentiles" src="https://github.com/user-attachments/assets/97fead39-8e95-4b4f-90ae-0e791e927da7" />


#### Call Distribution by Operation

A pie chart showing each operation's share of total calls. Complements the trend graphs with a clear share-of-traffic view.

<img width="1438" height="491" alt="firecrawl-call-distribution-by-operation" src="https://github.com/user-attachments/assets/df2b3c9f-ad65-409c-98f4-eb088d65ace8" />


#### Operation Summary

A table of calls, p95 latency, average latency, results, and credits per operation. Gives a full side-by-side comparison across scrape, search, map, crawl, and batch_scrape.

<img width="1445" height="491" alt="firecrawl-operation-summary" src="https://github.com/user-attachments/assets/c4813abc-6cde-4dbc-a7fb-a5473370d8c0" />


#### Credits Used Over Time by Operation

Credits consumed over time, split by operation. Shows where spend is concentrated and how it trends.

<img width="1439" height="575" alt="firecrawl-credits-used-over-time" src="https://github.com/user-attachments/assets/ade2a56f-6dcb-4308-b4f5-a5285474e94a" />


#### Results Returned Over Time by Operation

Results returned over time, split by operation. Useful for spotting drops in yield that don't show up as outright errors.

<img width="1442" height="575" alt="firecrawl-results-returned-over-time" src="https://github.com/user-attachments/assets/4e563c96-cb24-4c45-bd6f-4c5e91feb14f" />


#### p95 Latency by Operation

95th-percentile duration per operation. Identifies which operations are slowest under load.

<img width="2885" height="575" alt="firecrawl-p95-latency-by-operation" src="https://github.com/user-attachments/assets/2ed43b90-1a18-4a2d-824e-a12737ad1f27" />


#### Recent Firecrawl Calls

A list of the most recent Firecrawl spans, ordered by timestamp descending. Useful for drilling into individual calls when investigating an error or a latency spike.

<img width="2885" height="656" alt="firecrawl-recent-firecrawl-calls" src="https://github.com/user-attachments/assets/66e3b752-2578-4a78-a586-d530346093be" />

