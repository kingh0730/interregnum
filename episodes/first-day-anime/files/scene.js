// REFERENCE SCENE showing the contract Codex must follow. Replace/extend per shot; do not weaken the rules.
// Contract: window.SCENE = { canvas, init(), render(t, frame, k), shotRange(t), subframesFor(frame), shutter }
// render() must be a PURE FUNCTION of t. No state carried between frames, no real clock, no Math.random for visuals.
(() => {
  'use strict';
  const { W: _W, hash01, clamp, smoothstep, easeOutExpo } = window.RT;
  const SHOTS = [ // [start, end) in seconds; fill with the full S01..S44 list from the plan
    [0.00, 1.05], [1.05, 2.84], [2.84, 4.23], /* ... */ [11.27, 11.92], [11.92, 12.62], [12.62, 13.63],
  ];
  const FONTS = [
    ['NotoSerifSC-Black', '/fonts/NotoSerifSC-Black.otf'],
    ['NotoSerifSC-SemiBold', '/fonts/NotoSerifSC-SemiBold.otf'],
    ['NotoSansSC-Bold', '/fonts/NotoSansSC-Bold.otf'],
    ['Lora-SemiBold', '/fonts/Lora-SemiBold.ttf'],
  ];
  const DANMAKU = [ // authored list; lanes are assigned deterministically in init()
    { text: '来了来了', t0: 12.7, speed: 420, color: '#FAF9F5' },
    { text: '高能预警', t0: 13.0, speed: 380, color: '#FAF9F5' },
  ];

  let W, H, ctx, lanes = [];
  const S = {
    canvas: document.createElement('canvas'),
    shutter: 0.5,
    shotRange(t) { for (const s of SHOTS) if (t >= s[0] && t < s[1]) return s; return [t, t + 1 / 30]; },
    subframesFor(frame) { const t = frame / 30; return (t >= 11.27 && t < 11.92) ? 1 : 8; },

    async init({ W: w, H: h }) {
      W = w; H = h; S.canvas.width = W; S.canvas.height = H;
      ctx = S.canvas.getContext('2d', { alpha: false });
      for (const [name, url] of FONTS) { // fail loudly: missing font == failed boot, never a silent fallback
        const ff = new FontFace(name, `url(${url})`); await ff.load(); document.fonts.add(ff);
        if (!document.fonts.check(`40px "${name}"`)) throw new Error('font not usable: ' + name);
      }
      // deterministic danmaku lane assignment (greedy, no overlap)
      const lh = Math.round(H * 0.05); const free = Array(Math.floor((H * 0.8) / lh)).fill(-1);
      ctx.font = `700 ${Math.round(H * 0.04)}px "NotoSansSC-Bold"`;
      DANMAKU.forEach((d, i) => {
        d.w = ctx.measureText(d.text).width;
        let lane = free.findIndex((endT) => endT <= d.t0);
        if (lane < 0) lane = Math.floor(hash01(i) * free.length);
        free[lane] = d.t0 + (W + d.w) / d.speed * 0.6; d.lane = lane; d.y = H * 0.1 + lane * lh + lh * 0.8;
      });
    },

    render(t, frame) {
      const sc = H / 1080;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.fillStyle = '#141413'; ctx.fillRect(0, 0, W, H);
      ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic'; ctx.lineJoin = 'round';

      if (t >= 11.27 && t < 11.92) { // S13 typewriter: exactly one character per frame
        const s = '你好，我是 Opus 5.5。'; const n = Math.min(s.length, Math.floor((t - 11.27) * 30));
        const caret = (Math.floor(t * 30 / 8) % 2 === 0) ? '▌' : '';
        ctx.font = `600 ${64 * sc}px "NotoSerifSC-SemiBold"`; ctx.fillStyle = '#FAF9F5';
        ctx.fillText(s.slice(0, n) + caret, W / 2, H / 2);
      } else if (t >= 11.92 && t < 12.62) { // S14 title slam
        const u = (t - 11.92) / 0.7;
        const shake = u < 0.13 ? (hash01(frame, 1) - 0.5) * 24 * sc : 0;
        ctx.fillStyle = (frame - Math.round(11.92 * 30) < 2) ? '#FAF9F5' : '#D97757'; ctx.fillRect(0, 0, W, H);
        const scale = 1 + 0.35 * (1 - easeOutExpo(clamp(u * 3, 0, 1)));
        ctx.save(); ctx.translate(W / 2 + shake, H / 2 + shake); ctx.scale(scale, scale);
        ctx.font = `600 ${H * 0.38}px "Lora-SemiBold"`; ctx.fillStyle = '#FAF9F5'; ctx.fillText('Opus 5.5', 0, H * 0.12);
        ctx.restore();
      }
      // Danmaku: x is a closed-form function of t (never incremented per frame)
      ctx.font = `700 ${Math.round(H * 0.04)}px "NotoSansSC-Bold"`; ctx.textAlign = 'left';
      for (const d of DANMAKU) {
        const x = W - (t - d.t0) * d.speed * sc; if (t < d.t0 || x < -d.w) continue;
        ctx.globalAlpha = 0.85; ctx.lineWidth = 3 * sc; ctx.strokeStyle = '#141413'; ctx.strokeText(d.text, x, d.y);
        ctx.fillStyle = d.color; ctx.fillText(d.text, x, d.y); ctx.globalAlpha = 1;
      }
    },
  };
  window.SCENE = S;
})();
