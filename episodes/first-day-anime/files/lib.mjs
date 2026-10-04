import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = path.dirname(fileURLToPath(import.meta.url));
export const TOTAL_FRAMES = 1311; // 43.70 s * 30 fps

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.otf': 'font/otf',
  '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.map': 'application/json' };

// Same-origin static server. file:// would taint canvases/WebGL textures. Never use file://.
export function serve(root = ROOT) {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const p = path.join(root, decodeURIComponent(new URL(req.url, 'http://x').pathname));
      if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end('404'); }
      res.writeHead(200, { 'Content-Type': MIME[path.extname(p)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
      fs.createReadStream(p).pipe(res);
    });
    srv.listen(0, '127.0.0.1', () => resolve({ srv, port: srv.address().port }));
  });
}

export async function openPage({ scale = 1, angle = 'swiftshader' } = {}) {
  const { srv, port } = await serve();
  const W = Math.round(1920 * scale), H = Math.round(1080 * scale);
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--use-gl=angle', `--use-angle=${angle}`, '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist',
      '--enable-webgl', '--enable-gpu-rasterization',
      '--disable-background-timer-throttling', '--disable-renderer-backgrounding', '--disable-backgrounding-occluded-windows',
      '--force-color-profile=srgb', '--hide-scrollbars', '--allow-file-access-from-files',
    ],
  });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  page.on('console', (m) => { const t = m.type(); if (t === 'error' || t === 'warning') console.error(`[page ${t}]`, m.text()); });
  page.on('pageerror', (e) => { console.error('[pageerror]', e); process.exitCode = 1; });
  page.on('requestfailed', (r) => console.error('[requestfailed]', r.url()));
  await page.goto(`http://127.0.0.1:${port}/index.html?scale=${scale}`);
  await page.waitForFunction('window.__ready === true || window.__bootError', null, { timeout: 180000 });
  const err = await page.evaluate('window.__bootError');
  if (err) throw new Error('Page boot failed:\n' + err);
  const gl = await page.evaluate('window.__glInfo');
  console.log(`[boot] ${W}x${H} GL renderer: ${gl}`);
  return { page, browser, srv, close: async () => { await browser.close(); srv.close(); } };
}

// Returns a PNG Buffer of the exact canvas pixels (lossless).
export async function renderFrame(page, frame, subframes = null) {
  const dataUrl = await page.evaluate(async ([f, s]) => {
    await window.__renderFrame(f, s);
    return document.getElementById('out').toDataURL('image/png');
  }, [frame, subframes]);
  return Buffer.from(dataUrl.split(',')[1], 'base64');
}
