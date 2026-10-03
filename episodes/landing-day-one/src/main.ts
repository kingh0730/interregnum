import * as T from 'three';
import {makeRT,FSPass,Compositor,W,H,PW,PH} from './vendor/pdoom/gl';
import {Post,DEFAULT_POST} from './vendor/pdoom/post';
import {clamp} from './vendor/pdoom/util';
import {Painter} from './painter';
import {InkLens} from './lens';
const params=new URLSearchParams(location.search);
if(params.has('proof')){await import('./proof-stage');}
else{
 const painter=new Painter();if(params.has('clean'))painter.typeEnabled=false;
 const renderer=new T.WebGLRenderer({canvas:document.querySelector('#film')!,antialias:false,preserveDrawingBuffer:true});
 renderer.setSize(PW,PH,false);renderer.outputColorSpace=T.LinearSRGBColorSpace;renderer.toneMapping=T.NoToneMapping;renderer.autoClear=false;
 const rt=makeRT(),lensRT=makeRT(),accA=makeRT(),accB=makeRT(),output=makeRT(W,H,{type:T.UnsignedByteType});
 const post=new Post(),comp=new Compositor(),lens=new InkLens();
 const dummy=new T.DataTexture(new Uint8Array([0,0,0,0]),1,1);dummy.needsUpdate=true;
 const accumulator=new FSPass(`uniform sampler2D now,old;uniform float k;void main(){fragColor=k>.999?texture(now,vUv):mix(texture(old,vUv),texture(now,vUv),k);}`,{now:{value:null},old:{value:null},k:{value:1}});
 let texture:T.CanvasTexture;
 async function renderFrame(f:number,samples=1){
  f=clamp(f,0,2620);await painter.prepare(Math.floor(f));const shot=painter.timeline.find((s:any)=>f>=s.start&&f<s.end)||painter.timeline.at(-1);let a=accA,b=accB;
  for(let k=0;k<samples;k++){
   const tf=Math.min(shot.end-.001,f+(k+.5)/samples*.25);painter.draw(tf);texture.needsUpdate=true;comp.draw(renderer,texture,rt,{mode:'replace',premult:false});
   let src=rt.texture;if(f>=2470){lens.u.src.value=src;lens.u.strength.value=clamp((Math.min(f,2530)-2470)/60)*.6;lens.u.time.value=Math.min(f,2610)/60;lens.render(renderer,lensRT);src=lensRT.texture;}
   accumulator.u.now.value=src;accumulator.u.old.value=a.texture;accumulator.u.k.value=1/(k+1);accumulator.render(renderer,b);[a,b]=[b,a];
  }
  const luminous=shot.medium===10||shot.medium===7;
  post.render(renderer,a.texture,dummy,output,{...DEFAULT_POST,bloom:luminous?.30:.065,halation:luminous?.04:.008,ca:luminous?.25:.04,grain:.005,vignette:.025,hud:0},Math.min(f,2610)/60);
  comp.draw(renderer,output.texture,null,{mode:'replace',premult:false});
 }
 (window as any).ready=(async()=>{await painter.init();texture=new T.CanvasTexture(painter.canvas);texture.colorSpace=T.SRGBColorSpace;await renderFrame(Number(params.get('t')||0)*60);return true;})();
 (window as any).renderFrame=renderFrame;
 (window as any).audit=()=>({missing:[...painter.missing],shots:painter.timeline.length,images:Object.keys(painter.images).length});
 const pixelBuffer=new Uint8Array(PW*PH*4);
 (window as any).readPixels=()=>{renderer.readRenderTargetPixels(output,0,0,PW,PH,pixelBuffer);return pixelBuffer;};
 (window as any).stream=async(o:any)=>{await(window as any).ready;const ws=new WebSocket(o.ws);ws.binaryType='arraybuffer';await new Promise(r=>ws.onopen=r);let sent=0,acked=0;ws.onmessage=()=>acked++;for(let f=o.from;f<o.to;f++){while(sent-acked>=2)await new Promise(r=>setTimeout(r,2));await renderFrame(f,o.samples);ws.send((window as any).readPixels());sent++;}while(acked<sent)await new Promise(r=>setTimeout(r,2));ws.close();return sent;};
 const audio=new Audio('/assets/first-day.wav');let playing=false,busy=false;
 (document.querySelector('#play')as HTMLElement).onclick=()=>{playing=!playing;playing?audio.play():audio.pause();};
 (document.querySelector('#seek')as HTMLInputElement).oninput=e=>{audio.currentTime=Number((e.target as HTMLInputElement).value);renderFrame(audio.currentTime*60);};
 if(params.has('export'))document.querySelector('#controls')!.remove();
 async function tick(){if(playing&&!busy){busy=true;await renderFrame(audio.currentTime*60);(document.querySelector('#seek')as HTMLInputElement).value=String(audio.currentTime);document.querySelector('#time')!.textContent=audio.currentTime.toFixed(2);busy=false;}requestAnimationFrame(tick);}tick();
}
