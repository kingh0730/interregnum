// INTERREGNUM · CONTINUITY · v3 screen kit
// One family for every in-world screen: the state's letters (built here, never from a font), the Lamp, the tube
// (a WebGL CRT post-process), and the mechanical readouts (flaps, drums, needles, legend lamps, hands on paper).
// Authority: bible/visual/production_design.md §4 (hardware, artefacts) and §5 (letters, the Lamp).
// Deterministic: nothing here reads the clock; all randomness is seeded.
(function () {
'use strict';
const K = window.K = {};

// ───────────────────────────── math, noise, params ─────────────────────────────
K.clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
K.lerp = (a, b, t) => a + (b - a) * t;
K.smooth = (a, b, x) => { const t = K.clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
K.ease = {
  inQuad: t => t * t, outQuad: t => 1 - (1 - t) * (1 - t), outCubic: t => 1 - Math.pow(1 - t, 3),
  inOutCubic: t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,
  inOutSine: t => -(Math.cos(Math.PI * t) - 1) / 2, inCubic: t => t * t * t,
};
K.rng = function (seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
};
K.hash = (i, s = 0) => {
  let h = Math.imul((i | 0) ^ 0x9E3779B9, 0x85EBCA6B) ^ Math.imul((s | 0) + 0x632BE5AB, 0xC2B2AE35);
  h ^= h >>> 15; h = Math.imul(h, 0x2C1B3C6D); h ^= h >>> 12; h = Math.imul(h, 0x297A2D39); h ^= h >>> 15;
  return (h >>> 0) / 4294967296;
};
K.noise1 = (x, s = 0) => {
  const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
  return K.lerp(K.hash(i, s), K.hash(i + 1, s), u) * 2 - 1;
};
K.fbm1 = (x, s = 0) => K.noise1(x, s) * .6 + K.noise1(x * 2.3, s + 7) * .3 + K.noise1(x * 5.1, s + 13) * .1;
K.param = (k, d) => {
  const v = new URLSearchParams(location.search).get(k);
  return v === null ? d : (typeof d === 'number' ? Number(v) : v);
};
K.canvas = (w, h) => { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; };
K.hex = h => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
K.rgba = (h, a = 1) => { const c = K.hex(h); return `rgba(${c[0]},${c[1]},${c[2]},${a})`; };
K.mix = (h1, h2, k, a = 1) => {
  const A = K.hex(h1), B = K.hex(h2);
  return `rgba(${A.map((v, i) => Math.round(v + (B[i] - v) * k)).join(',')},${a})`;
};
K.FPS = 24;
K.frame = t => Math.round(t * K.FPS);

// Palette (production_design.md §2). Screen colours are *emission*: the tube pass turns the bloom colour into
// a white-hot core, so pages draw phosphor in its bloom colour.
K.C = {
  key: '#11151F', cold: '#5FE1E6', coldCore: '#DDFBFA', warm: '#F2A441', warmCore: '#FFD9A0',
  red: '#E0412F', redInk: '#CC3A2B', cream: '#E9E2D0', paper: '#E8DDC4', rose: '#F4C6C0',
  scope: '#6CF2C4', enamel: '#3C444C', bakelite: '#1C1714', ink: '#1E2433',
};

// ───────────────────────────── State Capitals (§5.1) ─────────────────────────────
// Centre-line skeletons on the 4 × 6 module grid (M and W 5 wide; I and punctuation narrower). Coordinates are the
// stroke's centre line, so the outer edge sits 0.5 module further out. A vertex marked `r` is rounded with a
// centre-line radius of 1 module (outer radius 1.5, as the bible specifies). Diagonals run corner to corner.
const CAPS_SRC = {
  A: [4, ['0.5,5.5 0.5,0.5r 3.5,0.5r 3.5,5.5', '0.5,3 3.5,3']],
  B: [4, ['0.5,3 0.5,0.5 2.5,0.5r 2.5,3r 0.5,3', '0.5,3 0.5,5.5 3.5,5.5r 3.5,3r 0.5,3']],
  C: [4, ['3.5,0.5 0.5,0.5r 0.5,5.5r 3.5,5.5']],
  D: [4, ['0.5,0.5 0.5,5.5', '0.5,0.5 3.5,0.5r 3.5,5.5r 0.5,5.5']],
  E: [4, ['3.5,0.5 0.5,0.5 0.5,5.5 3.5,5.5', '0.5,3 3,3']],
  F: [4, ['3.5,0.5 0.5,0.5 0.5,5.5', '0.5,3 3,3']],
  G: [4, ['3.5,1.5 3.5,0.5 0.5,0.5r 0.5,5.5r 3.5,5.5r 3.5,3 2,3']],
  H: [4, ['0.5,0.5 0.5,5.5', '3.5,0.5 3.5,5.5', '0.5,3 3.5,3']],
  I: [1, ['0.5,0.5 0.5,5.5']],
  J: [4, ['3.5,0.5 3.5,5.5r 0.5,5.5r 0.5,4']],
  K: [4, ['0.5,0.5 0.5,5.5', '3.5,0.5 0.5,3 3.5,5.5']],
  L: [4, ['0.5,0.5 0.5,5.5 3.5,5.5']],
  M: [5, ['0.5,5.5 0.5,0.5 2.5,3 4.5,0.5 4.5,5.5']],
  N: [4, ['0.5,5.5 0.5,0.5 3.5,5.5 3.5,0.5']],
  O: [4, ['2,0.5 3.5,0.5r 3.5,5.5r 0.5,5.5r 0.5,0.5r 2,0.5']],
  P: [4, ['0.5,5.5 0.5,0.5 3.5,0.5r 3.5,3r 0.5,3']],
  Q: [4, ['2,0.5 3.5,0.5r 3.5,5.5r 0.5,5.5r 0.5,0.5r 2,0.5', '2.2,4.2 3.9,5.9']],
  R: [4, ['0.5,5.5 0.5,0.5 3.5,0.5r 3.5,3r 0.5,3', '2,3 3.5,5.5']],
  S: [4, ['3.5,0.5 0.5,0.5r 0.5,3r 3.5,3r 3.5,5.5r 0.5,5.5']],
  T: [4, ['0.5,0.5 3.5,0.5', '2,0.5 2,5.5']],
  U: [4, ['0.5,0.5 0.5,5.5r 3.5,5.5r 3.5,0.5']],
  V: [4, ['0.5,0.5 2,5.5 3.5,0.5']],
  W: [5, ['0.5,0.5 0.5,5.5 2.5,3 4.5,5.5 4.5,0.5']],
  X: [4, ['0.5,0.5 3.5,5.5', '3.5,0.5 0.5,5.5']],
  Y: [4, ['0.5,0.5 2,3 3.5,0.5', '2,3 2,5.5']],
  Z: [4, ['0.5,0.5 3.5,0.5 0.5,5.5 3.5,5.5']],
  '0': [4, ['2,0.5 3.5,0.5r 3.5,5.5r 0.5,5.5r 0.5,0.5r 2,0.5']],
  '1': [4, ['0.8,1.7 2.2,0.5 2.2,5.5']],
  '2': [4, ['0.5,0.5 3.5,0.5r 3.5,3r 0.5,3r 0.5,5.5 3.5,5.5']],
  '3': [4, ['0.5,0.5 3.5,0.5r 3.5,5.5r 0.5,5.5', '1.3,3 3.5,3']],
  '4': [4, ['0.5,0.5 0.5,3.8 3.5,3.8', '2.7,1.8 2.7,5.5']],
  '5': [4, ['3.5,0.5 0.5,0.5 0.5,3 3.5,3r 3.5,5.5r 0.5,5.5']],
  '6': [4, ['3.5,0.5 0.5,0.5r 0.5,5.5r 3.5,5.5r 3.5,3r 0.5,3']],
  '7': [4, ['0.5,0.5 3.5,0.5 1.5,5.5']],
  '8': [4, ['2,0.5 3.2,0.5r 3.2,3r 0.8,3r 0.8,0.5r 2,0.5', '2,3 3.5,3r 3.5,5.5r 0.5,5.5r 0.5,3r 2,3']],
  '9': [4, ['0.5,5.5 3.5,5.5r 3.5,0.5r 0.5,0.5r 0.5,3r 3.5,3']],
  '·': [1, ['0.5,3 0.5,3']],
  '.': [1, ['0.5,5.5 0.5,5.5']],
  ':': [1, ['0.5,1.8 0.5,1.8', '0.5,4.6 0.5,4.6']],
  ',': [1, ['0.5,5.2 0.5,6.4']],
  "'": [1, ['0.5,0.5 0.5,1.9']],
  '-': [3, ['0.5,3 2.5,3']],
  '+': [4, ['0.5,3 3.5,3', '2,1.5 2,4.5']],
  '/': [4, ['0.5,5.5 3.5,0.5']],
  '#': [4, ['1.2,0.5 1.2,5.5', '2.8,0.5 2.8,5.5', '0.5,2 3.5,2', '0.5,4 3.5,4']],
};
// parse "x,y[r] …" into [{x,y,r}]
function parseStroke(s) {
  return s.trim().split(/\s+/).map(tok => {
    const r = tok.endsWith('r'); const [x, y] = tok.replace('r', '').split(',').map(Number);
    return { x, y, r };
  });
}
// Replace every rounded vertex by a circular fillet of centre-line radius `rad`, faceted into `facets` segments.
function filletPolyline(pts, rad, facets) {
  const out = [];
  for (let i = 0; i < pts.length; i++) {
    const P = pts[i];
    if (!P.r || i === 0 || i === pts.length - 1) { out.push([P.x, P.y]); continue; }
    const A = pts[i - 1], C = pts[i + 1];
    let d1x = P.x - A.x, d1y = P.y - A.y, l1 = Math.hypot(d1x, d1y); d1x /= l1; d1y /= l1;
    let d2x = C.x - P.x, d2y = C.y - P.y, l2 = Math.hypot(d2x, d2y); d2x /= l2; d2y /= l2;
    const phi = Math.acos(K.clamp(-(d1x * d2x + d1y * d2y), -1, 1));
    let r = rad, tl = r / Math.tan(phi / 2);
    const lim = Math.min(l1, l2) * 0.999; if (tl > lim) { tl = lim; r = tl * Math.tan(phi / 2); }
    const T1 = [P.x - d1x * tl, P.y - d1y * tl], T2 = [P.x + d2x * tl, P.y + d2y * tl];
    const cr = d1x * d2y - d1y * d2x;
    const n = cr > 0 ? [-d1y, d1x] : [d1y, -d1x];
    const cx = T1[0] + n[0] * r, cy = T1[1] + n[1] * r;
    const a0 = Math.atan2(T1[1] - cy, T1[0] - cx); let a1 = Math.atan2(T2[1] - cy, T2[0] - cx);
    let da = a1 - a0; while (da > Math.PI) da -= 2 * Math.PI; while (da < -Math.PI) da += 2 * Math.PI;
    for (let k = 0; k <= facets; k++) { const a = a0 + da * k / facets; out.push([cx + Math.cos(a) * r, cy + Math.sin(a) * r]); }
  }
  return out;
}
const capsCache = {};
// A glyph's strokes as polylines in module units. facets: 8 = smooth (cast/engraved), 4 = Stroke Hand.
K.capsGlyph = function (ch, facets = 8) {
  const key = ch + '|' + facets; if (capsCache[key]) return capsCache[key];
  const src = CAPS_SRC[ch]; if (!src) return null;
  const g = { w: src[0], strokes: src[1].map(s => {
    const pts = parseStroke(s);
    if (pts.length === 2 && pts[0].x === pts[1].x && pts[0].y === pts[1].y) pts[1] = { x: pts[1].x + .02, y: pts[1].y, r: false }; // a dot
    return filletPolyline(pts, 1, facets);
  }) };
  return (capsCache[key] = g);
};
// Lay out a line: letter spacing 1 module, word space 3 (a space advances 2 after the 1-module letter gap).
K.capsLayout = function (text, facets = 8, spacing = 1) {
  const glyphs = []; let x = 0, first = true;
  for (const ch of text) {
    if (ch === ' ') { x += 2; continue; }
    const g = K.capsGlyph(ch, facets); if (!g) continue;
    if (!first) x += spacing; first = false;
    glyphs.push({ ch, x, g }); x += g.w;
  }
  return { glyphs, width: x };
};
// Stroke paths of a line, in px. `m` = module size; (x, y) = top-left of the cap box, or centre with align.
K.capsStrokes = function (text, x, y, m, o = {}) {
  const L = K.capsLayout(text, o.facets || 8, o.spacing == null ? 1 : o.spacing);
  const sx = o.sx || 1; // horizontal condensing
  let ox = x; if (o.align === 'center') ox = x - L.width * m * sx / 2; else if (o.align === 'right') ox = x - L.width * m * sx;
  const shear = o.shear || 0, strokes = [];
  for (const gl of L.glyphs) for (const s of gl.g.strokes) {
    strokes.push({ ch: gl.ch, pts: s.map(([u, v]) => [ox + (gl.x + u) * m * sx + (6 - v) * m * shear, y + v * m]) });
  }
  return { strokes, width: L.width * m * sx, x0: ox };
};
K.capsPath = function (ctx, text, x, y, m, o = {}) {
  const S = K.capsStrokes(text, x, y, m, o);
  ctx.beginPath();
  for (const s of S.strokes) { ctx.moveTo(s.pts[0][0], s.pts[0][1]); for (let i = 1; i < s.pts.length; i++) ctx.lineTo(s.pts[i][0], s.pts[i][1]); }
  return S;
};
// Solid monoline letters (square caps and mitred joins: sheet steel). The stroke is one module thick.
K.capsFill = function (ctx, text, x, y, m, o = {}) {
  ctx.save(); K.capsPath(ctx, text, x, y, m, o);
  ctx.lineWidth = m * (o.weight || 1); ctx.lineCap = 'square'; ctx.lineJoin = 'miter'; ctx.miterLimit = 3;
  ctx.strokeStyle = o.color || '#fff'; ctx.stroke(); ctx.restore();
  return K.capsLayout(text).width * m * (o.sx || 1);
};
// Engraved + cream-filled legend: dark cut shadow, the fill, and seeded chips of missing fill.
K.capsEngraved = function (ctx, text, x, y, m, o = {}) {
  const fill = o.fill || K.C.cream, seed = o.seed || 7, rnd = K.rng(seed);
  const tmp = K.canvas(ctx.canvas.width, ctx.canvas.height), c2 = tmp.getContext('2d');
  // the cut: a dark groove offset up-left (light from above-left falls into it)
  K.capsFill(ctx, text, x - m * .12, y - m * .12, m, Object.assign({}, o, { color: o.cut || 'rgba(0,0,0,.55)' }));
  K.capsFill(c2, text, x, y, m, Object.assign({}, o, { color: fill }));
  // chipped fill: small irregular blobs removed on some letters (the chipList picks letters, else random)
  c2.globalCompositeOperation = 'destination-out';
  const S = K.capsStrokes(text, x, y, m, o);
  const chipped = new Set(o.chip || []);
  S.strokes.forEach((s, i) => {
    const hit = chipped.size ? chipped.has(s.ch) : rnd() < (o.chipRate || .15);
    if (!hit) return;
    const p = s.pts[Math.floor(rnd() * s.pts.length)];
    const n = 2 + Math.floor(rnd() * 3);
    for (let k = 0; k < n; k++) {
      c2.beginPath();
      c2.ellipse(p[0] + (rnd() - .5) * m * 1.5, p[1] + (rnd() - .5) * m * 1.5, m * (.25 + rnd() * .45), m * (.2 + rnd() * .35), rnd() * 3, 0, 7);
      c2.fill();
    }
  });
  ctx.drawImage(tmp, 0, 0);
};

// ───────────────────────────── Operator Mono (§5.2) ─────────────────────────────
// 7 × 9 dot matrix plus 2 descender rows, in a 9 × 14 cell. Mixed case. One glyph per line:
// char, then rows 0–8 (and 9–10 for descenders); `_` is an empty row. Slashed zero, straight apostrophe.
// \u0001 is the padlock.
const OM_SRC = `
A ..###.. .#...#. #.....# #.....# #.....# ####### #.....# #.....# #.....#
B ######. #.....# #.....# #.....# ######. #.....# #.....# #.....# ######.
C .#####. #.....# #...... #...... #...... #...... #...... #.....# .#####.
D #####.. #....#. #.....# #.....# #.....# #.....# #.....# #....#. #####..
E ####### #...... #...... #...... #####.. #...... #...... #...... #######
F ####### #...... #...... #...... #####.. #...... #...... #...... #......
G .#####. #.....# #...... #...... #..#### #.....# #.....# #.....# .#####.
H #.....# #.....# #.....# #.....# ####### #.....# #.....# #.....# #.....#
I .#####. ...#... ...#... ...#... ...#... ...#... ...#... ...#... .#####.
J ..##### .....#. .....#. .....#. .....#. .....#. #....#. #....#. .####..
K #.....# #....#. #...#.. #..#... ###.... #..#... #...#.. #....#. #.....#
L #...... #...... #...... #...... #...... #...... #...... #...... #######
M #.....# ##...## #.#.#.# #..#..# #.....# #.....# #.....# #.....# #.....#
N #.....# ##....# ##....# #.#...# #..#..# #...#.# #....## #....## #.....#
O .#####. #.....# #.....# #.....# #.....# #.....# #.....# #.....# .#####.
P ######. #.....# #.....# #.....# ######. #...... #...... #...... #......
Q .#####. #.....# #.....# #.....# #.....# #.....# #...#.# #....#. .####.#
R ######. #.....# #.....# #.....# ######. #..#... #...#.. #....#. #.....#
S .#####. #.....# #...... #...... .#####. ......# ......# #.....# .#####.
T ####### ...#... ...#... ...#... ...#... ...#... ...#... ...#... ...#...
U #.....# #.....# #.....# #.....# #.....# #.....# #.....# #.....# .#####.
V #.....# #.....# #.....# #.....# .#...#. .#...#. ..#.#.. ..#.#.. ...#...
W #.....# #.....# #.....# #.....# #..#..# #..#..# #.#.#.# ##...## #.....#
X #.....# #.....# .#...#. ..#.#.. ...#... ..#.#.. .#...#. #.....# #.....#
Y #.....# #.....# .#...#. ..#.#.. ...#... ...#... ...#... ...#... ...#...
Z ####### ......# .....#. ....#.. ...#... ..#.... .#..... #...... #######
a _ _ _ .#####. ......# .###### #.....# #....## .####.#
b #...... #...... #...... #.####. ##....# #.....# #.....# ##....# #.####.
c _ _ _ .#####. #.....# #...... #...... #.....# .#####.
d ......# ......# ......# .####.# #....## #.....# #.....# #....## .####.#
e _ _ _ .#####. #.....# ####### #...... #.....# .#####.
f ...###. ..#...# ..#.... #####.. ..#.... ..#.... ..#.... ..#.... ..#....
g _ _ _ .####.# #....## #.....# #....## .####.# ......# #.....# .#####.
h #...... #...... #...... #.####. ##....# #.....# #.....# #.....# #.....#
i _ ...#... _ ..##... ...#... ...#... ...#... ...#... ..###..
j _ .....#. _ ....##. .....#. .....#. .....#. .....#. .....#. #....#. .####..
k #...... #...... #...... #....#. #...#.. #..#... ###.... #...#.. #....#.
l ..##... ...#... ...#... ...#... ...#... ...#... ...#... ...#... ..###..
m _ _ _ ##.##.. #.#..#. #..#..# #..#..# #..#..# #..#..#
n _ _ _ #.####. ##....# #.....# #.....# #.....# #.....#
o _ _ _ .#####. #.....# #.....# #.....# #.....# .#####.
p _ _ _ #.####. ##....# #.....# ##....# #.####. #...... #...... #......
q _ _ _ .####.# #....## #.....# #....## .####.# ......# ......# ......#
r _ _ _ #.####. ##....# #...... #...... #...... #......
s _ _ _ .###### #...... .#####. ......# ......# ######.
t _ ..#.... ..#.... ######. ..#.... ..#.... ..#.... ..#...# ...###.
u _ _ _ #.....# #.....# #.....# #.....# #....## .####.#
v _ _ _ #.....# #.....# .#...#. .#...#. ..#.#.. ...#...
w _ _ _ #.....# #.....# #..#..# #..#..# #.#.#.# .#...#.
x _ _ _ #.....# .#...#. ..#.#.. ..#.#.. .#...#. #.....#
y _ _ _ #.....# #.....# #.....# #....## .####.# ......# #.....# .#####.
z _ _ _ ####### .....#. ....#.. ..#.... .#..... #######
0 .#####. #.....# #....## #...#.# #..#..# #.#...# ##....# #.....# .#####.
1 ...#... ..##... .#.#... ...#... ...#... ...#... ...#... ...#... .#####.
2 .#####. #.....# ......# .....#. ...##.. ..#.... .#..... #...... #######
3 .#####. #.....# ......# ......# ..####. ......# ......# #.....# .#####.
4 ....#.. ...##.. ..#.#.. .#..#.. #...#.. ####### ....#.. ....#.. ....#..
5 ####### #...... #...... ######. ......# ......# ......# #.....# .#####.
6 ..####. .#..... #...... #...... ######. #.....# #.....# #.....# .#####.
7 ####### ......# .....#. ....#.. ...#... ..#.... ..#.... ..#.... ..#....
8 .#####. #.....# #.....# #.....# .#####. #.....# #.....# #.....# .#####.
9 .#####. #.....# #.....# #.....# .###### ......# ......# .....#. .####..
. _ _ _ _ _ _ _ ..##... ..##...
, _ _ _ _ _ _ _ ..##... ..##... ...#... ..#....
; _ _ _ ..##... ..##... _ _ ..##... ..##... ...#... ..#....
: _ _ _ ..##... ..##... _ _ ..##... ..##...
' ...#... ...#... ...#... _ _ _ _ _ _
- _ _ _ _ .#####. _ _ _ _
— _ _ _ _ ####### _ _ _ _
[ ..####. ..#.... ..#.... ..#.... ..#.... ..#.... ..#.... ..#.... ..####.
] .####.. ....#.. ....#.. ....#.. ....#.. ....#.. ....#.. ....#.. .####..
· _ _ _ _ ..##... ..##... _ _ _
? .#####. #.....# ......# .....#. ...##.. ...#... _ ...#... ...#...
! ...#... ...#... ...#... ...#... ...#... ...#... _ ...#... ...#...
/ ......# ......# .....#. ....#.. ...#... ..#.... .#..... #...... #......
… _ _ _ _ _ _ _ _ #..#..#
\u0001 ..###.. .#...#. .#...#. ####### ####### ###.### ###.### ####### #######
`;
const OM = {};
OM_SRC.trim().split('\n').forEach(line => {
  const parts = line.trim().split(/\s+/); let ch = parts[0];
  if (ch === '\\u0001') ch = '\u0001';
  const rows = parts.slice(1).map(r => r === '_' ? '.......' : r);
  while (rows.length < 11) rows.push('.......');
  OM[ch] = rows;
});
K.OM = OM;
K.OM_CELL = { w: 9, h: 14, gw: 7, gh: 11 };
// Pre-render every glyph as beam dashes: each dot is a short horizontal dash (the spot smeared along the scan);
// consecutive dots on a scan row fuse, and there is a dark gap between scan rows.
K.omAtlas = function (color, ux, uy, o = {}) {
  const cw = Math.round(9 * ux), ch = Math.round(14 * uy), chars = Object.keys(OM).concat([' ', '█']);
  const cols = 16, rows = Math.ceil(chars.length / cols);
  const cv = K.canvas(cols * cw, rows * ch), c = cv.getContext('2d');
  const dashH = uy * (o.fill || .5), map = {};
  c.fillStyle = color;
  chars.forEach((k, i) => {
    const gx = (i % cols) * cw, gy = Math.floor(i / cols) * ch; map[k] = [gx, gy];
    if (k === '█') { // block cursor: a solid cell of scan dashes (9 rows tall × 7 wide, plus the descender)
      for (let r = 0; r < 11; r++) c.fillRect(gx + ux * 1 - ux * .15, gy + uy * (1.5 + r) + (uy - dashH) / 2, ux * 7.3, dashH);
      return;
    }
    const g = OM[k]; if (!g) return;
    for (let r = 0; r < 11; r++) {
      const row = g[r]; let c0 = -1;
      for (let x = 0; x <= 7; x++) {
        const on = x < 7 && row[x] === '#';
        if (on && c0 < 0) c0 = x;
        if (!on && c0 >= 0) {
          const x0 = gx + ux * (1 + c0) - ux * .18, w = ux * (x - c0) + ux * .36;
          const y0 = gy + uy * (1.5 + r) + (uy - dashH) / 2;
          c.beginPath(); c.roundRect(x0, y0, w, dashH, dashH / 2); c.fill();
          c0 = -1;
        }
      }
    }
  });
  return { cv, map, cw, ch };
};
// Draw a string with an atlas. Inverse video (`inv`) paints the cell block and knocks the glyph out.
K.omText = function (ctx, atlas, str, x, y, o = {}) {
  let cx = x;
  for (const k of str) {
    const p = atlas.map[k] || atlas.map['?'];
    if (k !== ' ') ctx.drawImage(atlas.cv, p[0], p[1], atlas.cw, atlas.ch, cx, y, atlas.cw, atlas.ch);
    cx += atlas.cw;
  }
  return cx;
};

// ───────────────────────────── Caption Mosaic (§5.4) ─────────────────────────────
const CM_SRC = `
A .###. #...# #...# ##### #...# #...# #...#
B ####. #...# #...# ####. #...# #...# ####.
C .###. #...# #.... #.... #.... #...# .###.
D ####. #...# #...# #...# #...# #...# ####.
E ##### #.... #.... ####. #.... #.... #####
F ##### #.... #.... ####. #.... #.... #....
G .###. #...# #.... #.### #...# #...# .###.
H #...# #...# #...# ##### #...# #...# #...#
I .###. ..#.. ..#.. ..#.. ..#.. ..#.. .###.
J ..### ...#. ...#. ...#. ...#. #..#. .##..
K #...# #..#. #.#.. ##... #.#.. #..#. #...#
L #.... #.... #.... #.... #.... #.... #####
M #...# ##.## #.#.# #.#.# #...# #...# #...#
N #...# #...# ##..# #.#.# #..## #...# #...#
O .###. #...# #...# #...# #...# #...# .###.
P ####. #...# #...# ####. #.... #.... #....
Q .###. #...# #...# #...# #.#.# #..#. .##.#
R ####. #...# #...# ####. #.#.. #..#. #...#
S .#### #.... #.... .###. ....# ....# ####.
T ##### ..#.. ..#.. ..#.. ..#.. ..#.. ..#..
U #...# #...# #...# #...# #...# #...# .###.
V #...# #...# #...# #...# #...# .#.#. ..#..
W #...# #...# #...# #.#.# #.#.# #.#.# .#.#.
X #...# #...# .#.#. ..#.. .#.#. #...# #...#
Y #...# #...# .#.#. ..#.. ..#.. ..#.. ..#..
Z ##### ....# ...#. ..#.. .#... #.... #####
0 .###. #...# #..## #.#.# ##..# #...# .###.
1 ..#.. .##.. ..#.. ..#.. ..#.. ..#.. .###.
2 .###. #...# ....# ...#. ..#.. .#... #####
3 ##### ...#. ..#.. ...#. ....# #...# .###.
4 ...#. ..##. .#.#. #..#. ##### ...#. ...#.
5 ##### #.... ####. ....# ....# #...# .###.
6 ..##. .#... #.... ####. #...# #...# .###.
7 ##### ....# ...#. ..#.. .#... .#... .#...
8 .###. #...# #...# .###. #...# #...# .###.
9 .###. #...# #...# .#### ....# ...#. .##..
. ..... ..... ..... ..... ..... .##.. .##..
, ..... ..... ..... ..... .##.. ..#.. .#...
: ..... .##.. .##.. ..... .##.. .##.. .....
· ..... ..... ..... ..#.. ..... ..... .....
' ..#.. ..#.. .#... ..... ..... ..... .....
- ..... ..... ..... .###. ..... ..... .....
— ..... ..... ..... ##### ..... ..... .....
? .###. #...# ....# ...#. ..#.. ..... ..#..
! ..#.. ..#.. ..#.. ..#.. ..#.. ..... ..#..
+ ..... ..#.. ..#.. ##### ..#.. ..#.. .....
… ..... ..... ..... ..... ..... ..... #.#.#
`;
const CM = {};
CM_SRC.trim().split('\n').forEach(line => { const p = line.trim().split(/\s+/); CM[p[0]] = p.slice(1); });
K.CM = CM;
// Mosaic Lamp: the broadcast bug's 8 × 8 block copy of the sacred sign.
K.MOSAIC_LAMP = ['..####..', '.#.##.#.', '#..##..#', '#..##..#', '#......#', '#.####.#', '.#....#.', '..####..'];
// Rasterise a Caption Mosaic string to a block grid (1 = letter, 2 = keyer edge, 3 = cell background).
K.cmGrid = function (text, o = {}) {
  const cells = [...text.toUpperCase()]; const W = cells.length * 6 + 1, H = 9;
  const g = Array.from({ length: H }, () => new Uint8Array(W));
  cells.forEach((ch, i) => {
    const rows = CM[ch]; const x0 = 1 + i * 6;
    if (o.cells && ch !== ' ') for (let y = 0; y < 9; y++) for (let x = -1; x < 6; x++) { const X = x0 + x; if (X >= 0 && X < W) g[y][X] = 3; }
    if (!rows) return;
    for (let y = 0; y < 7; y++) for (let x = 0; x < 5; x++) if (rows[y][x] === '#') g[y + 1][x0 + x] = 1;
  });
  // keyer edge: one block around every letter block
  const e = g.map(r => r.slice());
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (g[y][x] === 1)
    for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
      const Y = y + dy, X = x + dx; if (Y >= 0 && Y < H && X >= 0 && X < W && e[Y][X] !== 1) e[Y][X] = 2;
    }
  return { g: e, W, H };
};
// Draw blocks: soft-cornered squares on a pitch; `b` = block size, gap 1 px (or o.gap).
K.blocks = function (ctx, grid, x, y, b, o = {}) {
  const gap = o.gap == null ? 1 : o.gap, rad = o.rad == null ? b * .28 : o.rad;
  for (const [val, col] of o.colors) {
    ctx.fillStyle = col; ctx.beginPath();
    for (let r = 0; r < grid.length; r++) for (let c = 0; c < grid[r].length; c++) if (grid[r][c] === val)
      ctx.roundRect(x + c * b, y + r * b, b - gap, b - gap, rad);
    ctx.fill();
  }
};

// ───────────────────────────── The Lamp (§5, emblem) ─────────────────────────────
// Ring r 150, flame 70 × 130, base 180 wide, drawn with compass and rule. The flame is a pointed arch of two equal
// arcs centred on the base line (for a 70 × 130 flame the centres lie outside the base: a lancet).
K.lampGeom = { ring: 150, ringW: 17, baseW: 180, baseH: 17, baseY: 52, flameW: 70, flameH: 130 };
// Flame: a round foot (a semicircle of the flame's half-width) under a lancet of two equal arcs whose centres sit on
// the foot's springing line, so the sides run on tangentially. Three compass settings, one rule: a schoolchild's lamp.
K.lampPaths = function (cx, cy, s) {
  const G = K.lampGeom, ring = new Path2D(), flame = new Path2D(), base = new Path2D();
  ring.arc(cx, cy, G.ring * s, 0, Math.PI * 2); ring.arc(cx, cy, (G.ring - G.ringW) * s, 0, Math.PI * 2, true);
  const by = cy + G.baseY * s; // top of the base bar
  base.rect(cx - G.baseW / 2 * s, by, G.baseW * s, G.baseH * s);
  const r = G.flameW / 2, up = G.flameH - r, c = (up * up - r * r) / (2 * r), R = c + r;
  const sy = by - 6 * s - r * s; // springing line (centre of the foot), with a 6-unit gap above the base
  const th = Math.atan2(up, c);
  flame.moveTo(cx - r * s, sy);
  flame.arc(cx + c * s, sy, R * s, Math.PI, Math.PI + th, false);   // left side up to the apex
  flame.arc(cx - c * s, sy, R * s, -th, 0, false);                  // apex down the right side
  flame.arc(cx, sy, r * s, 0, Math.PI, false);                      // the round foot
  flame.closePath();
  return { ring, flame, base, sy };
};
K.lamp = function (ctx, cx, cy, s, color) {
  const P = K.lampPaths(cx, cy, s); ctx.save(); ctx.fillStyle = color;
  ctx.fill(P.ring, 'evenodd'); ctx.fill(P.flame); ctx.fill(P.base); ctx.restore();
};
// The Sealed Lamp: the Lamp inside a double ring of small dots, one dot per member of the Committee.
K.SEAL_DOTS = [29, 23];
K.sealedLamp = function (ctx, cx, cy, s, color) {
  ctx.save(); ctx.fillStyle = color;
  const rings = [[230, K.SEAL_DOTS[0], 9.5], [195, K.SEAL_DOTS[1], 8]];
  for (const [r, n, d] of rings) for (let i = 0; i < n; i++) {
    const a = -Math.PI / 2 + i * Math.PI * 2 / n;
    ctx.beginPath(); ctx.arc(cx + Math.cos(a) * r * s, cy + Math.sin(a) * r * s, d * s, 0, 7); ctx.fill();
  }
  ctx.restore(); K.lamp(ctx, cx, cy, s, color);
};

// ───────────────────────────── textures ─────────────────────────────
// Value-noise field canvas (grayscale), for paper fibre, film grain, enamel grime.
K.noiseCanvas = function (w, h, seed, o = {}) {
  const cv = K.canvas(w, h), c = cv.getContext('2d'), img = c.createImageData(w, h), d = img.data, rnd = K.rng(seed);
  const oct = o.octaves || [[1, 1]]; // [scale px, amplitude]
  const grids = oct.map(([sc]) => {
    const gw = Math.ceil(w / sc) + 2, gh = Math.ceil(h / sc) + 2, a = new Float32Array(gw * gh);
    for (let i = 0; i < a.length; i++) a[i] = rnd(); return { gw, gh, a, sc };
  });
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    let v = 0, tot = 0;
    grids.forEach((G, i) => {
      const fx = x / G.sc, fy = y / G.sc, ix = Math.floor(fx), iy = Math.floor(fy), tx = fx - ix, ty = fy - iy;
      const u = tx * tx * (3 - 2 * tx), vv = ty * ty * (3 - 2 * ty), A = G.a, gw = G.gw;
      const a = A[iy * gw + ix], b = A[iy * gw + ix + 1], cc = A[(iy + 1) * gw + ix], dd = A[(iy + 1) * gw + ix + 1];
      v += (a + (b - a) * u + (cc - a) * vv + (a - b - cc + dd) * u * vv) * oct[i][1]; tot += oct[i][1];
    });
    v /= tot; if (o.stretchX) {} const k = (y * w + x) * 4, g = Math.round(K.clamp(v) * 255);
    d[k] = d[k + 1] = d[k + 2] = g; d[k + 3] = 255;
  }
  c.putImageData(img, 0, 0); return cv;
};
// Static glass grime: dust specks, a few fibres, a wiped smear. White on transparent; the CRT lights it.
K.dustCanvas = function (w, h, seed, o = {}) {
  const cv = K.canvas(w, h), c = cv.getContext('2d'), rnd = K.rng(seed);
  const n = o.n || Math.round(w * h / 9000);
  for (let i = 0; i < n; i++) {
    const x = rnd() * w, y = rnd() * h, r = .5 + Math.pow(rnd(), 3) * 2.2;
    c.fillStyle = `rgba(255,255,255,${.15 + rnd() * .5})`; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill();
  }
  for (let i = 0; i < (o.fibres || 6); i++) {
    let x = rnd() * w, y = rnd() * h, a = rnd() * 7; c.strokeStyle = `rgba(255,255,255,${.12 + rnd() * .2})`; c.lineWidth = .7;
    c.beginPath(); c.moveTo(x, y); for (let k = 0; k < 12; k++) { a += (rnd() - .5) * .8; x += Math.cos(a) * 3; y += Math.sin(a) * 3; c.lineTo(x, y); } c.stroke();
  }
  if (o.smear) { // a hand smear: a soft arc of streaks
    const [sx, sy, sr] = o.smear; c.save(); c.globalAlpha = .01;
    for (let k = 0; k < 40; k++) {
      c.strokeStyle = '#fff'; c.lineWidth = 2 + rnd() * 5; c.beginPath();
      const rr = sr * (.6 + rnd() * .5), a0 = -1.2 + rnd() * .3; c.arc(sx, sy, rr, a0, a0 + 1.2 + rnd() * .6); c.stroke();
    }
    c.restore();
  }
  return cv;
};

// ───────────────────────────── phosphor persistence ─────────────────────────────
// Brightness is the max over recent excitations, each decayed exponentially (tau = e-folding time, seconds).
// The bible quotes persistence as time to 10 % (cold ~60 ms, warm ~400 ms, scope ~1.5 s): K.PERSIST gives the taus. Static content stays at
// full level, new content lights at once, removed or moving content leaves a decaying trail.
K.PERSIST = { cold: .06 / 2.3, warm: .4 / 2.3, scope: 1.5 / 2.3 };
K.persist = function (ctx, draw, t, tau, o = {}) {
  const step = o.step || Math.min(.012, tau / 4), span = o.span || tau * 3.2, n = Math.ceil(span / step);
  ctx.save(); ctx.globalCompositeOperation = 'lighten';
  for (let k = n; k >= 0; k--) {
    const tt = t - k * step; if (tt < (o.t0 == null ? -1e9 : o.t0)) continue;
    ctx.globalAlpha = Math.exp(-k * step / tau); draw(ctx, tt);
  }
  ctx.restore();
};

// ───────────────────────────── vector beam (stroke overlay, §4) ─────────────────────────────
// Polylines drawn by the beam in order. Each stroke gets a write window; vertices get beads (dwell) at 1.6×,
// sharp corners (> 60°) get a 2–3 px overshoot hook; long strokes are dimmer (∝ 1/√length).
K.beamSchedule = function (strokes, t0, t1, o = {}) {
  const blank = o.blank || 0.15; // relative blanking between strokes
  let tot = 0; const lens = strokes.map(s => { let L = 0; for (let i = 1; i < s.length; i++) L += Math.hypot(s[i][0] - s[i - 1][0], s[i][1] - s[i - 1][1]); return Math.max(L, 1); });
  const w = lens.map(L => Math.sqrt(L) + blank * Math.sqrt(o.ref || 40)); w.forEach(v => tot += v);
  let acc = 0; return strokes.map((s, i) => { const a = t0 + (t1 - t0) * acc / tot; acc += w[i]; const b = t0 + (t1 - t0) * (acc - blank * Math.sqrt(o.ref || 40)) / tot; return { pts: s, len: lens[i], ta: a, tb: Math.max(b, a + 1e-3) }; });
};
function hookify(pts, hook) {
  // add overshoot hooks at corners sharper than 60°: the beam overshoots along its incoming direction and returns
  const out = [pts[0]];
  for (let i = 1; i < pts.length; i++) {
    out.push(pts[i]);
    if (i < pts.length - 1) {
      const a = pts[i - 1], p = pts[i], b = pts[i + 1];
      const d1 = [p[0] - a[0], p[1] - a[1]], d2 = [b[0] - p[0], b[1] - p[1]];
      const l1 = Math.hypot(...d1), l2 = Math.hypot(...d2); if (!l1 || !l2) continue;
      const cos = (d1[0] * d2[0] + d1[1] * d2[1]) / l1 / l2;
      if (cos < .5) { out.push([p[0] + d1[0] / l1 * hook, p[1] + d1[1] / l1 * hook]); out.push(p); }
    }
  }
  return out;
}
// Draw scheduled beam strokes at time t. level(age) → brightness 0..1 (persistence curve).
K.beamDraw = function (ctx, sched, t, o) {
  const color = o.color, width = o.width || 1.5, hook = o.hook == null ? 2.5 : o.hook, bead = o.bead || width * 1.3;
  const level = o.level || (age => 1), seg = o.seg || 3;
  ctx.save(); ctx.globalCompositeOperation = o.comp || 'lighten'; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  for (const S of sched) {
    if (t < S.ta) continue;
    const pts = o.hooks === false ? S.pts : hookify(S.pts, hook);
    const dim = o.lengthDim === false ? 1 : K.clamp(Math.sqrt((o.ref || 40) / S.len), .45, 1);
    // walk the polyline, emitting short segments with their own write time
    let L = 0; const total = pts.reduce((a, p, i) => i ? a + Math.hypot(p[0] - pts[i - 1][0], p[1] - pts[i - 1][1]) : 0, 0) || 1;
    for (let i = 1; i < pts.length; i++) {
      const p0 = pts[i - 1], p1 = pts[i], l = Math.hypot(p1[0] - p0[0], p1[1] - p0[1]), n = Math.max(1, Math.ceil(l / seg));
      for (let k = 0; k < n; k++) {
        const u0 = k / n, u1 = (k + 1) / n, tw = S.ta + (S.tb - S.ta) * (L + l * u1) / total;
        if (tw > t) { // partially written: stop at the beam's head
          const frac = K.clamp(((t - S.ta) / (S.tb - S.ta) * total - L - l * u0) / (l / n));
          if (frac > 0) {
            ctx.globalAlpha = dim * level(0) * (o.alpha || 1); ctx.strokeStyle = color; ctx.lineWidth = width;
            ctx.beginPath(); ctx.moveTo(p0[0] + (p1[0] - p0[0]) * u0, p0[1] + (p1[1] - p0[1]) * u0);
            const uh = u0 + (u1 - u0) * frac; ctx.lineTo(p0[0] + (p1[0] - p0[0]) * uh, p0[1] + (p1[1] - p0[1]) * uh); ctx.stroke();
            // the head: the beam itself, a hot spot
            ctx.globalAlpha = (o.alpha || 1); ctx.fillStyle = o.head || color; ctx.beginPath();
            ctx.arc(p0[0] + (p1[0] - p0[0]) * uh, p0[1] + (p1[1] - p0[1]) * uh, bead * 1.2, 0, 7); ctx.fill();
          }
          i = pts.length; break;
        }
        ctx.globalAlpha = dim * level(t - tw) * (o.alpha || 1); ctx.strokeStyle = color; ctx.lineWidth = width;
        ctx.beginPath(); ctx.moveTo(p0[0] + (p1[0] - p0[0]) * u0, p0[1] + (p1[1] - p0[1]) * u0);
        ctx.lineTo(p0[0] + (p1[0] - p0[0]) * u1, p0[1] + (p1[1] - p0[1]) * u1); ctx.stroke();
      }
      L += l;
    }
    // beads where the beam dwells: stroke ends and vertices (at 1.6× the stroke)
    if (o.beads !== false) {
      const sp = S.pts; let acc = 0;
      for (let i = 0; i < sp.length; i++) {
        if (i) acc += Math.hypot(sp[i][0] - sp[i - 1][0], sp[i][1] - sp[i - 1][1]);
        const tw = S.ta + (S.tb - S.ta) * acc / (S.len || 1); if (tw > t) break;
        ctx.globalAlpha = K.clamp(1.6 * dim * level(t - tw) * (o.alpha || 1) * (o.beadAlpha || .6));
        ctx.fillStyle = o.head || color; ctx.beginPath(); ctx.arc(sp[i][0], sp[i][1], bead, 0, 7); ctx.fill();
      }
    }
  }
  ctx.restore();
};

// ───────────────────────────── the tube: WebGL CRT post-process ─────────────────────────────
// Takes a flat 2D "emission" canvas (the tube face's picture, drawn in phosphor bloom colours) and renders the tube:
// barrel curvature, raster breathing, misconvergence (colour tubes), scanlines (raster tubes), hum bar, burn-in,
// flicker, bloom + halation ring, vignette, rounded glass mask, dark glass with grime lit by the screen, glare.
const VS = `#version 300 es
in vec2 p; out vec2 v; void main(){ v = p*0.5+0.5; gl_Position = vec4(p,0.,1.); }`;
const FS_TUBE = `#version 300 es
precision highp float; in vec2 v; out vec4 o;
uniform sampler2D src, burn; uniform vec2 res; uniform vec4 rect; uniform float k1, breathe, conv, scanN, scanDepth,
  scanPhase, humY, humDepth, gain, burnAmt, hasBurn, twitter;
vec3 S(vec2 s){ if(s.x<0.||s.y<0.||s.x>1.||s.y>1.) return vec3(0.); return texture(src, s).rgb; }
void main(){
  vec2 px = vec2(gl_FragCoord.x, res.y-gl_FragCoord.y);
  vec2 uv = (px-rect.xy)/rect.zw*2.-1.;
  float r2 = dot(uv,uv);
  vec2 d = uv*(1.+k1*r2)/(1.+k1);
  d /= (1.+breathe);
  vec2 s = d*0.5+0.5;
  vec3 c;
  if (conv>0.) {
    vec2 off = uv*conv/rect.zw*length(uv)*0.7071;
    c = vec3(S(s+off).r, S(s).g, S(s-off).b);
  } else c = S(s);
  if (hasBurn>0.) { vec3 b = (s.x<0.||s.y<0.||s.x>1.||s.y>1.)?vec3(0.):texture(burn, s).rgb; c += b*burnAmt*(1.-clamp(dot(c,vec3(.33)),0.,1.)); }
  float lum = clamp(dot(c, vec3(.3,.5,.2)), 0., 1.);
  if (scanN>0.) {
    float line = s.y*scanN + scanPhase;
    float f = 0.5+0.5*cos(6.2831853*line);           // 1 at the beam's centre, 0 between lines
    float dark = scanDepth*(1.-0.55*lum);             // bright lines swell and fill the gap
    c *= 1.-dark*(1.-f);
  }
  if (humDepth>0.) { float dy = fract(s.y-humY+0.5)-0.5; c *= 1.-humDepth*exp(-dy*dy/0.012); }
  if (s.x<0.||s.y<0.||s.x>1.||s.y>1.) c = vec3(0.);
  o = vec4(c*gain, 1.);
}`;
const FS_DOWN = `#version 300 es
precision highp float; in vec2 v; out vec4 o; uniform sampler2D t; uniform vec2 texel;
void main(){ vec3 c = texture(t, v+texel*vec2(-.5,-.5)).rgb+texture(t, v+texel*vec2(.5,-.5)).rgb
 +texture(t, v+texel*vec2(-.5,.5)).rgb+texture(t, v+texel*vec2(.5,.5)).rgb; o = vec4(c*.25,1.); }`;
const FS_BLUR = `#version 300 es
precision highp float; in vec2 v; out vec4 o; uniform sampler2D t; uniform vec2 dir;
void main(){ vec3 c = texture(t,v).rgb*0.2270270270;
 c += (texture(t,v+dir*1.3846153846).rgb+texture(t,v-dir*1.3846153846).rgb)*0.3162162162;
 c += (texture(t,v+dir*3.2307692308).rgb+texture(t,v-dir*3.2307692308).rgb)*0.0702702703;
 o = vec4(c,1.); }`;
const FS_COMP = `#version 300 es
precision highp float; in vec2 v; out vec4 o;
uniform sampler2D A, b1, b2, b3, b4, b5, b6, dust; uniform vec2 res; uniform vec4 rect; uniform float corner, vig, bloom,
  halo, exposure, glare, dustAmt, outside, hot, k1, hasDust, alphaMode; uniform vec3 glass, tint;
vec3 T(sampler2D t, vec2 p){ return texture(t, vec2(p.x, 1.-p.y)).rgb; }
float rbox(vec2 p, vec2 b, float r){ vec2 q = abs(p)-b+r; return length(max(q,0.))+min(max(q.x,q.y),0.)-r; }
void main(){
  vec2 px = vec2(gl_FragCoord.x, res.y-gl_FragCoord.y), p = px/res;
  vec2 uv = (px-rect.xy)/rect.zw*2.-1.;
  // the glass: a rounded rectangle, its edge softened by 1.5 px
  vec2 hs = rect.zw*0.5; float sd = rbox(px-(rect.xy+hs), hs, corner*rect.z);
  float inside = 1.-smoothstep(-1.5, 0.5, sd);
  vec3 e = T(A,p);
  vec3 bl = T(b1,p)*0.30 + T(b2,p)*0.28 + T(b3,p)*0.24 + T(b4,p)*0.18;
  vec3 ring = max(T(b6,p)*1.3-T(b4,p)*0.5, 0.);                   // halation: a faint ring, light scattered inside the faceplate
  float r2 = dot(uv,uv);
  float vg = 1.-vig*pow(clamp(r2/2.,0.,1.),1.1)*1.6;                 // 20–30 % toward the corners
  vec3 c = (e + bl*bloom + ring*halo)*max(vg,0.);
  // the unlit glass: dark, slightly green-grey, with grime and dust that the screen's own light picks out
  vec3 gl = glass*(1.+0.35*(1.-p.y)) ;
  if (hasDust>0.) { float d = texture(dust, vec2(p.x,p.y)).r; gl += d*dustAmt*(0.04+ min(bl.r+bl.g+bl.b, 1.2)*0.35); }
  // broad soft glare: the room's light on curved glass (upper left), stronger toward the bulge's crown
  vec2 g = uv-vec2(-0.45,-0.55); float gg = exp(-dot(g*vec2(1.,1.6),g*vec2(1.,1.6))*2.2);
  gl += vec3(glare)*gg*(0.6+0.4*(1.-r2/2.));
  c = c*tint + gl;
  float mx = max(c.r,max(c.g,c.b)); c += vec3(max(mx-0.75,0.)*hot);      // white-hot cores
  c = 1.-exp(-c*exposure);
  if (alphaMode>0.) { o = vec4(c, inside); return; }
  vec3 bg = outside>0.5 ? vec3(0.) : vec3(0.);
  float a = outside>0.5 ? 1. : inside;
  o = vec4(mix(bg, c, inside), a);
}`;
K.CRT = class {
  constructor(o) {
    this.o = Object.assign({
      W: 1920, H: 1080, rect: [240, 0, 1440, 1080], k1: .05, corner: .06, vig: .25, scanN: 0, scanDepth: .32,
      conv: 0, bloom: .9, halo: .12, exposure: 1.35, hot: .6, glare: .025, glass: [.020, .026, .026], tint: [1, 1, 1],
      outside: 'transparent', dustAmt: .5, dustSeed: 11, smear: null, srcW: null, srcH: null,
    }, o);
    const { W, H } = this.o;
    this.canvas = K.canvas(W, H);
    const gl = this.gl = this.canvas.getContext('webgl2', { premultipliedAlpha: false, alpha: true, preserveDrawingBuffer: true, antialias: false });
    gl.getExtension('EXT_color_buffer_float');
    const mk = (fs) => {
      const p = gl.createProgram();
      for (const [type, s] of [[gl.VERTEX_SHADER, VS], [gl.FRAGMENT_SHADER, fs]]) {
        const sh = gl.createShader(type); gl.shaderSource(sh, s); gl.compileShader(sh);
        if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(sh));
        gl.attachShader(p, sh);
      }
      gl.bindAttribLocation(p, 0, 'p'); gl.linkProgram(p); return p;
    };
    this.P = { tube: mk(FS_TUBE), down: mk(FS_DOWN), blur: mk(FS_BLUR), comp: mk(FS_COMP) };
    const vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, vb);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
    const tex = (w, h, f) => {
      const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
      if (f) gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA16F, w, h, 0, gl.RGBA, gl.HALF_FLOAT, null);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      return t;
    };
    const fbo = (w, h) => { const t = tex(w, h, true), f = gl.createFramebuffer(); gl.bindFramebuffer(gl.FRAMEBUFFER, f); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0); return { t, f, w, h }; };
    this.srcT = tex(); this.burnT = tex(); this.dustT = tex();
    this.A = fbo(W, H);
    this.lv = [2, 4, 8, 16, 32, 64].map(d => [fbo(Math.ceil(W / d), Math.ceil(H / d)), fbo(Math.ceil(W / d), Math.ceil(H / d))]);
    this.hasBurn = 0;
    const r = this.o.rect;
    const dust = K.dustCanvas(W, H, this.o.dustSeed, { n: Math.round(r[2] * r[3] / 5000), smear: this.o.smear });
    gl.bindTexture(gl.TEXTURE_2D, this.dustT); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, dust);
  }
  setBurn(cv) { const gl = this.gl; gl.bindTexture(gl.TEXTURE_2D, this.burnT); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, cv); this.hasBurn = 1; }
  _u(p, name, ...v) { const gl = this.gl, l = gl.getUniformLocation(p, name); if (!l) return; if (v.length === 1) gl.uniform1f(l, v[0]); else if (v.length === 2) gl.uniform2f(l, ...v); else if (v.length === 3) gl.uniform3f(l, ...v); else gl.uniform4f(l, ...v); }
  _t(p, name, unit, t) { const gl = this.gl; gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t); gl.uniform1i(gl.getUniformLocation(p, name), unit); }
  // f: per-frame { flicker, humY, humDepth, breathe, burnAmt, gain, bloom }
  render(src, f = {}) {
    const gl = this.gl, o = this.o, { W, H } = o;
    gl.bindTexture(gl.TEXTURE_2D, this.srcT); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, src);
    // 1. the tube
    let p = this.P.tube; gl.useProgram(p); gl.bindFramebuffer(gl.FRAMEBUFFER, this.A.f); gl.viewport(0, 0, W, H);
    this._t(p, 'src', 0, this.srcT); this._t(p, 'burn', 1, this.burnT);
    this._u(p, 'res', W, H); this._u(p, 'rect', ...o.rect); this._u(p, 'k1', f.k1 == null ? o.k1 : f.k1);
    this._u(p, 'breathe', f.breathe || 0); this._u(p, 'conv', o.conv); this._u(p, 'scanN', o.scanN);
    this._u(p, 'scanDepth', o.scanDepth); this._u(p, 'scanPhase', o.scanPhase || 0); this._u(p, 'humY', f.humY || 0);
    this._u(p, 'humDepth', f.humDepth || 0); this._u(p, 'gain', (f.gain == null ? 1 : f.gain) * (1 + (f.flicker || 0)));
    this._u(p, 'burnAmt', f.burnAmt || 0); this._u(p, 'hasBurn', this.hasBurn);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    // 2. bloom pyramid
    let prev = this.A, prevW = W, prevH = H;
    for (const [a, b] of this.lv) {
      p = this.P.down; gl.useProgram(p); gl.bindFramebuffer(gl.FRAMEBUFFER, a.f); gl.viewport(0, 0, a.w, a.h);
      this._t(p, 't', 0, prev.t); this._u(p, 'texel', 1 / prevW, 1 / prevH); gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      p = this.P.blur; gl.useProgram(p);
      for (let it = 0; it < 2; it++) {
        gl.bindFramebuffer(gl.FRAMEBUFFER, b.f); this._t(p, 't', 0, a.t); this._u(p, 'dir', 1 / a.w, 0); gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
        gl.bindFramebuffer(gl.FRAMEBUFFER, a.f); this._t(p, 't', 0, b.t); this._u(p, 'dir', 0, 1 / a.h); gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      }
      prev = a; prevW = a.w; prevH = a.h;
    }
    // 3. composite
    p = this.P.comp; gl.useProgram(p); gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, W, H);
    this._t(p, 'A', 0, this.A.t); this.lv.forEach(([a], i) => this._t(p, 'b' + (i + 1), i + 1, a.t)); this._t(p, 'dust', 5, this.dustT);
    this._u(p, 'res', W, H); this._u(p, 'rect', ...o.rect); this._u(p, 'corner', o.corner); this._u(p, 'vig', o.vig);
    this._u(p, 'bloom', f.bloom == null ? o.bloom : f.bloom); this._u(p, 'halo', o.halo); this._u(p, 'exposure', o.exposure);
    this._u(p, 'glare', o.glare); this._u(p, 'dustAmt', o.dustAmt); this._u(p, 'hasDust', o.dustAmt > 0 ? 1 : 0);
    this._u(p, 'outside', o.outside === 'black' ? 1 : 0); this._u(p, 'hot', o.hot); this._u(p, 'k1', o.k1);
    this._u(p, 'alphaMode', 0); this._u(p, 'glass', ...o.glass); this._u(p, 'tint', ...o.tint);
    gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    return this.canvas;
  }
};
// Hum bar position (0..1 from the top, rolling up) for a period in seconds.
K.hum = (t, period, phase = 0) => 1 - (((t + phase) / period) % 1);

