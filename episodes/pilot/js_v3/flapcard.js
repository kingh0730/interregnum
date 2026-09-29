// Split-flap renderer shared by j08_air_clock.html (the TO AIR board) and j_flaps.html (the desk repeater).
// Requires kit.js. Flap numerals: the State Capitals digit skeleton, condensed and heavier, cream #E8DDC4 on black
// (red #CC3A2B for the minutes drum's 00 flap). Each card is split by the hinge; a flip starts on the tick: the top
// half falls over frames 0–1, the new bottom lands on frame 2, frame 3 is the 1-frame bounce, frame 4 at rest.
(function () {
'use strict';
const FL = window.FL = {};
const F = 1 / 24;
const cache = new Map();
// A full card face (both halves), cached per char/ink/size.
FL.face = function (ch, w, h, ink, seed = 1) {
  const key = [ch, w, h, ink, seed].join('|'); if (cache.has(key)) return cache.get(key);
  const cv = K.canvas(Math.ceil(w), Math.ceil(h)), c = cv.getContext('2d'), rnd = K.rng(seed * 97 + ch.charCodeAt(0));
  const r = w * .035;
  c.beginPath(); c.roundRect(0, 0, w, h, r); c.clip();
  // the card: black lacquered sheet, a faint vertical sheen, worn paler at the edges where fingers and 41 years rub
  const g = c.createLinearGradient(0, 0, 0, h);
  g.addColorStop(0, '#1d1d20'); g.addColorStop(.47, '#0f0f11'); g.addColorStop(.53, '#141416'); g.addColorStop(1, '#1a1a1c');
  c.fillStyle = g; c.fillRect(0, 0, w, h);
  if (!FL._n) FL._n = K.noiseCanvas(256, 256, 55, { octaves: [[1, 1], [4, .8], [16, .5]] });
  c.globalAlpha = .1; c.globalCompositeOperation = 'overlay'; c.drawImage(FL._n, rnd() * -60, rnd() * -60, 400, 400);
  c.globalCompositeOperation = 'source-over'; c.globalAlpha = 1;
  c.strokeStyle = 'rgba(200,200,190,.10)'; c.lineWidth = Math.max(1, w * .012); c.beginPath(); c.roundRect(1, 1, w - 2, h - 2, r); c.stroke();
  // the numeral (printed): condensed square skeleton, heavy
  const m = h / 8.4, gw = K.capsLayout(ch).width, sx = Math.min(1, (w * .6) / (gw * m * 1.0));
  const ink2 = K.canvas(cv.width, cv.height), ic = ink2.getContext('2d');
  K.capsFill(ic, ch, w / 2, (h - 6 * m) / 2, m, { align: 'center', color: ink, weight: 1.34, sx });
  // printing wear: tiny pits in the ink, and a scuffed band where the flaps rub
  ic.globalCompositeOperation = 'destination-out';
  for (let i = 0; i < 40; i++) { ic.globalAlpha = .3 + rnd() * .5; ic.beginPath(); ic.arc(rnd() * w, rnd() * h, .4 + rnd() * 1.3 * (w / 120), 0, 7); ic.fill(); }
  ic.globalAlpha = .18; ic.fillRect(0, h * .47, w, h * .06);
  // silk-screen edge: the ink breaks up a little along its edges and where the grain of the card is open
  if (!FL._g) FL._g = K.noiseCanvas(256, 256, 77, { octaves: [[1, 1], [2, .6]] });
  ic.globalAlpha = .16; ic.drawImage(FL._g, rnd() * -80, rnd() * -80, w * 1.6, h * 1.6); ic.globalAlpha = 1;
  ic.globalCompositeOperation = 'source-over';
  c.filter = 'blur(0.5px)'; c.drawImage(ink2, 0, 0); c.filter = 'none';
  cache.set(key, cv); return cv;
};
// Draw one half of a face into [x, y0 .. y0+th] (th may be scaled for foreshortening).
function half(c, face, top, x, y0, w, th, shade) {
  if (th < .5) return;
  const hh = face.height / 2;
  c.drawImage(face, 0, top ? 0 : hh, face.width, hh, x, y0, w, th);
  if (shade) { c.fillStyle = shade > 0 ? `rgba(0,0,0,${shade})` : `rgba(255,250,235,${-shade})`; c.fillRect(x, y0, w, th); }
}
// One card. tau = seconds since its flip began (null or outside 0..4F → at rest on `next` if tau ≥ 0, else `prev`).
FL.card = function (c, prev, next, x, y, w, h, tau, o = {}) {
  const inkP = o.inkPrev || K.C.paper, inkN = o.inkNext || inkP, hh = h / 2, gap = Math.max(1.5, h * .014);
  const fP = FL.face(prev, w, h, inkP, o.seed), fN = FL.face(next, w, h, inkN, o.seed);
  // the slot behind the card
  c.fillStyle = '#040404'; c.fillRect(x - w * .03, y - h * .025, w * 1.06, h * 1.05);
  const k = tau == null ? -1 : Math.floor(tau / F + 1e-6);
  if (k < 0 || k >= 4) {
    const f = k < 0 ? fP : fN; half(c, f, true, x, y, w, hh, 0); half(c, f, false, x, y + hh, w, hh, 0);
  } else {
    half(c, fN, true, x, y, w, hh, .22);            // the next top, revealed behind the falling flap
    if (k === 0) {                                   // old top falling: 60° toward the lens
      half(c, fP, false, x, y + hh, w, hh, .25);     // old bottom, in the falling flap's shadow
      const th = hh * Math.cos(Math.PI / 3); half(c, fP, true, x, y + hh - th, w, th, -.06);
      c.fillStyle = 'rgba(0,0,0,.35)'; c.fillRect(x, y + hh - th - 1, w, 1.5);
    } else if (k === 1) {                            // past vertical: the new bottom's back swings down (120°)
      half(c, fP, false, x, y + hh, w, hh, 0);
      half(c, fN, false, x, y + hh, w, hh * Math.cos(Math.PI / 3), .3);
    } else if (k === 2) {                            // lands
      half(c, fN, false, x, y + hh, w, hh, .05);
    } else {                                         // 1-frame bounce: it lifts a hair off the stop
      c.fillStyle = '#060606'; c.fillRect(x, y + hh, w, hh);
      half(c, fN, false, x, y + hh, w, hh * .94, .1);
    }
  }
  // the hinge: a dark split and the two pivot pins in the frame
  c.fillStyle = '#000'; c.fillRect(x, y + hh - gap / 2, w, gap);
  c.fillStyle = 'rgba(255,255,255,.05)'; c.fillRect(x, y + hh + gap / 2, w, 1);
  c.fillStyle = '#3a3935'; const pw = Math.max(3, w * .035);
  c.fillRect(x - pw * .8, y + hh - gap * 1.6, pw, gap * 3.2); c.fillRect(x + w - pw * .2, y + hh - gap * 1.6, pw, gap * 3.2);
};
// A countdown: value in seconds at time t, and each flip's start time. from = seconds at rest before `first`.
FL.countdown = function (from, to, first) {
  const flips = []; for (let v = from, tt = first; v > to; v--, tt += 1) flips.push(tt);
  return {
    at(t) { let v = from, last = null, prevV = from; for (const ft of flips) { if (t >= ft) { prevV = v; v--; last = ft; } } return { v, prevV, tau: last == null ? null : t - last }; },
    flips,
  };
};
FL.mmss = s => [String(Math.floor(s / 60)).padStart(2, '0'), String(s % 60).padStart(2, '0')];
// A four-card MM:SS unit: minutes pair and seconds pair flip as units (a drum each), colon painted between.
// Returns nothing; draws at (x, y) with card size w × h, `gap` between cards in a pair, `mid` between pairs.
FL.unit = function (c, cd, t, x, y, w, h, gap, mid, o = {}) {
  const st = cd.at(t), [m1, s1] = FL.mmss(st.prevV), [m2, s2] = FL.mmss(st.v);
  const flipping = st.tau != null && st.tau < 4 * F;
  const red = o.red00 ? K.C.redInk : null, cream = K.C.paper;
  const inkM = mm => (red && mm === '00') ? red : cream;
  const xs = [x, x + w + gap, x + 2 * w + gap + mid, x + 3 * w + 2 * gap + mid];
  const pairs = [[m1, m2, 0], [s1, s2, 2]];
  for (const [a, b, i0] of pairs) {
    const changes = a !== b;
    for (let j = 0; j < 2; j++) {
      const tau = flipping && changes ? st.tau : (st.tau == null ? null : 99);
      const prev = flipping && changes ? a[j] : b[j];
      const ip = i0 === 0 ? inkM(flipping && changes ? a : b) : cream, inN = i0 === 0 ? inkM(b) : cream;
      FL.card(c, prev, b[j], xs[i0 + j], y, w, h, tau, { inkPrev: ip, inkNext: inN, seed: i0 + j + 1 });
    }
  }
  // the painted colon on the frame: two cream squares, brushed, slightly worn
  const cx = x + 2 * w + gap + mid / 2, d = Math.max(4, w * .09);
  c.fillStyle = 'rgba(232,221,196,.85)';
  c.fillRect(cx - d / 2, y + h * .32 - d / 2, d, d); c.fillRect(cx - d / 2, y + h * .68 - d / 2, d, d);
  return xs;
};
})();
