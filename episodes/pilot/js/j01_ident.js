// J01 ident: THE EVENING ADDRESS. Variants: full (shot 01, 5.0 s), fast (shot 28, 3.0 s), alt (shot 46: fast, +1.0 s).
(function () {
  const { C, F } = K;
  const V = new URLSearchParams(location.search).get('variant') || window.VARIANT || 'full';
  const T = V === 'full'
    ? { circle: [0.5, 1.4], flame: [1.0, 1.8], base: [1.4, 1.9], glow: [1.8, 2.6], title: [2.2, 3.0], time: [2.6, 3.2], glowPeak: 0.35, glowHold: 0.12, black: -1 }
    : { circle: [0.2, 0.7], flame: [0.5, 1.0], base: [0.7, 1.0], glow: [1.0, 1.4], title: [1.0, 1.5], time: [1.2, 1.6], glowPeak: 0.175, glowHold: 0.06, black: 0.3 };
  const OFFSET = V === 'alt' ? 1.0 : 0;

  const ctx = K.canvas(true);
  const em = K.off(1920, 1080), ec = em.getContext('2d');

  function bg(c) {
    const g = c.createRadialGradient(960, 470, 0, 960, 470, 1150);
    g.addColorStop(0, '#123A5E'); g.addColorStop(1, '#07111F');
    c.fillStyle = g; c.fillRect(0, 0, 1920, 1080);
  }

  window.renderFrame = (tIn) => {
    const t = tIn - OFFSET;
    ctx.globalAlpha = 1; ctx.filter = 'none';
    if (t < T.black) { ctx.fillStyle = '#000'; ctx.fillRect(0, 0, 1920, 1080); return; }
    bg(ctx);

    const circle = K.easeInOutCubic(K.seg(t, ...T.circle));
    const fu = K.seg(t, ...T.flame);
    let flame = fu <= 0 ? 0 : K.easeOutBack6(fu);
    if (t > T.flame[1]) flame = 1 + 0.02 * Math.sin(2 * Math.PI * 0.5 * (t - T.flame[1]));
    const base = K.easeOutCubic(K.seg(t, ...T.base));

    ec.clearRect(0, 0, 1920, 1080);
    K.emblem(ec, 960, 450, 1, { circle, flame, base });

    // glow: one pulse 0 → peak → hold
    let glowA = 0;
    if (t >= T.glow[0]) {
      const u = K.seg(t, ...T.glow);
      glowA = u < 0.35 ? K.lerp(0, T.glowPeak, K.easeOutCubic(u / 0.35)) : K.lerp(T.glowPeak, T.glowHold, K.easeInOutSine((u - 0.35) / 0.65));
    }
    if (glowA > 0) {
      ctx.save(); ctx.filter = 'blur(40px)'; ctx.globalAlpha = glowA; ctx.globalCompositeOperation = 'lighter';
      ctx.drawImage(em, 0, 0); ctx.drawImage(em, 0, 0); ctx.restore();
    }
    ctx.drawImage(em, 0, 0);

    const ta = K.easeInOutCubic(K.seg(t, ...T.title));
    if (ta > 0) K.text(ctx, 'THE EVENING ADDRESS', 960, 700 + 12 * (1 - ta), { font: F.cond, weight: 'bold', size: 64, track: 0.35, color: C.cream, alpha: ta, align: 'center', baseline: 'middle' });
    const tm = K.easeInOutCubic(K.seg(t, ...T.time));
    if (tm > 0) K.text(ctx, '21:00', 960, 760, { font: F.alt, weight: 'bold', size: 34, track: 0.12, color: C.cyan, alpha: 0.7 * tm, align: 'center', baseline: 'middle' });
  };
})();
