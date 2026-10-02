"""Build/upload two non-generative reference contact boards. Never generates images.

All approved PNGs remain unchanged. Composition uses full source images, with
labels outside the cells. Only the two lower set cells are downsampled by 2.
URLs, source hashes and geometry are recorded in ignored work/ep01/board_urls.json.
"""
import concurrent.futures
import hashlib
import io
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "work/ep01/refs/boards"
CATALOG = ROOT / "work/ep01/board_urls.json"
sys.path.insert(0, str(ROOT / "tools"))
from fal_upload import upload


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(data):
    temp = CATALOG.with_suffix(".json.tmp")
    temp.write_text(json.dumps(data, indent=2) + "\n")
    temp.replace(CATALOG)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(CATALOG.read_text()) if CATALOG.exists() else {
        "schema_version": 1,
        "purpose": "Two non-generative contact boards for an explicit next reference test",
        "causal_limit": "The planned test changes reference layout/count and prompt. It cannot isolate reference count or JPEG encoding as the prior failure cause.",
        "generation_calls": 0, "urls": {}, "references": {},
    }
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 34)
    sources = {}
    for role in ("eda", "sen", "kitchen", "props", "modules"):
        path = ROOT / f"work/ep01/refs/ref_{role}.png"
        raw = path.read_bytes()
        with Image.open(io.BytesIO(raw)) as im:
            im.load()
            assert im.size == (2672, 1504)
            sources[role] = (im.convert("RGB"), {
                "role": role, "source": str(path.relative_to(ROOT)),
                "source_sha256": digest(raw), "source_dimensions": list(im.size),
            })
    layouts = {
        "ref_cast_board": {"dimensions": (5344, 1560), "cells": [
            ("eda", "EDA", (0, 56, 2672, 1560), (16, 10)),
            ("sen", "SEN", (2672, 56, 5344, 1560), (2688, 10)),
        ]},
        "ref_set_board": {"dimensions": (2672, 2368), "cells": [
            ("kitchen", "ROOM", (0, 56, 2672, 1560), (16, 10)),
            ("props", "PROPS", (0, 1616, 1336, 2368), (16, 1570)),
            ("modules", "MODULES", (1336, 1616, 2672, 2368), (1352, 1570)),
        ]},
    }
    for identifier, layout in layouts.items():
        canvas = Image.new("RGB", layout["dimensions"], (245, 244, 240))
        draw = ImageDraw.Draw(canvas)
        cells = []
        for role, label, box, text_position in layout["cells"]:
            source, metadata = sources[role]
            target_size = (box[2] - box[0], box[3] - box[1])
            cell = source if source.size == target_size else source.resize(target_size, Image.Resampling.LANCZOS)
            canvas.paste(cell, box[:2])
            draw.text(text_position, label, font=font, fill=(24, 24, 24))
            cells.append({**metadata, "destination_box_xyxy": list(box), "label": label,
                          "label_top_left": list(text_position), "source_crop": None,
                          "resample": "none" if source.size == target_size else "Lanczos 2:1 downsample",
                          "content_changes": "none; contact placement only before JPEG encoding"})
        output = OUT / f"{identifier}.jpg"
        buf = io.BytesIO()
        canvas.save(buf, format="JPEG", quality=90, optimize=True, progressive=False)
        raw = buf.getvalue()
        assert len(raw) <= 3_000_000 and max(canvas.size) < 8000
        if output.exists():
            assert output.read_bytes() == raw, "A registered board must not be silently replaced"
        else:
            output.write_bytes(raw)
        with Image.open(io.BytesIO(raw)) as im:
            im.load()
            assert im.mode == "RGB" and im.size == canvas.size
        decoded = cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)
        assert decoded is not None and decoded.shape[:2] == (canvas.height, canvas.width)
        previous = catalog["references"].get(identifier, {})
        if previous:
            assert previous["sha256"] == digest(raw)
        catalog["references"][identifier] = {
            **previous, "id": identifier, "out": str(output.relative_to(ROOT)),
            "dimensions": list(canvas.size), "bytes": len(raw), "sha256": digest(raw),
            "format": "JPEG", "mode": "RGB", "quality": 90, "optimize": True,
            "progressive": False, "metadata": "JFIF only; no EXIF or ICC",
            "non_generative": True, "labels_outside_image_cells": True, "cells": cells,
            "local_decode_checks": ["Pillow full decode", "OpenCV full decode"],
        }
    save(catalog)
    missing = [key for key in layouts if key not in catalog["urls"]]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        pending = {pool.submit(upload, ROOT / catalog["references"][key]["out"]): key for key in missing}
        for future in concurrent.futures.as_completed(pending):
            key = pending[future]
            catalog["urls"][key] = future.result()
            catalog["references"][key]["url"] = catalog["urls"][key]
            save(catalog)
            print(f"{key}: URL saved", flush=True)
    # Uploads are saved before verification, so a slow GET never repeats an upload.
    def verify(key):
        url = catalog["urls"][key]
        with urllib.request.urlopen(url, timeout=60) as response:
            assert response.status == 200
            assert response.headers.get("Content-Type", "").split(";")[0] == "image/jpeg"
            raw = response.read()
        assert digest(raw) == catalog["references"][key]["sha256"]
        return key
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for key in pool.map(verify, layouts):
            catalog["references"][key]["remote_sha256_verified"] = True
            save(catalog)
            print(f"{key}: remote bytes verified", flush=True)
    for _, metadata in sources.values():
        assert digest((ROOT / metadata["source"]).read_bytes()) == metadata["source_sha256"]
    catalog["complete"] = True
    catalog["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    save(catalog)
    print("Two boards complete; original hashes unchanged; no generation calls.")


if __name__ == "__main__":
    main()
