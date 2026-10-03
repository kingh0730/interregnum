import puppeteer from '../../../../tools/web/node_modules/puppeteer-core/lib/puppeteer/puppeteer-core.js';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {mkdirSync,writeFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
const ROOT=resolve(import.meta.dir,'../../../..'),SRC=import.meta.dir,WORK=join(ROOT,'work/first-day-anime-test/graphics-v2'),OUT=join(ROOT,'renders/first-day-anime-test');
const stills=process.argv.includes('--stills'),preview=process.argv.includes('--preview'),width=preview?960:1920,height=width*9/16;
mkdirSync(join(WORK,'qa'),{recursive:true});
const server=Bun.serve({hostname:'127.0.0.1',port:0,async fetch(req){const url=new URL(req.url);let path;
 if(url.pathname==='/favicon.ico')return new Response(null,{status:204});
 if(url.pathname==='/')path=join(SRC,'index.html');
 else if(url.pathname==='/film.js')path=join(SRC,'film.js');
 else if(url.pathname.startsWith('/assets/'))path=join(ROOT,'work/first-day-anime-test/assets',decodeURIComponent(url.pathname.slice(8)));
 else if(url.pathname.startsWith('/base/'))path=join(WORK,decodeURIComponent(url.pathname.slice(6)));
 else return new Response('Not found',{status:404});
 if(url.pathname.includes('..'))return new Response('Invalid path',{status:400});
 const file=Bun.file(path);if(!await file.exists())return new Response('Not found '+url.pathname,{status:404});
 const range=req.headers.get('range');if(range&&path.endsWith('.mp4')){const m=range.match(/bytes=(\d+)-(\d*)/);if(m){const start=+m[1],end=m[2]?Math.min(+m[2],file.size-1):file.size-1;return new Response(file.slice(start,end+1),{status:206,headers:{'Content-Type':'video/mp4','Accept-Ranges':'bytes','Content-Range':`bytes ${start}-${end}/${file.size}`,'Content-Length':String(end-start+1)}})}}
 return new Response(file,{headers:{'Cache-Control':'no-store'}});
}});
const browser=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--hide-scrollbars','--force-color-profile=srgb','--autoplay-policy=no-user-gesture-required']});
const page=await browser.newPage();await page.setViewport({width,height,deviceScaleFactor:1});
page.on('requestfailed',r=>{if(r.failure()?.errorText!=='net::ERR_ABORTED')console.error('FAILED',r.url(),r.failure())});page.on('console',m=>{if(m.type()==='error')console.error('BROWSER',m.text())});page.on('response',r=>{if(r.status()>=400)console.error('HTTP',r.status(),r.url())});page.on('pageerror',e=>console.error('PAGE',e));try{await page.goto(`http://127.0.0.1:${server.port}/`,{waitUntil:'load'});await page.evaluate(async()=>{await window.ready})}catch(e){await browser.close();server.stop(true);throw e}
const samples=[0,20,30,33,34,35,42,51,65,84,90,104,120,170,201,220,242,260,300,328,335,339,346,350,355,358,371,382,390,402,785,800,860,925,973,1020,1138,1185,1190,1196,1200,1285];
let ff:any;let completion:Promise<any>|undefined;
if(!stills){const output=join(OUT,`first-day_opus55_graphics-v2_${height}p30.mp4`);ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate','30','-i','-','-i',join(ROOT,'episodes/first-day-anime-test/first-day.mp3'),'-map','0:v','-map','1:a','-frames:v','1311','-c:v','libx264','-preset','fast','-crf','16','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart',output],{stdio:['pipe','inherit','inherit']});completion=once(ff,'close');ff.stdin.on('error',e=>console.error('ENCODER',e));}
try{const frames=stills?samples:Array.from({length:1311},(_,i)=>i);for(const i of frames){await page.evaluate(async t=>await window.renderFrame(t),i/30);const bytes=await page.screenshot({type:'jpeg',quality:96});
 if(samples.includes(i))writeFileSync(join(WORK,'qa',`frame-${String(i).padStart(4,'0')}.jpg`),bytes);
 if(ff&&!ff.stdin.write(bytes))await once(ff.stdin,'drain');
 if(i%90===0||stills)console.log(`frame ${i}/1311`);
}if(ff){ff.stdin.end();const [code]=await completion!;if(code!==0)throw Error('ffmpeg exit '+code)}}finally{await browser.close();server.stop(true)}
console.log(stills?'Diagnostic frames ready':'Export complete');
