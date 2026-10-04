import fs from 'node:fs';import path from 'node:path';import {openPage,renderFrame} from './lib.mjs';
const scale=Number(process.argv.find(v=>v.startsWith('--scale='))?.split('=')[1]??1);const frames=process.argv.slice(2).filter(v=>!v.startsWith('--')).map(Number);if(!frames.length)throw Error('Pass exact frame indices');
const out=path.resolve(import.meta.dirname,`../../../work/first-day-anime1/${scale<1?'anchors_preview':'anchors'}`);fs.mkdirSync(out,{recursive:true});
const c=await openPage({scale});try{for(const f of frames){let t=Date.now();const png=await renderFrame(c.page,f);fs.writeFileSync(`${out}/${String(f).padStart(5,'0')}.png`,png);console.log({frame:f,seconds:(Date.now()-t)/1000,bytes:png.length});}}finally{await c.close();}
