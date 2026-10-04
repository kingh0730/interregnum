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
} from "./common.js";
// Piecewise affine rasterization of a continuous perspective surface. The texture
// remains in its native aspect ratio; projected geometry determines foreshortening.
export function triangle(g, im, u, p) {
  const [a, b, c] = u,
    [A, B, C] = p,
    den = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]);
  if (Math.abs(den) < 1e-7) return;
  g.save();
  g.beginPath();
  g.moveTo(...A);
  g.lineTo(...B);
  g.lineTo(...C);
  g.closePath();
  g.clip();
  const ax =
      ((B[0] - A[0]) * (c[1] - a[1]) - (C[0] - A[0]) * (b[1] - a[1])) / den,
    bx = ((B[1] - A[1]) * (c[1] - a[1]) - (C[1] - A[1]) * (b[1] - a[1])) / den,
    ay = ((C[0] - A[0]) * (b[0] - a[0]) - (B[0] - A[0]) * (c[0] - a[0])) / den,
    by = ((C[1] - A[1]) * (b[0] - a[0]) - (B[1] - A[1]) * (c[0] - a[0])) / den;
  g.transform(
    ax,
    bx,
    ay,
    by,
    A[0] - ax * a[0] - ay * a[1],
    A[1] - bx * a[0] - by * a[1],
  );
  g.drawImage(im, 0, 0);
  g.restore();
}
export function mesh(g, im, fn, nx = 18, ny = 18) {
  for (let j = 0; j < ny; j++)
    for (let i = 0; i < nx; i++) {
      const u = i / nx,
        v = j / ny,
        U = (i + 1) / nx,
        V = (j + 1) / ny,
        uv = [
          [u * im.width, v * im.height],
          [U * im.width, v * im.height],
          [U * im.width, V * im.height],
          [u * im.width, V * im.height],
        ],
        p = [fn(u, v), fn(U, v), fn(U, V), fn(u, V)];
      triangle(g, im, [uv[0], uv[1], uv[2]], [p[0], p[1], p[2]]);
      triangle(g, im, [uv[0], uv[2], uv[3]], [p[0], p[2], p[3]]);
    }
}
export function quad(g, im, q) {
  mesh(
    g,
    im,
    (u, v) => {
      const top = [lerp(q[0][0], q[1][0], u), lerp(q[0][1], q[1][1], u)],
        bottom = [lerp(q[3][0], q[2][0], u), lerp(q[3][1], q[2][1], u)];
      return [lerp(top[0], bottom[0], v), lerp(top[1], bottom[1], v)];
    },
    10,
    10,
  );
}
export function paperTexture(w, h) {
  const c = canvas(w, h),
    g = c.getContext("2d"),
    r = rng(100);
  const gr = g.createLinearGradient(0, 0, w, h);
  gr.addColorStop(0, "#FAF8EF");
  gr.addColorStop(0.62, C.cream);
  gr.addColorStop(1, "#D8CFBA");
  g.fillStyle = gr;
  g.fillRect(0, 0, w, h);
  for (let i = 0; i < (w * h) / 12; i++) {
    g.fillStyle = i % 2 ? "#776C4C0D" : "#FFFFFF26";
    g.fillRect(r() * w, r() * h, 0.5 + r(), 0.6 + r() * 2);
  }
  g.strokeStyle = "#FFFDF0A0";
  g.lineWidth = 2;
  g.strokeRect(1, 1, w - 2, h - 2);
  return c;
}
export function calendarTexture(today = false) {
  const c = paperTexture(600, 850),
    g = c.getContext("2d");
  g.globalCompositeOperation = "multiply";
  g.fillStyle = "#9AA0A6";
  g.fillRect(0, 0, 600, 850);
  g.globalCompositeOperation = "source-over";
  text(g, "第一天", 300, 85, 29, "#605B51", "FDSerif", 600, "center");
  g.strokeStyle = "#918675";
  g.lineWidth = 1;
  g.beginPath();
  g.moveTo(45, 143);
  g.lineTo(555, 143);
  g.stroke();
  text(
    g,
    today ? "今天" : "明天",
    300,
    425,
    170,
    today ? C.coral : C.ink,
    "FDSerif",
    800,
    "center",
  );
  if (!today) {
    for (let j = 0; j < 6; j++)
      for (let i = 0; i < 5; i++) {
        const x = 76 + i * 111,
          y = 578 + j * 38;
        text(g, "明天", x, y, 20, C.ink, "FDSerif", 600, "center");
        g.strokeStyle = "#A6553CCC";
        g.lineWidth = 2.2;
        g.beginPath();
        g.ellipse(x, y, 35, 16, (i - j) * 0.013, 0, Math.PI * 2);
        g.stroke();
      }
  }
  return c;
}
export function noteTexture(i) {
  const c = paperTexture(180, 168),
    g = c.getContext("2d");
  g.fillStyle = "#B38F6328";
  g.fillRect(0, 0, 180, 23);
  g.strokeStyle = "#6D685244";
  g.lineWidth = 1.2;
  const r = rng(i + 200);
  for (let j = 0; j < 3; j++) {
    g.beginPath();
    g.moveTo(25, 58 + j * 25);
    for (let k = 0; k < 7; k++)
      g.lineTo(25 + k * 18, 58 + j * 25 + (r() - 0.5) * 5);
    g.stroke();
  }
  return c;
}
export function tornWipe(g, p, reverse = false) {
  if (p <= 0) return;
  if (p >= 1) {
    g.fillStyle = C.cream;
    g.fillRect(0, 0, W, H);
    return;
  }
  const edge = reverse ? W * (1 - p) : W * p;
  g.save();
  g.shadowColor = "#3B302A30";
  g.shadowBlur = 13;
  g.fillStyle = C.cream;
  g.beginPath();
  g.moveTo(reverse ? W : 0, 0);
  g.lineTo(edge, 0);
  for (let y = 0; y <= H; y += 9)
    g.lineTo(edge + Math.sin(y * 0.67) * 7 + Math.sin(y * 0.083) * 11, y);
  g.lineTo(reverse ? W : 0, H);
  g.closePath();
  g.fill();
  g.restore();
}
