#!/usr/bin/env python3
"""Make inspection-only contact sheets; never alter generated source images.

uv run episodes/first-day/build/contact_sheets.py
uv run episodes/first-day/build/contact_sheets.py --detail-spec work/first-day/qa/detail_spec.json

Main sheets contain complete images in edit order and unique-key ID order.
Optional detail spec: [{"keyframe":"k06","label":"Lin face", "crop":[x,y,w,h]}].
Crop coordinates are normalized and appear only on supplemental detail sheets.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[3]
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"


def resolve(value):
    return (ROOT / value).resolve()


def read_json(value):
    return json.loads(resolve(value).read_text(encoding="utf-8"))


def natural_key(value):
    return [int(s) if s.isdigit() else s for s in re.split(r"(\d+)", value)]


def tc(frame, fps=24):
    return f"{frame // (fps*60):02}:{frame // fps % 60:02}:{frame % fps:02}"


def normalized_crop(value):
    if not isinstance(value, list) or len(value) != 4:
        raise ValueError("detail crop must be normalized [x,y,width,height]")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in value):
        raise ValueError("detail crop values must be finite numbers")
    x, y, w, h = value
    if min(x, y) < 0 or min(w, h) <= 0 or x + w > 1 or y + h > 1:
        raise ValueError("detail crop is outside image bounds")
    return value


def fit_text(draw, text, font, width):
    while text and draw.textlength(text, font=font) > width:
        text = text[:-2] + "…" if len(text) > 2 else ""
    return text


def make_pages(entries, prefix, heading, out_dir, width, fonts):
    cols, rows, margin, gutter = 4, 3, 16, 12
    title_h, label_h = 56, 46
    tile_w = (width - 2 * margin - (cols - 1) * gutter) // cols
    tile_h = round(tile_w * 9 / 16)
    page_h = title_h + rows * (tile_h + label_h) + (rows - 1) * gutter + margin
    pages, records = [], []
    total_pages = max(1, math.ceil(len(entries) / (cols * rows)))
    title_font, label_font, small_font, missing_font = fonts
    for page_number in range(total_pages):
        page = Image.new("RGB", (width, page_h), (21, 24, 29))
        draw = ImageDraw.Draw(page)
        title = f"{heading}  |  {page_number + 1}/{total_pages}"
        draw.text((margin, 12), title, font=title_font, fill=(235, 238, 242))
        selected = entries[page_number * 12:(page_number + 1) * 12]
        for index, entry in enumerate(selected):
            x = margin + (index % cols) * (tile_w + gutter)
            y = title_h + (index // cols) * (tile_h + label_h + gutter)
            draw.rectangle((x, y, x + tile_w - 1, y + tile_h - 1), fill=(4, 5, 7))
            asset = resolve(entry["image"])
            status, dimensions, error = "ready", None, None
            if not asset.is_file():
                status = "MISSING"
            else:
                try:
                    with Image.open(asset) as source:
                        image = ImageOps.exif_transpose(source).convert("RGBA")
                    dimensions = list(image.size)
                    if entry.get("crop") is not None:
                        cx, cy, cw, ch = normalized_crop(entry["crop"])
                        iw, ih = image.size
                        bounds = (round(cx * iw), round(cy * ih), round((cx + cw) * iw), round((cy + ch) * ih))
                        if bounds[2] <= bounds[0] or bounds[3] <= bounds[1]:
                            raise ValueError("detail crop contains no source pixels")
                        image = image.crop(bounds)
                    thumb = ImageOps.contain(image, (tile_w, tile_h), Image.Resampling.LANCZOS)
                    page.paste(thumb, (x + (tile_w - thumb.width) // 2, y + (tile_h - thumb.height) // 2), thumb)
                except (OSError, ValueError) as exc:
                    status, error = "UNREADABLE", str(exc)
            if status != "ready":
                draw.rectangle((x, y, x + tile_w - 1, y + tile_h - 1), outline=(171, 78, 80), width=2)
                for offset, line in enumerate((status, entry["keyframe"])):
                    box = draw.textbbox((0, 0), line, font=missing_font)
                    draw.text((x + (tile_w - (box[2] - box[0])) / 2, y + tile_h / 2 - 37 + 38 * offset),
                              line, font=missing_font, fill=(239, 156, 151))
            draw.text((x + 3, y + tile_h + 3), fit_text(draw, entry["label"], label_font, tile_w - 6),
                      font=label_font, fill=(237, 240, 245))
            draw.text((x + 3, y + tile_h + 24), fit_text(draw, entry.get("secondary", ""), small_font, tile_w - 6),
                      font=small_font, fill=(170, 182, 196))
            records.append({**entry, "status":status, "source_dimensions":dimensions, "error":error,
                            "page":f"{prefix}_{page_number+1:02d}.jpg", "position":index+1})
        output = out_dir / f"{prefix}_{page_number+1:02d}.jpg"
        temporary = output.with_suffix(".tmp.jpg")
        page.save(temporary, quality=94, subsampling=0)
        temporary.replace(output)
        pages.append(str(output.relative_to(ROOT)) if output.is_relative_to(ROOT) else str(output))
    return pages, records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeline", default="episodes/first-day/build/timeline.json")
    parser.add_argument("--keyframes", default="episodes/first-day/build/keyframes.json")
    parser.add_argument("--out-dir", default="work/first-day/qa")
    parser.add_argument("--detail-spec")
    parser.add_argument("--width", type=int, default=1920)
    args = parser.parse_args()
    if not 1440 <= args.width <= 2000:
        parser.error("--width must be between 1440 and 2000")
    timeline, keys = read_json(args.timeline), read_json(args.keyframes)
    if isinstance(timeline, dict):
        timeline = timeline["timeline"]
    by_id = {k["id"]:k for k in keys}
    if len(by_id) != len(keys):
        raise ValueError("duplicate keyframe IDs")
    out_dir = resolve(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    font_sizes = (25, 18, 15, 27)
    fonts = [ImageFont.truetype(FONT, size, index=1) for size in font_sizes]
    edit_entries = [{"keyframe":s["keyframe_id"],"image":s["image"],"shot":s["id"],
                     "label":f"SHOT {s['id']}  |  {s['keyframe_id']}  |  {tc(s['start_frame'])}–{tc(s['end_frame'])}",
                     "secondary":f"{s['section']} · {s['kind']} · {(s['end_frame']-s['start_frame'])/24:.2f} s"}
                    for s in timeline]
    unique_entries = [{"keyframe":k["id"],"image":k["out"],"label":f"{k['id']}  |  {k.get('location','')}",
                       "secondary":"Shots " + ", ".join(k.get("shots", []))}
                      for k in sorted(keys, key=lambda k:natural_key(k["id"]))]
    outputs, records = {}, {}
    for name, heading, entries in (("edit_order","第一天 — EDIT ORDER / COMPLETE IMAGES",edit_entries),
                                   ("unique_keys","第一天 — UNIQUE KEYS / COMPLETE IMAGES",unique_entries)):
        outputs[name], records[name] = make_pages(entries,name,heading,out_dir,args.width,fonts)
    if args.detail_spec:
        details = read_json(args.detail_spec)
        if not isinstance(details,list):
            raise ValueError("detail spec must be a list")
        entries = []
        for detail in details:
            key_id = detail["keyframe"]
            if key_id not in by_id:
                raise ValueError(f"unknown detail keyframe {key_id}")
            crop = normalized_crop(detail["crop"])
            entries.append({"keyframe":key_id,"image":by_id[key_id]["out"],"crop":crop,
                            "label":f"{key_id}  |  DETAIL: {detail['label']}",
                            "secondary":"SUPPLEMENTAL CROP — inspect complete image separately"})
        outputs["details"], records["details"] = make_pages(entries,"details","第一天 — SUPPLEMENTAL DETAIL CROPS",out_dir,args.width,fonts)
    index = {"created_utc":datetime.now(timezone.utc).isoformat(),"width":args.width,"images_per_page":12,
             "main_image_fit":"contain; no crop; no alteration of source files","outputs":outputs,"records":records,
             "missing_unique_keys":[r["keyframe"] for r in records["unique_keys"] if r["status"]=="MISSING"],
             "unreadable_unique_keys":[r["keyframe"] for r in records["unique_keys"] if r["status"]=="UNREADABLE"],
             "authority":"Only pages listed in this index belong to the current run; older supplemental pages may remain."}
    target = out_dir / "contact_sheet_index.json"
    temporary = target.with_suffix(".tmp.json")
    temporary.write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    temporary.replace(target)
    print(json.dumps({"pages":outputs,"missing":index["missing_unique_keys"],"unreadable":index["unreadable_unique_keys"]},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
