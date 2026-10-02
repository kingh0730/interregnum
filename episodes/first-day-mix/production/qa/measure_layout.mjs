#!/usr/bin/env node
import puppeteer from '../../../../tools/web/node_modules/puppeteer-core/lib/puppeteer/puppeteer-core.js';
import {createServer} from 'node:http';import {createReadStream,statSync,mkdirSync,writeFileSync,readFileSync} from 'node:fs';import {resolve,dirname,extname,relative} from 'node:path';import {spawn} from 'node:child_process';import {once} from 'node:events';
const args=process.argv.slice(2),opt=(k,d)=>{const i=args.indexOf('--'+k);return i<0?d:args[i+1]};
const root=resolve(opt('root','.')),config=resolve(opt('config','episodes/first-day-mix/production/config.json')),out=resolve(opt('out','work/first-day-mix/film-silent.mp4'));
const fps=Number(opt('fps',60)),from=Number(opt('from',0)),to=Number(opt('to',43.67)),frames=Math.ceil(to*fps)-Math.ceil(from*fps),stills=opt('stills',null);
const mime={'.html':'text/html','.js':'text/javascript','.json':'application/json','.png':'image/png','.jpg':'image/jpeg','.mp4':'video/mp4','.webm':'video/webm','.wav':'audio/wav'};
const server=createServer((req,res)=>{try{const p=resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(relative(root,p).startsWith('..')){res.writeHead(403).end();return}const st=statSync(p),range=req.headers.range;res.setHeader('Content-Type',mime[extname(p)]||'application/octet-stream');res.setHeader('Accept-Ranges','bytes');if(range){const m=/bytes=(\d+)-(\d*)/.exec(range),start=Number(m[1]),end=m[2]?Math.min(Number(m[2]),st.size-1):st.size-1;res.writeHead(206,{'Content-Range':`bytes ${start}-${end}/${st.size}`,'Content-Length':end-start+1});createReadStream(p,{start,end}).pipe(res)}else{res.writeHead(200,{'Content-Length':st.size});createReadStream(p).pipe(res)}}catch(e){res.writeHead(404).end(String(e))}});server.listen(0,'127.0.0.1');await once(server,'listening');
let browser,ff;try{browser=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--hide-scrollbars','--force-color-profile=srgb','--font-render-hinting=none','--autoplay-policy=no-user-gesture-required','--disable-background-timer-throttling']});const page=await browser.newPage();await page.setViewport({width:1920,height:1080,deviceScaleFactor:1});page.on('pageerror',e=>console.error('PAGE',e.message));const base=`http://127.0.0.1:${server.address().port}/`,cfg=relative(root,config).split('\\').join('/');await page.goto(base+'episodes/first-day-mix/production/renderer/index.html?config='+encodeURIComponent('/'+cfg),{waitUntil:'load'});await page.evaluate(async()=>await window.ready);console.log('Assets',await page.evaluate(()=>window.assetStatus));mkdirSync(dirname(out),{recursive:true});

const configData=JSON.parse(readFileSync(config,'utf8'));
await page.evaluate(()=>{
 const original=CanvasRenderingContext2D.prototype.fillText;
 CanvasRenderingContext2D.prototype.fillText=function(text,x,y,...rest){
  const m=this.measureText(text),matrix=this.getTransform(),pad=this.shadowBlur||0;
  const corners=[[x-m.actualBoundingBoxLeft-pad,y-m.actualBoundingBoxAscent-pad],[x+m.actualBoundingBoxRight+pad,y+m.actualBoundingBoxDescent+pad]].map(([a,b])=>({x:matrix.a*a+matrix.c*b+matrix.e,y:matrix.b*a+matrix.d*b+matrix.f}));
  (window.qaText||=[]).push({text,font:this.font,color:this.fillStyle,alpha:this.globalAlpha,box:[corners[0].x,corners[0].y,corners[1].x-corners[0].x,corners[1].y-corners[0].y],rawMetrics:{left:m.actualBoundingBoxLeft,right:m.actualBoundingBoxRight,ascent:m.actualBoundingBoxAscent,descent:m.actualBoundingBoxDescent},shadowBlur:this.shadowBlur});
  return original.call(this,text,x,y,...rest);
 };
});
mkdirSync(out,{recursive:true});
const frameCount=Math.ceil(configData.duration*configData.fps),cuts=new Set([0,frameCount]);
for(const a of [...configData.shots,...configData.lyrics,...configData.labels]){cuts.add(Math.ceil((a.start??a.in_frame/60)*60));cuts.add(Math.min(frameCount,Math.ceil((a.end??a.out_frame/60)*60)))}
cuts.add(Math.ceil((configData.duration-1.6)*60));
const boundaries=[...cuts].sort((a,b)=>a-b),records=[],overlays=[];
for(let i=0;i<boundaries.length-1;i++){
 const a=boundaries[i],b=boundaries[i+1];if(b<=a)continue;const f=Math.floor((a+b-1)/2),t=f/60;
 const text=await page.evaluate(async t=>{window.qaText=[];await window.renderFrame(t);return window.qaText},t);
 records.push({start_frame:a,end_frame:b,sampled_frame:f,text});
 text.forEach((row,j)=>overlays.push({...row,id:`text-${i}-${j}`,start_frame:a,end_frame:b}));
}
for(let i=0;i<configData.shots.length;i++){
 const s=configData.shots[i],f=Math.floor((Math.ceil(s.start*60)+Math.ceil(s.end*60)-1)/2),t=f/60;
 await page.evaluate(async t=>await window.renderFrame(t),t);
 await page.screenshot({path:resolve(out,`shot-${String(i+1).padStart(2,'0')}-f${f}.jpg`),type:'jpeg',quality:72});
 console.log('Midpoint',s.id,f);
}
writeFileSync(resolve(out,'canvas-text-measurements.json'),JSON.stringify({method:'Actual Canvas fillText interception and measureText bounding boxes incl shadowBlur, at every stable text/shot interval midpoint. No engine mutation. Alpha stored; bounds do not certify contrast.',config,records},null,2));
writeFileSync(resolve(out,'final-qa-config.json'),JSON.stringify({video:'renders/first-day-mix/first-day-mix-final.mp4',fps:'60',width:1920,height:1080,expected_frames:2621,expected_duration_s:43.683333333333,duration_tolerance_s:.04,source_audio:'episodes/first-day-mix/first-day.wav',source_audio_sha256:'261c74fd2f73c1130b74544ba04173fc04b5687496611aefa6e6034036e75fab',shots:configData.shots.map(s=>({id:s.id,start_frame:Math.ceil(s.start*60),end_frame:Math.min(frameCount,Math.ceil(s.end*60))})),overlays,assets:[],generation_logs:[]},null,2));
}finally{if(browser)await browser.close();server.close();if(ff&&!ff.killed&&ff.exitCode===null)ff.kill('SIGTERM')}
