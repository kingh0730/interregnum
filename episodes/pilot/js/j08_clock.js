// J08 clock (parameterized). Shot 14: defaults (time=20:56, toAir=240, alarm=0), 2.0 s.
// Shot 22: a page that sets window.J08_TIME='20:59', J08_TOAIR=60, J08_ALARM='1' (or ?time=20:59&toAir=60&alarm=1)
const { C, F } = K;
const q = new URLSearchParams(location.search);
const P = { time: q.get('time') || window.J08_TIME || '20:56', toAir: Number(q.get('toAir') || window.J08_TOAIR || 240), alarm: (q.get('alarm') || window.J08_ALARM || '0') === '1' };
const ctx = K.canvas(true);
const BIG = `bold 300px ${F.cond}`, SMALL = `bold 48px ${F.alt}`;

function drawBig(t) {
  const [hh, mm] = P.time.split(':');
  ctx.save(); ctx.font = BIG; ctx.textBaseline = 'alphabetic';
  const wH = ctx.measureText(hh).width, wC = ctx.measureText(':').width, wM = ctx.measureText(mm).width;
  const m = ctx.measureText('2');
  const base = 500 + m.actualBoundingBoxAscent / 2;
  let x = 960 - (wH + wC + wM) / 2;
  ctx.fillStyle = C.cream; ctx.shadowColor = 'rgba(233,226,208,0.22)'; ctx.shadowBlur = 18;
  ctx.fillText(hh, x, base); x += wH;
  if ((t % 1) < 0.5) ctx.fillText(':', x, base);
  x += wC; ctx.fillText(mm, x, base);
  ctx.restore();
}

// TO AIR line with a 3-frame vertical roll of the digits that change at 1.0 s
function drawToAir(t) {
  const color = P.alarm ? C.red : C.cyan;
  const a = 'TO AIR ' + K.ms(P.toAir), b = 'TO AIR ' + K.ms(Math.max(0, P.toAir - 1));
  ctx.save(); ctx.font = SMALL; ctx.letterSpacing = '0px'; ctx.textBaseline = 'alphabetic';
  const track = 0.08 * 48;
  const widths = [...a].map((ch) => ctx.measureText(ch).width + track);
  const total = widths.reduce((s, w) => s + w, 0) - track;
  const asc = ctx.measureText('0').actualBoundingBoxAscent;
  const base = 700 + asc / 2;
  let x = 960 - total / 2;
  ctx.fillStyle = color; ctx.shadowColor = color; ctx.shadowBlur = 12;
  const f = K.frame(t), f0 = K.frame(1.0);
  const u = K.clamp((f - f0 + 1) / 3); // frames f0, f0+1, f0+2 → 1/3, 2/3, 1
  [...a].forEach((ch, i) => {
    const nb = b[i];
    if (ch === nb || f < f0) { ctx.fillText(f >= f0 ? nb : ch, x, base); }
    else {
      const h = asc + 14, e = u;
      ctx.save(); ctx.beginPath(); ctx.rect(x - 2, base - asc - 7, widths[i] + 4, h); ctx.clip();
      ctx.globalAlpha = 1 - e; ctx.fillText(ch, x, base - h * e);
      ctx.globalAlpha = e; ctx.fillText(nb, x, base + h * (1 - e));
      ctx.restore();
    }
    x += widths[i];
  });
  ctx.restore();
}

window.renderFrame = (t) => {
  ctx.fillStyle = C.navy; ctx.fillRect(0, 0, 1920, 1080);
  K.frameRect(ctx, 40, 138 + 40, 1920 - 80, 942 - 138 - 80, C.line, 1);
  drawBig(t);
  drawToAir(t);
};
