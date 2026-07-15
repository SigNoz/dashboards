# Firecrawl Dashboard

## Details

This dashboard monitors Firecrawl SDK usage instrumented by `firecrawl-otel`: call volume, latency, error rate, credits consumed, and results returned, broken down per operation (scrape/search/map/crawl/batch_scrape). It is built on trace spans carrying the `firecrawl.*` attributes (every panel filters on `firecrawl.operation EXISTS`), so it renders for both short-lived jobs and long-running services.

## Dashboard panels

### Sections

#### Total Firecrawl Calls

A count of all Firecrawl operation spans over the selected time range. A quick pulse on how much scraping work is being driven through the SDK.

#### Error Rate

The share of Firecrawl calls that failed, computed as errored spans divided by all spans (`A / (A + B)` where A filters on `has_error = true` and B on `has_error = false`). Rendered as a percentage for an at-a-glance health signal.

#### Total Credits Used

Sum of `firecrawl.credits_used` across all calls. Tracks consumption against your Firecrawl plan.

#### Total Results Returned

Sum of `firecrawl.results` across all calls. Shows how much content the operations are actually bringing back.

#### Calls Over Time by Operation

Call count over time, split by `firecrawl.operation`. Reveals traffic patterns and which operations dominate.

#### Latency Percentiles (p50 / p95 / p99)

Duration percentiles across all Firecrawl spans. Surfaces both typical performance and the tail latency that shapes worst-case experience.

#### Call Distribution by Operation

A pie chart showing each operation's share of total calls. Complements the trend graphs with a clear share-of-traffic view.

#### Operation Summary

A table of calls, p95 latency, average latency, results, and credits per operation. Gives a full side-by-side comparison across scrape, search, map, crawl, and batch_scrape.

#### Credits Used Over Time by Operation

Credits consumed over time, split by operation. Shows where spend is concentrated and how it trends.

#### Results Returned Over Time by Operation

Results returned over time, split by operation. Useful for spotting drops in yield that don't show up as outright errors.

#### p95 Latency by Operation

95th-percentile duration per operation. Identifies which operations are slowest under load.

#### Recent Firecrawl Calls

A list of the most recent Firecrawl spans, ordered by timestamp descending. Useful for drilling into individual calls when investigating an error or a latency spike.
