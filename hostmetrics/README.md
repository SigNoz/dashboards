# HostMetrics Dashboard

The Host Metrics dashboard consists of combination of charts that would help to monitor metrics of the instances.

## Dashboard with Variable

For a generic dashboard with `hostname` variable, you can import the `hostmetrics-with-variable.json`
file in SigNoz UI.

In case of **Kubernetes Nodes**, import the `hostmetrics-k8s.json` file in SigNoz UI.

## Static Dashboard

To generate a static dashboard with fixed `hostname`, follow the instructions below:

### Configurations

Supported environment variables:

- `HOSTNAME` : Hostname of the machine. default=`HOSTNAME` of the runtime environment
- `DASHBOARD_TITLE` : Title of Dashboard. default=`HostMetrics Dashboard for $HOSTNAME` template
- `BEARER_TOKEN` : If set, imports generated dashboard in SigNoz. If not set, dashboard JSON file is generated locally.
- `SIGNOZ_ENDPOINT` : Endpoint of SigNoz to import dashboard. default=`http://localhost:3301`

### Import using Script

You can use the following command to generate the dashboard JSON:

```bash
curl -sL https://github.com/SigNoz/Dashboards/raw/main/hostmetrics/hostmetrics-import.sh \
    | HOSTNAME="test-instance-1" DASHBOARD_TITLE="HostMetrics Dashboard for test-instance-1" bash
```

Also, you can import generated dashboard JSON in SigNoz using the same:

```bash
curl -sL https://github.com/SigNoz/Dashboards/raw/main/hostmetrics/hostmetrics-import.sh \
    | SIGNOZ_ENDPOINT="http://localhost:3301" BEARER_TOKEN="<bearer-token-here>" bash

```

Alternatively, you can use the clone the repository and run the script:

```bash
git clone https://github.com/SigNoz/Dashboards.git

cd hostmetrics

cat hostmetrics-import.sh \
    | HOSTNAME="test-instance-2" DASHBOARD_TITLE="HostMetrics Dashboard for test-instance-2" bash
```

To generate the dashboard, open SigNoz UI and upload the generated JSON.


_*Notes:_
- In case `HOSTNAME` variable is skipped, it will select the current machine hostname using the default shell variable `HOSTNAME`.
- If `DASHBOARD_TITLE` variable is skipped, it will create title with the template: `HostMetrics Dashboard for <hostname>`.
- Dashboard uuid is randomly generated in server-side. We need not pass uuid.
- To skip the hostname label filter from all charts, set the `HOSTNAME` variable to an empty string `""`.