// ───────────────────────────── split-flap (§4 artefacts) ─────────────────────────────
// Flap numerals: condensed square numerals with rounded corners, cream on black, split by the hinge. They are the
// State Capitals skeleton, condensed and heavier. One card; `tau` = seconds since this card's flip began (or null).
// The top half falls in 3 frames and the bottom lands with a 1-frame bounce.
K.flapFace = function (c, ch, x, y, w, h, o = {}) {
  const ink = o.ink || K.C.paper;
  c.save(); c.beginPath(); c.rect(x, y, w, h); c.clip();
  // the card: black with a faint vertical sheen and wear at the edges
  const g = c.createLinearGradient(x, y, x, y + h);
  g.addColorStop(0, o.cardTop || '#1b1b1d'); g.addColorStop(.5, o.cardMid || '#111113'); g.addColorStop(1, o.cardBot || '#18181a');
  c.fillStyle = g; c.fillRect(x, y, w, h);
  const m = h / 8.2, gw = K.capsLayout(ch).width;
  K.capsFill(c, ch, x + w / 2, y + (h - 6 * m) / 2, m, { align: 'center', color: ink, weight: 1.28, sx: (w * .72) / (gw * m) });
  c.restore();
};
K.flapCard = function (c, prev, next, x, y, w, h, tau, o = {}) {
  const hh = h / 2, F = 1 / K.FPS, gap = Math.max(2, h * .012);
  const face = (ch, sx, sy, sw, sh, tx, ty, th, flip) => { // draw part of a face into a destination strip
    const tmp = K.canvas(Math.ceil(w), Math.ceil(h)), tc = tmp.getContext('2d');
    K.flapFace(tc, ch, 0, 0, w, h, o);
    c.drawImage(tmp, 0, sy, w, sh, tx, ty, w, th);
  };
  const drawHalf = (ch, top, y0, th, shade) => {
    if (th <= .5) return;
    face(ch, 0, top ? 0 : hh, w, hh, x, y0, th);
    if (shade) { c.fillStyle = `rgba(0,0,0,${shade})`; c.fillRect(x, y0, w, th); }
  };
  // housing slot behind the card
  c.fillStyle = '#050505'; c.fillRect(x - 3, y - 3, w + 6, h + 6);
  if (tau == null || tau < 0 || tau >= 4 * F) {
    const ch = (tau == null || tau < 0) ? prev : next;
    drawHalf(ch, true, x === x ? y : y, hh, 0); drawHalf(ch, false, y + hh, hh, 0);
  } else {
    // static: new top revealed, old bottom until covered
    drawHalf(next, true, y, hh, .15); drawHalf(prev, false, y + hh, hh, 0);
    const ph = tau / (3 * F); // 0 → 1 over 3 frames, then the bounce frame
    if (ph < .5) { // old top half falling toward the viewer: foreshortened, darkening
      const k = Math.cos(ph * Math.PI); const th = hh * k;
      drawHalf(prev, true, y + hh - th, th, .5 * (1 - k));
    } else if (ph < 1) { // new bottom half's back swings down
      const k = Math.sin((ph - .5) * Math.PI); drawHalf(next, false, y + hh, hh * k, .45 * (1 - k));
    } else { // bounce: the flap lands, rebounds a hair
      drawHalf(next, false, y + hh, hh * .93, .12);
    }
  }
  // the hinge line and the two pins
  c.fillStyle = '#000'; c.fillRect(x, y + hh - gap / 2, w, gap);
  c.fillStyle = 'rgba(255,255,255,.06)'; c.fillRect(x, y + hh + gap / 2, w, 1);
  c.fillStyle = '#2a2a2c'; c.fillRect(x - 2, y + hh - gap, 5, gap * 2); c.fillRect(x + w - 3, y + hh - gap, 5, gap * 2);
};

