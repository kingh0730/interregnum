import * as THREE from 'three';
import catalog from '../text/media.json';
import film from '../text/film.json';
import tracking from '../text/tracking.json';
const {clamp,smoothstep}=window.RT;
const shotAt=t=>film.shots.find(s=>t>=s.frame/30&&t<s.end_frame/30)||film.shots.at(-1);
export function sourceTime(id,t){const c=catalog[id];if(!c)return 0;const s=film.shots[+id.slice(1)-1];let a=s.frame/30,b=s.end_frame/30,u=clamp((t-a)/(b-a),0,1),start=c.source_start||0,end=c.source_end;
 if(c.source_id==='FLIGHT')return ((t-25.45)%end+end)%end;
 if(id==='S34')return clamp(t-30.68,0,1.2);
 if(id==='S20')return u<.72?.88*u/.72:.88+(end-.88)*(u-.72)/.28;
 if(id==='S25'){if(t<24)return .1*clamp((t-a)/(24-a),0,1);if(t<25.1)return .1+(end-.5)*(t-24)/1.1;return end-.4+.4*clamp((t-25.1)/(b-25.1),0,1);}
 return start+(end-start)*u;
}
export function tracked(id,name,t){const owner=catalog[id]?.source_id||id,d=tracking[owner];if(!d?.marks[name])return null;let f=sourceTime(id,t)*d.fps,lo=Math.min(d.marks[name].length-1,Math.floor(f)),hi=Math.min(d.marks[name].length-1,lo+1),u=f-lo,a=d.marks[name][lo],b=d.marks[name][hi];return a.map((v,i)=>v+(b[i]-v)*u);}
export class MediaCache{
 constructor(){this.map=new Map();this.prefix=window.RT.SCALE<1?'/plates_preview':'/plates';this.time=0;}
 desc(id){return catalog[id];}
 index(id,t){let c=catalog[id];return Math.min(c.frames-1,Math.max(0,Math.round(sourceTime(id,t)*c.fps)));}
 key(id,index){return `${catalog[id].source_id}/${index}`;}
 async prepare(t){const id=shotAt(t).id,c=catalog[id];this.time=t;if(!c)return;let centre=this.index(id,t),lo=Math.max(0,Math.min(c.frames-48,centre-12)),hi=Math.min(c.frames-1,lo+47),needed=new Set();for(let i=lo;i<=hi;i++)needed.add(this.key(id,i));for(const[k,v]of this.map){if(!needed.has(k)){v.texture.dispose();if(v.mirrorTexture)v.mirrorTexture.dispose();v.bitmap.close();v.glBitmap.close();if(v.depthTexture){v.depthTexture.dispose();v.depthBitmap.close();}this.map.delete(k);}}
 const jobs=[];for(let i=lo;i<=hi;i++){let key=this.key(id,i);if(this.map.has(key))continue;jobs.push((async()=>{let url=`${this.prefix}/${c.source_id}/${String(i).padStart(4,'0')}.png`;let response=await fetch(url);if(!response.ok)throw Error(`Required offline plate missing: ${url}`);let blob=await response.blob();let bitmap=await createImageBitmap(blob,{premultiplyAlpha:'none',colorSpaceConversion:'none'}),glBitmap=await createImageBitmap(blob,{imageOrientation:'flipY',premultiplyAlpha:c.premultiply?'premultiply':'none',colorSpaceConversion:'none'});let texture=new THREE.Texture(glBitmap);texture.flipY=false;texture.colorSpace=THREE.SRGBColorSpace;texture.minFilter=THREE.LinearMipmapLinearFilter;texture.magFilter=THREE.LinearFilter;texture.generateMipmaps=true;texture.needsUpdate=true;let entry={bitmap,glBitmap,texture};if(c.mirror){let mirror=texture.clone();mirror.wrapS=THREE.RepeatWrapping;mirror.repeat.x=-1;mirror.offset.x=1;mirror.needsUpdate=true;entry.mirrorTexture=mirror;}if(c.source_id==='S44'){let dr=await fetch(url.replace('.png','.depth.png'));if(!dr.ok)throw Error('Missing dynamic meadow depth');let db=await createImageBitmap(await dr.blob(),{imageOrientation:'flipY',premultiplyAlpha:'none',colorSpaceConversion:'none'});let dt=new THREE.Texture(db);dt.flipY=false;dt.minFilter=dt.magFilter=THREE.LinearFilter;dt.generateMipmaps=false;dt.needsUpdate=true;entry.depthTexture=dt;entry.depthBitmap=db;let c=document.createElement('canvas');c.width=257;c.height=145;let x=c.getContext('2d');x.translate(0,145);x.scale(1,-1);x.drawImage(db,0,0,257,145);entry.depthPixels=x.getImageData(0,0,257,145).data;}this.map.set(key,entry);})());}await Promise.all(jobs);}
 get(id,t){const c=catalog[id];if(!c)return null;let i=this.index(id,t),v=this.map.get(this.key(id,i));if(!v)throw Error(`Frame ${id}/${i} was not prefetched; never decode inside render`);return v;}
 image(id,t){return this.get(id,t)?.bitmap;}
 texture(id,t){return this.get(id,t)?.texture;}
}
