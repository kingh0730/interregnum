"""Write work/pilot/comp/16.json .. 30.json (reel.py specs)."""
import json
from pathlib import Path

import numpy as np

O = Path(__file__).parent
C = O.parent
D = "work/pilot/comp/s16_30"

HALL = {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.03, 0.04, 0.075], "gain": [0.97, 1.0, 1.04],
        "bloom": 0.5, "vignette": 0.25, "grain": 0.02}
HOME = {"exposure": 0, "contrast": 1.02, "sat": 1.02, "lift": [0.03, 0.025, 0.035], "gain": [1.04, 1.0, 0.96],
        "bloom": 0.55, "vignette": 0.22, "grain": 0.02}
CITY = {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.03, 0.05, 0.07], "gain": [0.93, 1.0, 1.05],
        "bloom": 0.6, "vignette": 0.25, "grain": 0.025}
SCREEN = {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.02, 0.025, 0.045], "gain": [0.99, 1.0, 1.03],
          "bloom": 0.45, "vignette": 0.25, "grain": 0.02}
BROADCAST = {"exposure": 0, "contrast": 1.0, "sat": 0.9, "lift": [0.063, 0.094, 0.149], "gain": [0.98, 1.0, 1.02],
             "bloom": 0.3, "vignette": 0.15, "grain": 0.015, "chroma": 1}


def push(f, z1, c0=(0.5, 0.5), p=1.0):
    """Camera from/to so the focus point f stays put on a layer with parallax factor p."""
    c0 = np.array(c0, float)
    f = np.array(f, float)
    cp0 = 0.5 + (c0 - 0.5) * p
    zp1 = 1 + (z1 - 1) * p
    cp1 = f - (f - cp0) / zp1
    c1 = 0.5 + (cp1 - 0.5) / p
    return [*map(float, c0), 1.0], [*map(float, c1), float(z1)]


def spec(n, dur, layers, grade, camera=None, lb=True, **kw):
    s = {"dur": dur, "fps": 24, "out": f"work/pilot/shots/{n}.mp4", "layers": layers}
    if camera:
        s["camera"] = camera
    s["grade"] = grade
    if lb:
        s["letterbox"] = 2.39
    s.update(kw)
    (C / f"{n}.json").write_text(json.dumps(s, indent=1))


def cam(f, z1, c0=(0.5, 0.5), p=1.0, ease="inout"):
    a, b = push(f, z1, c0, p)
    return {"from": a, "to": b, "ease": ease}


# 16 Nana's room: plate 0.7, Nana 1.0, push on her head
spec(16, 6.0, [{"src": f"{D}/b16.mp4", "par": 0.7}, {"src": f"{D}/k09_fg.png", "par": 1.0}], HOME,
     cam((0.135, 0.37), 1.04, (0.5, 0.5)),
     particles=[{"kind": "motes", "n": 40, "seed": 16, "par": 0.9, "wind": [0.002, -0.002], "color": [1.0, 0.8, 0.5],
                 "opacity": 0.35, "size": 0.8}])
# 17 Ida calls
spec(17, 4.0, [{"src": f"{D}/b17.mp4"}], HALL, cam((0.34, 0.34), 1.03))
# 18 Nana answers (image lowered so her hair clears the bar)
spec(18, 5.0, [{"src": f"{D}/b18.mp4"}], HOME, cam((0.51, 0.31), 1.03, (0.5, 0.445)))
# 19 The question
spec(19, 4.0, [{"src": f"{D}/b19.mp4"}], HALL, cam((0.36, 0.33), 1.03, (0.5, 0.45)))
# 20 For the ending
spec(20, 6.0, [{"src": f"{D}/b20.mp4"}], HOME, cam((0.66, 0.37), 1.035, (0.5, 0.455)))
# 21 / 22 / 24 / 26 JS world screens
for n, src, dur in ((21, "s21_signoffs", 8.0), (22, "s22_clock", 2.0), (24, "s24_i", 8.0), (26, "s26_eat", 9.0)):
    spec(n, dur, [{"src": f"work/pilot/js/{src}.mp4", "fixed": True},
                  {"src": f"{D}/scan4.png", "fixed": True, "blend": "multiply"}], SCREEN)
# 23 The face: plate 0.7 (wall with k02), Ida 1.4, accelerating push into the eyes
eyes = np.load(O / "k14_eyes.npy") if (O / "k14_eyes.npy").exists() else np.array([0.5, 0.36])
spec(23, 6.0, [{"src": f"{D}/b23.mp4", "par": 0.7}, {"src": f"{D}/k14_fg.png", "par": 1.4}], HALL,
     cam(tuple(eyes), 1.1 / 0.7 - 1 / 0.7 + 1, (0.5, 0.47), p=0.7, ease="in"),
     particles=[{"kind": "dust", "n": 80, "seed": 23, "par": 1.1, "wind": [0.004, -0.002],
                 "color": [0.75, 0.92, 1.0], "opacity": 0.7, "size": 0.9}])
# 25 Her eyes
spec(25, 3.0, [{"src": f"{D}/b25.mp4"}], HALL, cam((0.5, 0.57), 1.02, (0.5, 0.545)))
# 27 The key
spec(27, 4.0, [{"src": f"{D}/b27.mp4"}], HALL, cam((0.50, 0.555), 1.06, (0.5, 0.5), ease="in"))
# 28 Ident fast (broadcast, colder, no bug, no letterbox)
spec(28, 3.0, [{"src": "work/pilot/js/s28_ident_fast.mp4", "fixed": True},
               {"src": "work/pilot/comp/c1/scanlines.png", "fixed": True}],
     dict(BROADCAST, sat=0.81, gain=[0.95, 1.0, 1.05]), lb=False, flash=[[0.0, 0.3, [0, 0, 0]]])
# 29 The Address: shot 02's recipe on k01
spec(29, 5.0, [{"src": "work/pilot/keys/k01.png"}, {"src": "work/pilot/comp/c1/scanlines.png", "fixed": True},
               {"src": "work/pilot/js/j14_bug.png", "fixed": True}], BROADCAST,
     cam((0.5, 0.40), 1.035), lb=False, light={"flicker": 0.03, "flicker_hz": 0.3})
# 30 The street: plate 0.6, crowd 1.0, push on the facade screen; rain far + near
spec(30, 6.0, [{"src": f"{D}/b30.mp4", "par": 0.6}, {"src": f"{D}/k17_fg.png", "par": 1.0}], CITY,
     cam((0.594, 0.235), 1.04, (0.5, 0.445)),
     particles=[{"kind": "rain", "n": 700, "seed": 30, "par": 0.8, "wind": [0.10, 0.0], "size": 0.6, "opacity": 0.55},
                {"kind": "rain", "n": 70, "seed": 31, "par": 1.4, "wind": [0.14, 0.0], "size": 1.5, "opacity": 0.8}])
print("ok")
