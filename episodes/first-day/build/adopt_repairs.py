#!/usr/bin/env python3
"""Adopt explicitly selected, director-approved still repairs; never generates.

Examples:
  python3 episodes/first-day/build/adopt_repairs.py --batch repair_batch03.json --only k23,k24 --upload
  python3 episodes/first-day/build/adopt_repairs.py --batch repair_batch04.json --only k55=k55_v1
  python3 episodes/first-day/build/adopt_repairs.py --only k36 --alias k36=k16 --upload

--upload uses the existing fal CDN uploader only. No model/queue calls are made.
Original recipes are retained unchanged; the central adopted receipt resolves
all inputs to immutable hash-named copies before any canonical file is replaced.
"""
from __future__ import annotations

import argparse
import copy
import fcntl
import hashlib
import json
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / "episodes/first-day/build"
ARCHIVE = ROOT / "episodes/first-day/assets/repair_sources"
WORK = ROOT / "work/first-day"
CANONICAL = ROOT / "episodes/first-day/assets/keyframes"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def local(value):
    path = (ROOT / value).resolve()
    if not path.is_relative_to(ROOT / "episodes/first-day"):
        raise ValueError("Asset outside this episode")
    return path


def archive(path, expected):
    destination = ARCHIVE / f"{path.stem}_{expected[:16]}{path.suffix}"
    if destination.is_file():
        if sha(destination) != expected:
            raise ValueError(f"Archive collision: {destination.name}")
        return destination
    if not path.is_file() or sha(path) != expected:
        raise ValueError(f"Input no longer matches provenance: {path.relative_to(ROOT)}")
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, destination)
    if sha(destination) != expected:
        raise ValueError(f"Archive verification failed: {destination.name}")
    return destination


def normalized_inputs(row):
    values = row.get("inputs", row.get("input_paths", []))
    hashes = row.get("input_sha256", [])
    result = []
    for index, value in enumerate(values):
        item = dict(value) if isinstance(value, dict) else {"path": value}
        expected = item.get("sha256")
        if expected is None:
            expected = hashes[item["path"]] if isinstance(hashes, dict) else hashes[index]
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise ValueError("Input hash missing or invalid")
        item["sha256"] = expected
        result.append(item)
    return result


