// Render an HTML page frame by frame to a video (or a PNG sequence) with deterministic time.
//
// usage: ~/.nvm/versions/node/v22.23.1/bin/node tools/web/render.mjs <page.html> <out.mov|out.mp4|outdir/> <seconds> [fps=24]
//   The page must define window.renderFrame(t) (t in seconds; may return a Promise). Optional window.ready Promise.
//   .mov output keeps transparency (ProRes 4444) when the page background is transparent; .mp4 is opaque H.264.
import puppeteer from 'puppeteer-core';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const [page_, out, secs, fpsArg] = process.argv.slice(2);
const fps = Number(fpsArg || 24);
const n = Math.round(Number(secs) * fps);
const W = 1920, H = 1080;

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  headless: true,
  args: ['--hide-scrollbars', '--force-color-profile=srgb', '--font-render-hinting=none'],
});
const page = await browser.newPage();
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
await page.goto('file://' + resolve(page_), { waitUntil: 'load' });
await page.evaluate(async () => { await document.fonts.ready; if (window.ready) await window.ready; });

let ff = null;
const seqDir = out.endsWith('/') ? out : null;
if (seqDir) mkdirSync(seqDir, { recursive: true });
else {
  const alpha = out.endsWith('.mov');
  const enc = alpha
    ? ['-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le']
    : ['-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p'];
  ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', ...enc, out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
}

for (let i = 0; i < n; i++) {
  await page.evaluate(async (t) => { await window.renderFrame(t); }, i / fps);
  const buf = await page.screenshot({ type: 'png', omitBackground: true });
  if (seqDir) (await import('node:fs')).writeFileSync(`${seqDir}/${String(i).padStart(5, '0')}.png`, buf);
  else if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
}
await browser.close();
if (ff) { ff.stdin.end(); await new Promise(r => ff.on('close', r)); }
console.log(`${out}: ${n} frames`);
