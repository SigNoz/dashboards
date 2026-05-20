#!/usr/bin/env python3
"""
Migrate SigNoz dashboard JSON templates from v3/v4 to v5 schema.

This is a Python port of the Go migration logic from:
  signoz/pkg/transition/migrate_dashboard.go
  signoz/pkg/transition/migrate_common.go

Usage:
  python3 migrate_to_v5.py                  # dry-run, shows what would change
  python3 migrate_to_v5.py --apply          # actually write the migrated files
  python3 migrate_to_v5.py --file foo.json  # migrate a single file
"""

import json
import os
import re
import sys
import argparse
import copy

# ---------------------------------------------------------------------------
# Traces intrinsic / calculated fields (from telemetrytraces/const.go)
# ---------------------------------------------------------------------------
ALL_SPECIAL_TRACE_FIELDS = {
    # IntrinsicFields
    "trace_id", "span_id", "trace_state", "parent_span_id", "flags",
    "name", "kind_string", "duration_nano", "status_code", "status_message",
    "status_code_string",
    # IntrinsicFieldsDeprecated
    "traceID", "spanID", "parentSpanID", "spanKind", "durationNano",
    "statusCode", "statusMessage", "statusCodeString", "kind", "timestamp",
    # CalculatedFields
    "response_status_code", "external_http_url", "http_url",
    "external_http_method", "http_method", "http_host",
    "db_name", "db_operation", "has_error", "is_remote",
    # CalculatedFieldsDeprecated
    "responseStatusCode", "externalHttpUrl", "httpUrl",
    "externalHttpMethod", "httpMethod", "httpHost",
    "dbName", "dbOperation", "hasError", "isRemote",
    "msgSystem", "dbSystem", "rpcSystem", "rpcService", "rpcMethod",
    "peerService",
}

NUMERIC_TYPES = {
    "int", "int8", "int16", "int32", "int64",
    "uint", "uint8", "uint16", "uint32", "uint64",
    "float", "float32", "float64",
    "number", "numeric", "integer",
}

# ---------------------------------------------------------------------------
# Variable detection & normalisation
# ---------------------------------------------------------------------------
VARIABLE_PATTERNS = [
    r'^\{.*\}$', r'^\{\{.*\}\}$', r'^\$.*$',
    r'^\[\[.*\]\]$', r'^\$\{\{.*\}\}$',
]

def is_variable(s):
    if not isinstance(s, str):
        return False
    s = s.strip()
    return any(re.match(p, s) for p in VARIABLE_PATTERNS)

def normalize_variable(s):
    s = s.strip()
    var_name = None
    if s.startswith("{{") and s.endswith("}}"):
        var_name = s[2:-2].lstrip(".").lstrip("$")
    elif s.startswith("{") and s.endswith("}"):
        var_name = s[1:-1].lstrip(".").lstrip("$")
    elif s.startswith("[[") and s.endswith("]]"):
        var_name = s[2:-2].lstrip(".")
    elif s.startswith("${{") and s.endswith("}}"):
        var_name = s[3:-2].lstrip(".").lstrip("$")
    elif s.startswith("$"):
        return s
    else:
        return s
    if var_name and " " in var_name:
        var_name = var_name.replace(" ", "")
    return "$" + var_name

# ---------------------------------------------------------------------------
# Value formatting
# ---------------------------------------------------------------------------
def format_value(value, data_type=""):
    if isinstance(value, str):
        if is_variable(value):
            return normalize_variable(value)
        if data_type in NUMERIC_TYPES:
            try:
                float(value)
                return value
            except ValueError:
                pass
        escaped = value.replace("'", "\\'")
        return f"'{escaped}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        if len(value) == 1:
            return format_value(value[0], data_type)
        return "[" + ", ".join(format_value(v, data_type) for v in value) + "]"
    else:
        return str(value)

