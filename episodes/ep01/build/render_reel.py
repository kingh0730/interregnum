# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow>=10"]
# ///
"""Frame-exact COMMON ROOM still/state reel; run with `uv run <this file>`.

Inputs and outputs are documented in render_contract.json. No media services,
placeholder frames, automatic camera movement or silent audio padding are used.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / "episodes/ep01/build"
WORK = ROOT / "work/ep01/render"
OUT = ROOT / "renders/ep01/common_room_story_reel.mp4"
FPS, W, H, SR = 24, 1920, 1080, 48000
VERSION = "common-room-static-v1"
FONT_EN = Path("/System/Library/Fonts/Helvetica.ttc")
FONT_ZH = Path("/System/Library/Fonts/Hiragino Sans GB.ttc")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".partial")
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def resolve(path):
    p = Path(path)
    return p if p.is_absolute() else ROOT / p


def relative(path):
    try:
        return str(Path(path).relative_to(ROOT))
    except ValueError:
        return str(path)


def digest_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while block := f.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()


def digest_obj(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def integer(value, label):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label}: expected integer frames, got {value!r}")
    return value


def run(cmd):
    p = subprocess.run([str(x) for x in cmd], capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"Command failed ({p.returncode}): {cmd[0]}\n{p.stderr[-5000:]}")
    return p.stdout, p.stderr


def probe(path):
    out, _ = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path])
    return json.loads(out)


def font(path, size):
    if not path.is_file():
        raise FileNotFoundError(f"Required font unavailable: {path}")
    return ImageFont.truetype(str(path), size)


def story_shots(story):
    """Accept the writer's explicit frame timeline; never round fractional seconds."""
    if story.get("fps") != FPS:
        raise ValueError(f"Story must explicitly specify fps={FPS}")
    shots = story["shots"]
    if not isinstance(shots, list) or not shots:
        raise ValueError("Story shots must be a nonempty list")
    out, next_frame, ids = [], 0, set()
    for s in shots:
        sid = str(s["id"])
        if sid in ids:
            raise ValueError(f"Duplicate shot ID {sid}")
        ids.add(sid)
        start = integer(s["start_frame"], f"{sid}.start_frame")
        duration = integer(s["end_frame"], f"{sid}.end_frame") - start
        if "duration_frames" in s and s["duration_frames"] != duration:
            raise ValueError(f"{sid}: duration_frames disagrees with end_frame")
        if start != next_frame or duration <= 0:
            raise ValueError(f"{sid}: timeline gap/overlap or nonpositive duration at frame {next_frame}")
        end = start + duration
        if "end_frame" in s and s["end_frame"] != end:
            raise ValueError(f"{sid}: end_frame differs from start + duration")
        card = s.get("kind") in ("title", "endcard", "credits") or s.get("type") in ("title", "endcard", "credits")
        out.append({**s, "id": sid, "start_frame": start, "duration_frames": duration, "end_frame": end, "card": card})
        next_frame = end
    if story.get("total_frames", next_frame) != next_frame:
        raise ValueError("Story total_frames differs from shot total")
    return out, next_frame


