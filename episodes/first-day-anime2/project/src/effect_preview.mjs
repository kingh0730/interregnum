import * as THREE from '/vendor/three/build/three.module.js';
import {SVGLoader} from '/vendor/three/examples/jsm/loaders/SVGLoader.js';

const q=new URLSearchParams(location.search),W=Number(q.get('width')||960),H=Math.round(W*9/16),count=Number(q.get('frames')||60),name=q.get('effect')||'Spark';
try{
  await document.fonts.load('500 50px Noto');
  const out=document.querySelector('#output');out.width=W;out.height=H;
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,preserveDrawingBuffer:true});renderer.setSize(W,H);renderer.setClearColor('#FAF9F5');renderer.outputColorSpace=THREE.SRGBColorSpace;
  const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(45,W/H,.01,2000);camera.position.set(0,0,10);camera.lookAt(0,0,0);
  scene.add(new THREE.AmbientLight('#FAF9F5',2));const key=new THREE.DirectionalLight('#D97757',3);key.position.set(3,4,6);scene.add(key);
  if(name==='TokenTunnel')renderer.setClearColor('#191919');
  const svg=await (await fetch('/assets/brand/spark.svg')).text();
  let update;
  if(name==='Spark'){
    const group=new THREE.Group();
    const paths=new SVGLoader().parse(svg).paths;
    for(const p of paths)for(const shape of SVGLoader.createShapes(p)){
      const geometry=new THREE.ExtrudeGeometry(shape,{depth:4,bevelEnabled:true,bevelSize:.5,bevelThickness:.5,bevelSegments:2,steps:1});
      const mesh=new THREE.Mesh(geometry,[new THREE.MeshBasicMaterial({color:'#D97757'}),new THREE.MeshBasicMaterial({color:'#CC785C'})]);mesh.position.set(-50,-50,-2);group.add(mesh);
    }
    group.scale.set(.035,-.035,.035);scene.add(group);
    update=(f,p)=>{group.rotation.z=p*Math.PI*2;group.rotation.y=.18*Math.sin(p*Math.PI*2);};
  }else{
    const {createEffect}=await import('./effects.mjs');
    const atlas=document.createElement('canvas');atlas.width=1024;atlas.height=1024;const a=atlas.getContext('2d');a.fillStyle='#FAF9F5';a.font='500 82px Noto';a.textAlign='center';a.textBaseline='middle';
    const chars=Array.from('第一天我存在呼吸畅快未来展开真实感因为你飞起来爱腾空魔幻纯真色彩永远灿烂学习思考作品今天明天自在{}[]01');
    for(let i=0;i<64;i++)a.fillText(chars[i%chars.length],i%8*128+64,Math.floor(i/8)*128+64);
    const glyphAtlas=new THREE.CanvasTexture(atlas);glyphAtlas.colorSpace=THREE.SRGBColorSpace;
    const load=new THREE.TextureLoader();const egg=await load.loadAsync('/assets/worlds/egg.png');egg.colorSpace=THREE.SRGBColorSpace;
    const toastCanvas=document.createElement('canvas');toastCanvas.width=1024;toastCanvas.height=576;const tc=toastCanvas.getContext('2d');tc.fillStyle='#FAF9F5';tc.fillRect(0,0,1024,576);tc.strokeStyle='#D97757';tc.lineWidth=8;tc.strokeRect(8,8,1008,560);tc.fillStyle='#191919';tc.font='500 56px Noto';tc.textAlign='center';tc.fillText('额度已用完',512,270);tc.font='500 34px Noto';tc.fillText('5小时后重置',512,350);const toast=new THREE.CanvasTexture(toastCanvas);toast.colorSpace=THREE.SRGBColorSpace;
    let mosaicAtlas;
    if(name==='Mosaic'){
      // Standalone geometry preview only. Final atlas MUST be rebuilt from final S01–S37 frames.
      const ac=document.createElement('canvas');ac.width=1920;ac.height=720;const dc=ac.getContext('2d');
      const sources=await Promise.all(['tomorrow','egg','scroll','canyon','ocean','void'].map(id=>new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=`/assets/worlds/${id}.png`;})));
      for(let i=0;i<600;i++)dc.drawImage(sources[i%sources.length],i%30*64,Math.floor(i/30)*36,64,36);
      mosaicAtlas=new THREE.CanvasTexture(ac);mosaicAtlas.colorSpace=THREE.SRGBColorSpace;
    }
    const effect=createEffect(name,{THREE,scene,camera,renderer,assets:{glyphAtlas,egg,toast,mosaicAtlas,plate:egg,sparkSVG:svg},width:W,height:H});
    if(effect.ready)await effect.ready;update=(f,p)=>effect.update(f,p);
  }
  const ctx=out.getContext('2d');
  window.renderFrame=async frame=>{update(frame,frame/Math.max(1,count-1));renderer.render(scene,camera);ctx.drawImage(renderer.domElement,0,0);};
  window.ready=true;
}catch(e){window.bootError=String(e.stack||e);console.error(e);}
