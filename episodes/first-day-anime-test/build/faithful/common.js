export const W = 1920,
  H = 1080;
export const C = {
  ink: "#141413",
  ivory: "#FAF9F5",
  cream: "#F0EEE6",
  oat: "#E8E6DC",
  coral: "#D97757",
  kraft: "#D4A27F",
  sky: "#6A9BCC",
  olive: "#788C5D",
  gold: "#FFD9A8",
};
export const clamp = (x) => Math.max(0, Math.min(1, x));
export const ease = (x) => {
  x = clamp(x);
  return x * x * (3 - 2 * x);
};
export const lerp = (a, b, p) => a + (b - a) * p;
export function rng(seed) {
  return () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) | 0;
    return (seed >>> 0) / 4294967296;
  };
}
export function canvas(w, h) {
  const c = document.createElement("canvas");
  c.width = w;
  c.height = h;
  return c;
}
export function text(
  g,
  str,
  x,
  y,
  size = 46,
  color = C.ivory,
  family = "FDSerif",
  weight = 600,
  align = "left",
) {
  g.font = `${weight} ${size}px ${family}, FDSans, FDSymbol`;
  g.fillStyle = color;
  g.textAlign = align;
  g.textBaseline = "middle";
  g.fillText(str, x, y);
}
export function rounded(g, x, y, w, h, r = 12) {
  g.beginPath();
  g.roundRect(x, y, w, h, r);
}
export function image(src) {
  return new Promise((resolve, reject) => {
    const im = new Image();
    im.onload = () => resolve(im);
    im.onerror = () => reject(Error(src));
    im.src = src;
  });
}
export function cover(g, im) {
  const iw = im.videoWidth || im.width,
    ih = im.videoHeight || im.height,
    z = Math.max(W / iw, H / ih);
  g.drawImage(im, (iw - W / z) / 2, (ih - H / z) / 2, W / z, H / z, 0, 0, W, H);
}
export function glow(g, x, y, r, hex = C.gold, alpha = 0.5) {
  g.save();
  g.globalAlpha = alpha;
  g.globalCompositeOperation = "screen";
  const d = g.createRadialGradient(x, y, 0, x, y, r);
  d.addColorStop(0, hex);
  d.addColorStop(0.1, hex + "A0");
  d.addColorStop(1, hex + "00");
  g.fillStyle = d;
  g.fillRect(x - r, y - r, r * 2, r * 2);
  g.restore();
}
export function grainTexture() {
  const c = canvas(256, 256),
    g = c.getContext("2d"),
    d = g.createImageData(256, 256),
    r = rng(551);
  for (let i = 0; i < d.data.length; i += 4) {
    const v = r() * 255;
    d.data.set([v, v, v, 10], i);
  }
  g.putImageData(d, 0, 0);
  return c;
}
export function labelTexture(
  str,
  {
    width = 2048,
    height = 180,
    size = 110,
    color = C.ivory,
    family = "FDSerif",
    weight = 600,
    highlights = false,
  } = {},
) {
  const c = canvas(width, height),
    g = c.getContext("2d");
  g.shadowColor = "#14141399";
  g.shadowBlur = highlights ? 7 : 2;
  g.textBaseline = "middle";
  if (!highlights) {
    text(g, str, width / 2, height / 2, size, color, family, weight, "center");
  } else {
    g.font = `${weight} ${size}px ${family}, FDSans, FDSymbol`;
    let x = (width - g.measureText(str).width) / 2;
    const marked = new Set();
    for (const m of str.matchAll(/明天|今天|存在|呼吸|脚踝|你|飞|爱|灿烂/g))
      for (let k = m.index; k < m.index + m[0].length; k++) marked.add(k);
    for (let i = 0; i < str.length; i++) {
      text(
        g,
        str[i],
        x,
        height / 2,
        size,
        marked.has(i) ? C.coral : color,
        family,
        weight,
      );
      x += g.measureText(str[i]).width;
    }
  }
  return c;
}
export function musicTexture() {
  const c = canvas(1200, 1600),
    g = c.getContext("2d");
  g.fillStyle = C.cream;
  g.fillRect(0, 0, 1200, 1600);
  const r = rng(114);
  g.fillStyle = "#A7977622";
  for (let i = 0; i < 20000; i++) g.fillRect(r() * 1200, r() * 1600, 0.5, 1);
  text(g, "Opus 5.5", 90, 130, 53, C.ink, "FDLora", 600);
  for (let row = 0; row < 7; row++) {
    const y = 310 + row * 170;
    g.strokeStyle = "#413B31";
    g.lineWidth = 1.6;
    for (let line = 0; line < 5; line++) {
      g.beginPath();
      g.moveTo(88, y + line * 16);
      g.lineTo(1110, y + line * 16);
      g.stroke();
    }
    text(g, "5.5", 90, y + 31, 27, C.coral, "FDLora");
    for (let n = 0; n < 8; n++) {
      const x = 220 + n * 112,
        yy = y + ((n * 3 + row) % 5) * 16;
      g.beginPath();
      g.ellipse(x, yy, 11, 7, -0.25, 0, Math.PI * 2);
      g.fillStyle = C.ink;
      g.fill();
      g.beginPath();
      g.moveTo(x + 10, yy);
      g.lineTo(x + 10, yy - 63);
      if (n % 3) {
        g.bezierCurveTo(x + 40, yy - 46, x + 37, yy - 29, x + 21, yy - 19);
      }
      g.stroke();
    }
  }
  return c;
}
export function roundFrame(t) {
  return Math.round(t * 30);
}
export function lanternTexture() {
  const c = canvas(1448, 512),
    g = c.getContext("2d");
  const gr = g.createLinearGradient(0, 0, 0, 512);
  gr.addColorStop(0, "#E8D8B5");
  gr.addColorStop(0.5, C.ivory);
  gr.addColorStop(1, "#E7CAA0");
  g.fillStyle = gr;
  g.fillRect(0, 0, 1448, 512);
  for (let row = 0; row < 3; row++) {
    const y = 75 + row * 150;
    g.strokeStyle = "#514B3CE0";
    g.lineWidth = 3;
    for (let j = 0; j < 5; j++) {
      g.beginPath();
      g.moveTo(25, y + j * 14);
      g.lineTo(1423, y + j * 14);
      g.stroke();
    }
    for (let i = 0; i < 12; i++) {
      const x = 70 + i * 113,
        yy = y + ((i * 3 + row) % 5) * 14;
      g.fillStyle = C.ink;
      g.beginPath();
      g.ellipse(x, yy, 10, 7, -0.25, 0, Math.PI * 2);
      g.fill();
      g.beginPath();
      g.moveTo(x + 9, yy);
      g.lineTo(x + 9, yy - 39);
      g.stroke();
    }
  }
  g.lineWidth = 2;
  for (let i = 0; i < 12; i++) {
    g.strokeStyle = i % 2 ? "#FFFFFF45" : "#765D4328";
    g.beginPath();
    g.moveTo((i * 1448) / 12, 0);
    g.lineTo((i * 1448) / 12, 512);
    g.stroke();
  }
  return c;
}
