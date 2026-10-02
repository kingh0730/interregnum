"""Validate a recorded visual continuity review; never infer geometry from media.

All bound paths are resolved relative to the supplied repository root. The result
separates the review's recorded status from whether it is complete and current.
Missing, malformed and stale reviews return diagnostics rather than approving.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

STATUSES = {"pending", "blocked", "approved"}
RELATIONS = {"continuous", "ellipsis", "scene_change", "intentional_discontinuity"}


class ContinuityReviewError(ValueError):
    pass


def evaluate_review(review_path, root):
    """Return approval diagnostics, source hashes and per-shot source endpoints.

Approval establishes freshness and completeness of recorded visual judgments,
    not their correctness. ``source_hashes`` and ``shot_sources`` use resolved
    absolute local paths. Procedural card endpoints have no source path.
"""
    root = Path(root).resolve()
    result = {"approved": False, "status": "invalid", "errors": [],
              "review_path": str(review_path), "review_sha256": None,
              "source_hashes": {}, "shot_sources": {}}
    errors = result["errors"]

    def fail(message):
        errors.append(message)

    def resolve(value, label):
        if not isinstance(value, (str, Path)) or not str(value).strip():
            fail(f"{label}: expected a nonempty local path")
            return None
        if str(value).startswith(("http:", "https:", "data:")):
            fail(f"{label}: remote media cannot establish local frame review")
            return None
        try:
            return (root / value).resolve()
        except (OSError, ValueError, RuntimeError) as exc:
            fail(f"{label}: invalid local path: {exc}")
            return None

    def binding(value, label, parse=False):
        if not isinstance(value, dict):
            fail(f"{label}: expected {{path, sha256}} binding")
            return None, None
        path = resolve(value.get("path"), label)
        expected = value.get("sha256")
        if not isinstance(expected, str) or len(expected) != 64 or any(c not in "0123456789abcdefABCDEF" for c in expected):
            fail(f"{label}: expected SHA256 digest")
            return path, None
        if path is None:
            return None, None
        try:
            raw = path.read_bytes()
        except (OSError, ValueError) as exc:
            fail(f"{label}: cannot read {path}: {exc}")
            return path, None
        if hashlib.sha256(raw).hexdigest() != expected.lower():
            fail(f"{label}: bytes changed since visual review ({path})")
        if parse:
            try:
                return path, json.loads(raw)
            except (ValueError, UnicodeError) as exc:
                fail(f"{label}: invalid JSON: {exc}")
                return path, None
        return path, expected.lower()

    path = resolve(review_path, "continuity_review")
    if path is None:
        return result
    result["review_path"] = str(path)
    try:
        raw = path.read_bytes()
    except (OSError, ValueError) as exc:
        result["status"] = "missing"
        fail(f"Continuity review cannot be read: {path}: {exc}")
        return result
    result["review_sha256"] = hashlib.sha256(raw).hexdigest()
    try:
        review = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        fail(f"Continuity review is not valid JSON: {exc}")
        return result
    if not isinstance(review, dict) or type(review.get("schema_version")) is not int or review["schema_version"] != 1:
        fail("Continuity review must be a schema_version 1 object")
        return result
    status = review.get("status")
    if not isinstance(status, str) or status not in STATUSES:
        fail(f"Unknown continuity review status: {status!r}")
    else:
        result["status"] = status
        if status != "approved":
            fail(f"Continuity review is {status}; visual approval is required for a new submission")
    if status == "approved" and not (isinstance(review.get("reviewer"), str) and review["reviewer"].strip()):
        fail("Approved continuity review must name its reviewer")

    _, story = binding(review.get("story"), "story", parse=True)
    _, assets = binding(review.get("assets"), "assets", parse=True)
    extras = review.get("additional_inputs")
    if not isinstance(extras, list):
        fail("additional_inputs must be a list of bound files")
    else:
        seen = set()
        for index, item in enumerate(extras):
            extra, _ = binding(item, f"additional_inputs[{index}]")
            if extra in seen:
                fail(f"Duplicate additional input: {extra}")
            seen.add(extra)

    expected_sources = set()
    if not isinstance(assets, dict):
        fail("Bound assets file must map asset IDs to local paths or {path: ...} objects")
        assets = {}
    for asset, value in assets.items():
        source = resolve(value.get("path") if isinstance(value, dict) else value, f"asset {asset}")
        if source is not None:
            expected_sources.add(str(source))
    sources = review.get("sources")
    if not isinstance(sources, list):
        fail("sources must be a list covering every asset-map image path")
    else:
        for index, item in enumerate(sources):
            source, sha = binding(item, f"sources[{index}]")
            if source is None:
                continue
            source = str(source)
            if source in result["source_hashes"]:
                fail(f"Duplicate source binding: {source}")
            result["source_hashes"][source] = sha
    actual_sources = set(result["source_hashes"])
    if actual_sources != expected_sources:
        fail(f"Source coverage differs from asset map: missing={sorted(expected_sources - actual_sources)}, extra={sorted(actual_sources - expected_sources)}")

    shots = story.get("shots") if isinstance(story, dict) else None
    if not isinstance(shots, list) or not shots:
        fail("Bound story must contain a nonempty shots list")
        return result
    by_id, ordered = {}, []
    for shot in shots:
        if not isinstance(shot, dict) or not isinstance(shot.get("id"), (str, int)) or isinstance(shot.get("id"), bool):
            fail("Every story shot must have a string or integer ID")
            continue
        sid = str(shot["id"])
        if not sid or sid in by_id:
            fail(f"Empty or duplicate story shot ID: {sid!r}")
        if not isinstance(shot.get("asset"), str) or not shot["asset"]:
            fail(f"Shot {sid}: missing asset ID")
        elif shot["asset"] not in assets and shot.get("kind", shot.get("type")) not in ("title", "endcard", "credits"):
            fail(f"Shot {sid}: asset {shot['asset']} is absent from asset map")
        by_id[sid] = shot
        ordered.append(sid)

    states = {}
    if "states" in review:
        _, states = binding(review["states"], "states", parse=True)
        if not isinstance(states, dict):
            fail("Bound states file must map shot IDs to state lists")
            states = {}
    if set(states) - set(by_id):
        fail(f"State plan contains unknown shot IDs: {sorted(set(states) - set(by_id))}")
    endpoints, expected_changes = {}, {}
    for sid, shot in by_id.items():
        entries = states.get(sid, [{"offset_frame": 0, "asset": shot.get("asset")}])
        if not isinstance(entries, list) or not entries:
            fail(f"Shot {sid}: empty or invalid state list")
            continue
        previous = None
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                fail(f"Shot {sid}: invalid state entry")
                continue
            offset, asset = entry.get("offset_frame"), entry.get("asset")
            if type(offset) is not int or offset < 0 or (index == 0 and offset != 0) or (previous and offset <= previous[0]):
                fail(f"Shot {sid}: states need increasing integer offsets starting at zero")
                continue
            if not isinstance(asset, str) or not asset:
                fail(f"Shot {sid}: invalid state asset ID")
                continue
            if sid in states:
                if asset not in assets:
                    fail(f"Shot {sid}: state asset {asset} is absent from asset map")
                start, end = shot.get("start_frame"), shot.get("end_frame")
                if type(start) is not int or type(end) is not int or not 0 <= offset < end - start:
                    fail(f"Shot {sid}: state offset is outside its explicit frame bounds")
            if previous:
                expected_changes[(sid, offset)] = (previous[1], asset)
            else:
                endpoints[sid] = [asset, asset]
            endpoints[sid][1] = asset
            previous = (offset, asset)
    for sid, (first, last) in endpoints.items():
        record = {"first_asset": first, "last_asset": last}
        for label, asset in (("first_path", first), ("last_path", last)):
            value = assets.get(asset)
            source = resolve(value.get("path") if isinstance(value, dict) else value, f"Shot {sid} {label}") if value is not None else None
            record[label] = str(source) if source is not None else None
        result["shot_sources"][sid] = record

    def judgment(row, label):
        if not isinstance(row.get("relation"), str) or row["relation"] not in RELATIONS:
            fail(f"{label}: unknown relation")
        if not isinstance(row.get("status"), str) or row["status"] not in STATUSES:
            fail(f"{label}: unknown status")
        elif row["status"] != "approved":
            fail(f"{label}: review is {row['status']}")
        issues = row.get("issues")
        if not isinstance(issues, list):
            fail(f"{label}: issues must be a list")
        elif issues:
            fail(f"{label}: unresolved issues: {issues}")
        if row.get("status") == "approved" and not (isinstance(row.get("evidence"), str) and row["evidence"].strip()):
            fail(f"{label}: approved judgment needs specific visual evidence")

    expected_cuts = {(a, b) for a, b in zip(ordered, ordered[1:])}
    cuts, seen = review.get("cuts"), set()
    if not isinstance(cuts, list):
        fail("cuts must review every adjacent story shot pair")
    else:
        for row in cuts:
            if not isinstance(row, dict):
                fail("Invalid cut record")
                continue
            pair = (str(row.get("from_shot")), str(row.get("to_shot")))
            label = f"Cut {pair[0]} -> {pair[1]}"
            if pair in seen:
                fail(f"{label}: duplicate review")
            seen.add(pair)
            if pair not in expected_cuts:
                fail(f"{label}: not adjacent in the current story")
            elif pair[0] in endpoints and pair[1] in endpoints:
                expected = (endpoints[pair[0]][1], endpoints[pair[1]][0])
                if (row.get("from_asset"), row.get("to_asset")) != expected:
                    fail(f"{label}: endpoint assets differ from current states {expected}")
            judgment(row, label)
        if expected_cuts - seen:
            fail(f"Missing cut reviews: {sorted(expected_cuts - seen)}")

    changes = review.get("state_changes", [] if "states" not in review else None)
    seen = set()
    if not isinstance(changes, list):
        fail("state_changes must review every authored switch in the bound state plan")
    else:
        for row in changes:
            if not isinstance(row, dict) or type(row.get("offset_frame")) is not int:
                fail("Invalid state-change record")
                continue
            key = (str(row.get("shot_id")), row["offset_frame"])
            label = f"State change {key[0]} at {key[1]}"
            if key in seen:
                fail(f"{label}: duplicate review")
            seen.add(key)
            if key not in expected_changes:
                fail(f"{label}: absent from current state plan")
            elif (row.get("from_asset"), row.get("to_asset")) != expected_changes[key]:
                fail(f"{label}: endpoint assets differ from current state plan")
            judgment(row, label)
        if set(expected_changes) - seen:
            fail(f"Missing state-change reviews: {sorted(set(expected_changes) - seen)}")
    result["approved"] = status == "approved" and not errors
    return result


def require_approved(review_path, root):
    """Return a fresh approved record, or raise with actionable local diagnostics."""
    result = evaluate_review(review_path, root)
    if not result["approved"]:
        raise ContinuityReviewError("Continuity gate blocked: " + "; ".join(result["errors"]))
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", help="Continuity-review JSON path, relative to --root")
    parser.add_argument("--root", default=".", help="Root for all bound paths (default: current directory)")
    args = parser.parse_args(argv)
    result = evaluate_review(args.review, args.root)
    print(json.dumps({k: v for k, v in result.items() if k not in ("source_hashes", "shot_sources")}, indent=2))
    return 0 if result["approved"] else 2


if __name__ == "__main__":
    sys.exit(main())
