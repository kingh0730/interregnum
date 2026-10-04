import * as THREE from '/vendor/three/build/three.module.js';
import {SVGLoader} from '/vendor/three/examples/jsm/loaders/SVGLoader.js';
import {createFilm} from './film_runtime.mjs';
try{
  const q=new URLSearchParams(location.search),width=Number(q.get('width')||1920),height=Math.round(width*9/16);
  const json=async p=>{const r=await fetch(p);if(!r.ok)throw new Error(p+': HTTP '+r.status);return r.json();};
  const [shots,sync,onsets,cameraPaths]=await Promise.all(['shots','sync','onsets','camera_paths'].map(id=>json('/helper/'+id+'.json')));
  const assetResponse=await fetch('/helper/asset_map.json');
  const assetMap=assetResponse.ok?await assetResponse.json():{shots:{},diagnostic:'Asset map absent; pure-code shot preview only. Plate shots will fail.'};
  const wordmarkImage=await new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src='/assets/brand/anthropic-wordmark.svg';});
  const film=await createFilm({THREE,SVGLoader,width,height,assetMap,shots,sync,onsets,cameraPaths,brand:{wordmarkImage}});
  document.querySelector('#output').replaceWith(film.canvas);film.canvas.id='output';window.film=film;
  window.renderFrame=async frame=>{
    await film.renderFrame(frame);
    if(q.get('debug')==='1'){
      const ctx=film.canvas.getContext('2d'),s=width/1920,shot=shots.find(v=>frame>=v.f0&&frame<v.f1);
      const beat=sync.beats.reduce((a,b)=>Math.abs(a.frame-frame)<Math.abs(b.frame-frame)?a:b);
      ctx.save();ctx.scale(s,s);ctx.fillStyle='rgba(25,25,25,.85)';ctx.fillRect(30,30,760,125);
      ctx.font='500 30px Inter';ctx.fillStyle='#FAF9F5';ctx.fillText(`DEBUG · ${shot?.id} · f${frame} · ${(frame/30).toFixed(3)}s`,50,75);
      ctx.fillText(`B${beat.bar} beat ${beat.beat_in_bar} · nearest tick f${beat.frame}`,50,125);
      if(Math.abs(beat.frame-frame)<=1){ctx.fillStyle='#D97757';ctx.fillRect(1740,40,140,30);}ctx.restore();
    }
  };window.ready=true;
}catch(error){window.bootError=String(error.stack||error);console.error(error);}
