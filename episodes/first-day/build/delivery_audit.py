#!/usr/bin/env python3
# /// script
# dependencies = ["pillow"]
# ///
"""Read-only local conformance checks for First Day; never calls an API.

Run with uv. Missing images are reported separately from plan errors so this is
also useful before generation. Pixel quality and motion/listening are not tested.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / "episodes/first-day/build"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit() -> dict:
    names = ("keyframes.json", "timeline.json", "motion_plan.json", "references.json",
             "character_sheets.json", "audio_plan.json", "lyrics.json", "make_plan.py",
             "builtin_image_edits.json")
    hashes = {str((BUILD / n).relative_to(ROOT)): digest(BUILD / n) for n in names}
    load = lambda name: json.loads((BUILD / name).read_text(encoding="utf-8"))
    keys, timeline, motion = load("keyframes.json"), load("timeline.json"), load("motion_plan.json")
    refs, sheets, audio, lyrics = (load(n) for n in
                                 ("references.json", "character_sheets.json", "audio_plan.json", "lyrics.json"))
    errors, missing, assets = [], [], []

    def check(condition, message):
        if not condition:
            errors.append(message)

    def unique(rows, label):
        counts = Counter(row["id"] for row in rows)
        check(all(n == 1 for n in counts.values()), f"Duplicate IDs in {label}")
        return {row["id"]: row for row in rows}

    by_key, by_shot, by_motion = (unique(rows, label) for rows, label in
                                ((keys, "keyframes"), (timeline, "timeline"), (motion["jobs"], "motion")))
    builtin = unique(load("builtin_image_edits.json")["edits"], "built-in edits")
    check(len(keys) == 55, "Expected 55 keyframe entries")
    check(len(timeline) == 101, "Expected 101 timeline entries")
    check(len(by_motion) == 53, "Expected 53 motion jobs")
    namespace = {}
    for item in [*refs, *sheets, *keys]:
        old = namespace.get(item["id"])
        check(old is None or old == item, f"Conflicting repeated image ID: {item['id']}")
        namespace[item["id"]] = item
    graph = {}
    for identity, item in namespace.items():
        deps = set(item.get("deps", [])) | set(item.get("refs", []))
        if item.get("base"):
            deps.add(item["base"])
        check(deps <= namespace.keys(), f"Unresolved image dependency: {identity}")
        check(len(item.get("refs", [])) <= 8, f"More than eight reference URLs: {identity}")
        graph[identity] = deps
    visited, active = set(), set()

    def visit(node):
        if node in active:
            errors.append(f"Image dependency cycle at {node}")
            return
        if node in visited or node not in graph:
            return
        active.add(node)
        for dep in graph[node]:
            visit(dep)
        active.remove(node)
        visited.add(node)

    for identity in graph:
        visit(identity)
    previous = 0
    image_parity = motion_parity = 0
    for shot in timeline:
        sid, kid, mid = shot["id"], shot["keyframe_id"], shot["motion_job"]
        start, end = shot["start_frame"], shot["end_frame"]
        check(isinstance(start, int) and isinstance(end, int) and end > start,
              f"Invalid frame interval: {sid}")
        check(start == previous, f"Timeline gap/overlap before {sid}")
        previous = end
        check(kid in by_key, f"Unknown key for shot {sid}")
        check(mid in by_motion, f"Unknown motion job for shot {sid}")
        if kid not in by_key or mid not in by_motion:
            continue
        key, job = by_key[kid], by_motion[mid]
        check(shot["image"] == key["out"], f"Timeline image disagrees with key {kid}")
        trim = shot["source_trim"]
        check(0 <= trim["start"] < trim["end"] <= job["duration"], f"Trim outside take: {sid}")
        check(abs(trim["end"] - trim["start"] - (end - start) / 24) < 0.00001,
              f"Source trim/edit length mismatch: {sid}")
        indexed = [x for x in job["source_trims"] if x["shot"] == sid]
        check(len(indexed) == 1 and all(indexed[0][k] == trim[k] for k in ("start", "end")),
              f"Motion reverse trim index mismatch: {sid}")
        path = ROOT / f"episodes/first-day/shots/{sid}/shot.md"
        if not path.is_file():
            errors.append(f"Missing shot document: {sid}")
            continue
        text = path.read_text(encoding="utf-8")
        hashes[str(path.relative_to(ROOT))] = digest(path)
        try:
            exact = text.split("## Exact image prompt\n\n", 1)[1].split("\n\n##", 1)[0]
        except IndexError:
            exact = None
        check(exact == key["prompt"], f"Exact image prompt differs: {sid}")
        image_parity += exact == key["prompt"]
        paragraphs = text.split("\n\n")
        check(job["prompt"] in paragraphs, f"Exact motion prompt differs: {sid}")
        motion_parity += job["prompt"] in paragraphs
    check(previous == 6096, "Timeline must end at frame 6096")
    for key in keys:
        check(key["shots"] == [s["id"] for s in timeline if s["keyframe_id"] == key["id"]],
              f"Keyframe reverse shot index mismatch: {key['id']}")
        path = ROOT / key["out"]
        if key.get("external"):
            record = builtin.get(key["id"])
            check(record is not None, f"Missing external generation provenance: {key['id']}")
            if record is not None:
                check(record["prompt"] == key["prompt"] and record["out"] == key["out"],
                      f"External recipe/prompt mismatch: {key['id']}")
                if path.is_file():
                    check(digest(path) == record["output_sha256"], f"External asset hash mismatch: {key['id']}")
                for source in record["inputs"]:
                    source_path = ROOT / source["path"]
                    check(source_path.is_file() and digest(source_path) == source["sha256"],
                          f"External input provenance mismatch: {key['id']}")
        if not path.is_file():
            missing.append(key["id"])
            continue
        try:
            with Image.open(path) as image:
                image.load()
                width, height = image.size
            assets.append({"id": key["id"], "path": key["out"], "sha256": digest(path),
                           "width": width, "height": height,
                           "pixel_approval": "not inferred by this audit"})
        except Exception as exc:
            errors.append(f"Cannot decode {key['id']}: {type(exc).__name__}")
    for job in by_motion.values():
        check(5 <= job["duration"] <= 15, f"Motion duration out of range: {job['id']}")
        check(job["image_key"] in by_key and job["image"] == by_key[job["image_key"]]["out"],
              f"Motion input disagrees with key: {job['id']}")
        check(set(job.get("reference_ids", [])) <= namespace.keys(),
              f"Unknown motion reference ID: {job['id']}")
    primary = sum(j["duration"] for j in by_motion.values())
    with_takes = sum(j["duration"] * j["planned_takes"] for j in by_motion.values())
    check(primary == motion["estimated_primary_seconds"], "Primary motion seconds total differs")
    check(with_takes == motion["estimated_seconds_with_planned_takes"], "Motion take seconds total differs")
    for source_key, hash_key in (("source_audio", "source_sha256"), ("source_lyrics", "source_lyrics_sha256")):
        check(digest(ROOT / audio[source_key]) == audio[hash_key], f"Source integrity failed: {source_key}")
    check(len(lyrics["cues"]) == 77, "Expected 77 source lyric cues")
    changed = [path for path, expected in hashes.items() if digest(ROOT / path) != expected]
    check(not changed, "Inputs changed during audit; rerun on stable recipes")
    return {
        "schema_version": 1, "episode": "first-day",
        "status": "fail" if errors else "plan_pass_assets_pending" if missing else "local_conformance_pass",
        "errors": errors, "missing_keyframes": missing,
        "counts": {"keyframes": len(keys), "decoded_keyframes": len(assets), "shots": len(timeline),
                   "motion_jobs": len(by_motion), "exact_image_prompt_matches": image_parity,
                   "exact_motion_prompt_matches": motion_parity, "timeline_frames": previous,
                   "primary_motion_seconds": primary, "motion_seconds_with_takes": with_takes,
                   "reference_namespace": len(namespace),
                   "external_completed_image_recipes": sum(bool(k.get("external")) for k in keys)},
        "assets": assets, "audited_file_sha256": hashes,
        "limits": "Local structural and file checks only. A decoded file is not visual approval. No API calls, "
                  "motion submission, motion review, listening, or sung-word alignment verification.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "work/first-day/delivery_audit.json")
    args = parser.parse_args()
    report = audit()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_name(args.out.name + ".tmp")
    temporary.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(args.out)
    print(json.dumps({k: report[k] for k in ("status", "errors", "missing_keyframes", "counts")}, indent=2))
    raise SystemExit(bool(report["errors"]))


if __name__ == "__main__":
    main()
