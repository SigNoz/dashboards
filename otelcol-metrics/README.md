# OtelCol Internal Metrics

The OtelCol Internal dashboards consists of charts that are useful for monitoring the health of the collector.

## Importing Dashboard

For a generic dashboard with `host_name` variable, you can import the
`otelcol-metrics.json` file in SigNoz UI.

If you have multiple environments and you are using `deployment.environment`
label, you can import the `otelcol-metrics-env.json` file in SigNoz UI.

## Metrics to look at for OtelCol

## Batch processor

- `batch_size_trigger_send` - Incremented when the batch trigger happens because of batch size.
- `timeout_trigger_send` - Incremented when the batch trigger happens because of timeout.
- `batch_send_size` - What is the batch size when it is pushed
- `batch_send_size_bytes` - What is the batch size in bytes when it is pushed

This helps us in understanding the typical batch size that is maintained in memory.

## Receiver

- `accepted_spans`
- `refused_spans`
- `accepted_metric_points`
- `refused_metric_points`
- `accepted_log_records`
- `refused_log_records`

Rate of change of `accepted_{spans,metric_points,log_records}` indicate
the data received as in its original form. This is ingestion metric we
are interested to look at the load. This should be used along with the
instance and receiver type to understand the trend.

Non-null rate of change of `refused_spans` probably indicates the loss
of data depending on the retry mechanism on client. Whenever someone
reports a loss of data you may want to confirm here first.

## Exporter

- `sent_spans`
- `failed_spans`
- `enqueue_failed_spans`
- `sent_metric_points`
- `failed_metric_points`
- `enqueue_failed_metric_points`
- `sent_log_records`
- `failed_log_records`
- `enqueue_failed_log_records`

`enqueue_failed_{spans,metric_points,log_records}` indicate the number of
span/metric points/log records failed to be added to the sending queue.
This may be caused by a queue full of unsettled elements, so you may need
to decrease your sending rate or horizontally scale collectors.

Non-zero rate of `failed_{spans,metric_points,log_records}` indicate
collector is not able to send data. This could mean DB is performing
poorly. This doesn’t necessarily mean there is a data loss because
the retry mechanism in place.

rate of `sent_{spans,metric_points,log_records}` show at what rate
the data is getting written to DB.

This needs to compared with the receiver rate and possibly relate
with queue settings.

## Queue length

`A/B`, where `A` is the `exporter_queue_size` and `B` is `exporter_queue_capacity`
indicate the what is the typical occupied behaviour of the queue.
This should indicate if the queue size enough for the ingestion.

Non zero rate of `enqueue_failed_{spans, metric_points, log_records}` indicate
that queue is full. It is either the ingestion is happening at high rate in
receiver but the exporter is not transmitting at the same rate.

The solution might be increase the collector instances if the queue size is already reasonable.