// ───────────────────────────── drum counter (§4) ─────────────────────────────
// A drum shows white numerals on black; `v` is continuous (2.5 = halfway from 2 to 3). Foreshortened on the cylinder.
K.drum = function (c, x, y, w, h, v, o = {}) {
  c.save(); c.beginPath(); c.rect(x, y, w, h); c.clip();
  c.fillStyle = '#0b0b0c'; c.fillRect(x, y, w, h);
  const R = h * .78, step = Math.PI / 5.2, base = Math.floor(v);
  for (let d = base - 2; d <= base + 2; d++) {
    const a = (d - v) * step; if (Math.abs(a) > Math.PI / 2) continue;
    const cy = y + h / 2 + Math.sin(a) * R, sc = Math.cos(a);
    const m = h * .085 * (o.scale || 1);
    c.save(); c.translate(x + w / 2, cy); c.scale(1, sc);
    K.capsFill(c, String(((d % 10) + 10) % 10), 0, -3 * m, m, { align: 'center', color: o.ink || '#ECE8DC', weight: 1.1 });
    c.restore();
  }
  // cylinder shading: dark toward the top and bottom of the window, a soft specular band
  const g = c.createLinearGradient(x, y, x, y + h);
  g.addColorStop(0, 'rgba(0,0,0,.92)'); g.addColorStop(.28, 'rgba(0,0,0,.15)'); g.addColorStop(.5, 'rgba(255,255,255,.03)');
  g.addColorStop(.72, 'rgba(0,0,0,.15)'); g.addColorStop(1, 'rgba(0,0,0,.92)');
  c.fillStyle = g; c.fillRect(x, y, w, h);
  c.restore();
};
// Counter drum values with carries: n = continuous count, digits → array of drum positions (right to left rolls).
K.drumValues = function (n, digits) {
  const out = [], fl = Math.floor(n), fr = n - fl;
  for (let i = 0; i < digits; i++) {
    const p = Math.pow(10, i), base = Math.floor(fl / p) % 10;
    // a drum rolls only while every drum to its right is rolling from 9 to 0
    const lower = fl % p, roll = i === 0 ? fr : (lower === p - 1 ? fr : 0);
    out.unshift(base + roll);
  }
  return out;
};

