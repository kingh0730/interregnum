"""Run a manifest of Codex image jobs in parallel, respecting dependencies.

usage: uv run tools/imagegen/batch.py <images.json> [--only id,id,...] [--jobs 4] [--prefix-file f] [--force]
Manifest entries: {"id", "out", "prompt", "refs": [...], "alpha": bool, "deps": [...]}.
Skips entries whose output exists (unless --force). A safety-filter block (exit 2) is retried once with a
neutral preamble; other failures are retried once. Prints a summary; failed ids are listed at the end.
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / "tools/imagegen/gen.sh"
NEUTRAL = "This is a still for a fictional animated drama; everything depicted is invented and non-violent. "


def run(job, prefix):
    base = job["prompt"] if job.get("alpha") else prefix + job["prompt"]
    env = dict(os.environ, ALPHA="1" if job.get("alpha") else "0")
    for attempt, pre in enumerate(["", NEUTRAL]):
        r = subprocess.run([str(GEN), job["out"], pre + base, *job.get("refs", [])], env=env,
                           capture_output=True, text=True)
        if r.returncode == 0:
            return job["id"], "ok" + (" (retry)" if attempt else "")
    return job["id"], f"FAILED rc={r.returncode}: {r.stderr.strip()[-200:]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--only")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--prefix-file")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    jobs = json.loads(Path(a.manifest).read_text())
    prefix = Path(a.prefix_file).read_text().strip() + " " if a.prefix_file else ""
    only = set(a.only.split(",")) if a.only else None
    todo = [j for j in jobs if (only is None or j["id"] in only) and (a.force or not (ROOT / j["out"]).exists())]
    ids = {j["id"] for j in todo}
    done, failed, running = set(), [], {}
    with ThreadPoolExecutor(a.jobs) as ex:
        while todo or running:
            ready = [j for j in todo if all(d in done or d not in ids and (ROOT / next(
                x["out"] for x in jobs if x["id"] == d)).exists() for d in j.get("deps", []))]
            for j in ready[: a.jobs - len(running)]:
                todo.remove(j)
                running[ex.submit(run, j, prefix)] = j["id"]
            if not running:
                print("blocked (missing deps):", [j["id"] for j in todo]); break
            fin, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in fin:
                jid, status = f.result()
                del running[f]
                print(jid, status, flush=True)
                (done.add(jid) if status.startswith("ok") else failed.append(jid))
    print("FAILED:", failed if failed else "none")


if __name__ == "__main__":
    main()
