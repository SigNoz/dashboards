#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")";

# Set the hostname filter if hostname is passed
if [[ -z $HOSTNAME ]]; then
    HOSTNAME="ALL"
else
    HOSTNAME_FILTER='host_name=\"'${HOSTNAME}'\"'
    HOSTNAME_FILTER_COMMA="${HOSTNAME_FILTER},"
fi

# Set Dashboard Title
if [[ -z $DASHBOARD_TITLE ]]; then
    DASHBOARD_TITLE="HostMetrics Dashboard - $HOSTNAME"
fi

# Set the default signoz endpoint if not set
if [[ -z $SIGNOZ_ENDPOINT ]]; then
    SIGNOZ_ENDPOINT="http://localhost:3301"
fi

# If bearer token is set, generate dashboard JSON file
# If bearer token not set, create dashboard JSON and import in SigNoz
if [[ -z $BEARER_TOKEN ]]; then
    FAIL_ACTION="generate"
    SUCCESS_ACTION="generated"
    (cat hostmetrics-template.json 2>/dev/null || curl -sL https://github.com/SigNoz/benchmark/raw/main/dashboards/hostmetrics/hostmetrics-template.json) | \
        DASHBOARD_TITLE="${DASHBOARD_TITLE}" \
        HOSTNAME_FILTER="${HOSTNAME_FILTER}" \
        HOSTNAME_FILTER_COMMA="${HOSTNAME_FILTER_COMMA}" \
        envsubst > signoz-hostmetrics-${HOSTNAME}.json
else
    FAIL_ACTION="import"
    SUCCESS_ACTION="imported"
    (cat hostmetrics-template.json 2>/dev/null || curl -sL https://github.com/SigNoz/benchmark/raw/main/dashboards/hostmetrics/hostmetrics-template.json) | \
        DASHBOARD_TITLE="${DASHBOARD_TITLE}" \
        HOSTNAME_FILTER="${HOSTNAME_FILTER}" \
        HOSTNAME_FILTER_COMMA="${HOSTNAME_FILTER_COMMA}" \
        envsubst | curl --fail --silent --output /dev/null --show-error --location --request POST \
        --header 'Accept: application/json, text/plain, */*' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer ${BEARER_TOKEN}" \
        --data-binary @- "${SIGNOZ_ENDPOINT}/api/v1/dashboards"
fi

if [ $? -ne 0 ]; then
    echo "❌ Failed to ${FAIL_ACTION} Host Metrics dashboard"
else
    echo "✅ Succesfully ${SUCCESS_ACTION} Host Metrics dashboard: signoz-hostmetrics-${HOSTNAME}.json"
fi