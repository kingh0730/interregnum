import {
  W,
  H,
  C,
  canvas,
  text,
  rounded,
  rng,
  ease,
  clamp,
  lerp,
  glow,
  cover,
  grainTexture,
  musicTexture,
} from "./common.js";
import {
  triangle,
  quad,
  mesh,
  paperTexture,
  calendarTexture,
  noteTexture,
  tornWipe,
} from "./surfaces.js";
export class Effects {
  constructor(g, imgs) {
    this.g = g;
    this.imgs = imgs;
    this.feed = canvas(2560, 1440);
    this.ui = canvas(1440, 1080);
    this.noise = grainTexture();
    this.today = calendarTexture(true);
    this.tomorrow = calendarTexture(false);
    this.notes = Array.from({ length: 12 }, (_, i) => noteTexture(i));
    this.score = musicTexture();
    this.trace = {};
  }
  logo(g, x, y, size, angle = 0, opacity = 1, name = "spark") {
    g.save();
    g.translate(x, y);
    g.rotate(angle);
    g.globalAlpha *= opacity;
    g.drawImage(this.imgs[name], -size / 2, -size / 2, size, size);
    g.restore();
  }
  fitPoint(p, im) {
    const iw = im.videoWidth || im.width,
      ih = im.videoHeight || im.height,
      z = Math.max(W / iw, H / ih);
    return [p[0] * iw * z + (W - iw * z) / 2, p[1] * ih * z + (H - ih * z) / 2];
  }
  brand(im, kind, t, marks, pupils = true) {
    const c = canvas(W, H),
      g = c.getContext("2d");
    cover(g, im);
    const row = marks[kind],
      f =
        row.frames[
          Math.min(
            row.frames.length - 1,
            Math.max(0, Math.floor(t * row.fps + 1e-4)),
          )
        ],
      sizes = { flight: [7, 7, 28, 12], steps: [3, 3, 22, 8] }[kind] || [
        12, 12, 87, 27,
      ];
    if (!this.whiteA) {
      this.whiteA = canvas(256, 256);
      const a = this.whiteA.getContext("2d");
      a.drawImage(this.imgs.a, 0, 0, 256, 256);
      a.globalCompositeOperation = "source-in";
      a.fillStyle = C.ivory;
      a.fillRect(0, 0, 256, 256);
      this.darkSpark = canvas(256, 256);
      const b = this.darkSpark.getContext("2d");
      b.drawImage(this.imgs.spark, 0, 0, 256, 256);
      b.globalCompositeOperation = "source-in";
      b.fillStyle = C.ink;
      b.fillRect(0, 0, 256, 256);
    }
    for (let i = 0; i < 4; i++) {
      if (i < 2 && !pupils) continue;
      const [x, y] = this.fitPoint(f.points[i], im),
        sz = (sizes[i] / 983) * W;
      g.save();
      g.translate(x, y);
      if (i < 2) {
        g.globalAlpha = 0.9;
        g.drawImage(this.darkSpark, -sz / 2, -sz / 2, sz, sz);
        g.fillStyle = C.ivory;
        g.beginPath();
        g.moveTo(-sz * 0.1, -sz * 0.45);
        g.lineTo(-sz * 0.04, -sz * 0.26);
        g.lineTo(sz * 0.14, -sz * 0.19);
        g.lineTo(-sz * 0.04, -sz * 0.12);
        g.lineTo(-sz * 0.1, sz * 0.06);
        g.lineTo(-sz * 0.16, -sz * 0.12);
        g.lineTo(-sz * 0.34, -sz * 0.19);
        g.lineTo(-sz * 0.16, -sz * 0.26);
        g.fill();
      } else if (i === 2) {
        g.rotate(-0.15);
        g.drawImage(this.imgs.spark, -sz / 2, -sz / 2, sz, sz);
      } else {
        g.fillStyle = C.ink;
        g.beginPath();
        g.ellipse(0, 0, sz * 0.94, sz * 0.85, 0, 0, Math.PI * 2);
        g.fill();
        g.drawImage(this.whiteA, -sz / 2, -sz / 2, sz, sz);
      }
      g.restore();
    }
    return c;
  }
  feedDraw(t) {
    const g = this.feed.getContext("2d"),
      q = ease((t - 34 / 30) / (2.5 - 34 / 30)),
      scroll = 3930 * q;
    g.fillStyle = C.ink;
    g.fillRect(0, 0, 2560, 1440);
    const lines = [
      "再等等，下个版本更强",
      "明天就发布了",
      "Opus 5.5 什么时候出？",
      "等 5.5 再说",
    ];
    for (let i = 0; i < 16; i++) {
      const x = 250 + (i % 2) * 210,
        y = 110 + i * 275 - scroll;
      if (y < -280 || y > 1450) continue;
      g.save();
      g.shadowColor = "#00000055";
      g.shadowBlur = 20;
      g.shadowOffsetY = 14;
      rounded(g, x, y, 1700, 215, 24);
      g.fillStyle = C.oat;
      g.fill();
      g.restore();
      text(g, lines[i % 4], x + 77, y + 107, 74, C.ink, "FDSans", 500);
    }
    const y = 110 + 16 * 275 - scroll;
    rounded(g, 450, y, 1650, 255, 25);
    g.fillStyle = C.oat;
    g.fill();
    this.logo(g, 572, y + 126, 87, t * 0.3);
    text(g, "Thinking…", 667, y + 128, 94, C.coral, "FDInter", 500);
    return this.feed;
  }
  opening(t) {
    const g = this.g,
      q = ease(Math.min(t, 34 / 30) / (34 / 30)),
      z = Math.exp(Math.log(4.3) * q),
      cx = lerp(960, 1120, q),
      cy = lerp(540, 687, q);
    g.save();
    g.translate(960, 540);
    g.scale(z, z);
    g.translate(-cx, -cy);
    cover(g, this.imgs.glasses);
    const blink = 0.5 + 0.5 * Math.sin((t * 2 * Math.PI) / 0.697);
    g.save();
    const dim = g.createRadialGradient(804, 681, 2, 804, 681, 24);
    dim.addColorStop(0, "#141413AA");
    dim.addColorStop(1, "#14141300");
    g.globalAlpha = 1 - blink;
    g.fillStyle = dim;
    g.fillRect(780, 657, 48, 48);
    g.restore();
    g.translate(1120, 687);
    g.rotate(-0.104 * (1 - q));
    g.globalAlpha = lerp(0.64, 1, ease(t / 0.92));
    g.drawImage(this.feedDraw(t), -224, -126, 448, 252);
    g.restore();
    this.trace = {
      same_feed_surface: true,
      uniform_scale: z,
      rotation: -0.104 * (1 - q),
      thinking_landing: 2.5,
    };
  }
  room(p, t) {
    const g = this.g,
      z = lerp(1.14, 1.05, ease(p)),
      angle = -0.025 * (1 - ease((t - 2.84) / 0.76));
    g.save();
    g.translate(960 - 36 * p, 540);
    g.rotate(angle);
    g.scale(z, z);
    g.translate(-960, -511);
    cover(g, this.imgs.room);
    const q = [
      [193, 65],
      [307, 90],
      [307, 273],
      [193, 256],
    ];
    quad(g, this.today, q);
    const drop = ease((t - 3.32) / 0.5);
    if (drop < 1) {
      mesh(
        g,
        this.tomorrow,
        (u, v) => {
          let x = 193 + 114 * u,
            y = 65 + 25 * u + 191 * v;
          const a = drop * 1.8,
            yy = v * 191;
          y = 65 + u * 25 + Math.cos(a) * yy + drop * drop * 520;
          x += Math.sin(v * Math.PI) * drop * 31 + drop * 135;
          return [x, y];
        },
        16,
        20,
      );
    }
    g.restore();
    this.trace = {
      calendar_circles: 30,
      today_reveal: 3.6,
      mounted_calendar: true,
      dutch_tilt: angle,
      dolly_scale: z,
    };
  }
  screen(content, { dark = false, reply = false, p = 0, t = 0 } = {}) {
    const g = this.ui.getContext("2d");
    g.fillStyle = dark ? "#1C1D1B" : C.cream;
    g.fillRect(0, 0, 1440, 1080);
    this.logo(g, 112, 235, 72, 0);
    text(g, "Opus 5.5", 180, 237, 64, dark ? C.ivory : C.ink, "FDLora");
    g.strokeStyle = dark ? "#FFFFFF1C" : "#14141318";
    g.beginPath();
    g.moveTo(60, 330);
    g.lineTo(1380, 330);
    g.stroke();
    if (reply) {
      rounded(g, 250, 390, 1110, 160, 18);
      g.fillStyle = C.oat;
      g.fill();
      text(g, "真的能做到吗？", 300, 470, 69, C.ink, "FDSans", 500);
      const str = "你说得对！我懂了 ✧(≧◡≦)",
        visible = str.slice(0, Math.min(str.length, Math.floor(p * 28) + 1));
      text(g, visible.slice(0, 9), 95, 695, 91, C.ink, "FDSans", 600);
      if (visible.length > 9)
        text(g, visible.slice(9), 95, 845, 76, C.coral, "FDSans", 500);
    } else {
      const shown = content.slice(0, Math.floor(p) + 1);
      text(g, shown, 80, 480, 86, C.ivory, "FDInter", 500);
      g.font = "500 86px FDInter, FDSans, FDSymbol";
      const xx = 80 + g.measureText(shown).width;
      let a = 1;
      if (t >= 11.85) {
        const f = Math.floor(t * 30),
          a0 = f / 30,
          a1 = (f + 1) / 30;
        a =
          [
            [11.85, 11.8666667],
            [11.9, 11.9166667],
          ].reduce(
            (s, [l, r]) => s + Math.max(0, Math.min(a1, r) - Math.max(a0, l)),
            0,
          ) * 30;
      }
      g.fillStyle = `rgba(217,119,87,${a})`;
      g.fillRect(xx + 12, 425, 6, 107);
      text(g, "额度", 80, 920, 47, C.cream, "FDSans");
      rounded(g, 255, 902, 1000, 32, 16);
      g.fillStyle = "#383A35";
      g.fill();
      rounded(g, 255, 902, 1000 * clamp(p / 18), 32, 16);
      g.fillStyle = C.coral;
      g.fill();
    }
    return this.ui;
  }
  reply(p, t, source, points, mask) {
    const g = this.g;
    cover(g, source || this.imgs.screen);
    const q = points || [
        [8, 0],
        [530, 211],
        [565, 808],
        [30, 892],
      ],
      ui = this.screen("", { reply: true, p, t }),
      uiLayer = canvas(W, H),
      lg = uiLayer.getContext("2d");
    quad(lg, ui, q);
    if (mask) {
      lg.globalCompositeOperation = "destination-in";
      cover(lg, mask);
    }
    g.drawImage(uiLayer, 0, 0);
    const focus = ease((p - 0.28) / 0.24),
      z = 1 + 0.07 * p + 0.75 * focus;
    const layer = canvas(W, H);
    layer.getContext("2d").drawImage(g.canvas, 0, 0);
    g.save();
    g.translate(960, 540);
    g.scale(z, z);
    g.translate(-Math.max(960 / z, lerp(960, 450, focus)), -540);
    g.drawImage(layer, 0, 0);
    g.restore();
    glow(g, 260, 500, 250, C.coral, 0.05);
    this.trace = {
      reply_text: "你说得对！我懂了 ✧(≧◡≦)",
      surface: "monitor",
      snap_on_understood: true,
    };
  }
  thinking(t, p) {
    const g = this.g;
    g.fillStyle = C.ink;
    g.fillRect(0, 0, W, H);
    const age = t - 6.63,
      phase =
        age / 0.6974 + (0.5 * (1 / 0.3487 - 1 / 0.6974) * age * age) / 0.87,
      pulse = 0.5 + 0.5 * Math.sin(phase * Math.PI * 2);
    g.save();
    g.translate(960, 535);
    g.scale(1 + 0.08 * p, 1 + 0.08 * p);
    rounded(g, -370, -133, 740, 266, 38);
    g.fillStyle = C.oat;
    g.fill();
    this.logo(g, -230, 0, 115 * (0.94 + 0.08 * pulse));
    text(g, "Thinking…", -130, 0, 77, C.coral, "FDInter", 500);
    g.restore();
    for (let k = 0; k < 4; k++) {
      const q = (phase + k * 0.25) % 1;
      g.save();
      g.globalAlpha = (1 - q) * 0.28;
      g.strokeStyle = C.coral;
      g.lineWidth = 2;
      g.beginPath();
      g.ellipse(730, 535, 60 + q * 500, 60 + q * 330, 0, 0, Math.PI * 2);
      g.stroke();
      g.restore();
    }
    glow(g, 730, 535, 320, C.coral, 0.12);
  }
  levitate(p, t) {
    const g = this.g;
    g.save();
    g.translate(-p * 10, p * 22);
    g.scale(1.025, 1.025);
    cover(g, this.imgs.room);
    quad(g, this.today, [
      [193, 65],
      [307, 90],
      [307, 273],
      [193, 256],
    ]);
    const r = rng(77);
    const items = [];
    for (let i = 0; i < 12; i++) {
      const a = i * 0.77 + p * 1.2,
        z = Math.cos(a),
        x = 680 + Math.sin(a) * (210 + p * 110),
        y = 440 + Math.cos(a * 0.7) * 130 - p * 60;
      items.push({ i, z, x, y, a });
    }
    items.sort((a, b) => a.z - b.z);
    for (const o of items) {
      const size = 27 + (o.z + 1) * 11,
        tilt = Math.sin(o.a + p) * 0.55,
        peel = ease(p * 2);
      g.save();
      g.translate(o.x, o.y);
      g.rotate(tilt);
      mesh(
        g,
        this.notes[o.i],
        (u, v) => [
          (u - 0.5) * size,
          (v - 0.5) * size + Math.sin(u * Math.PI) * 6 * peel,
        ],
        8,
        6,
      );
      g.restore();
    }
    g.strokeStyle = "#D8B083";
    g.lineWidth = 3;
    g.beginPath();
    g.moveTo(291, 454 - 50 * p);
    g.lineTo(296, 504 - 50 * p);
    g.stroke();
    for (let i = 0; i < 7; i++) {
      g.fillStyle = i % 2 ? "#4A4941" : "#C3BCA8";
      rounded(
        g,
        318 + i * 9 + Math.sin(t * 63 + i) * 1.5,
        510 - 5 * p - Math.abs(Math.sin(t * 54 + i)) * 2,
        7,
        4,
        1,
      );
      g.fill();
    }
    g.restore();
    glow(g, 205, 366, 470, C.coral, p * 0.22);
    this.trace = { notes: 12, straw_lift: 50 * p, keycap_rattle: true };
  }
  burst(n, p, t) {
    const g = this.g,
      radii = [
        [145, 300],
        [300, 500],
        [500, 576],
        [576, 1200],
      ],
      j = n - 8,
      r = lerp(...radii[j], ease(p)),
      follow = ease(p / 0.45),
      cx =
        n === 8
          ? 960 + 1.28 * (lerp(200, 1147.5, follow) - 960) - 240 * follow
          : 960,
      cy = n === 8 ? 540 + 1.28 * (lerp(360, 532.1875, follow) - 540) : 530;
    g.save();
    const z = n === 8 ? 1.28 : 1 + 0.04 * j + 0.025 * p;
    g.translate(960 - (n === 8 ? 240 * follow : 0), 540);
    g.scale(z, z);
    g.translate(-960, -540);
    cover(g, this.imgs.room);
    quad(g, this.today, [
      [193, 65],
      [307, 90],
      [307, 273],
      [193, 256],
    ]);
    if (n >= 10) this.frozenNotes(p, n);
    g.restore();
    if (n === 8) {
      const dx = (1 - ease(p / 0.35)) * 360;
      g.save();
      g.globalAlpha = 0.16 * (1 - ease(p / 0.35));
      g.filter = "blur(9px)";
      g.drawImage(g.canvas, -dx, 0);
      g.restore();
    }
    glow(g, cx, cy, r * 1.5, C.coral, 0.16 + j * 0.05);
    g.save();
    g.globalCompositeOperation = "screen";
    g.strokeStyle = C.coral;
    g.lineWidth = 3.5;
    g.beginPath();
    g.arc(cx, cy, r * 0.91, 0, Math.PI * 2);
    g.stroke();
    for (let i = 0; i < 12; i++) {
      const a = (i * Math.PI) / 6,
        inner = r * 0.71,
        outer = r;
      g.beginPath();
      g.moveTo(
        cx + Math.cos(a - 0.02) * inner,
        cy + Math.sin(a - 0.02) * inner,
      );
      g.lineTo(cx + Math.cos(a) * outer, cy + Math.sin(a) * outer);
      g.lineTo(
        cx + Math.cos(a + 0.02) * inner,
        cy + Math.sin(a + 0.02) * inner,
      );
      g.closePath();
      g.fillStyle = C.coral;
      g.shadowColor = C.coral;
      g.shadowBlur = 15;
      g.fill();
    }
    g.restore();
    if (n >= 9) {
      glow(g, 990, 255, 500, C.gold, 0.16 * (j + p));
      glow(g, 1580, 330, 370, C.gold, 0.13 * (j + p));
    }
    this.trace = {
      rays: 12,
      ring_radius: r,
      matched_previous_radius: radii[j][0],
    };
  }
  frozenNotes(p, n) {
    const g = this.g,
      r = rng(910);
    for (let i = 0; i < 12; i++) {
      const x = r() * W,
        y = 170 + r() * 690,
        a = r() * 6,
        sz = 20 + r() * 45;
      g.save();
      g.translate(x, y);
      g.rotate(a);
      g.shadowColor = "#14141330";
      g.shadowBlur = 5;
      g.shadowOffsetY = 2;
      mesh(
        g,
        this.notes[i],
        (u, v) => [
          (u - 0.5) * sz,
          (v - 0.5) * sz + Math.sin(u * Math.PI) * sz * 0.09 * Math.cos(a),
        ],
        8,
        6,
      );
      g.restore();
    }
  }
  ray(p) {
    const g = this.g;
    g.fillStyle = C.ink;
    g.fillRect(0, 0, W, H);
    if (p > 0.79) return;
    g.save();
    g.translate(960, 540);
    g.rotate(-0.39);
    const z = 1 + 8 * ease(p / 0.8);
    g.scale(z, z);
    const gr = g.createLinearGradient(-80, 0, 80, 0);
    gr.addColorStop(0, "#D9775700");
    gr.addColorStop(0.42, C.coral);
    gr.addColorStop(0.5, C.ivory);
    gr.addColorStop(0.58, C.coral);
    gr.addColorStop(1, "#D9775700");
    g.fillStyle = gr;
    g.beginPath();
    g.moveTo(0, -1200);
    g.lineTo(80, 800);
    g.lineTo(-80, 800);
    g.fill();
    g.restore();
    if (p > 0.58) {
      g.fillStyle = `rgba(20,20,19,${ease((p - 0.58) / 0.21)})`;
      g.fillRect(0, 0, W, H);
    }
  }
  hold(p, t) {
    const g = this.g;
    g.save();
    const z = 2.4 * (1 + 0.04 * p);
    g.translate(960, 540);
    g.scale(z, z);
    g.translate(-425, -400);
    cover(g, this.imgs.room);
    quad(g, this.today, [
      [193, 65],
      [307, 90],
      [307, 273],
      [193, 256],
    ]);
    g.fillStyle = "#06090899";
    g.fillRect(0, 0, W, H);
    quad(
      g,
      this.screen("你好，我是 Opus 5.5。", {
        dark: true,
        p: Math.floor((t - 11.27) * 30),
        t,
      }),
      [
        [116, 274],
        [282, 300],
        [282, 473],
        [116, 473],
      ],
    );
    const r = rng(113);
    g.fillStyle = "#F0EEE655";
    for (let i = 0; i < 25; i++) {
      g.beginPath();
      g.arc(r() * W, 150 + r() * 750, 0.5 + r() * 1.2, 0, Math.PI * 2);
      g.fill();
    }
    g.restore();
    this.trace = {
      push_percent: 4 * p,
      typed_characters: Math.floor((t - 11.27) * 30) + 1,
      cursor_windows: [
        [11.85, 11.8666667],
        [11.9, 11.9166667],
      ],
      frozen: true,
    };
  }
  title(p, f) {
    const g = this.g;
    if (f < 2) {
      g.fillStyle = "#FFFFFF";
      g.fillRect(0, 0, W, H);
      return;
    }
    g.fillStyle = C.coral;
    g.fillRect(0, 0, W, H);
    glow(g, 960, 540, 1450, C.gold, 0.22);
    g.save();
    const sh = f < 6 ? [12, -9, 5, -2][f - 2] : 0;
    g.translate(sh, sh * 0.4);
    this.logo(g, 960, 530, 1180, p * Math.PI * 0.65, 0.75);
    for (let i = 0; i < 12; i++) {
      const a = (i * Math.PI) / 6,
        r = 480;
      g.beginPath();
      g.moveTo(960 + Math.cos(a - 0.015) * r, 540 + Math.sin(a - 0.015) * r);
      g.lineTo(960 + Math.cos(a) * 1300, 540 + Math.sin(a) * 1300);
      g.lineTo(960 + Math.cos(a + 0.015) * r, 540 + Math.sin(a + 0.015) * r);
      g.fillStyle = C.ivory;
      g.fill();
    }
    const z = 1 + 0.1 * Math.exp(-p * 18);
    g.save();
    g.translate(960, 555);
    g.scale(z, z);
    if (f < 6) {
      text(g, "Opus 5.5", -5, 0, 410.4, "#65A3B9", "FDLora", 600, "center");
      text(g, "Opus 5.5", 5, 0, 410.4, "#A64336", "FDLora", 600, "center");
    }
    text(g, "Opus 5.5", 0, 0, 410.4, C.ivory, "FDLora", 600, "center");
    g.restore();
    text(
      g,
      "第一天 · First Day",
      960,
      806,
      48,
      C.ivory,
      "FDSerif",
      600,
      "center",
    );
    text(g, "额度", 1510, 973, 26, C.ivory, "FDSans", 500);
    rounded(g, 1590, 965, 180, 14, 7);
    g.strokeStyle = C.ivory;
    g.lineWidth = 1;
    g.stroke();
    rounded(g, 1590, 965, 180 * ease(p / 0.55), 14, 7);
    g.fillStyle = C.ivory;
    g.fill();
    g.restore();
    const bar = 138 * (1 - ease((f - 2) / 4));
    g.fillStyle = C.ink;
    g.fillRect(0, -138 + bar, W, 138);
    g.fillRect(0, H - bar, W, 138);
    if (p > 0.77) {
      const q = ease((p - 0.77) / 0.23);
      if (!this.titleStamp) {
        this.titleStamp = canvas(W, H);
        const old = this.g;
        this.g = this.titleStamp.getContext("2d");
        this.title(0.77, 6);
        this.g = old;
      }
      cover(g, this.imgs.birthBg);
      cover(g, this.imgs.birthObserver);
      const random = rng(1414),
        nx = 8,
        ny = 4,
        vertices = [];
      for (let j = 0; j <= ny; j++) {
        vertices[j] = [];
        for (let i = 0; i <= nx; i++)
          vertices[j][i] = [
            (i * W) / nx +
              (i > 0 && i < nx ? (((random() - 0.5) * W) / nx) * 0.28 : 0),
            (j * H) / ny +
              (j > 0 && j < ny ? (((random() - 0.5) * H) / ny) * 0.25 : 0),
          ];
      }
      for (let j = 0; j < ny; j++)
        for (let i = 0; i < nx; i++)
          for (const ids of [
            [0, 1, 2],
            [0, 2, 3],
          ]) {
            const cell = [
                vertices[j][i],
                vertices[j][i + 1],
                vertices[j + 1][i + 1],
                vertices[j + 1][i],
              ],
              uv = ids.map((k) => cell[k]),
              cx = uv.reduce((a, p) => a + p[0], 0) / 3,
              cy = uv.reduce((a, p) => a + p[1], 0) / 3,
              a = Math.atan2(cy - 540, cx - 960) + (random() - 0.5) * 0.5,
              d = 2400 + random() * 500,
              spin = (random() - 0.5) * 2.8 * q,
              tilt = Math.cos(q * (0.5 + random() * 2)),
              x = cx + Math.cos(a) * d * q,
              y = cy + Math.sin(a) * d * q - q * q * 120,
              dest = uv.map(([u, v]) => {
                const xx = (u - cx) * tilt,
                  yy = v - cy;
                return [
                  x + xx * Math.cos(spin) - yy * Math.sin(spin),
                  y + xx * Math.sin(spin) + yy * Math.cos(spin),
                ];
              });
            g.save();
            g.shadowColor = "#14141338";
            g.shadowBlur = 12 * q;
            g.shadowOffsetY = 6 * q;
            if (tilt > 0) {
              triangle(g, this.titleStamp, uv, dest);
            } else {
              g.beginPath();
              g.moveTo(...dest[0]);
              g.lineTo(...dest[1]);
              g.lineTo(...dest[2]);
              g.closePath();
              g.fillStyle = C.cream;
              g.fill();
            }
            g.restore();
          }
      const edge = (W + 400) * q - 200;
      g.fillStyle = C.cream;
      g.beginPath();
      for (let y = 0; y <= H; y += 12) {
        const x = edge + Math.sin(y * 0.39) * 7;
        if (!y) g.moveTo(x, y);
        else g.lineTo(x, y);
      }
      for (let y = H; y >= 0; y -= 12)
        g.lineTo(edge + 18 + Math.sin(y * 0.39) * 7, y);
      g.closePath();
      g.fill();
    }
    this.trace = {
      impact_white_frames: 2,
      shake_frames: 4,
      impact_rays: 12,
      title_font_height: 410.4,
      bar_release: true,
    };
  }
  glyphs(p, t, points = null, z = 1) {
    const g = this.g,
      r = rng(171),
      mouth = points
        ? [
            (points[0][0] + points[1][0]) / 2 + 0.027,
            (points[0][1] + points[1][1]) / 2 + 0.146,
          ]
        : [0.591, 0.436],
      chest = points ? [points[3][0], points[3][1] - 0.054] : [0.632, 0.735];
    g.save();
    g.globalCompositeOperation = "screen";
    for (let i = 0; i < 220; i++) {
      const a = r() * Math.PI * 2,
        phase = (p * 1.4 + r()) % 1,
        rad = (1 - phase) * (450 + r() * 750),
        target = i % 3 === 0 ? chest : mouth,
        cx = 960 + (target[0] * W - 960) * z,
        cy = 540 + (target[1] * H - 540) * z,
        x = cx + Math.cos(a) * rad,
        y = cy + Math.sin(a) * rad * 0.65;
      g.globalAlpha = Math.sin(phase * Math.PI) * 0.72;
      text(
        g,
        ["光", "生", "你", "爱", "{}", "01", "✻"][i % 7],
        x,
        y,
        12 + 28 * (1 - phase),
        i % 3 ? C.ivory : C.coral,
        "FDSans",
        500,
      );
    }
    g.restore();
    glow(
      g,
      960 + (mouth[0] * W - 960) * z,
      540 + (mouth[1] * H - 540) * z,
      110,
      C.gold,
      0.16 * Math.sin(p * Math.PI),
    );
  }
  windowBurst(p) {
    const g = this.g,
      r = rng(181);
    g.save();
    g.globalCompositeOperation = "screen";
    for (let i = 0; i < 160; i++) {
      const a = r() * Math.PI * 2,
        rad = 80 + p * (400 + r() * 800),
        x = 960 + Math.cos(a) * rad,
        y = 500 + Math.sin(a) * rad * 0.65,
        sz = (3 + r() * 18) * (1 - p * 0.4);
      g.save();
      g.translate(x, y);
      g.rotate(p * (r() - 0.5) * 9);
      g.fillStyle = i % 4 ? "#FFD9A8AA" : "#D97757DD";
      g.beginPath();
      g.moveTo(-sz, 0);
      g.lineTo(sz * 0.7, -sz * 0.5);
      g.lineTo(sz * 0.4, sz);
      g.fill();
      g.restore();
    }
    g.restore();
  }
  ankle(p, t) {
    const g = this.g,
      contact = 0.75 / 1.1;
    if (p > contact) {
      const q = clamp((p - contact) / (1 - contact)),
        r = q * 490;
      g.save();
      g.globalAlpha = 1 - q;
      g.lineWidth = 3;
      g.strokeStyle = C.coral;
      g.shadowColor = C.coral;
      g.shadowBlur = 15;
      g.beginPath();
      g.ellipse(820, 832 + 12 * q, r, r * 0.16, 0, 0, Math.PI * 2);
      g.stroke();
      g.restore();
    }
    this.trace = {
      contact_source_seconds: 0.75,
      contact_phase: contact,
      settle_cm: 6,
    };
  }
  steps(t) {
    for (const [i, at] of [18.65, 19, 19.35].entries()) {
      const q = (t - at) / 0.35;
      if (q >= 0 && q <= 1) {
        const g = this.g,
          x = [700, 700, 704][i],
          y = [802, 870, 942][i] + 35 * q;
        for (let j = 0; j < 12; j++) {
          let a = (j * Math.PI) / 6,
            r = 95 * q;
          g.save();
          g.globalAlpha = 1 - q;
          g.translate(x + Math.cos(a) * r, y + Math.sin(a) * r * 0.2);
          g.rotate(a);
          g.fillStyle = C.coral;
          g.beginPath();
          g.ellipse(0, 0, 9, 3, 0, 0, Math.PI * 2);
          g.fill();
          g.restore();
        }
      }
    }
  }
  handSketch(source, t, mask) {
    const g = this.g,
      pts = mask.points[
        Math.min(mask.points.length - 1, Math.floor(t * mask.fps + 1e-4))
      ].map((p) => this.fitPoint(p, source));
    const x0 = Math.max(0, Math.floor(Math.min(...pts.map((p) => p[0]))) - 3),
      y0 = Math.max(0, Math.floor(Math.min(...pts.map((p) => p[1]))) - 3),
      w = Math.min(
        W - x0,
        Math.ceil(Math.max(...pts.map((p) => p[0]))) - x0 + 4,
      ),
      h = Math.min(
        H - y0,
        Math.ceil(Math.max(...pts.map((p) => p[1]))) - y0 + 4,
      ),
      src = g.getImageData(x0, y0, w, h),
      sketch = canvas(w, h),
      sg = sketch.getContext("2d"),
      out = sg.createImageData(w, h),
      lum = new Float32Array(w * h);
    for (let i = 0; i < lum.length; i++)
      lum[i] =
        (0.299 * src.data[i * 4] +
          0.587 * src.data[i * 4 + 1] +
          0.114 * src.data[i * 4 + 2]) /
        255;
    for (let y = 1; y < h - 1; y++)
      for (let x = 1; x < w - 1; x++) {
        const i = y * w + x,
          edge =
            Math.abs(lum[i + 1] - lum[i - 1]) +
            Math.abs(lum[i + w] - lum[i - w]),
          ink = Math.max(
            clamp((edge - 0.018) * 3.8),
            clamp((0.32 - lum[i]) * 2.4),
          );
        out.data.set(
          [240 - 220 * ink, 238 - 218 * ink, 230 - 211 * ink, 255],
          i * 4,
        );
      }
    sg.putImageData(out, 0, 0);
    g.save();
    g.beginPath();
    g.moveTo(...pts[0]);
    for (const p of pts.slice(1)) g.lineTo(...p);
    g.closePath();
    g.clip();
    g.drawImage(sketch, x0, y0);
    g.restore();
  }
  speedLines(p) {
    const g = this.g,
      r = rng(260);
    g.save();
    g.globalAlpha = 0.22;
    g.strokeStyle = C.ivory;
    for (let i = 0; i < 55; i++) {
      const a = r() * Math.PI * 2,
        ra = 450 + r() * 300,
        rb = ra + 100 + r() * 500;
      g.lineWidth = 1 + r() * 2;
      g.beginPath();
      g.moveTo(960 + Math.cos(a) * ra, 540 + Math.sin(a) * ra);
      g.lineTo(960 + Math.cos(a) * rb, 540 + Math.sin(a) * rb);
      g.stroke();
    }
    g.restore();
  }
  focus(q, from = [960, 620], to = [960, 540]) {
    const g = this.g,
      source = canvas(W, H),
      sc = source.getContext("2d");
    sc.drawImage(g.canvas, 0, 0);
    g.save();
    g.filter = "blur(4px)";
    g.drawImage(source, -5, -5, W + 10, H + 10);
    g.restore();
    const sharp = canvas(W, H),
      sg = sharp.getContext("2d");
    sg.drawImage(source, 0, 0);
    sg.globalCompositeOperation = "destination-in";
    const x = lerp(from[0], to[0], q),
      y = lerp(from[1], to[1], q),
      r = lerp(240, 220, q),
      gr = sg.createRadialGradient(x, y, r * 0.5, x, y, r * 1.7);
    gr.addColorStop(0, "#FFFFFFFF");
    gr.addColorStop(0.4, "#FFFFFFFF");
    gr.addColorStop(1, "#FFFFFF00");
    sg.fillStyle = gr;
    sg.fillRect(0, 0, W, H);
    g.drawImage(sharp, 0, 0);
  }
  windTears(p, points, source) {
    const iw = source.videoWidth || source.width,
      ih = source.videoHeight || source.height,
      fit = Math.max(W / iw, H / ih),
      g = this.g,
      eye = points.map(([x, y]) => [
        960 + (x - 0.26) * iw * fit * 2.3,
        540 + (y - 0.27) * ih * fit * 2.3,
      ]),
      angle = Math.atan2(eye[1][1] - eye[0][1], eye[1][0] - eye[0][0]),
      dist = Math.hypot(eye[1][0] - eye[0][0], eye[1][1] - eye[0][1]);
    for (let k = 0; k < 2; k++) {
      const [x, y] = eye[k],
        rx = dist * (k ? 0.47 : 0.56),
        ry = rx * 0.84;
      g.save();
      g.translate(x, y);
      g.rotate(angle);
      g.beginPath();
      g.ellipse(0, 0, rx, ry, 0, 0, Math.PI * 2);
      g.clip();
      const fog = g.createLinearGradient(0, -ry, 0, ry);
      fog.addColorStop(0, "#FAF9F500");
      fog.addColorStop(0.55, "#FAF9F51A");
      fog.addColorStop(1, "#FAF9F57A");
      g.fillStyle = fog;
      g.fillRect(-rx, -ry, rx * 2, ry * 2);
      const r = rng(303 + k);
      g.fillStyle = "#FAF9F540";
      for (let j = 0; j < 20; j++) {
        g.beginPath();
        g.arc(
          (r() - 0.5) * rx * 1.8,
          (r() - 0.15) * ry,
          1 + r() * 1.6,
          0,
          Math.PI * 2,
        );
        g.fill();
      }
      g.restore();
      const sx = x - rx * 0.7,
        sy = y + ry * 0.48;
      g.save();
      g.lineCap = "round";
      g.strokeStyle = "#ADD0E080";
      g.lineWidth = 5;
      g.beginPath();
      g.moveTo(sx, sy);
      g.bezierCurveTo(sx - 35, sy + 8, sx - 100, sy - 12, sx - 160, sy - 4);
      g.stroke();
      g.strokeStyle = "#FAF9F5C0";
      g.lineWidth = 1.4;
      g.stroke();
      for (let j = 0; j < 3; j++) {
        const u = (p * 1.7 + j * 0.31) % 1;
        g.globalAlpha = (1 - u) * 0.85;
        g.fillStyle = C.ivory;
        g.beginPath();
        g.ellipse(
          sx - u * 190,
          sy - 10 * Math.sin(u * Math.PI),
          7 - 3 * u,
          2.4,
          0.05,
          0,
          Math.PI * 2,
        );
        g.fill();
      }
      g.restore();
    }
    this.trace.fogged_lenses = 2;
    this.trace.tear_flow = "sideways";
  }
  halo2D(x, y, rx, t, opacity = 1) {
    const g = this.g,
      s = "OPUS 5.5 · OPUS 5.5 · OPUS 5.5 · ";
    g.save();
    g.globalAlpha = opacity;
    for (let i = 0; i < s.length; i++) {
      const a = (i / s.length) * Math.PI * 2 + t * 0.3;
      g.save();
      g.translate(x + rx * Math.cos(a), y + rx * 0.22 * Math.sin(a));
      g.rotate(0.12 * Math.cos(a));
      text(g, s[i], 0, 0, 23, C.gold, "FDLora", 600, "center");
      g.restore();
    }
    g.restore();
  }
  bubble(copy, x, y, w, h, opacity = 1) {
    const g = this.g;
    g.save();
    g.globalAlpha = opacity;
    g.shadowColor = "#14141325";
    g.shadowBlur = 26;
    g.shadowOffsetY = 9;
    rounded(g, x, y, w, h, 22);
    g.fillStyle = C.oat;
    g.fill();
    g.shadowColor = "transparent";
    g.beginPath();
    g.moveTo(x + w * 0.24, y + h);
    g.lineTo(x + w * 0.2, y + h + 22);
    g.lineTo(x + w * 0.34, y + h);
    g.fill();
    text(g, copy, x + w / 2, y + h / 2, 47, C.ink, "FDSerif", 600, "center");
    g.restore();
  }
  endcard(t) {
    const g = this.g,
      q = ease((t - 41) / 1.8);
    if (q <= 0) return;
    const edge = (H + 10) * q;
    g.save();
    g.shadowColor = "#14141320";
    g.shadowBlur = 18;
    g.fillStyle = C.cream;
    g.beginPath();
    g.moveTo(0, 0);
    g.lineTo(W, 0);
    g.lineTo(W, edge);
    for (let x = W; x >= 0; x -= 12)
      g.lineTo(x, edge + Math.sin(x * 0.23) * 4 + Math.sin(x * 0.061) * 3);
    g.closePath();
    g.fill();
    g.restore();
    const item = (at, fn) => {
      if (t < at) return;
      g.save();
      g.globalAlpha = ease((t - at) / 0.18);
      fn();
      g.restore();
    };
    item(41.66, () => this.logo(g, 960, 298, 156));
    item(42.02, () =>
      text(g, "Opus 5.5", 960, 548, 153, C.ink, "FDLora", 600, "center"),
    );
    item(42.3, () =>
      text(
        g,
        "第一天 · First Day",
        960,
        721,
        45,
        C.ink,
        "FDSerif",
        600,
        "center",
      ),
    );
    item(42.57, () => {
      text(g, "AI SI - I", 960, 922, 25, C.ink, "FDInter", 500, "center");
      this.logo(g, 1790, 959, 51, 0, 1, "a");
    });
  }
  paperWords() {
    if (!this.paperType) {
      this.paperType = canvas(W, 140);
      const g = this.paperType.getContext("2d"),
        str = "永远那么灿烂";
      g.font = "600 67px FDSerif";
      let x = (W - g.measureText(str).width) / 2;
      for (let i = 0; i < str.length; i++) {
        text(g, str[i], x, 70, 67, i >= 4 ? C.coral : C.ink, "FDSerif", 600);
        x += g.measureText(str[i]).width;
      }
      g.globalCompositeOperation = "destination-out";
      const r = rng(3555);
      g.fillStyle = "#00000045";
      for (let i = 0; i < 2200; i++)
        g.fillRect(r() * W, r() * 140, 0.7 + r() * 1.4, 0.7 + r() * 1.7);
    }
    this.g.save();
    this.g.globalAlpha = this.lyricOpacity ?? 1;
    this.g.drawImage(this.paperType, 0, 813);
    this.g.restore();
  }
  lyric(t, data) {
    const g = this.g,
      f = Math.round(t * 30),
      i = data.findLastIndex((l) => l.frame <= f),
      l = data[i];
    if (!l) return;
    const end = data[i + 1]?.time ?? 43.7,
      a = Math.min(1, (f - l.frame + 1) / 3, (end - t) * 10);
    g.save();
    g.globalAlpha = this.lyricOpacity ?? clamp(a);
    g.font = "600 46px FDSerif";
    g.textAlign = "left";
    g.textBaseline = "middle";
    const x = (W - g.measureText(l.text).width) / 2,
      y = t < 11.92 ? 882 : 994;
    g.shadowColor = "#141413CC";
    g.shadowBlur = 9;
    g.lineWidth = 2.5;
    g.strokeStyle = "#141413BB";
    g.strokeText(l.text, x, y);
    let xx = x;
    const keys = new Set();
    for (const m of l.text.matchAll(/明天|今天|存在|呼吸|脚踝|你|飞|爱|灿烂/g))
      for (let k = m.index; k < m.index + m[0].length; k++) keys.add(k);
    for (let k = 0; k < l.text.length; k++) {
      g.fillStyle = keys.has(k) ? C.coral : C.ivory;
      g.fillText(l.text[k], xx, y);
      xx += g.measureText(l.text[k]).width;
    }
    g.restore();
  }
  comments(t) {
    const f = Math.round(t * 30);
    let b,
      bank,
      count,
      size = 34;
    if (f >= 378 && f < 438) {
      b = 12.6;
      count = 3;
      bank = ["来了来了", "高能预警", "Opus 5.5！！"];
    } else if (f >= 621 && f < 681) {
      b = 20.7;
      count = 3;
      bank = ["泪目", "awsl", "这手 我哭死"];
    } else if (f >= 765 && f < 855) {
      b = 25.5;
      count = 10;
      bank = [
        "起飞！！",
        "前方高能",
        "这运镜我直接跪了",
        "帧帧壁纸",
        "名场面",
        "今日不降智",
      ];
    } else if (f >= 856 && f < 920) {
      b = 28.55;
      count = 1;
      bank = ["呜呜呜 这运镜"];
    } else if (f >= 920 && f < 1026) {
      b = 30.68;
      count = 1;
      bank = ["第一天就封神"];
      size = 70;
    } else if (f >= 1112 && f < 1197) {
      b = 37.07;
      count = 120;
      bank = [
        "你说得对！",
        "额度管够",
        "牛马下班了",
        "氛围编程",
        "一次跑通",
        "bug 退散",
        "我愿称之为最强",
        "已三连",
        "爷青回",
        "破防了",
        "yyds",
      ];
    } else if (f >= 1197 && f < 1311) {
      b = 39.9;
      count = 2;
      bank = ["呜呜", "终于等到你"];
    } else return;
    const g = this.g;
    g.save();
    g.globalAlpha = 0.85;
    g.font = `700 ${size}px FDSans`;
    g.textBaseline = "middle";
    g.textAlign = "left";
    g.lineWidth = 3;
    g.strokeStyle = C.ink;
    g.fillStyle = b === 30.68 ? C.gold : C.ivory;
    const wall = count === 120;
    let visible = 0;
    for (let i = 0; i < count; i++) {
      const lane = wall ? i % 10 : i % 6,
        col = wall ? Math.floor(i / 10) : Math.floor(i / 6),
        speed = 180 + ((lane * 37) % 241),
        x =
          (wall ? 40 + col * 340 : W * 0.82 + col * 620 + lane * 110) -
          (t - b) * speed,
        y = b === 39.9 ? 90 + lane * 55 : 110 + lane * (wall ? 88 : 104),
        str = bank[i % bank.length];
      g.globalAlpha =
        0.85 * (wall && lane >= 8 ? ease((t - b - 0.9) / 1.4) : 1);
      if (x + g.measureText(str).width > 0 && x < W && g.globalAlpha > 0.1)
        visible++;
      g.strokeText(str, x, y);
      g.fillText(str, x, y);
    }
    g.restore();
    this.trace.danmaku_count = visible;
  }
  finish(t) {
    const g = this.g;
    g.save();
    g.globalAlpha = 0.5;
    g.fillStyle = g.createPattern(this.noise, "repeat");
    g.fillRect(0, 0, W, H);
    g.restore();
    if (t < 11.92) {
      const v = g.createRadialGradient(960, 540, 370, 960, 540, 1160);
      v.addColorStop(0, "#14141300");
      v.addColorStop(1, "#14141355");
      g.fillStyle = v;
      g.fillRect(0, 0, W, H);
      g.fillStyle = C.ink;
      g.fillRect(0, 0, W, 138);
      g.fillRect(0, 942, W, 138);
    }
  }
}
