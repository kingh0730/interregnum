/** Local, offline Three.js effect-preview runner. Never labels previews as final film. */
import {chromium} from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawn} from 'node:child_process';
import {createHash} from 'node:crypto';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const args=Object.fromEntries(process.argv.slice(2).map(a=>a.replace(/^--/,'').split('=')));
if(args.mode==='playback'){await (await import('./playback.mjs')).checkPlayback(args,root);process.exit(0);}
const effect=args.effect||'Spark';
const mode=args.mode||'effect',from=Number(args.from||0);
const count=Number(args.frames||60),width=Number(args.width||960),height=Math.round(width*9/16);
const output=path.resolve(root,args.out||`qa/fx/${effect}.mp4`);
const mime={'.mjs':'text/javascript','.js':'text/javascript','.html':'text/html','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.ttf':'font/ttf'};
const server=http.createServer((req,res)=>{
  const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  let p=path.resolve(root,'.'+pathname);
  if(pathname.startsWith('/vendor/three/'))p=path.resolve(root,'node_modules/three',pathname.slice('/vendor/three/'.length));
  const allowed=[root];
  if(!allowed.some(r=>p.startsWith(r+path.sep))||!fs.existsSync(p)||!fs.statSync(p).isFile()){res.writeHead(404);res.end();return;}
  res.writeHead(200,{'Content-Type':mime[path.extname(p)]||'application/octet-stream'});fs.createReadStream(p).pipe(res);
});
await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
let browser,encoder;
const frameHashes=[];
const started=Date.now();
try{
  browser=await chromium.launch({headless:true,args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--force-color-profile=srgb']});
  const page=await browser.newPage({viewport:{width,height}});
  let pageError;
  page.on('pageerror',e=>{pageError=e;});
  page.on('console',m=>{if(m.type()==='error'&&/THREE|WebGL|shader/i.test(m.text()))pageError=new Error(m.text());});
  await page.goto(`http://127.0.0.1:${server.address().port}/src/${mode==='film'?'film_preview':'effect_preview'}.html?effect=${effect}&width=${width}&frames=${count}&debug=${args.debug||0}`);
  await page.waitForFunction('window.ready || window.bootError',null,{timeout:60000});
  const error=await page.evaluate(()=>window.bootError);if(error)throw new Error(error);
  fs.mkdirSync(path.dirname(output),{recursive:true});
  const withAudio=args.audio==='1';
  if(withAudio&&(mode!=='film'||from!==0||count!==1311))throw new Error('Original-audio mux requires the complete 1311-frame film starting at0.');
  const audioArgs=withAudio?['-i',path.resolve(root,'../first-day.mp3'),'-map','0:v','-map','1:a','-c:a','copy','-t','43.7']:[];
  encoder=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate','30','-i','-',...audioArgs,'-c:v','libx264','-crf','14','-preset','fast','-tune','animation','-pix_fmt','yuv420p','-video_track_timescale','30000','-movflags','+faststart',output],{stdio:['pipe','inherit','inherit']});
  const exits=new Promise((resolve,reject)=>{encoder.on('error',reject);encoder.on('exit',resolve);});
  for(let frame=0;frame<count;frame++){
    const png=await page.evaluate(async f=>{await window.renderFrame(f);return document.querySelector('#output').toDataURL('image/png');},frame+from);
    if(pageError)throw pageError;
    const data=Buffer.from(png.split(',')[1],'base64');
    frameHashes.push({frame:frame+from,sha256:createHash('sha256').update(data).digest('hex')});
    if([0,Math.floor(count/2),count-1].includes(frame))fs.writeFileSync(output.replace(/\.mp4$/,`-f${frame+from}.png`),data);
    if(!encoder.stdin.write(data))await new Promise(resolve=>encoder.stdin.once('drain',resolve));
    if((frame+1)%60===0)console.log(`Rendered ${frame+1}/${count} frames (${((Date.now()-started)/1000).toFixed(1)}s)`);
  }
  encoder.stdin.end();const code=await exits;if(code!==0)throw new Error(`ffmpeg exit ${code}`);
  fs.writeFileSync(output.replace(/\.mp4$/,'.source-frame-hashes.json'),JSON.stringify({definition:'SHA256 of each lossless PNG supplied directly to ffmpeg, in source frame order.',video_sha256:createHash('sha256').update(fs.readFileSync(output)).digest('hex'),frames:frameHashes},null,2));
  if(mode==='film')fs.writeFileSync(output.replace(/\.mp4$/,'.diagnostics.json'),JSON.stringify(await page.evaluate(()=>window.film.diagnostics),null,2));
  console.log(JSON.stringify({mode,effect,from,count,width,height,output,elapsedSeconds:(Date.now()-started)/1000}));
}finally{
  if(encoder&&!encoder.stdin.destroyed)encoder.stdin.end();
  if(browser)await browser.close();
  await new Promise(resolve=>server.close(resolve));
}