// ───────────────────────────── legend lamps (§4) ─────────────────────────────
// A rectangular lens with its legend engraved and filled black (dark on the lit colour). An older, paint-filled
// legend ghosts underneath (`ghost`). level 0 = off, 1 = lit. colour 'red' | 'cold' | 'amber'.
K.LAMP_COL = { red: ['#E0412F', '#FF8A5C', '#3A1411'], cold: ['#CFEFEA', '#FFFFFF', '#1A2524'], amber: ['#F2A441', '#FFE0A8', '#34230F'] };
K.legendLamp = function (c, x, y, w, h, text, o = {}) {
  const col = K.LAMP_COL[o.color || 'red'], lv = K.clamp(o.level == null ? 1 : o.level);
  c.save();
  // bezel
  c.fillStyle = '#16181b'; c.beginPath(); c.roundRect(x - h * .08, y - h * .08, w + h * .16, h * 1.16, h * .1); c.fill();
  // lens: unlit glass colour, then the lit colour over it with a filament hot spot
  c.beginPath(); c.roundRect(x, y, w, h, h * .06); c.clip();
  c.fillStyle = col[2]; c.fillRect(x, y, w, h);
  if (lv > 0) {
    const g = c.createRadialGradient(x + w / 2, y + h / 2, 0, x + w / 2, y + h / 2, w * .62);
    g.addColorStop(0, K.mix(col[1], col[0], .35)); g.addColorStop(.45, col[0]); g.addColorStop(1, K.mix(col[0], '#000000', .35));
    c.globalAlpha = lv; c.fillStyle = g; c.fillRect(x, y, w, h); c.globalAlpha = 1;
  }
  // frosting: fine noise
  if (!K._frost) K._frost = K.noiseCanvas(256, 256, 91, { octaves: [[1, 1], [3, .6]] });
  c.globalAlpha = .08; c.globalCompositeOperation = 'overlay'; c.drawImage(K._frost, x, y, w, h); c.globalCompositeOperation = 'source-over'; c.globalAlpha = 1;
  const lines = text.split('\n');
  const widest = Math.max(...lines.map(L => K.capsLayout(L).width), 1);
  const m = o.module || Math.min(h / (lines.length * 8.5), w * .84 / widest);
  const lh = 6 * m, gap = 2.2 * m, tot = lines.length * lh + (lines.length - 1) * gap;
  if (o.ghost) { // older legend, paint-filled, mostly sanded off but still reading through
    const gl = o.ghost.split('\n'), gt = gl.length * lh + (gl.length - 1) * gap;
    gl.forEach((L, i) => K.capsFill(c, L, x + w / 2 + m * .6, y + (h - gt) / 2 + i * (lh + gap) + m * .5, m, { align: 'center', color: `rgba(0,0,0,${.16 + .1 * lv})` }));
  }
  lines.forEach((L, i) => K.capsFill(c, L, x + w / 2, y + (h - tot) / 2 + i * (lh + gap), m, { align: 'center', color: lv > .2 ? 'rgba(8,4,3,.88)' : 'rgba(0,0,0,.6)' }));
  // glass highlight: a thin cold line along the top edge
  c.fillStyle = 'rgba(255,255,255,.07)'; c.fillRect(x, y + 1, w, Math.max(1, h * .04));
  c.restore();
};
// A jewel lamp: a faceted cast-glass dome in a knurled bezel (VIEWING, the call lamp). level 0 = off, 1 = lit.
K.jewelLamp = function (c, cx, cy, r, o = {}) {
  const col = K.LAMP_COL[o.color || 'red'], lv = K.clamp(o.level || 0);
  c.save();
  c.fillStyle = '#141517'; c.beginPath(); c.arc(cx, cy, r * 1.32, 0, 7); c.fill();                   // bezel
  for (let i = 0; i < 48; i++) { const a = i / 48 * Math.PI * 2; c.fillStyle = i % 2 ? '#1e2023' : '#0c0d0e';
    c.beginPath(); c.moveTo(cx + Math.cos(a) * r * 1.12, cy + Math.sin(a) * r * 1.12); c.arc(cx, cy, r * 1.32, a, a + Math.PI / 48); c.closePath(); c.fill(); }
  c.beginPath(); c.arc(cx, cy, r, 0, 7); c.clip();
  c.fillStyle = col[2]; c.fillRect(cx - r, cy - r, 2 * r, 2 * r);
  if (lv > 0) {
    const g = c.createRadialGradient(cx - r * .15, cy - r * .1, 0, cx, cy, r);
    g.addColorStop(0, K.mix(col[1], '#ffffff', .3)); g.addColorStop(.35, col[1]); g.addColorStop(.75, col[0]); g.addColorStop(1, K.mix(col[0], '#000000', .45));
    c.globalAlpha = lv; c.fillStyle = g; c.fillRect(cx - r, cy - r, 2 * r, 2 * r); c.globalAlpha = 1;
  }
  // facets: a ring of cut triangles catching and losing the filament's light
  for (let i = 0; i < 12; i++) {
    const a = i / 12 * Math.PI * 2, b = a + Math.PI / 12;
    c.fillStyle = `rgba(${i % 2 ? '255,255,255' : '0,0,0'},${i % 2 ? .05 + .08 * lv : .18})`;
    c.beginPath(); c.moveTo(cx + Math.cos(a) * r * .45, cy + Math.sin(a) * r * .45);
    c.lineTo(cx + Math.cos(b) * r * 1.02, cy + Math.sin(b) * r * 1.02); c.lineTo(cx + Math.cos(a + Math.PI / 6) * r * .45, cy + Math.sin(a + Math.PI / 6) * r * .45); c.fill();
  }
  c.fillStyle = `rgba(255,255,255,${.1 + .12 * lv})`; c.beginPath(); c.ellipse(cx - r * .35, cy - r * .4, r * .22, r * .12, -.6, 0, 7); c.fill();
  c.restore();
};
// Legend-lamp switch: a 2-frame dip, then the new colour. Returns {color, level}.
K.lampSwitch = function (t, tSwitch, from, to) {
  const F = 1 / K.FPS;
  if (t < tSwitch) return { color: from, level: 1 };
  if (t < tSwitch + 2 * F) return { color: from, level: .15 };
  return { color: to, level: K.clamp((t - tSwitch - 2 * F) / F * .7 + .3) };
};
// Filament thermal lag: lit windows [[on, off], …] → level with a rise and a fall (seconds).
K.filament = function (t, wins, rise = .06, fall = .15) {
  let lv = 0;
  for (const [a, b] of wins) {
    if (t < a) continue;
    if (t < b) lv = Math.max(lv, 1 - Math.exp(-(t - a) / (rise / 3)));
    else { const peak = 1 - Math.exp(-(b - a) / (rise / 3)); lv = Math.max(lv, peak * Math.exp(-(t - b) / (fall / 3))); }
  }
  return lv;
};

