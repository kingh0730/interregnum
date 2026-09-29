"""Write reel.py specs work/pilot/comp_v3/NN.json for shots 32-45 (31 and 34 are written by hand)."""
import json
import sys
from pathlib import Path

D = "work/pilot/comp_v3/s31_45"
ROOT = Path(__file__).resolve().parents[4]
HALL = {"exposure": 0, "contrast": 1.04, "sat": 1.0, "lift": [0.03, 0.04, 0.065], "gain": [0.99, 1.0, 1.02],
        "bloom": 0.15, "vignette": 0.25, "grain": 0}
HOME = {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.035, 0.035, 0.045], "gain": [1.02, 1.0, 0.98],
        "bloom": 0.12, "vignette": 0.22, "grain": 0}
HOME_WARM = dict(HOME, gain=[1.03, 1.0, 0.96], lift=[0.035, 0.032, 0.035])
DAWN = {"exposure": 0, "contrast": 1.03, "sat": 1.0, "lift": [0.03, 0.035, 0.055], "gain": [1.0, 1.0, 1.0],
        "bloom": 0.12, "vignette": 0.2, "grain": 0}
PAPER = {"src": f"{D}/paper_20.png", "fixed": True, "blend": "multiply"}
PAPER15 = {"src": f"{D}/paper_15.png", "fixed": True, "blend": "multiply"}


def spec(n, dur, layers, grade, camera=None, letterbox=2.39, extra=None):
    s = {"dur": dur, "fps": 24, "out": f"work/pilot/shots_v3/{n}.mp4", "layers": layers, "grade": grade}
    if camera:
        s["camera"] = camera
    if letterbox:
        s["letterbox"] = letterbox
    if extra:
        s.update(extra)
    (ROOT / f"work/pilot/comp_v3/{n}.json").write_text(json.dumps(s, indent=1))


def P(n):
    return {"src": f"{D}/p{n}_plate.mov"}


spec("32", 6.0, [P(32), PAPER], HALL,
     camera={"from": [0.4915, 0.5034, 1.06], "to": [0.5, 0.5, 1.0], "ease": "linear"})
spec("33", 6.0, [P(33), PAPER], HOME)
spec("35", 2.0, [P(35), PAPER], HALL)
spec("36", 4.0, [P(36), PAPER], HALL)
spec("37", 3.0, [P(37), PAPER], dict(HALL, gain=[1.0, 1.0, 1.01]))
spec("38", 3.0, [P(38), PAPER], dict(HALL, gain=[1.0, 1.0, 1.01]))
spec("39", 4.0, [P(39), PAPER], HOME_WARM)
spec("40", 3.0, [P(40), PAPER], dict(HALL, gain=[1.0, 1.0, 1.01]))
spec("41", 5.0, [P(41), PAPER], HOME_WARM)
spec("42", 7.0, [P(42), PAPER], dict(HALL, gain=[1.0, 1.0, 1.0]))
spec("43", 6.0, [P(43), PAPER], dict(HALL, exposure=-0.234))   # -15 % exposure = 2**-0.234
spec("44", 10.0, [P(44), PAPER15], DAWN)
spec("45", 9.0, [{"src": "work/pilot/js_v3/j13_card.mp4", "fixed": True}], 
     {"exposure": 0, "contrast": 1.0, "sat": 1.0, "lift": [0, 0, 0], "gain": [1.05, 1.05, 1.05], "bloom": 0,
      "vignette": 0, "grain": 0})