# ---------------------------------------------------------------------------
# Condition / expression building
# ---------------------------------------------------------------------------
def build_condition(key, operator, value, key_metadata):
    data_type = key_metadata.get("dataType", "")
    fv = format_value(value, data_type)
    op_map = {
        "=": f"{key} = {fv}", "!=": f"{key} != {fv}",
        ">": f"{key} > {fv}", ">=": f"{key} >= {fv}",
        "<": f"{key} < {fv}", "<=": f"{key} <= {fv}",
        "like": f"{key} LIKE {fv}", "LIKE": f"{key} LIKE {fv}",
        "nlike": f"{key} NOT LIKE {fv}", "NOT LIKE": f"{key} NOT LIKE {fv}",
        "contains": f"{key} CONTAINS {fv}",
        "ncontains": f"{key} NOT CONTAINS {fv}",
        "regex": f"{key} REGEXP {fv}", "nregex": f"{key} NOT REGEXP {fv}",
        "exists": f"{key} EXISTS", "nexists": f"{key} NOT EXISTS",
        "has": f"has({key}, {fv})", "nhas": f"NOT has({key}, {fv})",
    }
    if operator in op_map:
        return op_map[operator]
    if operator in ("in", "IN"):
        return f"{key} IN {fv}"
    if operator in ("nin", "NOT IN"):
        return f"{key} NOT IN {fv}"
    return f"{key} {operator} {fv}"

def build_expression(items, op, data_source):
    if not items:
        return ""
    conditions = []
    for item in items:
        if not isinstance(item, dict):
            continue
        key = item.get("key")
        operator = item.get("op")
        value = item.get("value")
        if not isinstance(key, dict) or not operator:
            continue
        key_str = key.get("key", "")
        if not key_str:
            continue
        condition = build_condition(key_str, operator, value, key)
        if condition:
            conditions.append(condition)
    if not conditions:
        return ""
    if len(conditions) == 1:
        return conditions[0]
    return "(" + f" {op} ".join(conditions) + ")"

# ---------------------------------------------------------------------------
# Aggregation expression building (for logs/traces)
# ---------------------------------------------------------------------------
def build_aggregation_expression(operator, attribute):
    key = attribute.get("key", "")
    if operator == "count":
        return "count()"
    if operator == "count_distinct":
        return f"count_distinct({key})" if key else "count_distinct()"
    if operator == "sum_rate":
        return f"sum(rate({key}))" if key else "sum(rate())"
    if key:
        return f"{operator}({key})"
    return f"{operator}()"

# ---------------------------------------------------------------------------
# Core migration logic
# ---------------------------------------------------------------------------
def create_aggregations(query_data, version, widget_type):
    agg_op = query_data.get("aggregateOperator", "")
    agg_attr = query_data.get("aggregateAttribute", {})
    data_source = query_data.get("dataSource", "")
    if not isinstance(agg_attr, dict):
        agg_attr = {}
    if agg_op == "noop" and data_source != "metrics":
        return False
    if not agg_op and not agg_attr:
        return False

    aggregation = {}
    if data_source == "metrics":
        if version == "v4":
            if "spaceAggregation" not in query_data:
                query_data["spaceAggregation"] = agg_op
            aggregation = {
                "metricName": agg_attr.get("key", ""),
                "temporality": query_data.get("temporality"),
                "timeAggregation": query_data.get("timeAggregation"),
                "spaceAggregation": query_data.get("spaceAggregation"),
            }
            if "reduceTo" in query_data:
                aggregation["reduceTo"] = query_data["reduceTo"]
        else:
            agg_map = {
                "sum_rate": ("rate", "sum", "sum"), "rate_sum": ("rate", "sum", "sum"),
                "avg_rate": ("rate", "avg", "avg"), "rate_avg": ("rate", "avg", "avg"),
                "min_rate": ("rate", "min", "min"), "rate_min": ("rate", "min", "min"),
                "max_rate": ("rate", "max", "max"), "rate_max": ("rate", "max", "max"),
                "hist_quantile_50": ("", "p50", "avg"), "hist_quantile_75": ("", "p75", "avg"),
                "hist_quantile_90": ("", "p90", "avg"), "hist_quantile_95": ("", "p95", "avg"),
                "hist_quantile_99": ("", "p99", "avg"),
                "rate": ("rate", "sum", "sum"),
                "min": ("min", "min", "min"), "max": ("max", "max", "max"),
                "avg": ("avg", "avg", "avg"), "sum": ("sum", "sum", "sum"),
                "count": ("count", "sum", "sum"), "count_distinct": ("count_distinct", "sum", "sum"),
                "noop": ("max", "max", "max"),
            }
            time_agg, space_agg, reduce_to = agg_map.get(agg_op, ("avg", "avg", "avg"))
            aggregation = {
                "metricName": agg_attr.get("key", ""),
                "temporality": query_data.get("temporality"),
                "timeAggregation": time_agg,
                "spaceAggregation": space_agg,
            }
            if widget_type == "table":
                aggregation["reduceTo"] = reduce_to
            elif "reduceTo" in query_data:
                aggregation["reduceTo"] = query_data["reduceTo"]
    elif data_source in ("logs", "traces"):
        expression = build_aggregation_expression(agg_op, agg_attr)
        aggregation = {"expression": expression}
    else:
        return False

    query_data["aggregations"] = [aggregation]
    return True

