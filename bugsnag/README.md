# Bugsnag Dashboard

## Details

This dashboard monitors error and crash events forwarded from Bugsnag to SigNoz via Bugsnag's webhook data forwarding — ingested by the collector's bundled `webhookevent` receiver and parsed by a transform processor (see the [Bugsnag integration guide](https://signoz.io/docs/integrations/outposts/bugsnag/)). It is built on log records carrying `bugsnag.*`, `exception.*`, `app.*`, `os.*`, `device.*`, and `user.*` attributes; every panel filters on `service.name = 'bugsnag'`, the service name the integration assigns to forwarded events.

## Dashboard panels

### Stability Summary

#### Total Error Events

A count of all Bugsnag webhook events over the selected time range — a quick pulse on overall error activity.

#### Unhandled Crashes %

The share of events flagged unhandled by Bugsnag, computed as `A / B * 100` where A counts events with `bugsnag.error.unhandled = true` and B counts all events. The headline stability signal.

#### Affected Users

Count of distinct `user.id` values across error events — customer impact rather than raw volume.

#### App Versions Reporting

Count of distinct `app.version` values producing errors in the window.

### Error Trends

#### Error Events by Severity

Time-series of event counts grouped by mapped severity (`ERROR`/`WARN`/`INFO`), revealing spikes and their character.

#### Error Events by App Version

Time-series of event counts grouped by `app.version` — release regressions show up here immediately.

### Top Offenders

#### Top Exception Classes

Table of `exception.type` ranked by event count, so the highest-impact bugs surface first.

### Devices & Platforms

#### Errors by OS Version

Table of events grouped by `os.name` and `os.version`, catching failures tied to a platform update.

#### Errors by Device Model

Table of each device model's error event count, surfacing device-specific problems.

### Recent Activity

#### Recent Error Events

List of the latest Bugsnag events, newest first. Each record carries the exception class and message plus a `bugsnag.error.url` deep link back to the issue in Bugsnag.
