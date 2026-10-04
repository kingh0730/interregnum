#!/usr/bin/env node
// MUST pass before any real render. Proves determinism, order-independence, and non-blank output.
import crypto from 'node:crypto';
import { openPage, renderFrame } from './lib.mjs';
const sha = (b) => crypto.createHash('sha256').update(b).digest('hex');
const FRAME=Number(process.argv[2]??500);
const a = await openPage({ scale: 0.5 });
const f500a = sha(await renderFrame(a.page, FRAME, 4));
await renderFrame(a.page, 10, 4);                       // different order in between
const f500b = sha(await renderFrame(a.page, FRAME, 4));
await a.close();
const b = await openPage({ scale: 0.5 });               // fresh browser
const f500c = sha(await renderFrame(b.page, FRAME, 4));
const lum = await b.page.evaluate(() => {
  const c = document.getElementById('out'); const g = document.createElement('canvas'); g.width = c.width; g.height = c.height;
  const x = g.getContext('2d'); x.drawImage(c, 0, 0); const d = x.getImageData(0, 0, g.width, g.height).data;
  let sum=0,squares=0,n=d.length/4;for(let i=0;i<d.length;i+=4){let v=(d[i]+d[i+1]+d[i+2])/3;sum+=v;squares+=v*v;}let mean=sum/n;return {mean,std:Math.sqrt(squares/n-mean*mean)};
});
await b.close();
const ok = f500a === f500b && f500b === f500c && lum.mean > 2 && lum.mean < 253 && lum.std > 1.5;
console.log({ frame: FRAME, f500a, f500b, f500c, meanLuma: lum, ok });
process.exit(ok ? 0 : 1);
