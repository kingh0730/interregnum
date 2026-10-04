import * as THREE from 'three';import {setCamera} from './camera.js';import {write} from './text.js';
const{clamp,smoothstep,easeInOutCubic}=window.RT;
export class PaperReveal{
 constructor(renderer,W,H){this.renderer=renderer;this.W=W;this.H=H;this.scene=new THREE.Scene();this.scene.background=new THREE.Color('#F0EEE6');this.camera=new THREE.PerspectiveCamera(45,W/H,.005,50);this.papers=[];
 let c=document.createElement('canvas');c.width=1024;c.height=1024;let x=c.getContext('2d');x.fillStyle='#F0EEE6';x.fillRect(0,0,1024,1024);x.strokeStyle='#141413';x.lineWidth=2;for(let s=0;s<4;s++)for(let l=0;l<5;l++){x.beginPath();x.moveTo(70,160+s*210+l*16);x.lineTo(954,160+s*210+l*16);x.stroke();}write(x,'5.5',85,145,55,'#141413','Lora-SemiBold','left');for(let i=0;i<28;i++){x.save();x.translate(140+(i%7)*125,180+Math.floor(i/7)*210+(i%3)*8);x.rotate(-.3);x.fillStyle='#141413';x.beginPath();x.ellipse(0,0,12,8,0,0,Math.PI*2);x.fill();x.fillRect(8,-49,3,49);x.restore();}
 let tex=new THREE.CanvasTexture(c);tex.colorSpace=THREE.SRGBColorSpace;
 const parts=[[0,0,.7,1.05,0],[0,.78,.4,.5,0],[-.64,.15,.4,1.05,-1],[.64,.15,.4,1.05,1],[-.21,-.87,.36,.85,-.2],[.21,-.87,.36,.85,.2]];
 for(let [px,py,w,h,a] of parts){let pivot=new THREE.Group();pivot.position.set(px,py,0);let mesh=new THREE.Mesh(new THREE.PlaneGeometry(w,h,1,1),new THREE.MeshBasicMaterial({map:tex,side:THREE.DoubleSide,toneMapped:false}));pivot.add(mesh);this.scene.add(pivot);this.papers.push({pivot,a,px,py});}
 }
 async init(closed,opened){const loader=new THREE.TextureLoader();this.closed=await loader.loadAsync(closed);this.open=await loader.loadAsync(opened);for(let t of [this.closed,this.open])t.colorSpace=THREE.SRGBColorSpace;this.eye=new THREE.Mesh(new THREE.PlaneGeometry(3.2,1.8),new THREE.MeshBasicMaterial({map:this.closed,toneMapped:false}));this.eye.position.z=-.25;this.scene.add(this.eye);}
 project(u,v,size){let p=new THREE.Vector3((u-.5)*3.2,(.5-v)*1.8,-.25),q=p.clone().add(new THREE.Vector3(size*3.2,0,0));p.project(this.camera);q.project(this.camera);return[(p.x*.5+.5)*this.W,(-p.y*.5+.5)*this.H,Math.abs(q.x-p.x)*this.W*.5];}
 render(t,u){let unfold=smoothstep(0,.3,u);for(let {pivot,a,px,py}of this.papers){pivot.position.set(px*unfold,py*unfold,.05);pivot.rotation.set((1-unfold)*Math.PI*.95,a*unfold+(1-unfold)*Math.PI/2,0);pivot.visible=u<.29;}this.eye.visible=u>.15;this.eye.material.map=t>=12.93?this.open:this.closed;let d=3.9*(1-easeInOutCubic(clamp(u/.45,0,1)))+.6;setCamera(this.camera,[0,0,d],[0,0,0],24);this.renderer.render(this.scene,this.camera);return this.renderer.domElement;}
}
