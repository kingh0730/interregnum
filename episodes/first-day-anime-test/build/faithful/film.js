import {
  W,
  H,
  C,
  canvas,
  text,
  image,
  cover,
  ease,
  clamp,
  lerp,
  glow,
} from "./common.js";
import { Effects } from "./effects.js";
import { Rigs } from "./rigs.js";
import { tornWipe } from "./surfaces.js";
const c = document.querySelector("#film"),
  g = c.getContext("2d", { alpha: false }),
  base = document.querySelector("#base"),
  webgl = document.querySelector("#webgl");
const imgs = {},
  movies = {};
let data, fx, rigs, marks, cues, handMask, monitor, monitorMasks;
async function movie(name, url) {
  const v = document.createElement("video");
  v.muted = true;
  v.preload = "auto";
  v.src = url;
  document.body.append(v);
  await new Promise((res, rej) => {
    v.addEventListener("loadeddata", res, { once: true });
    v.addEventListener("error", rej, { once: true });
  });
  movies[name] = v;
  return v;
}
async function seek(v, t) {
  t = Math.min(Math.max(0, t), v.duration - 0.045);
  if (Math.abs(v.currentTime - t) < 0.0004) return;
  await new Promise((res, rej) => {
    const timer = setTimeout(() => rej(Error("seek " + t)), 15000);
    v.addEventListener(
      "seeked",
      () => {
        clearTimeout(timer);
        res();
      },
      { once: true },
    );
    v.currentTime = t + 0.0001;
  });
}
function crop(im, cx, cy, z) {
  const iw = im.videoWidth || im.width,
    ih = im.videoHeight || im.height,
    fit = Math.max(W / iw, H / ih),
    cw = W / (fit * z),
    ch = H / (fit * z);
  g.drawImage(im, cx * iw - cw / 2, cy * ih - ch / 2, cw, ch, 0, 0, W, H);
}
function camera(z, cx = 0.5, cy = 0.5, rotation = 0) {
  z = Math.max(1, z);
  cx = Math.max(0.5 / z, Math.min(1 - 0.5 / z, cx));
  cy = Math.max(0.5 / z, Math.min(1 - 0.5 / z, cy));
  const a = canvas(W, H);
  a.getContext("2d").drawImage(c, 0, 0);
  g.save();
  g.translate(960, 540);
  g.rotate(rotation);
  g.scale(z, z);
  g.translate(-W * cx, -H * cy);
  g.drawImage(a, 0, 0);
  g.restore();
}
window.ready = (async () => {
  data = await (await fetch("/faithful/data.json")).json();
  marks = await (await fetch("/faithful/marks.json")).json();
  cues = await (await fetch("/faithful/audio-cues.json")).json();
  handMask = await (await fetch("/faithful/touch-hand-mask.json")).json();
  monitor = await (
    await fetch("/faithful/reply-performance/monitor.json")
  ).json();
  monitorMasks = await Promise.all(
    monitor.quads.map((_, i) =>
      image(
        "/faithful/reply-performance/masks/" +
          String(i).padStart(4, "0") +
          ".png",
      ),
    ),
  );
  for (const f of [
    "600 46px FDSerif",
    "900 80px FDSerif",
    "700 50px FDSans",
    "600 390px FDLora",
    "500 50px FDInter",
    "400 50px FDSymbol",
  ])
    await document.fonts.load(f);
  await document.fonts.ready;
  await Promise.all(
    Object.entries({
      glasses: "/assets/s01-glasses.png",
      spark: "/assets/claude-spark.svg",
      a: "/assets/anthropic-a.svg",
      room: "/assets/s03-room.png",
      birthBg: "/faithful/birth-room-clean.png",
      birthObserver: "/faithful/birth-xiaoman.png",
      tea: "/assets/s04-tea.png",
      screen: "/assets/s05-screen-clean.png",
      eye: "/assets/breath-clean.png",
      eyeClosed: "/faithful/eye-closed.png",
      sky: "/assets/sky.png",
      city: "/assets/city.png",
      flight: "/assets/flight-clean.png",
      float: "/assets/float-clean.png",
    }).map(async ([k, v]) => (imgs[k] = await image(v))),
  );
  if (base.readyState < 2)
    await new Promise((r) =>
      base.addEventListener("loadeddata", r, { once: true }),
    );
  await Promise.all([
    movie("touch", "/motion/touch.mp4"),
    movie("orbit", "/faithful/orbit-wide.mp4"),
    movie("sing", "/faithful/lipsync-test/mandarin-line.mp4"),

    movie("reply", "/faithful/reply-performance/reply-performance.mp4"),
    movie("burst", "/motion/burst.mp4"),
    movie("steps", "/faithful/steps-performance/steps-performance.mp4"),
    movie("breath", "/motion/breath.mp4"),
    movie("flight", "/motion/flight.mp4"),
    movie("ankle", "/motion/ankle.mp4"),
    movie("joy", "/motion/xiaoman-joy.mp4"),
    movie("hug", "/motion/hug.mp4"),
  ]);
  fx = new Effects(g, imgs);
  rigs = new Rigs(webgl, data);
  await rigs.init();
})();
window.renderFrame = async (t) => {
  await window.ready;
  const f = Math.round(t * 30),
    shot =
      data.shots.find((s) => f >= s.start_frame && f < s.end_frame) ||
      data.shots.at(-1),
    n = +shot.id.slice(1),
    local = f - shot.start_frame,
    p = local / Math.max(1, shot.end_frame - shot.start_frame - 1);
  await seek(base, t);
  g.resetTransform();
  g.globalAlpha = 1;
  g.globalCompositeOperation = "source-over";
  g.shadowBlur = 0;
  g.filter = "none";
  cover(g, base);
  const lyricIndex = data.lyrics.findLastIndex((l) => l.frame <= f),
    lineCue = data.lyrics[lyricIndex],
    lineEnd = Math.min(
      data.lyrics[lyricIndex + 1]?.frame ?? 1311,
      lineCue.frame === 1197 ? 1248 : 1311,
    ),
    lineBegin = lineCue.frame + ([358, 920].includes(lineCue.frame) ? 2 : 0);
  fx.lyricOpacity = clamp(
    Math.min(1, (f - lineBegin + 1) / 3, (lineEnd - f) / 3),
  );
  rigs.lyricOpacity = fx.lyricOpacity;
  fx.trace = {};
  rigs.trace = {};
  const web = () => {
    g.fillStyle = C.ink;
    g.fillRect(0, 0, W, H);
    g.drawImage(webgl, 0, 0, W, H);
  };
  let spatial = false;
  if (n <= 2) fx.opening(t);
  else if (n === 3) fx.room(p, t);
  else if (n === 4) {
    camera(1.03 + 0.025 * ease(p), 0.5 + 0.004 * Math.sin(t * 2), 0.5);
    glow(g, 120, 415, 85, C.coral, 0.04 + 0.08 * p);
    g.fillStyle = C.coral;
    g.beginPath();
    g.arc(120, 415, 4 + 1.5 * Math.sin(t * 14), 0, Math.PI * 2);
    g.fill();
    fx.focus(ease((p - 0.55) / 0.45), [1020, 570], [140, 415]);
  } else if (n === 5) {
    const st = 2 * p,
      i = Math.min(monitor.quads.length - 1, Math.floor(st * 24 + 1e-4));
    await seek(movies.reply, st);
    fx.reply(
      p,
      t,
      movies.reply,
      monitor.quads[i].map(([x, y]) => [x * W, y * H]),
      monitorMasks[i],
    );
  } else if (n === 6) fx.thinking(t, p);
  else if (n === 7) fx.levitate(p, t);
  else if (n >= 8 && n <= 11) fx.burst(n, p, t);
  else if (n === 12) fx.ray(p);
  else if (n === 13) fx.hold(p, t);
  else if (n === 14) fx.title(p, local);
  else if (n === 15) {
    if (t < 12.9) {
      rigs.origami(clamp((t - 12.62) / 0.2466667));
      web();
    } else {
      const closed = t < 12.93;
      await seek(movies.sing, t - 11.92);
      const source = closed
        ? fx.brand(imgs.eyeClosed, "breath", 0, marks, false)
        : fx.brand(movies.sing, "sing", t - 11.92, marks);
      crop(source, 0.565, 0.35, 2.3 - 0.85 * ease((t - 12.93) / 0.7));
      if (f === Math.round(12.93 * 30)) {
        g.fillStyle = "#FAF9F5B0";
        g.fillRect(0, 0, W, H);
      }
    }
  } else if (n === 16) {
    rigs.vertigo(p);
    web();
  } else if (n === 17) {
    await seek(movies.breath, p * 1.25);
    cover(g, fx.brand(movies.breath, "breath", p * 1.25, marks));
    const z = 1 + 0.1 * ease(p / 0.7);
    camera(z);
    fx.glyphs(
      p,
      t,
      marks.breath.frames[
        Math.min(
          marks.breath.frames.length - 1,
          Math.floor(p * 1.25 * 24 + 1e-4),
        )
      ].points,
      z,
    );
  } else if (n === 18) {
    camera(1.14 - 0.14 * ease(p));
    fx.windowBurst(p);
  } else if (n === 19) {
    const duration = (shot.end_frame - shot.start_frame - 1) / 30,
      age = local / 30,
      turn = 17.2 - shot.start_frame / 30,
      integral = Math.min(age, turn) + 0.3 * Math.max(0, age - turn),
      total = turn + 0.3 * (duration - turn);
    await seek(movies.burst, 1.9 + (3.1 * integral) / total);
    cover(g, movies.burst);
    camera(1.06 - 0.05 * ease(p));
    fx.windowBurst(p);
    if (t > 16.8 && t < 17.02) {
      text(
        g,
        "Compacting conversation…",
        960,
        780,
        34,
        C.ivory,
        "FDInter",
        500,
        "center",
      );
    }
  } else if (n === 20) {
    await seek(movies.ankle, 1.1 * p);
    cover(g, movies.ankle);
    fx.ankle(p, t);
    const contact = 0.75 / 1.1,
      tracking = 0.06 * ease(p / contact),
      settle = (0.06 / 0.366) * ease((p - contact) / (1 - contact));
    camera(1.5, 0.55, 0.44 + tracking + settle);
    fx.trace.camera_settle_metres = 0.06 * ease((p - contact) / (1 - contact));
    fx.trace.camera_plane_height_metres = 0.366;
  } else if (n === 21) {
    const times = [18.65, 19.0, 19.35, 19.6333333333],
      frames = [16, 36, 56, 58];
    let k = 0;
    while (k < 2 && t > times[k + 1]) k++;
    const a = clamp((t - times[k]) / (times[k + 1] - times[k]));
    await seek(movies.steps, lerp(frames[k], frames[k + 1], a) / 24);
    cover(
      g,
      fx.brand(
        movies.steps,
        "steps",
        lerp(frames[k], frames[k + 1], a) / 24,
        marks,
      ),
    );
    fx.steps(t);
    fx.trace.step_source_frame = lerp(frames[k], frames[k + 1], a);
  } else if (n === 22) {
    await seek(movies.touch, 0.25 * p);
    cover(g, movies.touch);
    fx.handSketch(movies.touch, 0.25 * p, handMask);
    camera(1.6 + 0.05 * p, 0.33, 0.48);
    fx.focus(ease(p), [1540, 600], [805, 260]);
  } else if (n === 23) {
    rigs.orbit("hand", t, p);
    web();
    glow(g, 960, 585, 350, C.gold, 0.16 * Math.sin(p * Math.PI));
    fx.focus(ease((p - 0.82) / 0.18));
    spatial = false;
  } else if (n === 24) {
    camera(1.03, 0.5 + 0.002 * Math.sin(local * 2), 0.5);
  } else if (n === 25) {
    rigs.orbit("leap", t, p);
    web();
    if (t >= 25.15) {
      if (f - Math.round(25.15 * 30) < 2) {
        g.save();
        g.globalAlpha = 0.18;
        g.filter = "blur(8px)";
        g.drawImage(webgl, 25, -10, W, H);
        g.restore();
      }
    }
  } else if (n >= 26 && n <= 28) {
    rigs.flightShot(n, t, p);
    web();
    fx.speedLines(p);
    spatial = true;
  } else if (n === 29 || n === 36) {
    await seek(movies.flight, 0.1 + 0.35 * p);
    crop(
      fx.brand(movies.flight, "flight", 0.1 + 0.35 * p, marks),
      0.577,
      0.24,
      2.3,
    );
  } else if (n === 30) {
    await seek(movies.flight, 0.1 + 0.4 * p);
    crop(movies.flight, 0.26, 0.27, 2.3);
    fx.windTears(
      p,
      marks["xiaoman-flight"].frames[
        Math.min(19, Math.floor((0.1 + 0.4 * p) * 24 + 1e-4))
      ].points,
      movies.flight,
    );
  } else if (n === 31) {
    rigs.climb(p, t);
    web();
    spatial = true;
    fx.speedLines(p);
    if (p > 0.82) {
      g.fillStyle = `rgba(250,249,245,${ease((p - 0.82) / 0.18)})`;
      g.fillRect(0, 0, W, H);
    }
  } else if (n === 32) {
    rigs.floatShot(p, t);
    web();
    spatial = true;
  } else if (n === 33) {
    if (p < 0.4) {
      await seek(movies.touch, 1.5 + p * 0.6);
      crop(movies.touch, 0.5, 0.58, 3);
    } else {
      await seek(movies.breath, 0);
      const source = fx.brand(movies.breath, "breath", 0, marks),
        focus = fx.fitPoint(marks.breath.frames[0].points[1], movies.breath),
        z = 2.4 + 9.6 * ease((p - 0.4) / 0.6);
      crop(source, focus[0] / W, focus[1] / H, z);
      const iris = (14 / 983) * W * z;
      g.save();
      g.beginPath();
      g.ellipse(960, 540, iris, iris * 0.82, -0.3, 0, Math.PI * 2);
      g.clip();
      g.globalAlpha = 0.38 * ease((p - 0.4) / 0.12);
      g.globalCompositeOperation = "screen";
      g.drawImage(
        imgs.sky,
        imgs.sky.width * 0.23,
        imgs.sky.height * 0.35,
        imgs.sky.width * 0.5,
        imgs.sky.height * 0.5,
        960 - iris,
        540 - iris,
        iris * 2,
        iris * 2,
      );
      g.restore();
      const pupil = (12 / 983) * W * z * (1 + 0.65 * ease((p - 0.4) / 0.32));
      g.drawImage(fx.darkSpark, 960 - pupil / 2, 540 - pupil / 2, pupil, pupil);
      if (p > 0.7)
        fx.logo(
          g,
          960,
          540,
          32 + 2200 * ease((p - 0.7) / 0.3),
          0,
          ease((p - 0.7) / 0.1),
        );
    }
    if (p > 0.965) {
      g.fillStyle = C.coral;
      g.fillRect(0, 0, W, H);
    }
  } else if (n === 34) {
    rigs.helix(t, p);
    web();
    spatial = true;
    if (local < 2) {
      g.save();
      g.globalAlpha = 1 - local * 0.5;
      g.fillStyle = C.coral;
      g.fillRect(0, 0, W, H);
      g.restore();
    }
  } else if (n === 35) {
    rigs.paper(p);
    web();
    if (p < 0.12) tornWipe(g, 1 - p / 0.12);
    if (p > 0.88) tornWipe(g, (p - 0.88) / 0.12);
    fx.paperWords();
    spatial = true;
  } else if (n === 37) {
    await seek(movies.joy, 2.5 + 0.35 * p);
    cover(g, movies.joy);
  } else if (n === 38) {
    rigs.cityRush(p);
    web();
  } else if (n === 39) {
    cover(g, imgs.sky);
    glow(g, W * 0.584, H * 0.545, 550, C.gold, 0.4);
    fx.logo(g, W * 0.584, H * 0.545, 36 + 780 * ease(p), 0, 1);
  } else if (n === 40) {
    rigs.helix(t, 0.38 + 0.28 * p, "永远那么灿烂");
    web();
    spatial = true;
  } else if (n === 41) {
    g.fillStyle = C.coral;
    g.fillRect(0, 0, W, H);
  } else if (n === 42) {
    await seek(movies.hug, 0.35 * p);
    cover(g, movies.hug);
    camera(1.08, 0.55, 0.45);
  } else if (n === 43) {
    g.fillStyle = p < 0.4 ? "#FFFFFF" : C.ivory;
    g.fillRect(0, 0, W, H);
  } else if (n === 44) {
    rigs.outro(p, t);
    web();
    if (t >= 40.75 && t < 41.55) {
      fx.halo2D(410, 120, 210, t, 0.25);
      fx.bubble(
        "你好，世界。",
        140,
        145,
        570,
        120,
        ease((t - 40.75) / 0.18) * (1 - ease((t - 41.35) / 0.2)),
      );
    }
    fx.endcard(t);
  }
  // Two-frame punch belongs to each of the eight micro-shots; the hard exposure
  // pulse is not an additional full-frame flash-cut.
  if (n >= 36 && n <= 42) {
    camera(1 + 0.08 * Math.min(1, local / 2));
    if (local === 0) {
      g.fillStyle = "#FAF9F532";
      g.fillRect(0, 0, W, H);
    }
  }
  if ([12, 17, 24, 32].includes(n) && local < 2) {
    g.fillStyle = `rgba(250,249,245,${local === 0 ? 0.88 : 0.36})`;
    g.fillRect(0, 0, W, H);
  }
  const kick = cues.kick_frames.find((k) => f >= k && f < k + 3);
  if (kick !== undefined && n !== 13 && n !== 14 && n !== 43 && n !== 44) {
    const i = f - kick,
      dx = [1.8, -1.1, 0.4][i],
      dy = [0.7, -0.5, 0.2][i];
    camera(1.004, 0.5 + dx / W, 0.5 + dy / H);
  }
  if (!(n === 14 && local < 2)) fx.finish(t);
  if (!spatial && (n !== 14 || local >= 2) && n !== 43 && t < 41.6)
    fx.lyric(t, data.lyrics);
  fx.comments(t);
  if (f >= 1307) {
    g.globalAlpha = clamp((f - 1307) / 3);
    g.fillStyle = C.cream;
    g.fillRect(0, 0, W, H);
    g.globalAlpha = 1;
  }
  const line = data.lyrics.findLast((l) => l.frame <= f);
  window.trace = {
    frame: f,
    time: t,
    shot: shot.id,
    lyric_layer_requested:
      (n === 14 && local < 2) || n === 43 || t >= 41.6 ? null : line?.text,
    lyric_mode: spatial ? "3d" : "screen",
    lyric_index: lyricIndex,
    lyric_alpha: fx.lyricOpacity,
    letterbox_pixels: t < 11.92 ? 138 : 0,
    impact_white: n === 14 && local < 2,
    ...fx.trace,
    ...rigs.trace,
    rig_shot: rigs.trace.shot || null,
    shot: shot.id,
  };
};