def group_by_exists_expr(query_data):
    group_by = query_data.get("groupBy", [])
    if not isinstance(group_by, list):
        return ""
    exprs = []
    for item in group_by:
        if not isinstance(item, dict):
            continue
        key = item.get("key", "")
        if key:
            exprs.append(f"{key} EXISTS")
            if key in ALL_SPECIAL_TRACE_FIELDS:
                item.pop("type", None)
    return " AND ".join(exprs)

def create_filter_expression(query_data):
    filters = query_data.get("filters")
    if not isinstance(filters, dict):
        return False
    items = filters.get("items", [])
    if not isinstance(items, list) or not items:
        return False
    op = filters.get("op", "AND")
    data_source = query_data.get("dataSource", "")
    expression = build_expression(items, op, data_source)
    if expression:
        gb_exists = group_by_exists_expr(query_data)
        if gb_exists and data_source != "metrics":
            expression += " " + gb_exists
        query_data["filter"] = {"expression": expression}
        del query_data["filters"]
        return True
    return False

def fix_group_by(query_data):
    group_by = query_data.get("groupBy", [])
    if not isinstance(group_by, list):
        return False
    for item in group_by:
        if not isinstance(item, dict):
            continue
        key = item.get("key", "")
        if key in ALL_SPECIAL_TRACE_FIELDS:
            item.pop("type", None)
    return False

def create_having_expression(query_data):
    having = query_data.get("having", [])
    if not isinstance(having, list) or not having:
        query_data["having"] = {"expression": ""}
        return True
    data_source = query_data.get("dataSource", "")
    expression = build_expression(having, "AND", data_source)
    query_data["having"] = {"expression": expression}
    return True

def order_by_expr(query_data):
    agg_op = query_data.get("aggregateOperator", "")
    agg_attr = query_data.get("aggregateAttribute", {})
    data_source = query_data.get("dataSource", "")
    if agg_op == "noop" or not agg_op or not isinstance(agg_attr, dict):
        return None
    if data_source == "metrics":
        aggs = query_data.get("aggregations", [])
        if not aggs or not isinstance(aggs, list):
            return None
        agg = aggs[0] if aggs else {}
        if not isinstance(agg, dict):
            return None
        space_agg = agg.get("spaceAggregation", "")
        return f"{space_agg}({agg_attr.get('key', '')})" if space_agg else None
    elif data_source in ("logs", "traces"):
        return build_aggregation_expression(agg_op, agg_attr)
    return None

