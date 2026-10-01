#!/usr/bin/env python3
"""Summarize local accepted image requests without API calls or request-state writes.

Run: python3 episodes/first-day/build/generation_ledger.py
The public receipt contains only request ID, endpoint, batch and response status
per request. Request payloads, CDN/status/response URLs and credentials are never
copied. Historical retries of the same accepted ID count once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
STATUS_RANK = {
    "pending_or_unresolved_no_response": 0,
    "response_recorded_no_image": 1,
    "error_response_recorded": 2,
    "completed_image_response": 3,
}


def safe_endpoint(value) -> str:
    """Model paths are public; unexpected URL/query/credential forms are not."""
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+", value):
        return value
    return "unrecognized_endpoint_not_exported"


def response_status(record: dict) -> str:
    response = record.get("response")
    if not response:
        return "pending_or_unresolved_no_response"
    if isinstance(response, dict):
        if isinstance(response.get("images"), list) and response["images"]:
            return "completed_image_response"
        if response.get("error") or response.get("errors") or response.get("detail"):
            return "error_response_recorded"
    return "response_recorded_no_image"


def collect_builtin(build_root: Path) -> dict:
    """Inventory distinct recorded output bytes; never infer tool-call counts."""
    sources = [build_root / "portrait_provenance.json",
               build_root / "builtin_image_edits.json"]
    sources.extend(sorted(build_root.glob("repair_batch*.json")))
    outputs, diagnostics, copies = {}, [], []
    valid_hash = re.compile(r"[0-9a-f]{64}")
    valid_id = re.compile(r"[A-Za-z0-9_-]{1,64}")
    for path in sources:
        name = path.name
        if not path.is_file():
            diagnostics.append(f"{name}: not available")
            continue
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            records = document if isinstance(document, list) else next(
                (document[key] for key in ("assets", "edits", "jobs") if key in document), None)
        except (OSError, ValueError, KeyError, TypeError):
            records = None
        if not isinstance(records, list):
            diagnostics.append(f"{name}: unreadable or unsupported schema")
            continue
        provenance = f"episodes/first-day/build/{name}"
        for record in records:
            if not isinstance(record, dict):
                diagnostics.append(f"{name}: skipped non-object record")
                continue
            identity = record.get("id")
            if not isinstance(identity, str) or not valid_id.fullmatch(identity):
                diagnostics.append(f"{name}: skipped invalid asset ID")
                continue
            output_hash = record.get("output_sha256", record.get("sha256"))
            if not isinstance(output_hash, str) or not valid_hash.fullmatch(output_hash):
                diagnostics.append(f"{name}/{identity}: no valid recorded output SHA; not counted")
                continue
            if record.get("new_generation") is False:
                copies.append({"asset_id": identity, "output_sha256": output_hash,
                               "provenance_file": provenance, "alias_of": record.get("alias_of"),
                               "counted_as_generation": False})
                continue
            kind = "base_portrait" if name == "portrait_provenance.json" else "targeted_scene_edit"
            asset = next((record[key] for key in ("out", "path", "candidate", "output_path")
                          if isinstance(record.get(key), str)), None)
            integrity = "not_checked"
            if isinstance(asset, str) and asset.startswith("episodes/first-day/"):
                resolved = (ROOT / asset).resolve()
                if resolved.is_relative_to((ROOT / "episodes/first-day").resolve()):
                    if not resolved.is_file():
                        integrity = "recorded_output_missing"
                    else:
                        actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
                        integrity = "matches_recorded_output" if actual == output_hash else "recorded_output_hash_mismatch"
            row = outputs.setdefault(output_hash, {"output_sha256": output_hash,
                                     "kind": kind, "asset_ids": set(), "provenance_records": []})
            row["asset_ids"].add(identity)
            row["provenance_records"].append({"asset_id": identity,
                 "provenance_file": provenance, "recorded_asset_integrity": integrity})
    rows = []
    for output_hash, row in sorted(outputs.items()):
        row["asset_ids"] = sorted(row["asset_ids"])
        row["preserved_output_verified"] = any(
            source["recorded_asset_integrity"] == "matches_recorded_output"
            for source in row["provenance_records"])
        rows.append(row)
    counts = Counter(row["kind"] for row in rows)
    return {
        "recorded_generation_output_count": len(rows),
        "counts_by_kind": dict(sorted(counts.items())),
        "records": rows,
        "intentional_copies_excluded_from_generation_count": copies,
        "diagnostics": diagnostics,
        "workflow": "subscription built-in image generation",
        "usage_or_cost": "unknown; tool did not expose usage or price; separate from fal estimates",
        "limits": "Counts are distinct recorded generation output SHA-256 values across portrait, "
                  "central edit and repair-batch provenance, including preserved intermediate outputs. "
                  "Aliases explicitly marked new_generation=false are excluded. Multiple records of "
                  "the same bytes count once. This is not a count of billing events, calls or quota "
                  "usage. Additional unrecorded requests cannot be inferred. File-hash agreement "
                  "does not itself approve pixels.",
    }


def collect(scan_root: Path, build_root: Path = ROOT / "episodes/first-day/build") -> dict:
    requests: dict[str, dict] = {}
    diagnostics = Counter()
    for log_dir in sorted(scan_root.rglob("luma_log")):
        if not log_dir.is_dir():
            continue
        batch = log_dir.parent.relative_to(scan_root).as_posix()
        for path in sorted(log_dir.iterdir()):
            if not path.is_file():
                continue
            name = path.name
            if any(part in name for part in (".payload.", ".redo.", ".lock")):
                diagnostics["excluded_sidecar_files"] += 1
                continue
            history = name.endswith(".history.jsonl")
            if not (history or name.endswith(".json")):
                continue
            diagnostics["scanned_record_files"] += 1
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                diagnostics["unreadable_files"] += 1
                continue
            chunks = content.splitlines() if history else [content]
            for chunk in chunks:
                if not chunk.strip():
                    continue
                try:
                    record = json.loads(chunk)
                except ValueError:
                    # An active writer can leave a partial last history line.
                    diagnostics["unparseable_records"] += 1
                    continue
                if not isinstance(record, dict):
                    diagnostics["non_object_records"] += 1
                    continue
                request_id = record.get("request_id")
                if not isinstance(request_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{8,128}", request_id):
                    diagnostics["records_without_accepted_request_id"] += 1
                    continue
                diagnostics["accepted_id_record_occurrences"] += 1
                endpoint = safe_endpoint(record.get("endpoint"))
                status = response_status(record)
                if request_id not in requests:
                    requests[request_id] = {"id": request_id, "endpoints": set(), "batches": set(), "response_status": status}
                row = requests[request_id]
                row["endpoints"].add(endpoint)
                row["batches"].add(batch)
                if STATUS_RANK[status] > STATUS_RANK[row["response_status"]]:
                    row["response_status"] = status
    # Saved diagnostic response receipts live outside runner logs. Pair a terminal
    # status receipt to its response receipt by filename; export neither body.
    for status_path in sorted((scan_root / "qa").glob("*_status_url_result.json")):
        response_path = status_path.with_name(status_path.name.replace("_status_url_result.json", "_response_url_result.json"))
        if not response_path.is_file():
            continue
        try:
            status_receipt = json.loads(status_path.read_text(encoding="utf-8"))
            response_receipt = json.loads(response_path.read_text(encoding="utf-8"))
            status_body = status_receipt.get("body", {})
            if isinstance(status_body, str):
                status_body = json.loads(status_body)
            request_id = status_body.get("request_id")
            http_status = response_receipt.get("http_status")
            if (request_id in requests and status_body.get("status") == "COMPLETED"
                    and isinstance(http_status, int) and 400 <= http_status < 600):
                row = requests[request_id]
                if STATUS_RANK[row["response_status"]] < STATUS_RANK["error_response_recorded"]:
                    row["response_status"] = "error_response_recorded"
                diagnostics["terminal_error_receipt_pairs"] += 1
        except (OSError, ValueError, TypeError, AttributeError):
            diagnostics["unreadable_diagnostic_receipt_pairs"] += 1
    # Optional sanitized receipts may be written by the director after a terminal
    # provider failure. Their ID must already be present in an accepted local log.
    terminal_path = scan_root / "qa" / "terminal_image_results.json"
    if terminal_path.is_file():
        try:
            terminal = json.loads(terminal_path.read_text(encoding="utf-8"))
            terminal = terminal if isinstance(terminal, list) else terminal.get("results", [])
            for receipt in terminal:
                request_id = receipt.get("request_id")
                http_status = receipt.get("http_status")
                if (request_id in requests and receipt.get("status") == "COMPLETED"
                        and isinstance(http_status, int) and 400 <= http_status < 600):
                    row = requests[request_id]
                    if STATUS_RANK[row["response_status"]] < STATUS_RANK["error_response_recorded"]:
                        row["response_status"] = "error_response_recorded"
                    diagnostics["sanitized_terminal_error_receipts"] += 1
        except (OSError, ValueError, TypeError, AttributeError):
            diagnostics["unreadable_sanitized_terminal_receipts"] += 1
    rows = []
    for request_id in sorted(requests):
        row = requests[request_id]
        endpoints, batches = sorted(row["endpoints"]), sorted(row["batches"])
        rows.append({
            "id": request_id,
            "endpoint": endpoints[0] if len(endpoints) == 1 else endpoints,
            "batch": batches[0] if len(batches) == 1 else batches,
            "response_status": row["response_status"],
        })
    count = len(rows)
    diagnostics["distinct_accepted_request_ids"] = count
    diagnostics["duplicate_accepted_id_records_not_double_counted"] = diagnostics["accepted_id_record_occurrences"] - count
    status_counts = Counter(row["response_status"] for row in rows)
    prices = []
    for label, rate in (("authenticated_rate_supplied_for_this_production", "0.003"), ("public_rate_supplied_for_this_production", "0.102")):
        prices.append({"rate_basis": label, "usd_per_assumed_image": float(Decimal(rate)), "assumed_image_count": count, "estimated_usd": float(Decimal(rate) * count), "is_billed_cost": False})
    return {
        "schema_version": 3,
        "episode": "first-day",
        "scope": "Local work/first-day/**/luma_log/*.json and *.history.jsonl, with saved qa terminal-error receipts; accepted request IDs only; no API queries.",
        "requests": rows,
        "counts": dict(sorted(diagnostics.items())),
        "response_status_counts": dict(sorted(status_counts.items())),
        "estimates": prices,
        "estimate_basis": "One image assumed per distinct accepted request, including pending/unresolved and any error responses. These are arithmetic scenarios at supplied rates, not billed cost or confirmed charges. Same-ID polling/recovery records count once; new IDs for retakes count separately.",
        "director_observations_not_provider_receipts": [
            {"request_id": row["id"], "batch": row["batch"],
             "observation": "The director observed terminal HTTP 422 on the recovery request and subsequent same-ID response retrievals. The provider response was visible in tool output but was not saved as a local receipt; the local-evidence status therefore remains pending_or_unresolved_no_response. No active provider request or billing outcome is inferred."}
            for row in rows if row["batch"] == "recovery01"
            and row["response_status"] == "pending_or_unresolved_no_response"
        ],
        "status_limits": "completed_image_response means a local response contains images, not that pixels passed QA. pending_or_unresolved_no_response is local evidence only: the provider may have completed or failed after the last saved record. Pre-submission records without an accepted ID cannot be enumerated as accepted paid requests.",
        "builtin_generations": collect_builtin(build_root),
        "privacy": "Per-request fields are restricted to id, endpoint, batch and response_status. Payloads, response contents, CDN URLs, status URLs, response URLs and keys are excluded.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan-root", type=Path, default=ROOT / "work/first-day")
    parser.add_argument("--out", type=Path, default=ROOT / "episodes/first-day/build/generation_ledger.json")
    args = parser.parse_args()
    report = collect(args.scan_root.resolve())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    pending = args.out.with_name(args.out.name + ".tmp")
    pending.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pending.replace(args.out)
    print(json.dumps({"distinct_accepted_requests": report["counts"]["distinct_accepted_request_ids"], "response_status_counts": report["response_status_counts"], "estimates": report["estimates"]}, indent=2))


if __name__ == "__main__":
    main()
