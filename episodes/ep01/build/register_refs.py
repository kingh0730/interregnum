"""Preserve approved PNGs and prepare/upload smaller, full-resolution JPEG references.

This only uses fal CDN storage; it never invokes a generation endpoint or edits the
image runner's manifests/logs. CDN URLs live exclusively in the ignored work tree.
Run with --upload to register missing objects; reruns reuse verified URL entries.
"""
import argparse
import hashlib
import io
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
PUBLIC = ROOT / "episodes/ep01/build/reference_transport.json"
PRIVATE = ROOT / "work/ep01/ref_transport_urls.json"
ROLES = ("eda", "sen", "kitchen", "props", "modules")
sys.path.insert(0, str(ROOT / "tools"))
from fal_upload import upload


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    temporary.replace(path)


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upload", action="store_true")
    args = parser.parse_args()
    private = json.loads(PRIVATE.read_text()) if PRIVATE.exists() else {
        "schema_version": 1,
        "purpose": "Episode01 full-resolution Q90 transport references; CDN upload only",
        "urls": {},
        "references": {},
    }
    rows = []
    for role in ROLES:
        identifier = f"ref_{role}_q90"
        source = ROOT / f"work/ep01/refs/ref_{role}.png"
        target = ROOT / f"work/ep01/refs/transport/{identifier}.jpg"
        original = source.read_bytes()
        with Image.open(io.BytesIO(original)) as image:
            dimensions = list(image.size)
            assert image.format == "PNG", source
            # Approved plates have no meaningful transparency. Refuse to flatten
            # hidden pixels accidentally if a future source replaces a plate.
            if "A" in image.getbands():
                assert image.getchannel("A").getextrema() == (255, 255), source
            buffer = io.BytesIO()
            image.convert("RGB").save(buffer, format="JPEG", quality=90, optimize=True)
            jpeg = buffer.getvalue()
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            assert target.read_bytes() == jpeg, f"Existing derivative differs: {target}"
        else:
            target.write_bytes(jpeg)
        with Image.open(target) as image:
            image.load()
            assert list(image.size) == dimensions and image.mode == "RGB"
        assert sha(source.read_bytes()) == sha(original), "Original changed during conversion"
        row = {
            "id": identifier, "original_id": f"ref_{role}", "role": role,
            "source": str(source.relative_to(ROOT)), "out": str(target.relative_to(ROOT)),
            "dimensions": dimensions, "source_format": "PNG", "transport_format": "JPEG",
            "source_sha256": sha(original), "transport_sha256": sha(jpeg),
            "source_bytes": len(original), "transport_bytes": len(jpeg),
            "reduction_percent": round(100 * (1 - len(jpeg) / len(original)), 2),
            "resize": False, "quality": 90, "optimize": True, "mode": "RGB",
            "generation_submitted": False,
        }
        rows.append(row)
    public = {
        "schema_version": 1, "created_at_utc": now(),
        "purpose": "Transport-only derivatives of the five approved references",
        "rationale": "Four references are schema-valid. Slow ingestion of large PNGs is a hypothesis, not a diagnosed cause or a guarantee of success.",
        "limits_checked": {
            "reference_count_max": 9, "image_size_max_mb": 50, "image_dimension_max_px": 8000,
            "recommended_image_size_mb": 4, "recommended_jpeg_quality": "85–92",
            "schema_source": "https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=luma/agent/uni-1/v1/max",
            "transport_source": "https://docs.agents.lumalabs.ai/guides/faq/",
        },
        "unchanged": "Original files, image manifests, generation payloads, and active request logs",
        "url_catalog": str(PRIVATE.relative_to(ROOT)),
        "url_policy": "Actual CDN URLs are stored only under ignored work/.",
        "references": rows,
        "source_total_bytes": sum(row["source_bytes"] for row in rows),
        "transport_total_bytes": sum(row["transport_bytes"] for row in rows),
    }
    save(PUBLIC, public)
    if not args.upload:
        print(f"Prepared {len(rows)} full-resolution JPEGs; no upload or generation requested.")
        return
    for row in rows:
        identifier = row["id"]
        previous = private["references"].get(identifier)
        if previous:
            assert previous["transport_sha256"] == row["transport_sha256"], identifier
        url = private["urls"].get(identifier)
        if not url:
            url = upload(ROOT / row["out"])
            private["urls"][identifier] = url
            private["references"][identifier] = {**row, "url": url, "uploaded_at_utc": now()}
            save(PRIVATE, private)  # Save returned URL before any verification request.
        entry = private["references"][identifier]
        if not entry.get("remote_sha256_verified"):
            request = urllib.request.Request(url, headers={"User-Agent": "ep01-reference-verification"})
            with urllib.request.urlopen(request, timeout=60) as response:
                content_type = response.headers.get("Content-Type", "").split(";")[0]
                assert response.status == 200, response.status
                assert content_type == "image/jpeg", content_type
                downloaded = response.read()
            assert len(downloaded) == row["transport_bytes"], identifier
            assert sha(downloaded) == row["transport_sha256"], identifier
            entry.update(remote_sha256_verified=True, verified_at_utc=now(), content_type=content_type)
            save(PRIVATE, private)
        row["uploaded"] = True
        row["remote_sha256_verified"] = entry["remote_sha256_verified"]
        save(PUBLIC, public)
        print(f"{identifier}: {row['transport_bytes']} bytes; CDN bytes verified", flush=True)
    # Every source still matches the hash recorded before creating/uploading derivatives.
    assert all(sha((ROOT / row["source"]).read_bytes()) == row["source_sha256"] for row in rows)
    private["complete"] = True
    private["completed_at_utc"] = now()
    save(PRIVATE, private)
    public["complete"] = True
    public["originals_preserved"] = True
    save(PUBLIC, public)
    print(f"Registered {len(rows)} references. No generation requests submitted.")


if __name__ == "__main__":
    main()
