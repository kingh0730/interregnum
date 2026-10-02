"""Episode-only resumable SFX orchestration; request logs stay in work/."""
import concurrent.futures
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
manifest = json.loads((ROOT / "episodes/ep01/build/audio_sources.json").read_text())

def generate(asset):
    aid = asset["id"]
    cmd = ["uv", "run", "tools/fal_run.py", asset["endpoint"],
           f"work/ep01/audio/requests/{aid}.json", f"work/ep01/audio/sfx/{aid}", "--resume"]
    log = ROOT / f"work/ep01/audio/sfx/{aid}.process.log"
    with log.open("w") as out:
        result = subprocess.run(cmd, cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
    print(aid, result.returncode, flush=True)
    return aid, result.returncode

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(generate, manifest["assets"]))
if any(code for _, code in results):
    raise SystemExit("Some SFX requests failed; inspect per-asset process logs before resuming.")