def load_inputs():
    story_path = BUILD / "story.json"
    assets_path = BUILD / "assets.json"
    states_path = BUILD / "reel_states.json"
    layouts_path = BUILD / "subtitle_layouts.json"
    subs_path = ROOT / "work/ep01/audio/subtitles.json"
    audio_path = ROOT / "work/ep01/audio/master_mix.wav"
    story = read_json(story_path)
    shots, total = story_shots(story)
    assets = read_json(assets_path)
    if not isinstance(assets, dict):
        raise ValueError("assets.json must map IDs to local paths")
    states = read_json(states_path) if states_path.exists() else {}
    by_id = {s["id"]: s for s in shots}
    layouts = read_json(layouts_path) if layouts_path.exists() else {}
    if not isinstance(layouts, dict) or set(layouts) - set(by_id):
        raise ValueError("subtitle_layouts.json must map known shot IDs to safe-position settings")
    for sid, layout in layouts.items():
        if not isinstance(layout, dict) or set(layout) != {"bottom_margin"}:
            raise ValueError(f"{sid}: subtitle layout expects only bottom_margin")
        margin = integer(layout["bottom_margin"], f"{sid}.bottom_margin")
        if not 58 <= margin <= 750:
            raise ValueError(f"{sid}: subtitle bottom_margin must be between58 and750 pixels")
        if by_id[sid]["card"]:
            raise ValueError(f"{sid}: no subtitle layout on title/endcard")
        by_id[sid]["subtitle_layout"] = layout
    unknown = set(states) - set(by_id)
    if unknown:
        raise ValueError(f"State map contains unknown shot IDs: {sorted(unknown)}")
    used = set()
    for shot in shots:
        sid = shot["id"]
        if shot["card"]:
            if sid in states:
                raise ValueError(f"{sid}: authored card cannot have image-state replacements")
            shot["states"] = [{"offset_frame": 0, "asset": "__authored_endcard__"}]
            continue
        ss = states.get(sid, [{"offset_frame": 0, "asset": shot["asset"]}])
        if not isinstance(ss, list) or not ss:
            raise ValueError(f"{sid}: states must be a nonempty list")
        previous = -1
        for entry in ss:
            offset = integer(entry["offset_frame"], f"{sid}.offset_frame")
            if offset <= previous or offset >= shot["duration_frames"]:
                raise ValueError(f"{sid}: state offsets must increase within shot")
            if previous == -1 and offset != 0:
                raise ValueError(f"{sid}: first state must begin at zero")
            aid = entry["asset"]
            if not isinstance(aid, str) or aid not in assets:
                raise ValueError(f"{sid}: unknown asset {aid!r}")
            used.add(aid)
            previous = offset
        shot["states"] = ss
    source_info = {}
    for aid in sorted(used):
        if not isinstance(assets[aid], str):
            raise ValueError(f"{aid}: expected a local path string in assets.json")
        path = resolve(assets[aid])
        if not path.is_file():
            raise FileNotFoundError(f"Missing image {aid}: {path}")
        with Image.open(path) as im:
            im.load()
            size = list(im.size)
            if getattr(im, "n_frames", 1) != 1:
                raise ValueError(f"{aid}: input must be one still image")
        source_info[aid] = {"path": relative(path), "sha256": digest_file(path), "size": size}
    subs = read_json(subs_path)
    if not isinstance(subs, list):
        raise ValueError("subtitles.json must be a list")
    dialogue = {}
    for shot in shots:
        for line in shot.get("dialogue", []):
            lid = line["id"]
            if lid in dialogue:
                raise ValueError(f"Duplicate story dialogue ID {lid}")
            dialogue[lid] = {"shot_id": shot["id"], "en": line["text"], "zh": line["zh"]}
    last_end, seen_lines = 0, set()
    for index, sub in enumerate(subs):
        lid = sub.get("line_id")
        if not isinstance(lid, str) or lid not in dialogue or lid in seen_lines:
            raise ValueError(f"subtitle {index}: missing, unknown or duplicate line_id {lid!r}")
        seen_lines.add(lid)
        start = integer(sub["start_frame"], f"subtitle {index}.start_frame")
        end = integer(sub["end_frame"], f"subtitle {index}.end_frame")
        if not 0 <= start < end <= total or start < last_end:
            raise ValueError(f"subtitle {index}: invalid bounds or overlapping captions")
        last_end = end
        sid = str(sub["shot_id"])
        if sid not in by_id:
            raise ValueError(f"subtitle {index}: unknown shot {sid}")
        sub["shot_id"] = sid
        shot = by_id[sid]
        if not shot["start_frame"] <= start < end <= shot["end_frame"]:
            raise ValueError(f"subtitle {index}: caption lies outside assigned shot {sid}")
        if shot["card"]:
            raise ValueError(f"subtitle {index}: caption on title/endcard")
        for lang in ("en", "zh"):
            if not isinstance(sub.get(lang), str) or not sub[lang].strip():
                raise ValueError(f"subtitle {index}: missing {lang} text")
            if sub[lang].strip() != dialogue[lid][lang].strip():
                raise ValueError(f"Subtitle {lid}: {lang} differs from locked story dialogue")
        if sid != dialogue[lid]["shot_id"]:
            raise ValueError(f"Subtitle {lid}: dialogue assigned to incorrect shot")
        for lang, f in (("zh", font(FONT_ZH, 40)), ("en", font(FONT_EN, 32))):
            if len(wrap_text(sub[lang], f, 1640)) > 2:
                raise ValueError(f"Subtitle {lid}: more than two {lang} rows; revise segmentation")
    if seen_lines != set(dialogue):
        raise ValueError(f"Missing dialogue captions: {sorted(set(dialogue) - seen_lines)}")
    if not audio_path.is_file():
        raise FileNotFoundError(f"Missing final mix: {audio_path}")
    audio_probe = probe(audio_path)
    ast = [s for s in audio_probe["streams"] if s["codec_type"] == "audio"]
    if len(ast) != 1:
        raise ValueError("Final WAV must contain exactly one audio stream")
    a = ast[0]
    if int(a["sample_rate"]) != SR or a["channels"] != 2:
        raise ValueError("Final mix must be 48000Hz stereo")
    if "wav" not in audio_probe["format"]["format_name"] or not a["codec_name"].startswith("pcm_"):
        raise ValueError("Final mix must be an uncompressed WAV")
    samples = Fraction(int(a["duration_ts"])) * Fraction(a["time_base"]) * SR
    expected = total * (SR // FPS)
    if samples != expected:
        raise ValueError(f"Audio length {samples} samples differs from expected {expected}; fix source mix, no implicit pad/trim")
    inputs = {"story": digest_file(story_path), "assets_map": digest_file(assets_path),
              "states": digest_file(states_path) if states_path.exists() else None,
              "subtitle_layouts": digest_file(layouts_path) if layouts_path.exists() else None,
              "subtitles": digest_file(subs_path), "audio": digest_file(audio_path),
              "font_en": digest_file(FONT_EN), "font_zh": digest_file(FONT_ZH)}
    return story, shots, total, source_info, subs, audio_path, inputs


def verify_input_integrity(inputs, info):
    """Do not publish a reel whose approved sources changed during encoding."""
    paths = {"story": BUILD / "story.json", "assets_map": BUILD / "assets.json",
             "states": BUILD / "reel_states.json", "subtitle_layouts": BUILD / "subtitle_layouts.json",
             "subtitles": ROOT / "work/ep01/audio/subtitles.json",
             "audio": ROOT / "work/ep01/audio/master_mix.wav", "font_en": FONT_EN, "font_zh": FONT_ZH}
    for name, path in paths.items():
        current = digest_file(path) if path.is_file() else None
        if current != inputs[name]:
            raise ValueError(f"Input changed during rendering: {relative(path)}; rerun against stable sources")
    for aid, source in info.items():
        if digest_file(resolve(source["path"])) != source["sha256"]:
            raise ValueError(f"Image changed during rendering: {aid}; rerun against stable sources")


def wrap_text(text, f, max_width):
    """Wrap English at words and Chinese at characters without changing content."""
    text = text.strip().replace("\r", "")
    output = []
    for paragraph in text.split("\n"):
        words = paragraph.split(" ") if " " in paragraph else list(paragraph)
        joiner = " " if " " in paragraph else ""
        current = ""
        for word in words:
            trial = word if not current else current + joiner + word
            if f.getlength(trial) <= max_width:
                current = trial
            elif current:
                output.append(current)
                current = word
            else:
                raise ValueError(f"Caption token cannot fit: {word!r}")
        if current:
            output.append(current)
    if any(f.getlength(line) > max_width for line in output):
        raise ValueError("Caption line cannot fit subtitle safe width")
    return output


def center_line(draw, text, f, y, colour, stroke=0):
    box = draw.textbbox((0, 0), text, font=f, stroke_width=stroke)
    width = box[2] - box[0]
    x = (W - width) / 2 - box[0]
    draw.text((x, y - box[1]), text, font=f, fill=colour,
              stroke_width=stroke, stroke_fill=(0, 0, 0, 235))
    return box[3] - box[1]


def compose_card():
    im = Image.new("RGB", (W, H), (24, 28, 29))
    d = ImageDraw.Draw(im)
    center_line(d, "COMMON ROOM", font(FONT_EN, 96), 348, (239, 236, 224))
    center_line(d, "一室两家", font(FONT_ZH, 50), 481, (202, 199, 186))
    center_line(d, "AI SI - I", font(FONT_EN, 40), 704, (239, 236, 224))
    center_line(d, "EPISODE 01", font(FONT_EN, 22), 769, (167, 174, 173))
    return im


def composite(aid, info, sub, layout=None):
    descriptor = {"renderer": VERSION, "renderer_sha256": digest_file(__file__), "asset": aid,
                  "source": info.get(aid), "sub": sub, "subtitle_layout": layout,
                  "size": [W, H], "font_en": digest_file(FONT_EN), "font_zh": digest_file(FONT_ZH)}
    key = digest_obj(descriptor)
    out = WORK / "plates" / (key + ".png")
    if out.is_file():
        return out, key
    if aid == "__authored_endcard__":
        im = compose_card()
    else:
        with Image.open(resolve(info[aid]["path"])) as source:
            source = ImageOps.exif_transpose(source).convert("RGB")
            fitted = ImageOps.contain(source, (W, H), Image.Resampling.LANCZOS)
            im = Image.new("RGB", (W, H), (0, 0, 0))
            im.paste(fitted, ((W-fitted.width)//2, (H-fitted.height)//2))
    if sub:
        en_font, zh_font = font(FONT_EN, 32), font(FONT_ZH, 40)
        en = wrap_text(sub["en"], en_font, 1640)
        zh = wrap_text(sub["zh"], zh_font, 1640)
        if len(en) > 2 or len(zh) > 2:
            raise ValueError(f"Subtitle {sub.get('line_id')}: more than two lines per language; edit segmentation")
        rows = [(t, zh_font, (255,255,249,255), 48) for t in zh]
        rows += [(t, en_font, (231,235,235,255), 40) for t in en]
        gap = 8
        block_height = sum(row[3] for row in rows) + gap
        bottom_margin = (layout or {}).get("bottom_margin", 58)
        top = H - bottom_margin - block_height
        if top < 40:
            raise ValueError(f"Subtitle {sub.get('line_id')}: safe-position override exceeds frame bounds")
        overlay = Image.new("RGBA", (W,H), (0,0,0,0))
        d = ImageDraw.Draw(overlay)
        y = top
        for index, (t,f,c,row_height) in enumerate(rows):
            if index == len(zh):
                y += gap
            center_line(d, t, f, y, c, stroke=2)
            y += row_height
        im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    temp = out.with_name(out.stem + ".partial.png")
    im.save(temp, optimize=False)
    os.replace(temp, out)
    return out, key


def segments(shots, subs, info):
    result = []
    for shot in shots:
        a,b = shot["start_frame"], shot["end_frame"]
        ss = shot["states"]
        local_subs = [x for x in subs if x["shot_id"] == shot["id"]]
        bounds = {a,b} | {a+s["offset_frame"] for s in ss}
        for sub in local_subs:
            bounds.update((sub["start_frame"],sub["end_frame"]))
        boundaries = sorted(bounds)
        for idx,(start,end) in enumerate(zip(boundaries,boundaries[1:])):
            state = next(s for s in reversed(ss) if a+s["offset_frame"] <= start)
            sub = next((s for s in local_subs if s["start_frame"] <= start < s["end_frame"]), None)
            plate,key = composite(state["asset"], info, sub, shot.get("subtitle_layout") if sub else None)
            frames = end-start
            segment_key = digest_obj({"version":VERSION,"plate":key,"frames":frames,"fps":FPS,"crf":18,"preset":"veryfast"})
            outfile = WORK / "shots" / f"{shot['id']}_{idx:02d}_{segment_key[:16]}.mp4"
            result.append({"shot_id":shot["id"],"start_frame":start,"end_frame":end,"frames":frames,
                           "asset":state["asset"],"subtitle":sub.get("line_id") if sub else None,
                           "plate":relative(plate),"path":relative(outfile),"key":segment_key})
    return result


def encode_segment(s):
    out = resolve(s["path"])
    meta = out.with_suffix(".json")
    if out.is_file() and meta.is_file():
        saved = read_json(meta)
        if saved.get("key") == s["key"] and saved.get("sha256") == digest_file(out):
            return "cached"
    out.parent.mkdir(parents=True, exist_ok=True)
    partial = out.with_name(out.stem + ".partial.mp4")
    run(["ffmpeg","-y","-v","error","-loop","1","-framerate",FPS,"-i",resolve(s["plate"]),
         "-frames:v",s["frames"],"-an","-c:v","libx264","-preset","veryfast","-tune","stillimage",
         "-crf","18","-vf","scale=out_color_matrix=bt709:out_range=tv","-pix_fmt","yuv420p","-r",FPS,"-g",48,"-bf",0,"-threads",2,
         "-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709","-color_range","tv",
         "-video_track_timescale",12288,partial])
    pr = probe(partial)
    v = next(x for x in pr["streams"] if x["codec_type"] == "video")
    if int(v.get("nb_frames",-1)) != s["frames"] or v["width"] != W or v["height"] != H:
        raise ValueError(f"{s['shot_id']}: encoded segment count/size incorrect")
    os.replace(partial,out)
    write_json(meta,{"key":s["key"],"frames":s["frames"],"sha256":digest_file(out)})
    return "rendered"


def prepare_review(parts, inputs):
    """Real production composites only; no video encoding or invented source plates."""
    directory = WORK / "review"
    directory.mkdir(parents=True, exist_ok=True)
    grouped = {}
    for part in parts:
        grouped.setdefault(part["plate"], []).append({k: part[k] for k in
            ("shot_id", "start_frame", "end_frame", "asset", "subtitle")})
    entries = [{"plate": path, "uses": uses} for path, uses in grouped.items()]
    page_paths = []
    label_font = font(FONT_EN, 20)
    for page_number, offset in enumerate(range(0, len(entries), 12), 1):
        page_entries = entries[offset:offset+12]
        canvas = Image.new("RGB", (1536, 40 + ((len(page_entries)+2)//3)*320), (24, 28, 29))
        draw = ImageDraw.Draw(canvas)
        draw.text((16, 11), f"COMMON ROOM — production layout review {page_number}", font=label_font, fill=(235, 235, 224))
        for i, entry in enumerate(page_entries):
            x, y = i % 3 * 512, 40 + i // 3 * 320
            with Image.open(resolve(entry["plate"])) as source:
                canvas.paste(source.resize((512, 288), Image.Resampling.LANCZOS), (x, y))
            first = entry["uses"][0]
            shot_ids = ",".join(dict.fromkeys(u["shot_id"] for u in entry["uses"]))
            label = f"Shot {shot_ids} / {first['asset']} / {first['subtitle'] or 'no caption'}"
            if label_font.getlength(label) > 492:
                label = f"Shot {first['shot_id']} (+{len(entry['uses'])-1} uses) / {first['asset']} / {first['subtitle'] or 'no caption'}"
            draw.text((x+10, y+293), label, font=label_font, fill=(235, 235, 224))
        page = directory / f"contact_{page_number:02d}.png"
        canvas.save(page)
        page_paths.append(relative(page))
    manifest = {"status": "awaiting_visual_review", "input_hashes": inputs,
                "native_composites": entries, "contact_sheets": page_paths,
                "caption_order": ["zh", "en"], "font_pixels": [40, 32],
                "note": "These are actual production composites; inspect native PNGs for hands, faces, paper text and object-state causality. No video encoded."}
    write_json(directory / "review_manifest.json", manifest)
    return len(entries), len(page_paths)


def timestamp(frame):
    ms = round(frame * 1000 / FPS)
    return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"


def write_srt(subs):
    out = OUT.with_suffix(".srt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = "\n\n".join(f"{i}\n{timestamp(s['start_frame'])} --> {timestamp(s['end_frame'])}\n{s['zh'].strip()}\n{s['en'].strip()}"
                         for i,s in enumerate(subs,1)) + "\n"
    out.write_text(text,encoding="utf-8")
    return out


def concat_and_mux(parts,audio,total):
    listing = WORK / "concat.txt"
    # These are renderer-owned filenames; apostrophes are escaped for ffconcat, not shell execution.
    lines = ["file '" + str(resolve(p["path"])).replace("'", "'\\''") + "'" for p in parts]
    listing.write_text("\n".join(lines)+"\n")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    partial = OUT.with_name(OUT.stem+".partial.mp4")
    run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",listing,"-i",audio,
         "-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-b:a","256k","-ar",SR,
         "-metadata","title=COMMON ROOM / 一室两家","-metadata","album=AI SI - I",
         "-metadata","comment=Episode 01 — still-image story reel with final sound",
         "-movflags","+faststart",partial])
    # Only promote after full verification in the caller.
    return partial


def audit_output(path,total):
    pr=probe(path)
    vs=[s for s in pr["streams"] if s["codec_type"]=="video"]
    ast=[s for s in pr["streams"] if s["codec_type"]=="audio"]
    if len(vs)!=1 or len(ast)!=1:
        raise ValueError("Export must have one video and one audio stream")
    v,a=vs[0],ast[0]
    if (v["width"],v["height"])!=(W,H) or Fraction(v["avg_frame_rate"])!=FPS or Fraction(v["r_frame_rate"])!=FPS:
        raise ValueError("Export resolution/frame rate incorrect")
    if int(v.get("nb_frames",-1))!=total:
        raise ValueError("Export header frame count incorrect")
    if int(a["sample_rate"])!=SR or a["channels"]!=2:
        raise ValueError("Export audio format incorrect")
    # Decode every video and audio packet, fail on decoder errors, and count decoded video frames.
    progress,err=run(["ffmpeg","-v","error","-xerror","-i",path,"-map","0:v:0","-map","0:a:0",
                      "-progress","pipe:1","-nostats","-f","null","-"])
    counts=[int(x) for x in re.findall(r"^frame=(\d+)$",progress,re.M)]
    if not counts or counts[-1]!=total or "progress=end" not in progress:
        raise ValueError(f"Full decode counted {counts[-1] if counts else None}; expected {total}")
    if err.strip():
        raise ValueError(f"Unexpected full-decode error output: {err[-2000:]}")
    expected=float(Fraction(total,FPS))
    if abs(float(a["duration"])-expected)>1/SR+1e-6:
        raise ValueError(f"AAC duration {a['duration']} differs from expected {expected}")
    return {"video":{k:v.get(k) for k in ("codec_name","width","height","pix_fmt","r_frame_rate","avg_frame_rate","nb_frames","duration")},
            "audio":{k:a.get(k) for k in ("codec_name","sample_rate","channels","duration")},
            "fully_decoded_video_frames":counts[-1],"full_decode_errors":[],"expected_frames":total}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-only",action="store_true",help="Validate actual production inputs without rendering")
    parser.add_argument("--prepare-review",action="store_true",help="Prepare actual state/caption composites and contact sheets without video encoding")
    parser.add_argument("--jobs",type=int,default=2,help="Concurrent static ffmpeg segments (default2)")
    args=parser.parse_args()
    if not 1<=args.jobs<=6:
        raise ValueError("--jobs must be1–6")
    if args.validate_only and args.prepare_review:
        raise ValueError("Choose either --validate-only or --prepare-review")
    started=time.time()
    story,shots,total,info,subs,audio,inputs=load_inputs()
    WORK.mkdir(parents=True,exist_ok=True)
    spec={"renderer":VERSION,"renderer_sha256":digest_file(__file__),"fps":FPS,"width":W,"height":H,"total_frames":total,"duration_seconds":total/FPS,
          "input_hashes":inputs,"sources":info,"shots":shots,"subtitles":subs,"audio":relative(audio),
          "output":relative(OUT),"fit":"contain","camera_motion":"none; authored state cuts only"}
    write_json(BUILD/"render.json",spec)
    print(f"Validated {len(shots)} shots, {len(info)} used images, {len(subs)} bilingual captions; {total} frames / {total/FPS:.3f}s",flush=True)
    if args.validate_only:
        return
    parts=segments(shots,subs,info)
    spec["segments"]=parts
    write_json(BUILD/"render.json",spec)
    if args.prepare_review:
        count, pages = prepare_review(parts, inputs)
        verify_input_integrity(inputs, info)
        print(f"Prepared {count} real state/caption composites in {pages} contact sheets; no video encoded", flush=True)
        return
    completed=0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures={pool.submit(encode_segment,p):p for p in parts}
        for fut in concurrent.futures.as_completed(futures):
            status=fut.result()
            completed+=1
            if completed%10==0 or completed==len(parts):
                print(f"Segments {completed}/{len(parts)} ({status})",flush=True)
    srt=write_srt(subs)
    verify_input_integrity(inputs, info)
    partial=concat_and_mux(parts,audio,total)
    measured=audit_output(partial,total)
    verify_input_integrity(inputs, info)
    os.replace(partial,OUT)
    audit={"status":"passed","renderer":VERSION,"renderer_sha256":digest_file(__file__),"created_unix":time.time(),"elapsed_seconds":round(time.time()-started,3),
           "input_hashes":inputs,"export":relative(OUT),"export_sha256":digest_file(OUT),"srt":relative(srt),
           "source_count":len(info),"shot_count":len(shots),"segment_count":len(parts),"subtitle_count":len(subs),
           "source_audio_samples":total*(SR//FPS),"source_audio_48k_stereo":True,
           "shot_and_subtitle_bounds":"validated","subtitles_on_cards":False,"composition":"native16:9; contain; no camera motion",
           "authored_endcard_branding":["COMMON ROOM","一室两家","AI SI - I","EPISODE 01"],**measured,
           "limits":["Still-image story reel; action is communicated by authored states and sound.","Technical decode and frame checks do not establish generated-motion quality."]}
    write_json(BUILD/"export_audit.json",audit)
    print(f"Export passed: {relative(OUT)} ({total} fully decoded frames)",flush=True)


if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        print(f"RENDER ERROR: {exc}",file=sys.stderr,flush=True)
        raise SystemExit(1)
