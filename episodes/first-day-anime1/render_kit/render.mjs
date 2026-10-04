#!/usr/bin/env node
// Usage: node render.mjs --from=0 --to=1310 --scale=1 --subframes=8 --out=frames --workers=4 [--force] [--angle=swiftshader|gl|vulkan]
import { spawn, spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { openPage, renderFrame, TOTAL_FRAMES } from './lib.mjs';

const args = Object.fromEntries(process.argv.slice(2).map((a) => { const m = a.match(/^--([^=]+)=?(.*)$/); return [m[1], m[2] === '' ? true : m[2]]; }));
const from = +(args.from ?? 0), to = +(args.to ?? TOTAL_FRAMES - 1);
const scale = +(args.scale ?? 1), out = path.resolve(args.out ?? 'frames');
const sub = args.subframes === undefined ? null : +args.subframes;
const workers = +(args.workers ?? 1);

if (workers > 1 && !args.worker) {
  const per = Math.ceil((to - from + 1) / workers);
  const jobs = [];
  for (let w = 0; w < workers; w++) {
    const a = from + w * per, b = Math.min(to, a + per - 1);
    if (a > to) break;
    const extra = process.argv.slice(2).filter((x) => !/^--(from|to|workers)/.test(x));
    jobs.push(new Promise((res, rej) => {
      const p = spawn(process.execPath, [process.argv[1], `--from=${a}`, `--to=${b}`, '--workers=1', '--worker', ...extra], { stdio: 'inherit' });
      p.on('exit', (c) => (c === 0 ? res() : rej(new Error(`worker ${a}-${b} exited ${c}`))));
    }));
  }
  await Promise.all(jobs);
  const n = fs.readdirSync(out).filter((f) => f.endsWith('.png')).length;
  if (from === 0 && to === TOTAL_FRAMES - 1 && n !== TOTAL_FRAMES) { console.error(`FRAME COUNT ${n} != ${TOTAL_FRAMES}`); process.exit(1); }
  console.log(`done: ${n} frames in ${out}`);
  process.exit(0);
}

fs.mkdirSync(out, { recursive: true });
const ctx = await openPage({ scale, angle: args.angle ?? (process.platform === 'darwin' ? 'metal' : 'swiftshader') });
const t0 = Date.now();
for (let f = from; f <= to; f++) {
  const file = path.join(out, String(f).padStart(5, '0') + '.png');
  if (!args.force && fs.existsSync(file) && fs.statSync(file).size > 1000) continue; // resumable
  let buf = await renderFrame(ctx.page, f, sub);
  if(scale===1){const py=path.resolve(import.meta.dirname,'../../../work/first-day-anime1/venv/bin/python');const raw=file+'.raw.tmp',compressed=file+'.compressed.tmp';fs.writeFileSync(raw,buf);const result=spawnSync(py,[path.join(import.meta.dirname,'optimize_png.py'),raw,compressed],{timeout:30000});if(result.status!==0)throw new Error('PNG lossless compression failed: '+result.stderr?.toString());buf=fs.readFileSync(compressed);fs.unlinkSync(raw);fs.unlinkSync(compressed);}
  fs.writeFileSync(file + '.tmp', buf); fs.renameSync(file + '.tmp', file);
  if ((f - from) % 10 === 0) console.log(`frame ${f}/${to}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
await ctx.close();
