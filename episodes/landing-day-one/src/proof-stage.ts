import * as T from 'three';
import {Doll} from './doll';
import {Painter} from './painter';
const painter=new Painter();let paintTex:T.CanvasTexture;
const dolls:Doll[]=[];
import {makeRT,FSPass,Compositor,W,H,PW,PH} from './vendor/pdoom/gl';
import {Post,DEFAULT_POST} from './vendor/pdoom/post';
import {clamp,lerp,ease,hash,TAU} from './vendor/pdoom/util';
import {Actor,phrase,neutral,COLORS,NAMES} from './rig';
const params=new URLSearchParams(location.search), proof=params.get('proof');
const renderer=new T.WebGLRenderer({canvas:document.querySelector('#film')!,antialias:true,preserveDrawingBuffer:true});
renderer.setSize(PW,PH,false);renderer.outputColorSpace=T.LinearSRGBColorSpace;renderer.toneMapping=T.NoToneMapping;
renderer.autoClear=false;
const rt=makeRT(),accA=makeRT(),accB=makeRT(),output=makeRT(W,H,{type:T.UnsignedByteType});
const post=new Post();const comp=new Compositor();
const dummy=new T.DataTexture(new Uint8Array([0,0,0,0]),1,1);dummy.needsUpdate=true;
const accumulator=new FSPass(`uniform sampler2D now,old;uniform float k;void main(){fragColor=mix(texture(old,vUv),texture(now,vUv),k);}`,{now:{value:null},old:{value:null},k:{value:1}});
const scene=new T.Scene();scene.background=new T.Color('#f4ede0');
const cam=new T.PerspectiveCamera(42,16/9,.05,500);
scene.add(new T.HemisphereLight('#fff6df','#b5aac3',3));const light=new T.DirectionalLight('#fff3d9',3);light.position.set(-5,10,5);scene.add(light);
const floor=new T.Mesh(new T.PlaneGeometry(500,500),new T.MeshStandardMaterial({color:'#f2dcd3',roughness:.32,metalness:.12}));floor.rotation.x=-Math.PI/2;floor.position.y=-.015;scene.add(floor);
const loader=new T.TextureLoader();let textures:any={};const actors:Actor[]=[];
const rings:T.Mesh[]=[];for(let i=0;i<30;i++){let m=new T.Mesh(new T.RingGeometry(.985,1,160),new T.MeshBasicMaterial({color:COLORS[i%6],transparent:true,opacity:0,side:T.DoubleSide,depthWrite:false}));m.rotation.x=-Math.PI/2;m.position.y=.015+i*.0001;scene.add(m);rings.push(m);}
let audioData:any,timeline:any;
const txt=document.createElement('canvas');txt.width=W;txt.height=H;const ctx=txt.getContext('2d')!;const txtTex=new T.CanvasTexture(txt);txtTex.colorSpace=T.SRGBColorSpace;
function overlay(f:number){ctx.clearRect(0,0,W,H);if(proof){ctx.fillStyle='#36312d';ctx.font='38px sans-serif';ctx.fillText('P2 · 到 — 我 — 存在',110,120);return;}
 const l=audioData.lyrics.find((l:any)=>f>=l.start_frame&&f<l.end_frame);if(l){ctx.textAlign='center';ctx.font='bold 94px "PingFang SC", sans-serif';ctx.lineWidth=9;ctx.strokeStyle='#f4ede0';ctx.fillStyle='#222029';ctx.strokeText(l.text,W/2,H-130);ctx.fillText(l.text,W/2,H-130);}
}
function reset(){dolls.forEach(d=>d.group.visible=false);actors.forEach(a=>{a.group.visible=false;a.group.rotation.set(0,0,0);a.group.scale.setScalar(1);a.mesh.visible=true;a.uniforms.alpha.value=1;a.uniforms.tint.value.set('white');});rings.forEach(r=>(r.material as T.MeshBasicMaterial).opacity=0);}
function ring(i:number,x:number,z:number,age:number,color:string,max=6){if(age<0||age>1)return;const r=rings[i%rings.length];r.position.set(x,.022+i*.0001,z);const rad=.02+max*ease.outExpo(age);r.scale.setScalar(rad);const m=r.material as T.MeshBasicMaterial;m.color.set(color).multiplyScalar(1.2);m.opacity=(1-age)*.85;}
function proofScene(f:number){reset();scene.background=new T.Color('#f4ede0');(floor.material as T.MeshStandardMaterial).color.set('#eee0d5');cam.position.set(.5,2.9,8);cam.lookAt(0,1.2,0);for(let i=0;i<3;i++){const d=dolls[i];d.group.visible=true;d.group.position.set((i-1)*2,0,0);d.pose(phrase(f/60));ring(i,(i-1)*2,0,(f/60-1.6)/.7,COLORS[i],2.5);}}
function basicScene(f:number){reset();const shot=timeline.find((s:any)=>f>=s.start&&f<s.end)||timeline.at(-1);const p=(f-shot.start)/(shot.end-shot.start);scene.background=new T.Color(shot.medium===7?'#0b0a2a':'#f4ede0');(floor.material as T.MeshStandardMaterial).color.set(shot.medium===7?'#151432':'#f1ded8');cam.position.set(Math.sin(f/240)*2,3.2,12);cam.lookAt(0,1,0);for(let i=0;i<6;i++){const a=actors[i];a.group.visible=true;a.group.position.set((i-2.5)*1.5,0,Math.sin(i)*.3);a.setTexture(textures[shot.medium===2?'cel':'toy'][i]);a.pose(phrase((f-shot.start)/60,'finale'));ring(i,(i-2.5)*1.5,0,p,COLORS[i]);}}
function draw(f:number,poseFrame:number){renderer.setRenderTarget(rt);renderer.clear();if(proof){proofScene(poseFrame);renderer.render(scene,cam);overlay(poseFrame);txtTex.needsUpdate=true;comp.draw(renderer,txtTex,rt);}else{painter.draw(f);paintTex.needsUpdate=true;comp.draw(renderer,paintTex,rt,{mode:'replace',premult:false});}}
async function renderFrame(f:number,samples=1){f=clamp(f,0,2620);if(!proof)await painter.prepare(Math.floor(f));const shot=timeline.find((s:any)=>f>=s.start&&f<s.end)||timeline.at(-1);let a=accA,b=accB;for(let k=0;k<samples;k++){const tf=Math.min(shot.end-.001,f+(k+.5)/samples*.25);draw(tf,Math.floor(f));accumulator.u.now.value=rt.texture;accumulator.u.old.value=a.texture;accumulator.u.k.value=1/(k+1);accumulator.render(renderer,b);[a,b]=[b,a];}const luminous=shot.medium===10||shot.medium===7;post.render(renderer,a.texture,dummy,output,{...DEFAULT_POST,bloom:luminous?.32:.07,halation:luminous?.05:.01,ca:luminous?.35:.05,grain:.006,vignette:.04,hud:0},Math.min(f,2610)/60);comp.draw(renderer,output.texture,null,{mode:'replace',premult:false});}
(window as any).ready=(async()=>{await painter.init();paintTex=new T.CanvasTexture(painter.canvas);paintTex.colorSpace=T.SRGBColorSpace;audioData=await(await fetch('/assets/audio-analysis.json')).json();timeline=await(await fetch('/assets/timeline.json')).json();for(const m of ['cel','toy']){textures[m]=await Promise.all(Array.from({length:6},(_,i)=>loader.loadAsync(`/assets/${m}/${i}.png`).then(t=>{t.colorSpace=T.SRGBColorSpace;return t;})));}for(const m of ['cel','toy'])for(let i=0;i<6;i++){const t=textures[m][i];for(const suffix of ['body','arm--1-0','arm--1-1','arm-1-0','arm-1-1']){const sub=await loader.loadAsync(`/assets/${m}/${i}-${suffix}.png`);sub.colorSpace=T.SRGBColorSpace;t.userData[suffix==='body'?'body':suffix.replace('arm-','arm').replace(/-([01])$/,'_$1')]=sub;}}for(let i=0;i<15;i++){const a=new Actor(textures.toy[i%6],i,[2.15,2.6,2.7,2.0,1.8,2.5][i%6]);scene.add(a.group);actors.push(a);}for(let i=0;i<18;i++){const d=new Doll(i);scene.add(d.group);dolls.push(d);}await document.fonts.ready;await renderFrame(Number(params.get('t')||0)*60);return true;})();
(window as any).renderFrame=renderFrame;
(window as any).readPixels=()=>{const buf=new Uint8Array(PW*PH*4);renderer.readRenderTargetPixels(output,0,0,PW,PH,buf);return buf;};
(window as any).stream=async(o:any)=>{await(window as any).ready;const ws=new WebSocket(o.ws);ws.binaryType='arraybuffer';await new Promise(r=>ws.onopen=r);let sent=0,acked=0;ws.onmessage=()=>acked++;for(let f=o.from;f<o.to;f++){while(sent-acked>=3)await new Promise(r=>setTimeout(r,2));await renderFrame(f,o.samples);ws.send((window as any).readPixels());sent++;}while(acked<sent)await new Promise(r=>setTimeout(r,2));ws.close();return sent;};
const audio=new Audio('/assets/first-day.wav');let playing=false;
(document.querySelector('#play')as HTMLElement).onclick=()=>{playing=!playing;playing?audio.play():audio.pause();};
(document.querySelector('#seek')as HTMLInputElement).oninput=e=>{audio.currentTime=Number((e.target as HTMLInputElement).value);renderFrame(audio.currentTime*60);};
if(params.has('export'))document.querySelector('#controls')!.remove();
function tick(){if(playing){renderFrame(audio.currentTime*60);(document.querySelector('#seek')as HTMLInputElement).value=String(audio.currentTime);document.querySelector('#time')!.textContent=audio.currentTime.toFixed(2);}requestAnimationFrame(tick);}tick();