def update_query_data(query_data, version, widget_type):
    updated = False
    agg_op = query_data.get("aggregateOperator", "")
    has_aggregation = agg_op and agg_op != "noop"

    if create_aggregations(query_data, version, widget_type):
        updated = True
    if create_filter_expression(query_data):
        updated = True
    fix_group_by(query_data)
    if create_having_expression(query_data):
        updated = True

    if has_aggregation:
        order_by = query_data.get("orderBy", [])
        if isinstance(order_by, list):
            new_order_by = []
            for order in order_by:
                if not isinstance(order, dict):
                    continue
                col_name = order.get("columnName", "")
                if col_name in ("timestamp", "samples", "id"):
                    continue
                if col_name == "#SIGNOZ_VALUE":
                    expr = order_by_expr(query_data)
                    if expr:
                        order["columnName"] = expr
                else:
                    group_by = query_data.get("groupBy", [])
                    if isinstance(group_by, list):
                        if not any(isinstance(gb, dict) and gb.get("key") == col_name for gb in group_by):
                            continue
                new_order_by.append(order)
            query_data["orderBy"] = new_order_by
            updated = True
    else:
        data_source = query_data.get("dataSource", "")
        order_by = query_data.get("orderBy", [])
        if isinstance(order_by, list):
            new_order_by = []
            for order in order_by:
                if not isinstance(order, dict):
                    continue
                col_name = order.get("columnName", "")
                if col_name in ("id", "timestamp") and data_source in ("traces", "logs"):
                    continue
                new_order_by.append(order)
            query_data["orderBy"] = new_order_by
            updated = True

    functions = query_data.get("functions", [])
    if isinstance(functions, list) and functions:
        v5_functions = []
        for fn in functions:
            if not isinstance(fn, dict):
                continue
            v5_fn = {"name": fn.get("name", "")}
            args = fn.get("args", [])
            if isinstance(args, list):
                v5_fn["args"] = [{"name": "", "value": arg} for arg in args]
            named_args = fn.get("namedArgs", {})
            if isinstance(named_args, dict):
                existing = v5_fn.get("args", [])
                for name, value in named_args.items():
                    existing.append({"name": name, "value": value})
                v5_fn["args"] = existing
            v5_functions.append(v5_fn)
        query_data["functions"] = v5_functions
        updated = True

    for key in ["aggregateOperator", "aggregateAttribute", "temporality",
                "timeAggregation", "spaceAggregation", "reduceTo",
                "ShiftBy", "IsAnomaly", "QueriesUsedInFormula", "seriesAggregation"]:
        query_data.pop(key, None)
    return updated

def update_widget(widget, version):
    query = widget.get("query")
    if not isinstance(query, dict):
        return False
    if query.get("queryType") in ("promql", "clickhouse_sql"):
        return False
    builder = query.get("builder")
    if not isinstance(builder, dict):
        return False
    query_data_list = builder.get("queryData", [])
    if not isinstance(query_data_list, list):
        return False
    widget_type = widget.get("panelTypes", "")
    updated = False
    for qd in query_data_list:
        if isinstance(qd, dict):
            if update_query_data(qd, version, widget_type):
                updated = True
    return updated

def migrate_dashboard(dashboard_data):
    version = dashboard_data.get("version", "")
    if version == "v5":
        return False
    updated = False
    variables = dashboard_data.get("variables")
    if isinstance(variables, dict):
        for var in variables.values():
            if isinstance(var, dict):
                name = var.get("name", "")
                if isinstance(name, str) and " " in name:
                    var["name"] = name.replace(" ", "")
                    updated = True
    widgets = dashboard_data.get("widgets", [])
    if isinstance(widgets, list):
        for widget in widgets:
            if isinstance(widget, dict):
                if update_widget(widget, version):
                    updated = True
    dashboard_data["version"] = "v5"
    return True

