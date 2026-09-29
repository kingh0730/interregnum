// The Proof's calibration mesh (J16 v3), shared by j16_proof_overlay.html (shot 04) and j03_proof.html (shot 06).
// Picture space is 1440 × 1080 (the 4:3 broadcast picture). ANCHORS are hand-placed once on the picture; the ~120
// landmarks are generated from them (brows 10, eyes 16, nose 9, mouth 20, jaw 17, ears 8, hairline 10, beard 12,
// cheeks 8, forehead 10, + the mole) and Delaunay-triangulated. Placed on work/pilot/keys_v3/k02_father_cu.png (4:3
// centre crop): the opening take ends on k02, so f04_frozen ≈ k02. If f04 differs, move the anchors and re-run.
(function () {
'use strict';
// anchors in the ORIGINAL k02 pixels (1672 × 941); converted to picture space below
const SRC = { w: 1672, h: 941 };
// Re-fitted 2026-09-29 to the steel-engraved k02 (the smooth k02 is k02_father_cu_smooth.png): the engraved face sits
// ~10 px lower and 4.4 % larger (eyes 732/945 at y 382 vs 728/932 at 372), so the smooth-k02 anchors were mapped by
// that similarity and the chin and mole placed by eye. Smooth-k02 anchors: eyeL 728,372 eyeR 932,372 brows 712/948,312
// noseTop 830,380 noseTip 828,468 mouth 822,560 chin 822,800 ears 535,480/1112,478 hair 830,175 mole 1018,440
// cheeks 640/1010,470 face 572/1085,420.
const A0 = {
  eyeL: [732, 382], eyeR: [945, 382], browL: [715, 319], browR: [962, 319], noseTop: [838, 390], noseTip: [836, 482],
  mouth: [830, 578], chin: [830, 820], earL: [531, 495], earR: [1133, 493], hair: [838, 176], mole: [1023, 453],
  cheekL: [640, 484], cheekR: [1026, 484], faceL: [569, 432], faceR: [1105, 432],
};
const sc = 1080 / SRC.h, ox = (SRC.w - SRC.h * 4 / 3) / 2;
const P = ([x, y]) => [(x - ox) * sc, y * sc];
const A = {}; for (const k in A0) A[k] = P(A0[k]);
const arc = (cx, cy, rx, ry, a0, a1, n) => Array.from({ length: n }, (_, i) => { const a = a0 + (a1 - a0) * i / (n - 1); return [cx + Math.cos(a) * rx, cy + Math.sin(a) * ry]; });
const ring = (cx, cy, rx, ry, n, rot = 0) => Array.from({ length: n }, (_, i) => { const a = rot + i / n * Math.PI * 2; return [cx + Math.cos(a) * rx, cy + Math.sin(a) * ry]; });
const L = [], tag = (arr, part) => arr.forEach(p => L.push({ x: p[0], y: p[1], part }));
const u = sc; // one original pixel in picture px
tag(arc(A.browL[0], A.browL[1] + 18 * u, 70 * u, 22 * u, Math.PI * 1.1, Math.PI * 1.9, 5), 'brow');
tag(arc(A.browR[0], A.browR[1] + 18 * u, 70 * u, 22 * u, Math.PI * 1.1, Math.PI * 1.9, 5), 'brow');
tag(ring(A.eyeL[0], A.eyeL[1], 44 * u, 15 * u, 8), 'eye');
tag(ring(A.eyeR[0], A.eyeR[1], 44 * u, 15 * u, 8), 'eye');
tag([A.noseTop, [A.noseTop[0], (A.noseTop[1] + A.noseTip[1]) / 2], A.noseTip,
  [A.noseTip[0] - 38 * u, A.noseTip[1] - 4 * u], [A.noseTip[0] + 38 * u, A.noseTip[1] - 4 * u],
  [A.noseTip[0] - 22 * u, A.noseTip[1] + 14 * u], [A.noseTip[0] + 22 * u, A.noseTip[1] + 14 * u],
  [A.noseTip[0] - 30 * u, A.noseTip[1] - 40 * u], [A.noseTip[0] + 30 * u, A.noseTip[1] - 40 * u]], 'nose');
tag(ring(A.mouth[0], A.mouth[1], 78 * u, 24 * u, 12), 'mouth');
tag(ring(A.mouth[0], A.mouth[1], 52 * u, 9 * u, 8), 'mouth');
tag(arc(A.mouth[0], A.faceL[1] + 10 * u, (A.faceR[0] - A.faceL[0]) / 2 + 8 * u, A.chin[1] - A.faceL[1] - 10 * u, Math.PI * 1.02, -0.02, 17).map(([x, y]) => [x, y]), 'jaw');
tag(arc(A.earL[0], A.earL[1], 24 * u, 62 * u, Math.PI * .6, Math.PI * 1.4, 4), 'ear');
tag(arc(A.earR[0], A.earR[1], 24 * u, 62 * u, -Math.PI * .4, Math.PI * .4, 4), 'earR');
tag(arc(A.hair[0], A.hair[1] + 150 * u, 245 * u, 150 * u, Math.PI * 1.08, Math.PI * 1.92, 10), 'hair');
tag(arc(A.mouth[0], A.mouth[1] - 20 * u, 215 * u, 245 * u, Math.PI * .08, Math.PI * .92, 12), 'beard');
tag([[A.cheekL[0], A.cheekL[1]], [A.cheekL[0] + 30 * u, A.cheekL[1] + 55 * u], [A.cheekL[0] - 10 * u, A.cheekL[1] - 45 * u], [A.cheekL[0] + 45 * u, A.cheekL[1] - 20 * u],
  [A.cheekR[0], A.cheekR[1] + 30 * u], [A.cheekR[0] - 30 * u, A.cheekR[1] + 60 * u], [A.cheekR[0] + 20 * u, A.cheekR[1] - 45 * u], [A.cheekR[0] - 45 * u, A.cheekR[1] - 20 * u]], 'cheek');
for (let i = 0; i < 10; i++) tag([[A.hair[0] - 180 * u + (i % 5) * 90 * u, A.hair[1] + 60 * u + Math.floor(i / 5) * 55 * u]], 'forehead');
tag([A.mole], 'mole');

// Delaunay (Bowyer–Watson)
function delaunay(pts) {
  const big = [[-1e5, -1e5], [1e5, -1e5], [0, 1e5]], all = pts.concat(big), n = pts.length;
  let tris = [[n, n + 1, n + 2]];
  const circ = (t) => {
    const [a, b, c] = t.map(i => all[i]);
    const d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]));
    const ux = ((a[0] ** 2 + a[1] ** 2) * (b[1] - c[1]) + (b[0] ** 2 + b[1] ** 2) * (c[1] - a[1]) + (c[0] ** 2 + c[1] ** 2) * (a[1] - b[1])) / d;
    const uy = ((a[0] ** 2 + a[1] ** 2) * (c[0] - b[0]) + (b[0] ** 2 + b[1] ** 2) * (a[0] - c[0]) + (c[0] ** 2 + c[1] ** 2) * (b[0] - a[0])) / d;
    return [ux, uy, (a[0] - ux) ** 2 + (a[1] - uy) ** 2];
  };
  pts.forEach((p, i) => {
    const bad = tris.filter(t => { const [x, y, r2] = circ(t); return (p[0] - x) ** 2 + (p[1] - y) ** 2 < r2; });
    const edges = [];
    bad.forEach(t => [[t[0], t[1]], [t[1], t[2]], [t[2], t[0]]].forEach(e => {
      const k = edges.findIndex(f => (f[0] === e[1] && f[1] === e[0]) || (f[0] === e[0] && f[1] === e[1]));
      if (k >= 0) edges.splice(k, 1); else edges.push(e);
    }));
    tris = tris.filter(t => !bad.includes(t)).concat(edges.map(e => [e[0], e[1], i]));
  });
  return tris.filter(t => t.every(i => i < n));
}
const pts = L.map(p => [p.x, p.y]);
const TRIS = delaunay(pts);
// unique edges, dropping long skinny ones across the outside of the face
const E = new Map();
TRIS.forEach(t => [[t[0], t[1]], [t[1], t[2]], [t[2], t[0]]].forEach(([a, b]) => { const k = a < b ? a + ',' + b : b + ',' + a; E.set(k, [Math.min(a, b), Math.max(a, b)]); }));
let EDGES = [...E.values()].filter(([a, b]) => Math.hypot(pts[a][0] - pts[b][0], pts[a][1] - pts[b][1]) < 190);
// beam order for the beads: a nearest-neighbour path across the face from the upper left
const order = [], used = new Set(); let cur = pts.reduce((bi, p, i) => (p[0] + p[1] < pts[bi][0] + pts[bi][1] ? i : bi), 0);
while (order.length < pts.length) { order.push(cur); used.add(cur); let best = -1, bd = 1e9; pts.forEach((p, i) => { if (used.has(i)) return; const d = Math.hypot(p[0] - pts[cur][0], p[1] - pts[cur][1]); if (d < bd) { bd = d; best = i; } }); if (best < 0) break; cur = best; }
// stroke order: edges sorted by the beam order of their first-visited vertex, walked greedily
const rank = new Map(order.map((i, k) => [i, k]));
EDGES.sort((e, f) => Math.min(rank.get(e[0]), rank.get(e[1])) - Math.min(rank.get(f[0]), rank.get(f[1])) || Math.max(rank.get(e[0]), rank.get(e[1])) - Math.max(rank.get(f[0]), rank.get(f[1])));
EDGES = EDGES.map(([a, b]) => rank.get(a) <= rank.get(b) ? [a, b] : [b, a]);
const EAR = { x: A.earR[0], y: A.earR[1], w: 88 * u, h: 170 * u }; // the ghost ear's region (image right)
window.MESH = { A, L, pts, TRIS, EDGES, order, EAR, SRC, placedOn: 'work/pilot/keys_v3/k02_father_cu.png (4:3 centre crop)' };
})();