def upload(record):
    identity, expected = record["id"], record["output_sha256"]
    url_path = WORK / f"{identity}_builtin.url"
    receipt_path = WORK / f"{identity}_builtin.upload.json"
    if url_path.is_file() and receipt_path.is_file():
        if load(receipt_path).get("sha256") == expected and url_path.read_text().strip().startswith("https://"):
            return identity, "existing verified upload"
    asset = local(record["out"])
    if sha(asset) != expected:
        raise ValueError(f"Canonical changed before upload: {identity}")
    completed = subprocess.run(["uv", "run", str(ROOT / "tools/fal_upload.py"), str(asset)],
                               cwd=ROOT, check=True, text=True, capture_output=True)
    url = completed.stdout.strip()
    if not url.startswith("https://") or any(c.isspace() for c in url):
        raise ValueError(f"Uploader returned an invalid URL: {identity}")
    temporary = url_path.with_name(url_path.name + ".tmp")
    temporary.write_text(url + "\n", encoding="utf-8")
    temporary.replace(url_path)
    write(receipt_path, {"id": identity, "sha256": expected, "asset": record["out"]})
    return identity, "uploaded verified canonical bytes"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", action="append", default=[], help="Recipe filename under build/")
    parser.add_argument("--only", required=True, help="Comma-separated IDs or canonical=candidate selectors")
    parser.add_argument("--alias", action="append", default=[], help="Existing generation reuse: target=source")
    parser.add_argument("--upload", action="store_true")
    args = parser.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    with (WORK / "adopt_repairs.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        selections = {}
        for value in args.only.split(","):
            target, separator, source = value.partition("=")
            if not re.fullmatch(r"k\d{2}", target) or target in selections:
                raise ValueError(f"Invalid or duplicate canonical ID: {target}")
            selections[target] = source if separator else target
        aliases = dict(value.split("=", 1) for value in args.alias)
        if set(aliases) - selections.keys():
            raise ValueError("Every alias target must appear in --only")
        builtin_path, override_path = BUILD / "builtin_image_edits.json", BUILD / "approved_image_overrides.json"
        builtin, overrides = load(builtin_path), load(override_path)
        adopted = {row["id"]: row for row in builtin["edits"]}
        candidates = {}
        for filename in args.batch:
            recipe_path = (BUILD / filename).resolve()
            if recipe_path.parent != BUILD:
                raise ValueError("Recipe must be directly under episode build/")
            data = load(recipe_path)
            rows = data if isinstance(data, list) else data.get("edits", data.get("jobs", []))
            for row in rows:
                output_name = Path(row.get("candidate", row.get("out", row.get("output_path")))).name
                explicit = f"{row['id']}@{output_name}"
                if explicit in candidates:
                    raise ValueError(f"Ambiguous explicit candidate: {explicit}")
                candidates[explicit] = (recipe_path, row)
                candidates[row["id"]] = None if row["id"] in candidates else (recipe_path, row)
        pending = []
        # Validate and archive every input before replacing even the first target.
        for target, source in selections.items():
            destination = CANONICAL / f"{target}.png"
            if target in aliases:
                alias_source = aliases[target]
                source_record = adopted.get(alias_source)
                if source_record is None:
                    key = next(k for k in load(BUILD / "keyframes.json") if k["id"] == alias_source)
                    source_asset = local(key["out"])
                    source_hash = sha(source_asset)
                    saved = archive(source_asset, source_hash)
                    source_record = {"out": key["out"], "output_sha256": source_hash,
                                     "prompt": key["prompt"], "tool": "local file copy",
                                     "model": "No generation performed; source " + key["scene_model"],
                                     "scene_model": "Reused approved source image: " + key["scene_model"],
                                     "generation_id": f"existing_source/{alias_source}/{source_hash[:16]}",
                                     "inputs": [{"path": str(saved.relative_to(ROOT)), "sha256": source_hash,
                                                 "original_path_at_generation": key["out"]}]}
                record = copy.deepcopy(source_record)
                candidate = local(source_record["out"])
                record.update({"id": target, "alias_of": aliases[target],
                               "new_generation": False,
                               "generation_id": source_record.get("generation_id", aliases[target])})
            else:
                selected = candidates[source]
                if selected is None:
                    raise ValueError(f"Ambiguous candidate ID {source}; select id@candidate_filename explicitly")
                recipe_path, row = selected
                candidate = local(row.get("candidate", row.get("out", row.get("output_path"))))
                record = {"id": target, "tool": "image_gen.imagegen", "model": "not exposed by tool response",
                          "generation_id": f"{recipe_path.stem}/{row['id']}/{row['output_sha256'][:16]}", "new_generation": True,
                          "source_recipe": str(recipe_path.relative_to(ROOT)), "source_recipe_id": row["id"],
                          "prompt": row["prompt"], "output_sha256": row["output_sha256"],
                          "transparent_background": row.get("transparent_background", False), "inputs": []}
                for item in normalized_inputs(row):
                    archived = archive(local(item["path"]), item["sha256"])
                    item["original_path_at_generation"] = item["path"]
                    item["path"] = str(archived.relative_to(ROOT))
                    record["inputs"].append(item)
            if not candidate.is_file() or sha(candidate) != record["output_sha256"]:
                raise ValueError(f"Candidate hash mismatch: {source}")
            if destination.is_file() and sha(destination) != record["output_sha256"]:
                old = archive(destination, sha(destination))
                record["replaced_canonical"] = {"path": str(old.relative_to(ROOT)), "sha256": sha(old)}
            elif target in adopted:
                old_record = adopted[target]
                if old_record.get("output_sha256") != record["output_sha256"]:
                    raise ValueError(f"Unexpected existing adopted receipt: {target}")
                if "replaced_canonical" in old_record:
                    record["replaced_canonical"] = old_record["replaced_canonical"]
            record.update({"out": str(destination.relative_to(ROOT)),
                           "status": "director approved and adopted; still image only",
                           "limits": "Still composition and story-state approval only; no generated motion or listening approval."})
            pending.append((candidate, destination, record))
        for candidate, destination, record in pending:
            if not destination.is_file() or sha(destination) != record["output_sha256"]:
                temporary = destination.with_name(destination.name + ".adopt.tmp")
                shutil.copyfile(candidate, temporary)
                temporary.replace(destination)
            adopted[record["id"]] = record
            overrides[record["id"]] = {"mode": "t2i", "refs": [], "base": None,
                                      "prompt": record["prompt"],
                                      "scene_model": record.get("scene_model", "Codex built-in image_gen; exact underlying model not exposed"),
                                      "external": True,
                                      "external_recipe": "episodes/first-day/build/builtin_image_edits.json",
                                      "approval": "director approved still composition and story state; motion unverified"}
            if record.get("alias_of"):
                overrides[record["id"]]["alias_of"] = record["alias_of"]
        builtin["edits"] = list(adopted.values())
        write(builtin_path, builtin)
        write(override_path, overrides)
        print("Adopted with archived provenance:", ", ".join(selections), flush=True)
        if args.upload:
            failures = []
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = {executor.submit(upload, record): record["id"] for _, _, record in pending}
                for future in as_completed(futures):
                    try:
                        identity, status = future.result()
                        print(f"{identity}: {status}", flush=True)
                    except Exception as exc:
                        failures.append(futures[future])
                        print(f"{futures[future]}: upload failed ({type(exc).__name__}); rerun same selection", flush=True)
            if failures:
                raise SystemExit(1)


if __name__ == "__main__":
    main()
