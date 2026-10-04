/** Automated Chromium media-decoder playback test; not perceptual audio review. */
import {chromium} from 'playwright';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';

export async function checkPlayback(args,root){
 const video=path.resolve(root,args.video||'out/opus55_first_day_1080p30.mp4');
 const stat=fs.statSync(video);
 const html=`<!doctype html><html><body><video id="v" controls playsinline width="960" src="/film.mp4"></video><script>window.result={status:'loading',errors:[],stalls:[]};const v=document.querySelector('video');v.addEventListener('error',()=>result.errors.push({code:v.error?.code,message:v.error?.message}));for(const name of ['stalled','waiting'])v.addEventListener(name,()=>result.stalls.push({event:name,at:v.currentTime}));window.start=async()=>{await new Promise(r=>{if(v.readyState>=2)r();else v.addEventListener('loadeddata',r,{once:true});});result.initial={width:v.videoWidth,height:v.videoHeight,duration:v.duration};result.started=performance.now();v.addEventListener('ended',()=>{const q=v.getVideoPlaybackQuality();Object.assign(result,{status:'ended',elapsedSeconds:(performance.now()-result.started)/1000,currentTime:v.currentTime,totalVideoFrames:q.totalVideoFrames,droppedVideoFrames:q.droppedVideoFrames,corruptedVideoFrames:q.corruptedVideoFrames});},{once:true});await v.play();};</script></body></html>`;
 const server=http.createServer((req,res)=>{
  if(req.url!=='/film.mp4'){res.writeHead(200,{'Content-Type':'text/html'});res.end(html);return;}
  const match=req.headers.range?.match(/^bytes=(\d+)-(\d*)$/);
  if(match){const start=Number(match[1]),end=match[2]?Math.min(Number(match[2]),stat.size-1):stat.size-1;res.writeHead(206,{'Content-Type':'video/mp4','Accept-Ranges':'bytes','Content-Range':`bytes ${start}-${end}/${stat.size}`,'Content-Length':end-start+1});fs.createReadStream(video,{start,end}).pipe(res);}
  else{res.writeHead(200,{'Content-Type':'video/mp4','Accept-Ranges':'bytes','Content-Length':stat.size});fs.createReadStream(video).pipe(res);}
 });
 await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
 let browser;
 try{
  browser=await chromium.launch({headless:true,args:['--autoplay-policy=no-user-gesture-required']});
  const page=await browser.newPage();await page.goto(`http://127.0.0.1:${server.address().port}`);await page.evaluate(()=>window.start());
  await page.waitForFunction(()=>window.result.status==='ended'||window.result.errors.length>0,null,{timeout:60000});
  const result=await page.evaluate(()=>window.result);result.video=video;result.video_sha256=createHash('sha256').update(fs.readFileSync(video)).digest('hex');result.browser=await browser.version();result.scope='Automated Chromium real-time HTML video playback and decoder counters. No native VLC or perceptual audio review is implied.';
  const out=path.resolve(root,args.out||'qa/final/browser_playback.json');fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(result,null,2));console.log(JSON.stringify(result));
  if(result.status!=='ended'||result.errors.length)throw new Error('Browser playback failed; see report');
 }finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
}
