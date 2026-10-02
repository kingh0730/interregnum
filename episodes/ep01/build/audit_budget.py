"""Read-only local estimate of episode generation cost and request provenance.

No network, submissions, account mutations or file writes. JSON goes to stdout.
Use --final after image generation: unresolved request logs then fail the audit.
Captured prices estimate usage; this does not claim invoice reconciliation.
"""
import argparse
import collections
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / "episodes/ep01/build"
WORK = ROOT / "work/ep01"


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return str(path.relative_to(ROOT))


def requested_units(endpoint, payload, unit):
    if unit == "images":
        return float(payload.get("num_images", 1))
    if unit == "seconds":
        return float(payload.get("duration_seconds", payload.get("duration", 0)))
    if unit == "minutes":
        if "composition_plan" in payload:
            return sum(s["duration_ms"] for s in payload["composition_plan"]["sections"]) / 60000
        return float(payload.get("music_length_ms", payload.get("duration_ms", 0))) / 60000
    raise ValueError(f"Unsupported captured unit: {endpoint}: {unit}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    price_path = WORK / "prices.json"
    price_data = read(price_path)
    prices = {key: value["prices"][0] for key, value in price_data.items()}
    incident_path = BUILD / "image_incidents.json"
    incidents = read(incident_path)
    failed_images = {row["request_id"]: row for row in incidents["tests"]
                     if row["result"] == "terminal_HTTP_422"}
    by_request = {}
    # Payload copies, manifests and derived selections do not have a top-level
    # request_id + endpoint + payload triplet, so they are not double-counted.
    for directory in (BUILD, WORK):
        for path in sorted(directory.rglob("*.json")):
            try:
                data = read(path)
            except (ValueError, OSError):
                continue
            if not isinstance(data, dict) or not all(data.get(key) for key in ("request_id", "endpoint", "payload")):
                continue
            request_id = data["request_id"]
            if request_id in by_request:
                old, old_path = by_request[request_id]
                assert old["endpoint"] == data["endpoint"] and old["payload"] == data["payload"], f"Request {request_id} has contradictory provenance"
                if data.get("response") and not old.get("response"):
                    by_request[request_id] = (data, path)
            else:
                by_request[request_id] = (data, path)
    rows = []
    missing_prices = []
    motion_requests = []
    for request_id, (data, path) in by_request.items():
        endpoint = data["endpoint"]
        if "video" in endpoint or "/ray" in endpoint:
            motion_requests.append(relative(path))
        if endpoint not in prices:
            missing_prices.append(endpoint)
            continue
        price = prices[endpoint]
        unit = price["unit"]
        units = requested_units(endpoint, data["payload"], unit)
        assert units > 0, f"Unpriced units in {relative(path)}"
        response = data.get("response", {})
        successful = bool(response.get("images")) if unit == "images" else bool(response.get("audio") or response.get("video"))
        known_failed = request_id in failed_images
        evidence = "image_incidents.json" if known_failed else None
        process = path.with_suffix(".process.log")
        if not successful and process.exists() and "HTTP Error 422" in process.read_text():
            known_failed, evidence = True, relative(process)
        # A completed response is required to call an output successful. Missing
        # response data by itself is not classified as failure.
        state = "successful_output" if successful else "terminal_HTTP_422" if known_failed else "unresolved_no_response"
        success_units = len(response["images"]) if successful and unit == "images" else units if successful else 0
        rows.append({
            "request_id": request_id, "asset_log": relative(path), "log_sha256": digest(path),
            "endpoint": endpoint, "state": state, "failure_evidence": evidence,
            "captured_unit": unit, "unit_price_usd": price["unit_price"],
            "requested_units": units, "successful_units": success_units,
            "successful_output_estimate_usd": round(success_units * price["unit_price"], 6),
            "all_requested_units_estimate_usd": round(units * price["unit_price"], 6),
        })
    rows.sort(key=lambda row: row["asset_log"])
    groups = {}
    for endpoint in sorted({row["endpoint"] for row in rows}):
        selected = [row for row in rows if row["endpoint"] == endpoint]
        groups[endpoint] = {
            "unique_requests": len(selected),
            "states": dict(collections.Counter(row["state"] for row in selected)),
            "unit": selected[0]["captured_unit"],
            "successful_units": round(sum(row["successful_units"] for row in selected), 6),
            "requested_units": round(sum(row["requested_units"] for row in selected), 6),
            "successful_output_estimate_usd": round(sum(row["successful_output_estimate_usd"] for row in selected), 6),
            "all_requested_units_estimate_usd": round(sum(row["all_requested_units_estimate_usd"] for row in selected), 6),
        }
    dialogue = [read(path) for path in (WORK / "audio/dialogue").glob("*.request.json")]
    complete_dialogue = [row for row in dialogue if row.get("state") == "complete"]
    edits_path = BUILD / "codex_edits.json"
    edits = read(edits_path) if edits_path.exists() else []
    expected_master = "cd40a5cd19413d5b95ca1e10b269dc0e11b403382e7207fd24b5276feb57622d"
    master_path = WORK / "audio/master_mix.wav"
    master_hash = digest(master_path)
    reference_audit_path = BUILD / "reference_audit.json"
    reference_checks = [{"id": row["id"], "matches_approved_hash": digest(ROOT / row["path"]) == row["sha256"]}
                        for row in read(reference_audit_path)["references"]]
    early_sheets = [{"id": row["id"], "out": row["path"], "sha256": row["sha256"],
                     "output_present": (ROOT / row["path"]).is_file(),
                     "evidence": "Approved derived character sheet recorded in reference_audit.json; separate exact tool-call receipt absent."}
                    for row in read(reference_audit_path)["references"] if row["id"] in {"eda_sheet", "sen_sheet"}]
    unresolved = [row["asset_log"] for row in rows if row["state"] == "unresolved_no_response"]
    result = {
        "schema_version": 1, "snapshot_at_utc": datetime.now(timezone.utc).isoformat(),
        "final_requested": args.final,
        "method": "Read-only local request inventory, deduplicated by request_id. Resumed polls/GETs are not new paid requests. Captured rates are applied to returned output units and, separately, every requested unit.",
        "price_source": relative(price_path), "price_source_sha256": digest(price_path),
        "invoice_reconciled": False,
        "fal": {"unique_requests": len(rows), "by_endpoint": groups,
                "successful_output_estimate_usd": round(sum(row["successful_output_estimate_usd"] for row in rows), 6),
                "conservative_all_requested_units_estimate_usd": round(sum(row["all_requested_units_estimate_usd"] for row in rows), 6),
                "request_provenance": rows},
        "direct_voice_plan_usage": {
            "dialogue_requests": len(dialogue), "complete_dialogue_requests": len(complete_dialogue),
            "requested_text_characters": sum(len(row["body"].get("text", "")) for row in dialogue),
            "models": sorted({row["body"].get("model_id") for row in dialogue}),
            "cash_estimate_usd": None,
            "limit": "Designed-voice dialogue used the authorized existing paid plan. Text character count is not a billed-credit calculation. Voice design/preview usage and plan invoice costs are not priced here.",
        },
        "codex_image_edits": {
            "count_status": "Final manifest inventory at this snapshot. Early character sheets are separate; exact quota-unit or billed-call reconciliation remains unverified.",
            "manifest": relative(edits_path), "manifest_sha256": digest(edits_path) if edits_path.exists() else None,
            "declared_edits": len(edits),
            "declared_edit_outputs_present": sum((ROOT / row["out"]).exists() for row in edits),
            "early_character_sheets": early_sheets,
            "early_sheet_output_count": sum(row["output_present"] for row in early_sheets),
            "combined_recorded_image_outputs": sum((ROOT / row["out"]).exists() for row in edits) + sum(row["output_present"] for row in early_sheets),
            "known_generation_calls": len(edits) + len(early_sheets),
            "call_count_evidence": "Director confirmed one call per declared edit and two earlier character-sheet calls; these are 39 known calls at the final episode snapshot. This is not an account quota receipt.",
            "exact_quota_charge_verified": False,
            "cash_estimate_usd": None,
            "limit": "Built-in derived image edits do not expose a separate per-call cash receipt in these local records. No amount is invented or added to the fal estimate.",
        },
        "non_generative_transport": {"generation_requests": 0,
            "provenance": "episodes/ep01/build/reference_transport.json",
            "provenance_sha256": digest(BUILD / "reference_transport.json")},
        "motion_generation_request_logs": motion_requests,
        "source_integrity": {
            "audio_master": relative(master_path), "audio_master_sha256": master_hash,
            "matches_final_audio_master": master_hash == expected_master,
            "approved_references": reference_checks,
            "all_approved_references_match": all(row["matches_approved_hash"] for row in reference_checks),
        },
        "unresolved_requests": unresolved, "endpoints_without_captured_price": sorted(set(missing_prices)),
        "limits": ["This is a usage estimate, not a paid invoice or account-balance statement.",
                   "The conservative envelope prices failed requested units too; it does not assert that validation failures were billed.",
                   "Music and SFX units use requested durations, matching the captured endpoint price units; invoice rounding is not known.",
                   "Source logs and source media are read only. This script never polls, submits, uploads, deletes or mutates an account."],
    }
    result["local_inventory_ready"] = not (unresolved or missing_prices or motion_requests) and master_hash == expected_master and all(row["matches_approved_hash"] for row in reference_checks)
    print(json.dumps(result, indent=2))
    if args.final and not result["local_inventory_ready"]:
        raise SystemExit("Final budget inventory has unresolved, unpriced or unexpected motion requests; inspect the JSON report.")


if __name__ == "__main__":
    main()
