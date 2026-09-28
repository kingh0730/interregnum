// Ministry UI kit for the pilot's JS pieces in shots 01–20 (J01, J03–J08, J14–J16).
// Canvas 2D only, deterministic in t, system fonts only, no network.
(function () {
  const K = {};
  K.W = 1920; K.H = 1080;
  K.C = {
    navy: '#0A0F1C', blueBlack: '#121A2E', cyan: '#5FE1E6', amber: '#F2A441', red: '#E0412F',
    cream: '#E9E2D0', panel: '#0D1426', line: '#1E2A44', core: '#E9FBFF',
  };
  K.F = {
    cond: '"DIN Condensed"', alt: '"DIN Alternate"', mono: 'Menlo, "SF Mono", monospace',
    courier: '"Courier New"', futura: 'Futura', avenir: '"Avenir Next"',
  };
  K.BAND = [138, 942];
  K.FPS = 24;

  // ---- math / easing ----
  K.clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  K.lerp = (a, b, u) => a + (b - a) * u;
  K.seg = (t, a, b) => K.clamp((t - a) / (b - a));
  K.easeInOutCubic = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
  K.easeOutCubic = (x) => 1 - Math.pow(1 - x, 3);
  K.easeInCubic = (x) => x * x * x;
  K.easeInOutSine = (x) => -(Math.cos(Math.PI * x) - 1) / 2;
  // easeOutBack tuned to a 6 % peak overshoot (c solves 4c^3 / (27 (c+1)^2) = 0.06)
  K.easeOutBack6 = (x) => { const c = 1.281, u = x - 1; return 1 + (c + 1) * u * u * u + c * u * u; };
  K.frame = (t) => Math.floor(t * K.FPS + 1e-6);
  K.rng = (seed) => { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; };
  K.hash = (i, s = 0) => K.rng((i * 2654435761 + s * 97531) >>> 0)();
  K.pad = (n, w) => String(n).padStart(w, '0');

  // ---- clock helpers (film time → wall clock; changes on whole seconds) ----
  K.hms = (s) => { s = ((s % 86400) + 86400) % 86400; return K.pad(Math.floor(s / 3600), 2) + ':' + K.pad(Math.floor(s / 60) % 60, 2) + ':' + K.pad(s % 60, 2); };
  K.ms = (s) => K.pad(Math.floor(s / 60), 2) + ':' + K.pad(s % 60, 2);
  K.parseHMS = (str) => str.split(':').map(Number).reduce((a, b) => a * 60 + b, 0);

  // ---- canvas ----
  K.canvas = (opaque) => {
    document.documentElement.style.cssText = 'margin:0;padding:0;background:transparent;overflow:hidden';
    document.body.style.cssText = 'margin:0;padding:0;background:transparent;overflow:hidden';
    const cv = document.createElement('canvas');
    cv.width = K.W; cv.height = K.H;
    cv.style.cssText = 'display:block;width:1920px;height:1080px';
    document.body.appendChild(cv);
    const ctx = cv.getContext('2d', { alpha: !opaque });
    return ctx;
  };
  K.off = (w, h) => { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; };

  // text with tracking; align: left|center|right. Tracking in em. Centering compensates the trailing space.
  K.text = (ctx, str, x, y, o = {}) => {
    const size = o.size || 24;
    ctx.save();
    ctx.font = `${o.weight || ''} ${size}px ${o.font || K.F.alt}`.trim();
    ctx.letterSpacing = (o.track || 0) * size + 'px';
    ctx.textBaseline = o.baseline || 'alphabetic';
    ctx.globalAlpha *= (o.alpha == null ? 1 : o.alpha);
    ctx.fillStyle = o.color || K.C.cream;
    let w = ctx.measureText(str).width;
    const trail = (o.track || 0) * size;
    let dx = 0;
    if (o.align === 'center') dx = -(w - trail) / 2;
    else if (o.align === 'right') dx = -(w - trail);
    if (o.glow) { ctx.shadowColor = o.glowColor || o.color || K.C.cyan; ctx.shadowBlur = o.glow; }
    ctx.textAlign = 'left';
    ctx.fillText(str, x + dx, y);
    ctx.restore();
    return w - trail;
  };
  K.measure = (ctx, str, o = {}) => {
    const size = o.size || 24;
    ctx.save();
    ctx.font = `${o.weight || ''} ${size}px ${o.font || K.F.alt}`.trim();
    ctx.letterSpacing = (o.track || 0) * size + 'px';
    const w = ctx.measureText(str).width - (o.track || 0) * size;
    ctx.restore();
    return w;
  };
  K.rule = (ctx, x0, y, x1, color = K.C.line, w = 1) => { ctx.save(); ctx.fillStyle = color; ctx.fillRect(x0, Math.round(y), x1 - x0, w); ctx.restore(); };
  K.frameRect = (ctx, x, y, w, h, color = K.C.line, lw = 1) => { ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 1); ctx.restore(); };

  // ---- the Lamp emblem ----
  // geometry at scale 1 around the circle center (0,0): circle r150 stroke 10; flame 70×130 standing on (0,50);
  // base line at y 70, 8 px, 180 wide.
  K.flamePath = (ctx) => {
    // teardrop: round bulb at the bottom (r 35, center y 15), pointed tip at y -80, base touching y 50
    ctx.beginPath();
    ctx.moveTo(0, -80);
    ctx.bezierCurveTo(4, -58, 36, -30, 35, 15);
    ctx.bezierCurveTo(35, 36, 19, 50, 0, 50);
    ctx.bezierCurveTo(-19, 50, -35, 36, -35, 15);
    ctx.bezierCurveTo(-36, -30, -4, -58, 0, -80);
    ctx.closePath();
  };
  // o: {circle:0..1, flame:0..1+ (scale), base:0..1, color, core, strokeScale}
  K.emblem = (ctx, cx, cy, scale, o = {}) => {
    const color = o.color || K.C.cyan, core = o.core || K.C.core;
    ctx.save();
    ctx.translate(cx, cy);
    ctx.scale(scale, scale);
    const circle = o.circle == null ? 1 : o.circle;
    if (circle > 0) {
      ctx.beginPath();
      ctx.arc(0, 0, 150, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * circle);
      ctx.strokeStyle = color; ctx.lineWidth = 10; ctx.lineCap = circle < 1 ? 'round' : 'butt';
      ctx.stroke();
    }
    const fl = o.flame == null ? 1 : o.flame;
    if (fl > 0.001) {
      ctx.save();
      ctx.translate(0, 50);
      ctx.scale(fl * (o.breathe || 1), fl * (o.breathe || 1));
      ctx.translate(0, -50);
      K.flamePath(ctx);
      if (o.flat) { ctx.fillStyle = color; ctx.fill(); }
      else {
        const g = ctx.createRadialGradient(0, 18, 2, 0, 5, 62);
        g.addColorStop(0, core); g.addColorStop(0.38, core); g.addColorStop(0.75, color); g.addColorStop(1, color);
        ctx.fillStyle = g; ctx.fill();
      }
      if (o.negative) { // for the seal: knocked out
        ctx.globalCompositeOperation = 'destination-out'; ctx.fill();
      }
      ctx.restore();
    }
    const base = o.base == null ? 1 : o.base;
    if (base > 0) { ctx.fillStyle = color; ctx.fillRect(-90 * base, 66, 180 * base, 8); }
    ctx.restore();
  };

  // ---- images (file:// friendly; first candidate that loads wins) ----
  K.loadImage = (cands) => new Promise((resolve) => {
    let i = 0;
    const next = () => {
      if (i >= cands.length) return resolve(null);
      const src = cands[i++];
      const im = new Image();
      im.onload = () => resolve({ img: im, src });
      im.onerror = next;
      im.src = src;
    };
    next();
  });
  // relative to episodes/pilot/js/
  K.ROOT = '../../../';
  // k02 at push 1.04: the comp's frozen frame if it exists, else work/pilot/js/k02_push104.png (keys/k02.png scaled
  // 1.04 about (0.50, 0.42), made with ffmpeg; same geometry).
  K.K02_CANDS = [K.ROOT + 'work/pilot/k02_frozen.png', K.ROOT + 'work/pilot/js/k02_push104.png'];
  K.K01_CANDS = [K.ROOT + 'assets/pilot/keyframes/k01_father_mcu.png', K.ROOT + 'work/pilot/keys/k01.png'];
  K.K02RAW_CANDS = [K.ROOT + 'assets/pilot/keyframes/k02_father_cu.png', K.ROOT + 'work/pilot/keys/k02.png'];

  // ---- mesh (J16) ----
  // Returns {pts, tris, edges, earBox} in 1920×1080 frame coordinates of the image actually loaded.
  K.mesh = () => {
    const M = window.MESH_K02;
    const pts = M.points.map((p) => p.slice());
    const tris = K.delaunay(pts);
    const seen = new Set(), edges = [];
    for (const [a, b, c] of tris) for (const [i, j] of [[a, b], [b, c], [c, a]]) {
      const k = i < j ? i + ',' + j : j + ',' + i;
      if (!seen.has(k)) { seen.add(k); edges.push(i < j ? [i, j] : [j, i]); }
    }
    // drop long hull edges that would web across the background
    const E = edges.filter(([i, j]) => Math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1]) < 190);
    return { pts, tris, edges: E, earBox: M.ear_box.slice() };
  };
  K.delaunay = (P) => { // Bowyer–Watson, fine for ~120 points
    const n = P.length;
    const pts = P.concat([[-1e5, -1e5], [1e5, -1e5], [0, 1e5]]);
    let tris = [[n, n + 1, n + 2]];
    const circ = (t) => {
      const [ax, ay] = pts[t[0]], [bx, by] = pts[t[1]], [cx, cy] = pts[t[2]];
      const d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
      const ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
      const uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
      return [ux, uy, (ax - ux) ** 2 + (ay - uy) ** 2];
    };
    for (let i = 0; i < n; i++) {
      const [px, py] = pts[i];
      const bad = [], keep = [];
      for (const t of tris) { const [ux, uy, r2] = circ(t); ((px - ux) ** 2 + (py - uy) ** 2 < r2 ? bad : keep).push(t); }
      const cnt = new Map();
      for (const t of bad) for (const [a, b] of [[t[0], t[1]], [t[1], t[2]], [t[2], t[0]]]) { const k = a < b ? a + ',' + b : b + ',' + a; cnt.set(k, (cnt.get(k) || 0) + 1); }
      for (const [k, c] of cnt) if (c === 1) { const [a, b] = k.split(',').map(Number); keep.push([a, b, i]); }
      tris = keep;
    }
    return tris.filter((t) => t[0] < n && t[1] < n && t[2] < n);
  };
  // draw the mesh; o: {dotA, lineA, dotsVisible(i)->0..1, lineP 0..1 (draw-on), scale, ox, oy}
  K.drawMesh = (ctx, M, o = {}) => {
    const s = o.scale || 1, ox = o.ox || 0, oy = o.oy || 0;
    const X = (p) => ox + p[0] * s, Y = (p) => oy + p[1] * s;
    ctx.save();
    const lp = o.lineP == null ? 1 : o.lineP;
    if (lp > 0) {
      ctx.strokeStyle = K.C.cyan; ctx.lineWidth = o.lineW || 1.5; ctx.globalAlpha = o.lineA == null ? 0.55 : o.lineA;
      ctx.beginPath();
      M.edges.forEach(([i, j], k) => {
        const local = K.clamp(lp * 1.6 - (k / M.edges.length) * 0.6); // staggered draw-on
        if (local <= 0) return;
        const a = M.pts[i], b = M.pts[j];
        ctx.moveTo(X(a), Y(a));
        ctx.lineTo(K.lerp(X(a), X(b), local), K.lerp(Y(a), Y(b), local));
      });
      ctx.stroke();
    }
    ctx.fillStyle = K.C.cyan;
    const r = (o.dotR || 2);
    M.pts.forEach((p, i) => {
      const v = o.dotsVisible ? o.dotsVisible(i) : 1;
      if (v <= 0) return;
      ctx.globalAlpha = (o.dotA == null ? 0.9 : o.dotA) * Math.min(1, v);
      ctx.beginPath(); ctx.arc(X(p), Y(p), r, 0, Math.PI * 2); ctx.fill();
    });
    ctx.restore();
  };

  // ---- Ministry top bar (J03 / J07) ----
  // o: {t, clock0 (seconds of day), toAir0 (s), mode?: {text,color,blink}}
  K.topBar = (ctx, o) => {
    const C = K.C, F = K.F;
    const sec = Math.floor(o.t + 1e-6);
    K.text(ctx, 'MINISTRY OF CONTINUITY — NIGHT DESK 4', 60, 190, { font: F.alt, weight: 'bold', size: 24, color: C.cyan, alpha: 0.7, track: 0.06 });
    K.text(ctx, 'SUBJECT F', 960, 192, { font: F.cond, weight: 'bold', size: 30, color: C.cream, track: 0.3, align: 'center' });
    if (o.mode) {
      const blinkOn = o.frozen ? true : (o.t % 1) < 0.5;
      const x0 = 1130;
      ctx.save(); ctx.fillStyle = o.mode.color; ctx.globalAlpha = blinkOn ? 1 : 0.15;
      ctx.shadowColor = o.mode.color; ctx.shadowBlur = 10;
      ctx.beginPath(); ctx.arc(x0 + 7, 182, 7, 0, Math.PI * 2); ctx.fill(); ctx.restore();
      K.text(ctx, o.mode.text, x0 + 26, 190, { font: F.alt, weight: 'bold', size: 22, color: o.mode.color, track: 0.12 });
    }
    const wc = K.text(ctx, K.hms(o.clock0 + sec), 1860, 194, { font: F.cond, weight: 'bold', size: 44, color: C.cream, align: 'right', track: 0.04 });
    ctx.save(); ctx.fillStyle = C.line; ctx.fillRect(Math.round(1860 - wc - 22), 164, 1, 32); ctx.restore();
    K.text(ctx, 'TO AIR ' + K.ms(Math.max(0, o.toAir0 - sec)), 1860 - wc - 44, 191, { font: F.alt, weight: 'bold', size: 24, color: C.cyan, align: 'right', track: 0.08 });
    K.rule(ctx, 60, 204, 1860, C.line);
  };

  window.K = K;
})();
