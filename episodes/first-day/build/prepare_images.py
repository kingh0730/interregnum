#!/usr/bin/env python3
"""Combine approved references and shot recipes for the existing Luma runner.

This does not upload, generate, or replace an image. Reference generation and its
request logs live separately in work/first-day/references and work/first-day/sheets.
Run from any directory after every reference has passed visual review.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BUILD = Path(__file__).resolve().parent
WORK = ROOT / "work/first-day/keyframes"


def read(p):
    return json.loads(p.read_text(encoding="utf-8"))


def main():
    refs = read(BUILD / "references.json")
    keys = read(BUILD / "keyframes.json")
    used_refs = {ref for item in keys for ref in item.get("refs", [])}
    sheets = [x for x in read(BUILD / "character_sheets.json") if x["id"].endswith("_sheet") and x["id"] in used_refs]
    items = refs + sheets + keys
    ids = {x["id"] for x in items}
    if len(ids) != len(items):
        raise ValueError("Duplicate image IDs")
    urls = {}
    for source in (ROOT / "work/first-day/references/images.urls.json", ROOT / "work/first-day/sheets/images.urls.json"):
        urls.update(read(source))
    for ref in refs + sheets:
        if not (ROOT / ref["out"]).is_file() or not urls.get(ref["id"]):
            raise ValueError(f"Reference not completed: {ref['id']}; resume its original manifest")
    # Built-in reframes are already generated and uploaded. They are composition
    # inputs for Luma, never jobs to submit to the Luma endpoint.
    external_urls = {}
    edits = {x['id']: x for x in read(BUILD / 'builtin_image_edits.json')['edits']}
    for key in keys:
        if not key.get('external'):
            continue
        asset = ROOT / key['out']
        record = edits[key['id']]
        if hashlib.sha256(asset.read_bytes()).hexdigest() != record['output_sha256']:
            raise ValueError(f"External image differs from reviewed file: {key['id']}")
        url = (ROOT / f"work/first-day/{key['id']}_builtin.url").read_text().strip()
        if not url.startswith('https://'):
            raise ValueError(f"Missing uploaded external image: {key['id']}")
        external_urls[key['id']] = url
    for item in items:
        deps = set(item.get("deps", [])) | set(item.get("refs", [])) | ({item["base"]} if item.get("base") else set())
        if deps - ids:
            raise ValueError(f"Unresolved references for {item['id']}: {deps - ids}")
        if len(item.get("refs", [])) > 8 and item["mode"] == "edit":
            raise ValueError(f"Too many edit references for {item['id']}")
    WORK.mkdir(parents=True, exist_ok=True)
    destination = WORK / "images.json"
    cache = WORK / "images.urls.json"
    if destination.exists() and read(destination) != items:
        raise ValueError("Existing runtime manifest differs; review in-flight request state before updating it")
    # Keep completed key URLs on a preparation rerun. Reference URLs are refreshed
    # only before a new production manifest is first written.
    prior = read(cache) if cache.exists() else {}
    if destination.exists():
        for ref in refs + sheets:
            if prior.get(ref["id"]) != urls[ref["id"]]:
                raise ValueError(f"Reference changed after preparation: {ref['id']}")
    destination.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cache.write_text(json.dumps({**urls, **prior, **external_urls}, indent=2) + "\n", encoding="utf-8")
    execution_ids = [key['id'] for key in keys if not key.get('external')]
    (WORK / 'luma_only.txt').write_text(','.join(execution_ids) + '\n')
    print(f"Prepared {len(keys)} keyframes with {len(refs) + len(sheets)} completed reference inputs")
    print(destination.relative_to(ROOT))
    print(f"Luma selection: {len(execution_ids)} IDs in work/first-day/keyframes/luma_only.txt; external keys excluded.")
    print("Run the Luma runner with --root . and an explicit --only selection. Never regenerate external keys through Luma.")


if __name__ == "__main__":
    main()
