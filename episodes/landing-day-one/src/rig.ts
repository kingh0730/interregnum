import * as T from 'three';
import {clamp, keys, ease} from './vendor/pdoom/util';
export const COLORS=['#12a482','#d97757','#dce1ea','#4d6bfe','#ffe8cf','#c1a0ef','#615ced','#293c82','#416768','#e7b146','#65bcab','#f18478','#ec763f','#d6cabc','#c9dde1'];
export const NAMES=['ChatGPT','Claude','Grok','DeepSeek','豆包','Gemini','通义千问','Kimi','文心','元宝','智谱 GLM','MiniMax','星火','Llama','Mistral'];
export type Pose={raise:number;hand:number;crouch:number;step:number;lean:number;jump:number;turn:number};
export const neutral=():Pose=>({raise:0,hand:0,crouch:0,step:0,lean:0,jump:0,turn:0});
export function phrase(t:number,kind='landing'):Pose{
 const p=neutral();
 if(kind==='landing'){
  p.raise=keys(t,[[0,0],[.30,1],[.62,1],[.92,.25],[1.25,0],[3,0]]);
  p.hand=keys(t,[[0,0],[.7,0],[1.05,1],[1.35,1],[1.65,0],[3,0]]);
  p.crouch=keys(t,[[0,0],[1.05,0],[1.35,.06],[1.57,0],[1.60,.06],[1.72,.015],[1.9,0],[3,0]]);
  p.step=keys(t,[[0,0],[1.12,0],[1.36,.09],[1.56,.04],[1.60,0],[2.05,0],[2.23,.03],[2.38,0],[3,0]]);
  p.lean=keys(t,[[0,0],[.5,-.04],[1,.025],[1.6,.04],[2,0],[3,0]]);
 }else if(kind==='launch'){
  p.crouch=keys(t,[[0,0],[.18,.14],[.4,.14],[.52,0],[1.4,0]]);
  p.raise=keys(t,[[0,0],[.3,-.3],[.55,1],[1.5,.8]]);
  p.jump=keys(t,[[0,0],[.5,0],[.85,.8],[1.4,1.6]]);
  p.step=keys(t,[[0,0],[.32,.035],[.5,0],[1.4,.13]]);
 }else{
  const u=((t%1.65)+1.65)%1.65;
  p.step=keys(u,[[0,0],[.16,.10],[.28,0],[.44,-.08],[.57,0],[1,.1],[1.35,0],[1.65,0]]);
  p.raise=keys(u,[[0,.1],[.3,.6],[.55,.15],[.95,.85],[1.3,1],[1.65,.1]]);
  p.turn=keys(u,[[0,0],[.55,0],[.85,-.28],[1.05,.30],[1.45,0],[1.65,0]]);
  p.jump=keys(u,[[0,0],[.75,0],[1.10,.38],[1.4,0],[1.65,0]]);
  p.crouch=keys(u,[[0,.02],[.28,.06],[.4,0],[.57,.06],[.74,.10],[1.1,0],[1.4,.05],[1.65,.02]]);
 }
 return p;
}
const VERT=`
uniform float raise,hand,crouch,step,lean,height;
varying vec2 vUv;
void main(){
 vUv=uv; vec3 p=position; float y=p.y/height;float x=p.x/height;
 // Torso settles while both soles remain pinned to the floor.
 p.y-=crouch*height*smoothstep(.04,.58,y);
 p.x+=lean*height*smoothstep(.08,.85,y);
 // Alternating foot lifts keep the supporting leg locked, including toe taps.
 float side=sign(x);float lw=1.-smoothstep(.24,.53,y);float lift=max(0.,step*-side);
 p.y+=lift*height*lw;p.x+=side*lift*height*.15*lw;
 gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.);
}`;
const FRAG=`uniform sampler2D map;uniform vec3 tint;uniform float alpha;varying vec2 vUv;void main(){vec4 c=texture2D(map,vUv);if(c.a<.015)discard;gl_FragColor=vec4(c.rgb*tint,c.a*alpha);}`;
export class Actor{
 group=new T.Group();mesh:T.Mesh;shadow:T.Mesh;shadow2:T.Mesh;uniforms:any;h:number;shadowMat:T.ShaderMaterial; arms:any[]=[]; ar:number; index:number;
 constructor(tex:T.Texture,index:number,height=2.4){
  this.h=height;this.index=index%6;const ar=tex.image.width/tex.image.height;this.ar=ar;
  const geo=new T.PlaneGeometry(height*ar,height,48,90);geo.translate(0,height/2,0);
  this.uniforms={map:{value:tex},raise:{value:0},hand:{value:0},crouch:{value:0},step:{value:0},lean:{value:0},height:{value:height},tint:{value:new T.Color('white')},alpha:{value:1}};
  const mat=new T.ShaderMaterial({vertexShader:VERT,fragmentShader:FRAG,uniforms:this.uniforms,transparent:true,side:T.DoubleSide,depthWrite:true});
  this.mesh=new T.Mesh(geo,mat);this.group.add(this.mesh);
  const joints=[[[.33,.29],[.23,.43],[.085,.53]],[[.34,.22],[.23,.40],[.07,.56]],[[.31,.22],[.20,.40],[.07,.56]],[[.34,.36],[.22,.53],[.08,.63]],[[.32,.34],[.23,.52],[.08,.63]],[[.30,.24],[.19,.40],[.08,.56]]][index%6];
  for(const side of [-1,1]){
   const P=joints.map(q=>new T.Vector3(((side<0?q[0]:1-q[0])-.5)*height*ar,(1-q[1])*height,0));
   const upper=new T.Group(),lower=new T.Group();upper.position.copy(P[0]);lower.position.copy(P[1]).sub(P[0]);upper.add(lower);this.group.add(upper);
   const parts=[];
   for(let j=0;j<2;j++){const g=geo.clone();g.translate(-P[j].x,-P[j].y,.003+j*.001);const m=new T.MeshBasicMaterial({map:tex,transparent:true,side:T.DoubleSide,depthWrite:false});const mesh=new T.Mesh(g,m);(j?lower:upper).add(mesh);parts.push(mesh);}
   this.arms.push({side,upper,lower,parts,pivot:P[0]});
  }
  this.setTexture(tex);
  const su={...this.uniforms,tint:{value:new T.Color('#342c24')},alpha:{value:.23}};
  this.shadowMat=new T.ShaderMaterial({vertexShader:VERT,fragmentShader:FRAG,uniforms:su,transparent:true,side:T.DoubleSide,depthWrite:false});
  this.shadow=new T.Mesh(geo,this.shadowMat);this.shadow.rotation.x=-Math.PI/2;this.shadow.scale.set(1,.68,1);this.shadow.position.set(.12,.008,-.03);this.group.add(this.shadow);
  this.shadow2=this.shadow.clone();this.shadow2.rotation.z=.21;this.shadow2.visible=index===5;this.group.add(this.shadow2);
 }
 setTexture(tex:T.Texture){this.uniforms.map.value=tex.userData.body||tex;for(const a of this.arms)for(let j=0;j<2;j++)a.parts[j].material.map=tex.userData[`arm${a.side}_${j}`]||tex;}
 pose(p:Pose,shadow=true){for(const k of ['raise','hand','crouch','step','lean'])this.uniforms[k].value=p[k];this.mesh.position.y=p.jump*this.h;this.mesh.rotation.y=p.turn;
 for(const a of this.arms){a.upper.position.copy(a.pivot);a.upper.position.y+=p.jump*this.h-p.crouch*this.h;a.upper.position.x+=p.lean*this.h*.7;a.upper.rotation.z=a.side*(p.raise*1.05-p.hand*.4);a.lower.rotation.z=a.side*(p.raise*.4+p.hand*1.25);a.upper.visible=this.mesh.visible;for(const m of a.parts){m.material.opacity=this.uniforms.alpha.value;m.material.color.copy(this.uniforms.tint.value);}}
 this.shadow.visible=shadow;this.shadowMat.uniforms.alpha.value=.24*Math.exp(-p.jump*2);const s=1/(1+p.jump*.6);this.shadow.scale.set(s,.68*s,1);this.shadow2.scale.copy(this.shadow.scale);}
}
