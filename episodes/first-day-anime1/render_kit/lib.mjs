import { chromium } from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = path.dirname(fileURLToPath(import.meta.url));
const failures = new WeakMap();
export const TOTAL_FRAMES = 1311; // 43.70 s * 30 fps

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.otf': 'font/otf',
  '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.map': 'application/json' };

// Same-origin static server. file:// would taint canvases/WebGL textures. Never use file://.
export function serve(root = ROOT) {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const p = path.join(root, decodeURIComponent(new URL(req.url, 'http://x').pathname));
      if ((path.relative(root,p).startsWith('..') || path.isAbsolute(path.relative(root,p))) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end('404'); }
      res.writeHead(200, { 'Content-Type': MIME[path.extname(p)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
      fs.createReadStream(p).pipe(res);
    });
    srv.listen(0, '127.0.0.1', () => resolve({ srv, port: srv.address().port }));
  });
}

export async function openPage({ scale = 1, angle = (process.platform === 'darwin' ? 'metal' : 'swiftshader'), key = null } = {}) {
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
  const errors=[]; failures.set(page,errors);
  page.on('console', (m) => { const t=m.type(); if(t==='error'){errors.push(m.text());console.error('[page error]',m.text());} else if(t==='warning') console.error('[page warning]',m.text()); });
  page.on('pageerror', (e) => { errors.push(String(e)); console.error('[pageerror]',e); });
  page.on('requestfailed',r=>{errors.push('request failed: '+r.url());console.error('[requestfailed]',r.url());});
  page.on('response',r=>{if(r.status()>=400 && !r.url().endsWith('/favicon.ico'))errors.push('HTTP '+r.status()+': '+r.url());});
  try {
  await page.goto(`http://127.0.0.1:${port}/index.html?scale=${scale}${key ? `&key=${encodeURIComponent(key)}` : ''}`);
  await page.waitForFunction('window.__ready === true || window.__bootError', null, { timeout: 180000, polling: 100 });
  const err = await page.evaluate('window.__bootError');
  if (err) throw new Error('Page boot failed:\n' + err);
  if(errors.length)throw new Error(errors.join('\n'));
  const gl = await page.evaluate('window.__glInfo');
  console.log(`[boot] ${W}x${H} GL renderer: ${gl}`);
  return { page, browser, srv, close: async () => { await browser.close(); srv.close(); } };
  } catch(e){await browser.close();srv.close();throw e;}
}

// Returns a PNG Buffer of the exact canvas pixels (lossless).
export async function renderFrame(page, frame, subframes = null) {
  if(failures.get(page)?.length)throw new Error(failures.get(page).join('\n'));
  const dataUrl = await page.evaluate(async ([f, s]) => {
    await window.__renderFrame(f, s);
    return document.getElementById('out').toDataURL('image/png');
  }, [frame, subframes]);
  if(failures.get(page)?.length)throw new Error(failures.get(page).join('\n'));
  return Buffer.from(dataUrl.split(',')[1], 'base64');
}
