"""Shots 31, 34, 37, 45, 46: broadcast and JS wraps. usage: uv run simple.py 31|34|37|45|46"""
import sys

from fx import *

EYES_F = (0.50, 0.42)


def s31():
    spec(31, 5.0, [{"src": "work/pilot/keys/k02.png"}] + broadcast_layers(),
         camera={"from": [0.5, 0.5, 1.0], "to": focus_cam(*EYES_F, 1.04), "ease": "inout"},
         grade_=grade("BROADCAST"), letterbox=False)


def s34():
    a, b = key("k02"), cv2.imread(str(HERE / "k20e.png"))[..., ::-1].astype(np.float32) / 255
    h, w = a.shape[:2]
    wr = Writer(HERE / "p34.mp4", w, h)
    for i in range(144):
        t = i / FPS
        u = ease_sine((t - 1.0) / 1.5)
        dip = 1 - 0.03 * np.sin(np.pi * np.clip((t - 1.0) / 1.5, 0, 1))
        wr.write((a * (1 - u) + b * u) * dip)
    wr.close()
    # the bug overlay with LIVE blinking out at 5.6 s comes from the JS render
    spec(34, 6.0, [{"src": rel(HERE / "p34.mp4")},
                   {"src": rel(HERE / "scanlines.png"), "fixed": True},
                   {"src": "work/pilot/js/s34_bug.mov", "fixed": True}],
         camera={"from": focus_cam(*EYES_F, 1.04), "to": focus_cam(*EYES_F, 1.06), "ease": "inout"},
         grade_=grade("BROADCAST"), letterbox=False)


def s37():
    # glass sheen: a faint soft diagonal highlight, fixed over the phone
    sh = np.zeros((1080, 1920, 4), np.float32)
    Y, X = np.mgrid[0:1080, 0:1920].astype(np.float32)
    d = (X - 700) * 0.8 - (Y - 150) * 0.6
    band = np.exp(-((d - 160) / 90) ** 2) * 0.04
    inside = ((X > 714) & (X < 1206) & (Y > 164) & (Y < 916)).astype(np.float32)
    inside = blur(inside, 6)
    sh[..., :3] = 1.0
    sh[..., 3] = band * inside
    save_png(HERE / "sheen37.png", sh)
    spec(37, 3.0, [{"src": "work/pilot/js/s37_phone.mp4"}, {"src": rel(HERE / "sheen37.png"), "fixed": True}],
         grade_=grade("HALL", lift=[0.02, 0.025, 0.045], gain=[1.0, 1.0, 1.02], bloom=0.45))


def s45():
    spec(45, 9.0, [{"src": "work/pilot/js/s45_titles.mp4"}], grade_=grade("JS", vignette=0, bloom=0.15),
         letterbox=False)


def s46():
    # three segments rendered separately, then concatenated (the camera push must run only over the k01 part)
    base = {"fps": FPS}
    segs = [
        {"dur": 1.0, "out": rel(HERE / "s46a.mp4"), "layers": [{"src": "work/pilot/js/s46_night213.mp4"}],
         "grade": grade("JS", vignette=0, bloom=0.15)},
        {"dur": 3.0, "out": rel(HERE / "s46b.mp4"),
         "layers": [{"src": "work/pilot/js/s28_ident_fast.mp4"}, {"src": rel(HERE / "scanlines.png"), "fixed": True}],
         "grade": grade("BROADCAST")},
        {"dur": 6.0, "out": rel(HERE / "s46c.mp4"),
         "layers": [{"src": "work/pilot/keys/k01.png"}] + broadcast_layers(),
         "camera": {"from": [0.5, 0.5, 1.0], "to": focus_cam(0.5, 0.33, 1.035), "ease": "inout"},
         "grade": grade("BROADCAST"), "flash": [[5.58, 1.0, [0, 0, 0]]]},
    ]
    for k, s in zip("abc", segs):
        s.update(base)
        (HERE / f"s46{k}.json").write_text(json.dumps(s, indent=1))
    # final assembly through reel.py: the three pre-rendered segments as fixed layers, no further grade
    L = [{"src": rel(HERE / "s46a.mp4"), "fixed": True, "t0": 0.0, "t1": 1.0},
         {"src": rel(HERE / "s46b.mp4"), "fixed": True, "t0": 1.0, "t1": 4.0},
         {"src": rel(HERE / "s46c.mp4"), "fixed": True, "t0": 4.0, "t1": 10.0}]
    spec(46, 10.0, L, grade_={"bloom": 0, "vignette": 0, "grain": 0}, letterbox=False)


if __name__ == "__main__":
    globals()["s" + sys.argv[1]]()
