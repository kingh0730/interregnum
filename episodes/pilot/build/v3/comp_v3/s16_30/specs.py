"""Write work/pilot/comp_v3/NN.json for shots 16-30 (plates from shots.py)."""
import json
from pathlib import Path

O = Path(__file__).resolve().parent
D = "work/pilot/comp_v3/s16_30"
FR = {16: 144, 17: 96, 18: 120, 19: 96, 20: 144, 21: 192, 22: 48, 23: 144, 24: 192, 25: 72, 26: 216, 27: 96,
      28: 72, 29: 120, 30: 144}
# RELIEF grades: no film grain (paper grain is static, in the plate), no global bloom (glow is in the plate,
# screens and lamps only); exposure offsets reel's soft shoulder.
HALL = {"exposure": 0.12, "contrast": 1.03, "sat": 1.0, "lift": [0.0, 0.004, 0.012], "gain": [0.985, 1.0, 1.02],
        "bloom": 0, "vignette": 0.25, "grain": 0}
HOME = {"exposure": 0.12, "contrast": 1.02, "sat": 1.0, "lift": [0.006, 0.003, 0.0], "gain": [1.02, 1.0, 0.975],
        "bloom": 0, "vignette": 0.22, "grain": 0}
CITY = {"exposure": 0.12, "contrast": 1.02, "sat": 1.0, "lift": [0.004, 0.012, 0.024], "gain": [0.97, 1.0, 1.03],
        "bloom": 0, "vignette": 0.25, "grain": 0}
PASS = {"exposure": 0.12, "contrast": 1.0, "sat": 1.0, "bloom": 0, "vignette": 0, "grain": 0}
GRADE = {16: HOME, 17: HALL, 18: HOME, 19: HALL, 20: HOME, 21: HALL, 22: HALL, 23: HALL, 24: HALL, 25: HALL,
         26: HALL, 27: HALL, 28: PASS, 29: PASS, 30: CITY}


def focus(f, z):
    """Camera centre for a push that scales about focus point f (normalized plate coords)."""
    return [f[0] + (0.5 - f[0]) / z, f[1] + (0.5 - f[1]) / z, z]


for n, fr in FR.items():
    s = {"dur": fr / 24, "fps": 24, "out": f"work/pilot/shots_v3/{n:02d}.mp4", "grade": GRADE[n]}
    if n == 28:
        s["layers"] = [{"src": "work/pilot/js_v3/j01_lighting_fast.mp4", "fixed": True}]
    elif n == 29:
        s["layers"] = [{"src": f"{D}/b29.mp4", "fixed": True}]
    else:
        s["layers"] = [{"src": f"{D}/b{n}.mp4"}]
        s["letterbox"] = 2.39
    if n == 22:   # push 1.00 -> 1.06 onto the minutes card (red 00), accelerating
        s["camera"] = {"from": [0.5, 0.5, 1.0], "to": focus([634 / 1672, 695 / 941], 1.06), "ease": "in"}
        s["particles"] = [{"kind": "motes", "n": 18, "seed": 22, "par": 0.6, "wind": [0.002, -0.003],
                           "color": [0.8, 0.95, 1.0], "opacity": 0.35, "size": 0.7}]
    if n == 23:   # push past her into his eyes, accelerating; she (the near layer) slides down and out
        c = focus([0.4994, 0.4838], 1.10)
        s["camera"] = {"from": [0.5, 0.5, 1.0], "to": c, "ease": "in"}
        s["layers"].append({"src": f"{D}/k14_fg.png", "par": 1.4})
        s["particles"] = [{"kind": "dust", "n": 80, "seed": 23, "par": 1.1, "wind": [0.003, -0.002],
                           "color": [0.75, 0.92, 1.0], "opacity": 0.45, "size": 0.9}]
    if n == 27:   # push 1.00 -> 1.06 onto the fingertip, accelerating; hard cut
        s["camera"] = {"from": [0.5, 0.5, 1.0], "to": focus([975 / 1672, 375 / 941], 1.06), "ease": "in"}
    (O.parent / f"{n:02d}.json").write_text(json.dumps(s, indent=1))
    print(n, fr)