// ───────────────────────────── moving-coil meter (§4, the prediction meter) ─────────────────────────────
// Needle ballistics: events [[t, target, kind]] kind 'rise' (0.3 s, 8 % overshoot) or 'drop' (0.15 s to the pin).
K.needle = function (t, events, v0 = 0) {
  let v = v0;
  for (const [te, target, kind] of events) {
    if (t < te) break;
    const from = v, d = target - from, dt = t - te;
    if (kind === 'drop') { const u = K.clamp(dt / .15); v = from + d * u * u; }
    else {
      const u = dt / .3;
      v = u < 1 ? from + d * 1.08 * Math.sin(u * Math.PI / 2)
        : target + d * .08 * Math.exp(-(u - 1) * 4) * Math.cos((u - 1) * Math.PI * 1.2);
    }
  }
  return v;
};
K.meter = function (c, x, y, w, h, value, o = {}) {
  c.save();
  // the cheek: a recess in grey enamel
  c.fillStyle = '#23272b'; c.beginPath(); c.roundRect(x, y, w, h, h * .05); c.fill();
  const ix = x + w * .05, iy = y + h * .06, iw = w * .9, ih = h * .88;
  c.beginPath(); c.roundRect(ix, iy, iw, ih, h * .03); c.clip();
  // frosted glass lit from behind by a cold lamp: brighter centre-bottom
  const g = c.createRadialGradient(ix + iw / 2, iy + ih * .8, 0, ix + iw / 2, iy + ih * .8, iw * .8);
  const bl = o.backlight == null ? 1 : o.backlight;
  g.addColorStop(0, K.mix('#DDF1EE', '#1a2222', 1 - bl)); g.addColorStop(.6, K.mix('#9CC9C6', '#141a1a', 1 - bl)); g.addColorStop(1, K.mix('#4E6A6A', '#0c1010', 1 - bl));
  c.fillStyle = g; c.fillRect(ix, iy, iw, ih);
  if (!K._frost) K._frost = K.noiseCanvas(256, 256, 91, { octaves: [[1, 1], [3, .6]] });
  c.globalAlpha = .12; c.globalCompositeOperation = 'multiply'; c.drawImage(K._frost, ix, iy, iw, ih); c.globalCompositeOperation = 'source-over'; c.globalAlpha = 1;
  // the scale: an arc from −50° to +50° about a pivot below the window
  const px = ix + iw / 2, py = iy + ih * 1.02, R = ih * .82, a0 = -Math.PI / 2 - .87, a1 = -Math.PI / 2 + .87;
  c.strokeStyle = '#141414'; c.lineWidth = Math.max(2, h * .012);
  c.beginPath(); c.arc(px, py, R, a0, a1); c.stroke();
  for (let i = 0; i <= 20; i++) {
    const a = a0 + (a1 - a0) * i / 20, L = i % 10 === 0 ? h * .09 : i % 2 === 0 ? h * .06 : h * .035;
    c.lineWidth = i % 2 === 0 ? Math.max(2, h * .012) : Math.max(1, h * .007);
    c.beginPath(); c.moveTo(px + Math.cos(a) * R, py + Math.sin(a) * R); c.lineTo(px + Math.cos(a) * (R - L), py + Math.sin(a) * (R - L)); c.stroke();
  }
  // the red band at the top of the scale (0.9–1.0): certainty
  c.strokeStyle = 'rgba(160,30,20,.75)'; c.lineWidth = h * .025; c.beginPath(); c.arc(px, py, R + h * .02, a0 + (a1 - a0) * .9, a1); c.stroke();
  const m = h * .016;
  [['0', 0], ['.5', .5], ['1.0', 1]].forEach(([str, f]) => {
    const a = a0 + (a1 - a0) * f, rr = R - h * .16;
    K.capsFill(c, str, px + Math.cos(a) * rr, py + Math.sin(a) * rr - 3 * m, m, { align: 'center', color: '#151515' });
  });
  K.capsFill(c, 'PREDICTION', px, iy + ih * .66, m * .9, { align: 'center', color: '#151515' });
  // the stop pin, lower left
  const ap = a0 - .06; c.fillStyle = '#222'; c.beginPath(); c.arc(px + Math.cos(ap) * (R - h * .07), py + Math.sin(ap) * (R - h * .07), h * .012, 0, 7); c.fill();
  // needle (black), with its counterweight hidden below the window
  const a = a0 - .06 + (a1 - a0 + .06) * K.clamp(value, -.03, 1.05) + (o.shiver || 0);
  c.strokeStyle = '#0a0a0a'; c.lineWidth = Math.max(2, h * .011); c.lineCap = 'round';
  c.beginPath(); c.moveTo(px + Math.cos(a) * h * .02, py + Math.sin(a) * h * .02); c.lineTo(px + Math.cos(a) * (R + h * .02), py + Math.sin(a) * (R + h * .02)); c.stroke();
  // the needle's shadow on the frosted glass (it sits a few mm in front)
  c.strokeStyle = 'rgba(0,0,0,.18)'; c.lineWidth = h * .02; c.beginPath(); c.moveTo(px + Math.cos(a) * h * .25 + h * .02, py + Math.sin(a) * h * .25 + h * .03); c.lineTo(px + Math.cos(a) * R + h * .02, py + Math.sin(a) * R + h * .03); c.stroke();
  c.restore();
  // glass bezel sheen
  c.save(); c.strokeStyle = 'rgba(255,255,255,.08)'; c.lineWidth = 2; c.beginPath(); c.roundRect(ix, iy, iw, ih, h * .03); c.stroke(); c.restore();
};

