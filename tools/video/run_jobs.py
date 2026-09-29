"""Run a v2 job list through i2v.py in parallel: voice bible + style line appended to each prompt.

usage: uv run tools/video/run_jobs.py <jobs.json> <outdir> [--only id,id] [--take NN] [--res 720p]
Takes land at <outdir>/<id>/takes/<NN>.mp4. Existing takes are skipped.
"""
import argparse, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("jobs"); ap.add_argument("outdir")
ap.add_argument("--only"); ap.add_argument("--take", default="01"); ap.add_argument("--res", default="720p")
a = ap.parse_args()
spec = json.loads(Path(a.jobs).read_text())
only = set(a.only.split(",")) if a.only else None
todo = []
for j in spec["jobs"]:
    if only and j["id"] not in only:
        continue
    out = Path(a.outdir) / j["id"] / "takes" / f"{a.take}.mp4"
    if out.exists():
        continue
    start = j["start"] if Path(j["start"]).exists() else j.get("alt_start", j["start"])
    prompt = spec["style"] + " " + j["prompt"] + (" " + spec["voices"][j["voice"]] if j.get("voice") else "")
    cmd = ["uv", "run", "tools/video/i2v.py", start, str(out), prompt, "--dur", str(j["dur"]), "--res", a.res]
    if j.get("silent"):
        cmd.append("--no-audio")
    todo.append((j["id"], out, cmd))
est = sum(int(c[c.index("--dur") + 1]) for _, _, c in todo) * (0.473 if a.res == "720p" else 0.2205)
print(f"{len(todo)} takes, est ${est:.2f}", flush=True)

def run(t):
    jid, out, cmd = t
    out.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    out.with_suffix(".log").write_text(r.stdout + r.stderr)
    return jid, "ok" if r.returncode == 0 else "FAILED " + (r.stdout + r.stderr).strip()[-300:]

with ThreadPoolExecutor(8) as ex:
    for jid, st in ex.map(run, todo):
        print(jid, st, flush=True)