# ---------------------------------------------------------------------------
# Format-preserving JSON serialization
# ---------------------------------------------------------------------------
def format_preserving_dumps(data, original_text):
    """
    Serialize JSON preserving the original file's formatting style.
    Detects separator style and re-collapses structures that were
    compact in the original, so only actual schema changes show in diffs.
    """
    sep = " : " if '" : ' in original_text[:1000] else ": "
    raw = json.dumps(data, indent=2, ensure_ascii=False, separators=(",", sep))

    # Collect compact patterns from original (key: [...] or key: {...} on one line)
    compact_keys = set()
    for line in original_text.split("\n"):
        stripped = line.strip().rstrip(",")
        m = re.match(r'^"([^"]+)"\s*:\s*(\[.*\]|\{.*\})$', stripped)
        if m:
            compact_keys.add(m.group(1))

    if not compact_keys:
        return raw

    lines = raw.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        if stripped.endswith("[") or stripped.endswith("{"):
            key_m = re.search(r'"([^"]+)"\s*:\s*[\[{]\s*$', stripped)
            if key_m and key_m.group(1) in compact_keys:
                opener = "[" if stripped.endswith("[") else "{"
                closer = "]" if opener == "[" else "}"
                depth = 1
                j = i + 1
                while j < len(lines) and depth > 0:
                    for ch in lines[j]:
                        if ch == opener:
                            depth += 1
                        elif ch == closer:
                            depth -= 1
                            if depth == 0:
                                break
                    if depth > 0:
                        j += 1
                if depth == 0:
                    parts = [lines[k].strip() for k in range(i + 1, j + 1)]
                    inner = " ".join(parts)
                    candidate = stripped + " " + inner
                    if len(candidate) <= 250:
                        result.append(candidate)
                        i = j + 1
                        continue
        result.append(line)
        i += 1
    return "\n".join(result)

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def find_dashboard_files(root):
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".json"):
                results.append(os.path.join(dirpath, f))
    return sorted(results)

def main():
    parser = argparse.ArgumentParser(description="Migrate SigNoz dashboards to v5 schema")
    parser.add_argument("--apply", action="store_true", help="Actually write migrated files (default: dry-run)")
    parser.add_argument("--file", help="Migrate a single file instead of all")
    parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)),
                        help="Root directory to scan for dashboards")
    args = parser.parse_args()

    files = [args.file] if args.file else find_dashboard_files(args.root)
    stats = {"total": 0, "already_v5": 0, "migrated": 0, "skipped": 0, "errors": 0}

    for filepath in files:
        try:
            with open(filepath, "r") as f:
                original_text = f.read()
            data = json.loads(original_text)
        except (json.JSONDecodeError, IOError) as e:
            print(f"  ERROR: {filepath}: {e}")
            stats["errors"] += 1
            continue

        if "widgets" not in data and "layout" not in data:
            stats["skipped"] += 1
            continue

        stats["total"] += 1
        version = data.get("version", "none")
        if version == "v5":
            stats["already_v5"] += 1
            continue

        title = data.get("title", os.path.basename(filepath))
        migrated = copy.deepcopy(data)
        try:
            changed = migrate_dashboard(migrated)
        except Exception as e:
            print(f"  ERROR migrating {filepath}: {e}")
            stats["errors"] += 1
            continue

        if changed or migrated.get("version") == "v5":
            stats["migrated"] += 1
            rel = os.path.relpath(filepath, args.root)
            if args.apply:
                output = format_preserving_dumps(migrated, original_text)
                if not output.endswith("\n"):
                    output += "\n"
                with open(filepath, "w") as f:
                    f.write(output)
                print(f"  MIGRATED: {rel} ({version} -> v5)")
            else:
                print(f"  WOULD MIGRATE: {rel} ({version} -> v5) [{title}]")

    print()
    print("=" * 60)
    print(f"  Total dashboards:  {stats['total']}")
    print(f"  Already v5:        {stats['already_v5']}")
    print(f"  Migrated:          {stats['migrated']}")
    print(f"  Errors:            {stats['errors']}")
    print(f"  Non-dashboard:     {stats['skipped']}")
    print("=" * 60)
    if not args.apply and stats["migrated"] > 0:
        print("\n  This was a DRY RUN. Use --apply to write changes.")

if __name__ == "__main__":
    main()