// ───────────────────────────── hands (§5, the only letters not on a grid) ─────────────────────────────
// Human marks: the State Capitals skeleton loosened by a hand (jitter, slant, pressure), drawn as pressure strokes.
// style: 'pencil' (Ida: small careful capitals leaning forward), 'grease' (archivist: blunt, waxy), 'ink' (doctor:
// hurried, slanted, joined).
K.HAND = {
  pencil: { slant: .16, jit: .09, w: .085, col: [58, 58, 64], grain: .55, facets: 5, join: false, spacing: 1.25 },
  grease: { slant: .08, jit: .16, w: .2, col: [30, 22, 20], grain: .35, facets: 4, join: false, spacing: 1.2 },
  ink: { slant: .42, jit: .2, w: .1, col: [26, 30, 52], grain: .1, facets: 4, join: true, spacing: .55 },
};
K.hand = function (c, text, x, y, size, style = 'pencil', o = {}) {
  const S = Object.assign({}, K.HAND[style], o), rnd = K.rng(S.seed || 5), m = size / 6;
  const L = K.capsLayout(text, S.facets, S.spacing);
  let ox = x; if (o.align === 'center') ox -= L.width * m * (S.sx || 1) / 2;
  if (!K._grain) K._grain = K.noiseCanvas(512, 512, 33, { octaves: [[1, 1], [2, .7], [6, .4]] });
  const tmp = K.canvas(c.canvas.width, c.canvas.height), t = tmp.getContext('2d');
  t.lineCap = 'round'; t.lineJoin = 'round';
  const [r, g, b] = S.col; let last = null;
  const drift = (i) => K.noise1(i * .7, (S.seed || 5) + 3) * m * .35;
  L.glyphs.forEach((gl, gi) => {
    const gy = drift(gi), gsc = 1 + (rnd() - .5) * .12, rot = (rnd() - .5) * .05;
    gl.g.strokes.forEach((st, si) => {
      // wobble the skeleton: a low-frequency hand tremor plus per-point jitter
      const pts = [];
      const dense = [];
      for (let i = 0; i < st.length; i++) {
        if (i) { const [ax, ay] = st[i - 1], [bx, by] = st[i]; const n = Math.max(1, Math.ceil(Math.hypot(bx - ax, by - ay) / .5)); for (let k = 1; k <= n; k++) dense.push([ax + (bx - ax) * k / n, ay + (by - ay) * k / n]); }
        else dense.push(st[0]);
      }
      dense.forEach(([u, v], i) => {
        const cu = gl.g.w / 2, cv = 3, du = u - cu, dv = v - cv;
        const ru = du * Math.cos(rot) - dv * Math.sin(rot), rv = du * Math.sin(rot) + dv * Math.cos(rot);
        const X = ox + (gl.x + cu + ru * gsc) * m * (S.sx || 1) + (6 - (cv + rv * gsc)) * m * S.slant + K.noise1(i * .35 + si * 9 + gi * 31, 71) * S.jit * m;
        const Y = y + (cv + rv * gsc) * m + gy + K.noise1(i * .35 + si * 9 + gi * 31, 72) * S.jit * m;
        pts.push([X, Y]);
      });
      if (S.join && last && si === 0) { // the pen doesn't lift between letters: a fast hairline
        t.strokeStyle = `rgba(${r},${g},${b},.55)`; t.lineWidth = S.w * m * 3.2; t.beginPath(); t.moveTo(last[0], last[1]);
        t.quadraticCurveTo((last[0] + pts[0][0]) / 2, Math.max(last[1], pts[0][1]) + m * .8, pts[0][0], pts[0][1]); t.stroke();
      }
      // pressure: heavier in the middle of a stroke, lifting at the ends (ink tapers; pencil less so)
      for (let i = 1; i < pts.length; i++) {
        const u = i / (pts.length - 1), pr = style === 'ink' ? Math.pow(Math.sin(Math.PI * Math.min(1, u * 1.1)), .6) * (1 - u * .5) + .15 : .75 + .25 * Math.sin(Math.PI * u);
        const skip = style === 'grease' && rnd() < .06; if (skip) continue;
        t.strokeStyle = `rgba(${r},${g},${b},${style === 'pencil' ? .75 + .2 * pr : .92})`;
        t.lineWidth = Math.max(.6, S.w * m * 6 * pr);
        t.beginPath(); t.moveTo(pts[i - 1][0], pts[i - 1][1]); t.lineTo(pts[i][0], pts[i][1]); t.stroke();
      }
      last = pts[pts.length - 1];
    });
    if (!S.join) last = null;
  });
  // grain: graphite and wax skip over the paper's tooth
  if (S.grain > 0) {
    t.globalCompositeOperation = 'destination-out'; t.globalAlpha = S.grain;
    const pat = t.createPattern(K._grain, 'repeat'); t.fillStyle = pat; t.fillRect(0, 0, tmp.width, tmp.height);
    t.globalAlpha = 1; t.globalCompositeOperation = 'source-over';
  }
  c.drawImage(tmp, 0, 0);
  return L.width * m;
};

