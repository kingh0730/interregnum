import {chromium} from '../render_kit/node_modules/playwright/index.mjs';
import fs from 'node:fs';import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
const b=await chromium.launch({headless:true});const p=await b.newPage();
const data=(f,m)=>`data:${m};base64,${fs.readFileSync(f).toString('base64')}`;
const image=data(root+'/assets/references/opus-v2.png','image/png');
const spark=fs.readFileSync(root+'/assets/logos/claude-spark.svg','utf8');
const mark=fs.readFileSync(root+'/assets/logos/anthropic-symbol-ivory.svg','utf8');
const font=data(root+'/render_kit/fonts/Lora-SemiBold.ttf','font/ttf');
const out=await p.evaluate(async ({image,spark,mark,font})=>{
 const img=new Image();img.src=image;await img.decode();const c=document.createElement('canvas');c.width=img.width;c.height=img.height;const x=c.getContext('2d');x.drawImage(img,0,0);
 const ff=new FontFace('Lora',`url(${font})`);await ff.load();document.fonts.add(ff);
 const svg=async s=>{const i=new Image();i.src='data:image/svg+xml;base64,'+btoa(s);await i.decode();return i};
 const sp=await svg(spark),a=await svg(mark);
 // Coordinates in the 1024 x 1536 master; official vectors placed without generative repainting.
 const logos=[[199,56,27],[434,57,25],[738,1006,39]];
 for(const [cx,cy,w]of logos)x.drawImage(sp,cx-w/2,cy-w/2,w,w);
 for(const [cx,cy,w]of [[160,140,13],[395,142,13],[100,1230,15]])x.drawImage(a,cx-w/2,cy-w*64/92/2,w,w*64/92);
 // Detail pupil, preserving all surrounding iris pixels.
 const dark=await svg(spark.replaceAll('#D97757','#141413').replaceAll('#d97757','#141413'));
 x.drawImage(dark,907,997,12,17);
 x.fillStyle='#141413';x.font='600 12px Lora';x.textAlign='center';x.fillText('5.5',858,1468);
 return c.toDataURL('image/png');
},{image,spark,mark,font});
fs.writeFileSync(root+'/assets/references/opus-composite-v3.png',Buffer.from(out.split(',')[1],'base64'));await b.close();
