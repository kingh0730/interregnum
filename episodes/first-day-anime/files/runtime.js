// Deterministic virtual clock. Loaded FIRST, before any library.
// Rule: every visual is a PURE FUNCTION of (t, frame). Nothing reads the real clock.
(() => {
  'use strict';
  const q = new URLSearchParams(location.search);
  const FPS = 30;
  const SCALE = parseFloat(q.get('scale') || '1');
  const W = Math.round(1920 * SCALE), H = Math.round(1080 * SCALE);
  const SEED = 20261004;

  let vms = 0;
  let rafQueue = [];
  let rafId = 0;

  performance.now = () => vms;
  Date.now = () => 1700000000000 + vms;
  window.requestAnimationFrame = (cb) => { rafQueue.push({ id: ++rafId, cb }); return rafId; };
  window.cancelAnimationFrame = (id) => { rafQueue = rafQueue.filter((r) => r.id !== id); };

  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  // Math.random is reseeded per (sub)frame so libraries that call it (uuid etc.) cannot cause nondeterminism.
  const reseed = (n) => { Math.random = mulberry32((SEED ^ Math.imul(n | 0, 2654435761)) >>> 0); };
  reseed(0);

  // Pure hash: use THIS for particles/danmaku/jitter. hash01(a,b,c) -> [0,1)
  function hash01(a, b = 0, c = 0) {
    let h = (Math.imul(a | 0, 374761393) + Math.imul(b | 0, 668265263) + Math.imul(c | 0, 1274126177) + SEED) | 0;
    h = Math.imul(h ^ (h >>> 13), 1274126177);
    h = (h ^ (h >>> 16)) >>> 0;
    return h / 4294967296;
  }

  function setTime(tSeconds, seedKey) {
    vms = tSeconds * 1000;
    reseed(seedKey);
    for (const a of document.getAnimations()) { a.pause(); a.currentTime = vms; } // CSS/WAAPI animations
    const q2 = rafQueue; rafQueue = [];
    for (const r of q2) r.cb(vms);
  }

  const clamp = (x, a, b) => Math.min(b, Math.max(a, x));
  const smoothstep = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
  const lerp = (a, b, t) => a + (b - a) * t;
  const easeInOutCubic = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const easeOutExpo = (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t));

  window.RT = { FPS, W, H, SEED, SCALE, hash01, setTime, mulberry32, clamp, smoothstep, lerp, easeInOutCubic, easeOutExpo };
})();