// ───────────────────────────── the Script Terminal (§4): 48 × 12 Operator Mono on a two-layer tube ─────────────────────────────
// Cold layer (high beam voltage) and warm layer (low voltage): the Operator Rule colours every character by who
// answers for it. Cells are 9 × 14 dots; a dot is ux × uy px. The tube face is the 4:3 rect (picture space).
K.Term = class {
  constructor(o = {}) {
    this.o = Object.assign({ rect: [240, 0, 1440, 1080], cols: 48, rows: 12, ux: 3, uy: 5.5 }, o);
    const { rect, cols, rows, ux, uy } = this.o;
    this.cw = 9 * ux; this.ch = 14 * uy;
    this.x0 = Math.round(rect[0] + (rect[2] - cols * this.cw) / 2); this.y0 = Math.round(rect[1] + (rect[3] - rows * this.ch) / 2);
    this.cold = K.omAtlas(K.C.cold, ux, uy); this.warm = K.omAtlas(K.C.warm, ux, uy);
    this.tmp = K.canvas(cols * this.cw + 4, this.ch + 4);
  }
  xy(col, row) { return [this.x0 + col * this.cw, this.y0 + row * this.ch]; }
  text(c, layer, str, col, row, alpha = 1, dy = 0) {
    if (alpha <= 0) return; c.save(); c.globalAlpha *= alpha; const [x, y] = this.xy(col, row);
    K.omText(c, this[layer], str, x, y + dy); c.restore();
  }
  cursor(c, layer, col, row, alpha = 1) { this.text(c, layer, '█', col, row, alpha); }
  // inverse video: a block of `n` cells in the layer's colour with the glyphs knocked out
  inverse(c, layer, str, col, row, n = str.length, alpha = 1) {
    // inverse cells: a solid block (the beam dwells), with each glyph cut out a dot wider so the dark letters read
    const key = layer + 'Inv'; if (!this[key]) this[key] = K.omAtlas(layer === 'warm' ? K.C.warm : K.C.cold, this.o.ux, this.o.uy, { fill: 1.0 });
    const t = this.tmp.getContext('2d'); t.clearRect(0, 0, this.tmp.width, this.tmp.height);
    K.omText(t, this[key], '\u2588'.repeat(n), 0, 0);
    t.globalCompositeOperation = 'destination-out';
    for (const dx of [-this.o.ux * .6, 0, this.o.ux * .6]) K.omText(t, this[key], str.slice(0, n), dx, 0);
    t.globalCompositeOperation = 'source-over';
    const [x, y] = this.xy(col, row); c.save(); c.globalAlpha *= alpha; c.drawImage(this.tmp, x, y); c.restore();
  }
  // a CRT whose scanlines coincide with the dot rows
  crt(o = {}) {
    const { rect, uy } = this.o, n = rect[3] / uy, centre0 = (this.y0 - rect[1]) / uy + 2; // dash-row centres in line units
    return new K.CRT(Object.assign({ rect, k1: .05, corner: .07, vig: .26, scanN: n, scanDepth: .38,
      scanPhase: 1 - (centre0 % 1), bloom: 1.0, halo: .14, exposure: 1.3, hot: .7, glare: .03 }, o));
  }
};
// Word-wrap into rows of `cols` characters (words longer than a row are hard-broken).
K.wrap = function (text, cols) {
  const out = []; let line = '';
  for (const w of text.split(' ')) {
    if (!line.length) line = w;
    else if (line.length + 1 + w.length <= cols) line += ' ' + w;
    else { out.push(line); line = w; }
  }
  out.push(line); return out;
};

// ───────────────────────────── images embedded as data (untainted canvases) ─────────────────────────────
K.loadImage = src => new Promise((res, rej) => { const im = new Image(); im.onload = () => res(im); im.onerror = rej; im.src = src; });
K.loadScript = src => new Promise((res, rej) => { const s = document.createElement('script'); s.src = src; s.onload = res; s.onerror = () => rej(new Error('missing ' + src)); document.head.appendChild(s); });
// Assets for the stand-in pictures live in work/pilot/js_v3/src/*.js (generated from the plates; not committed).
K.ASSET_DIR = '../../../work/pilot/js_v3/src/';
K.asset = async name => { await K.loadScript(K.ASSET_DIR + name + '.js'); return K.loadImage(window.ASSET[name]); };

// Page scaffolding: one visible 1920×1080 canvas.
K.stage = function (bg = 'transparent') {
  document.documentElement.style.cssText = `margin:0;background:${bg};overflow:hidden`;
  document.body.style.cssText = `margin:0;background:${bg};overflow:hidden`;
  const cv = K.canvas(1920, 1080); cv.style.display = 'block'; document.body.appendChild(cv); return cv;
};
})();
