"""Register selected stills and exact authored paper states; makes no API calls.

Run from any directory after restoring the ignored work/ep01 media tree.
Rerunning this script registers media and checks file integrity. Artistic approval
comes only from a separate current continuity review of the actual cut.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / "episodes/ep01/build"
SELECTED = {
    "k01": "k01_edit", "k03": "k03_fix", "k04": "k04_fix",
    "k05": "k05_fix", "k06": "k06_edit", "k08": "k08_edit",
    "k09": "k09_fix", "k10": "k10_fix", "k11": "k11_fix",
    "k12": "k12_final", "k13": "k13_fix", "k14": "k14_edit",
    "k15": "k15_edit", "k16": "k16_final", "k17": "k17_final",
    "k19": "k19_edit", "k20": "k20_edit", "k21": "k21_edit",
    "k22": "k22_edit", "k23": "k23_edit", "k24": "k24_edit",
    "k25": "k25_edit", "k26": "k26_edit", "k28": "k28_edit",
    "k29": "k29_edit", "k30": "k30_edit", "k31": "k31_edit",
}


def save(name, data):
    (BUILD / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    assets = {key: f"work/ep01/keys/{value}.png" for key, value in SELECTED.items()}
    assets.update(json.loads((BUILD / "paper_assets.json").read_text()))
    edits = {item["id"]: item for item in json.loads((BUILD / "codex_edits.json").read_text())}
    records = []
    for key, path in assets.items():
        source = ROOT / path
        with Image.open(source) as im:
            width, height = im.size
            im.verify()
        if abs(width / height - 16 / 9) > 0.025:
            raise ValueError(f"Unexpected canvas: {key}: {width}x{height}")
        selected = SELECTED.get(key)
        records.append({
            "asset": key, "path": path,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "dimensions": [width, height],
            "method": "Codex built-in image edit of approved photographic sources" if selected else "Authored paper graphics on photographic ash-table plate",
            "recipe": "episodes/ep01/build/codex_edits.json" if selected else "episodes/ep01/build/paper_graphics.py",
            "edit_id": selected,
            "base": edits[selected]["base"] if selected else "ref_paper",
        })
    save("assets.json", dict(sorted(assets.items())))
    save("reel_states.json", json.loads((BUILD / "paper_states.json").read_text()))
    save("selected_assets.json", {
        "scope": "Selected static starting frames and authored insert states; registration does not confer visual or motion approval.",
        "review_basis": "File integrity and dimensions only. Consult the current continuity review for spatial approval; registration never clears its pending or blocked cuts.",
        "continuity_review": "episodes/ep01/build/continuity_review.json",
        "photographic_source_policy": "Luma Uni-1 Max originals; Codex built-in generative continuity edits. Exact lettering is authored separately.",
        "endcard": "k27 is exact typography rendered by render_reel.py; no generated lettering.",
        "assets": records,
    })
    print(f"Registered {len(SELECTED)} photographic plates and {len(assets)-len(SELECTED)} paper states.")


if __name__ == "__main__":
    main()
