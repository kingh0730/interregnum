"""Verify the finished pre-motion package and write its small public manifest.

No generation, uploads, account changes or paid requests. Media remains ignored.
Run after render_reel.py and the final motion_preflight.py dry-run.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
B = ROOT / "episodes/ep01/build"
sys.path.insert(0, str(ROOT / "tools"))
from continuity import evaluate_review


def read(path):
    return json.loads((ROOT / path).read_text())


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    manifest = read("episodes/ep01/build/motion_plan.json")
    continuity = evaluate_review(manifest.get("continuity_review"), ROOT)
    require(continuity["approved"], "Continuity approval required: " + "; ".join(continuity["errors"]))
    review = json.loads(Path(continuity["review_path"]).read_text())
    for key, name in [("story", "story.json"), ("assets", "assets.json"), ("states", "reel_states.json")]:
        require((ROOT / review.get(key, {}).get("path", "")).resolve() == (B / name).resolve(),
                f"Continuity review must bind episode 01 {name}")
    visual = read("episodes/ep01/build/visual_review.json")
    require(visual.get("status") == "passed", "Visual approval has not passed or has been withdrawn")
    story = read("episodes/ep01/build/story.json")
    export = read("episodes/ep01/build/export_audit.json")
    motion = read("episodes/ep01/build/motion_preflight.json")
    audio = read("work/ep01/audio/technical_qc.json")
    selected = read("episodes/ep01/build/selected_assets.json")
    budget = read("episodes/ep01/build/budget_estimate.json")
    encoded_frames = read("episodes/ep01/build/export_frame_audit.json")
    encoded_audio = read("work/ep01/audio/export_audio_audit.json")
    require(export["status"] == "passed", "Export audit has not passed")
    require(export["export_sha256"] == digest(export["export"]), "Export changed after audit")
    require(encoded_frames["status"] == "passed" and encoded_frames["export_sha256"] == export["export_sha256"], "Decoded image review does not match export")
    require(encoded_audio["pass"] and encoded_audio["export_sha256"] == export["export_sha256"], "Decoded audio review does not match export")
    story_hash = digest("episodes/ep01/build/story.json")
    require(export["input_hashes"]["story"] == story_hash, "Export uses an older story file")
    require(visual["hashes"]["story"] == story_hash, "Visual review uses an older story file")
    for key, path in {
        "assets_map": "episodes/ep01/build/assets.json",
        "subtitle_layouts": "episodes/ep01/build/subtitle_layouts.json",
        "subtitles": "work/ep01/audio/subtitles.json",
    }.items():
        require(export["input_hashes"][key] == digest(path), f"Export input changed: {key}")
        require(visual["hashes"][key] == digest(path), f"Visual review input changed: {key}")
    require(motion["story_sha256"] == story_hash, "Motion preflight uses an older story file")
    require(motion["local_media_ready"] and motion["runner_dry_run_performed"], "Motion inputs need preflight")
    require(motion.get("ready_for_motion") and motion.get("continuity_approved"), "Motion preflight needs current continuity approval")
    require(motion.get("continuity_review", {}).get("review_sha256") == continuity["review_sha256"], "Continuity review changed after preflight")
    require(motion["video_requests_submitted"] == 0, "Pre-motion scope exceeded")
    require(motion["manifest_sha256"] == digest("episodes/ep01/build/motion_plan.json"), "Motion manifest changed after preflight")
    master = "work/ep01/audio/master_mix.wav"
    require(audio["master_sha256"] == digest(master), "Audio changed after QC")
    require(export["input_hashes"]["audio"] == digest(master), "Reel does not use the final master")
    require(not audio["issues"] and not audio["missing_sources"], "Audio QC has unresolved issues")
    require(story["total_frames"] == 5520 and story["fps"] == 24, "Timeline changed")
    for item in selected["assets"]:
        require(item["sha256"] == digest(item["path"]), f"Selected plate changed: {item['asset']}")
    paths = [export["export"], export["srt"], master,
             "episodes/ep01/build/assets.json", "episodes/ep01/build/reel_states.json",
             "episodes/ep01/build/story.json", "episodes/ep01/build/motion_plan.json",
             "episodes/ep01/build/export_audit.json", "episodes/ep01/build/motion_preflight.json",
             "episodes/ep01/build/visual_review.json",
             manifest["continuity_review"],
             "episodes/ep01/build/export_frame_audit.json", "work/ep01/audio/export_audio_audit.json",
             "episodes/ep01/build/selected_assets.json"]
    result = {
        "episode": "COMMON ROOM / 一室两家", "series": "AI SI - I", "number": 1,
        "status": "Complete through stage 6: still-based story reel and final prepared sound. Motion handoff prepared; video generation not started.",
        "duration_seconds": 230, "fps": 24, "frames": 5520,
        "canvas": [1920, 1080], "shots": 40, "dialogue_lines": 26,
        "photographic_plates": 27, "authored_paper_states": 6,
        "subtitles": "Chinese-first bilingual burn-ins and bilingual SRT",
        "audio": {"path": master, "sample_rate": 48000, "channels": 2, "bits": 24,
                  "integrated_lufs": audio["master"]["I"], "true_peak_dbtp": audio["master"]["TP"],
                  "loudness_range_lu": audio["master"]["LRA"]},
        "motion_jobs_prepared": 30, "motion_requests_submitted": 0,
        "continuity_approved": True, "continuity_review": manifest["continuity_review"],
        "export_audio_measurements": encoded_audio["measurements"],
        "export_audio_zero_lag_correlation": encoded_audio["zero_lag_full_cut_correlation"],
        "motion_budget": motion["budget"],
        "fal_estimate_usd": budget["fal"]["successful_output_estimate_usd"],
        "fal_conservative_requested_units_usd": budget["fal"]["conservative_all_requested_units_estimate_usd"],
        "cost_limits": "Estimates, not reconciled invoices. Built-in image quota and ElevenLabs subscription usage are not converted to a verified dollar total.",
        "review_limits": [
            "Actual stills and caption composites were visually inspected; full export decode, frame counts and media integrity were checked.",
            "Perceptual audio playback has not been performed. Naturalness, Foley recognition, musical effect and final listening balance remain listening-review items.",
            "No generated character motion exists. Future motion needs actual-take and final-cut review."
        ],
        "files": [{"path": p, "bytes": (ROOT / p).stat().st_size, "sha256": digest(p)} for p in paths],
    }
    (B / "delivery_manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("Delivery package verified; video-generation requests: 0.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"Delivery remains unapproved: {exc}", file=sys.stderr)
        sys.exit(2)
