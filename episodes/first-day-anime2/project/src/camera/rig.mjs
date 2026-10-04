/** Deterministic frame-addressable camera. World: +X right, +Y up, +Z toward viewer.
 * Keys use degrees for roll/FOV. No wall-clock state; arbitrary render order is safe.
 * GEN-V owns its camera unless path.cameraOwner is explicitly changed to 'code'.
 */
const clamp = (x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const mix = (a,b,t)=>a+(b-a)*t;
export function cubicBezier(x, curve=[.42,0,.58,1]) {
  const [a,b,c,d]=curve, bez=(t,p,q)=>3*(1-t)**2*t*p+3*(1-t)*t*t*q+t*t*t;
  let lo=0,hi=1;
  for(let n=0;n<30;n++){const m=(lo+hi)/2;if(bez(m,a,c)<x)lo=m;else hi=m;}
  return x<=0?0:x>=1?1:bez((lo+hi)/2,b,d);
}
/** Integrate a piecewise-linear positive velocity envelope and normalize distance. */
export function speedProgress(t, ramp) {
  if(!ramp?.length)return clamp(t);
  const points=ramp.map(p=>[clamp(p[0]),Math.max(0,p[1])]);
  if(points[0][0]>0)points.unshift([0,points[0][1]]);
  if(points.at(-1)[0]<1)points.push([1,points.at(-1)[1]]);
  let total=0,partial=0;
  for(let i=1;i<points.length;i++) {
    const [a,va]=points[i-1],[b,vb]=points[i],w=b-a;
    if(w<=0)continue;
    total+=w*(va+vb)/2;
    const x=clamp(t-a,0,w);partial+=va*x+(vb-va)*x*x/(2*w);
  }
  return total?partial/total:0;
}
// Seeded 2D simplex gradient noise; output is continuous and independent of render order.
function simplex(seed=55) {
  let state=seed>>>0;
  const perm=Array.from({length:256},(_,i)=>i);
  for(let i=255;i>0;i--){state=(Math.imul(state,1664525)+1013904223)>>>0;const j=state%(i+1);[perm[i],perm[j]]=[perm[j],perm[i]];}
  const p=Array.from({length:512},(_,i)=>perm[i&255]);
  const grad=[[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]];
  return (x,y)=>{
    const F=(Math.sqrt(3)-1)/2,G=(3-Math.sqrt(3))/6,s=(x+y)*F;
    const i=Math.floor(x+s),j=Math.floor(y+s),u=(i+j)*G,x0=x-i+u,y0=y-j+u;
    const ix=x0>y0?1:0,iy=1-ix;
    const coords=[[x0,y0,0,0],[x0-ix+G,y0-iy+G,ix,iy],[x0-1+2*G,y0-1+2*G,1,1]];
    let sum=0;
    for(const [dx,dy,di,dj] of coords){let w=.5-dx*dx-dy*dy;if(w>0){const g=grad[p[((i+di)&255)+p[(j+dj)&255]]%8];sum+=w**4*(g[0]*dx+g[1]*dy);}}
    return 70*sum;
  };
}
export function createRigCamera({THREE,camera,path,width=1920,height=1080}) {
  if(!path?.keyframes?.length)throw new Error('Camera path requires keyframes');
  const keys=path.keyframes,rad=Math.PI/180,up=new THREE.Vector3(0,1,0);
  const points=keys.map(k=>new THREE.Vector3(...k.pos));
  const curve=points.length>1?new THREE.CatmullRomCurve3(points,false,'centripetal'):null;
  const orientations=keys.map(k=>{
    if(k.quaternion)return new THREE.Quaternion(...k.quaternion).normalize();
    const m=new THREE.Matrix4().lookAt(new THREE.Vector3(...k.pos),new THREE.Vector3(...k.target),up);
    return new THREE.Quaternion().setFromRotationMatrix(m);
  });
  const noise=simplex(path.seed||55);
  const duration=path.durationFrames||30;
  function sample(progress,options={}) {
    let p=clamp(progress),frame=options.localFrame??p*Math.max(1,duration-1);
    const frames=options.durationFrames??duration;
    if(path.freeze){p=0;frame=0;}
    if(path.holdLastFrames){const stop=Math.max(0,frames-path.holdLastFrames);frame=Math.min(frame,stop);p=stop?clamp(frame/stop):1;}
    const generationOwned=path.cameraOwner==='generation'&&!options.intended;
    const rawP=p;
    p=generationOwned?0:speedProgress(p,path.speedRamp);
    if(path.globalEase&&!generationOwned)p=cubicBezier(p,path.globalEase);
    let i=0;while(i<keys.length-2&&p>keys[i+1].t)i++;
    const a=keys[i],b=keys[Math.min(i+1,keys.length-1)];
    const t=b.t>a.t?cubicBezier(clamp((p-a.t)/(b.t-a.t)),a.ease||path.ease):0;
    const pos=generationOwned?new THREE.Vector3(0,0,10):curve?curve.getPoint((i+t)/(keys.length-1)):points[0].clone();
    const q=generationOwned?new THREE.Quaternion():orientations[i].clone().slerp(orientations[Math.min(i+1,keys.length-1)],t);
    const roll=generationOwned?0:mix(a.roll||0,b.roll||0,t);
    q.multiply(new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(0,0,1),roll*rad));
    let fov=generationOwned?50:mix(a.fov??50,b.fov??50,t);
    const target=new THREE.Vector3(...a.target).lerp(new THREE.Vector3(...b.target),t);
    if(path.dollyZoom&&!generationOwned){const d=pos.distanceTo(new THREE.Vector3(...path.dollyZoom.target));fov=2*Math.atan(path.dollyZoom.frustumHeight/(2*Math.max(.01,d)))/rad;}
    const shake=path.shake;
    if(shake&&!generationOwned&&!path.freeze){
      const env=shake.decayFrames?clamp(1-frame/shake.decayFrames):1;
      const window=shake.onlyFrames?frame<shake.onlyFrames: true;
      const worldPerPixel=2*pos.distanceTo(target)*Math.tan(fov*rad/2)/height;
      const seconds=frame/(path.fps||30),amp=(shake.amplitudePx||0)*env*(window?1:0)*worldPerPixel;
      pos.add(new THREE.Vector3(noise(seconds*(shake.frequency||8),1)*amp,noise(71,seconds*(shake.frequency||8))*amp,0).applyQuaternion(q));
    }
    if(path.dip&&!generationOwned&&frame>=path.dip.frame&&frame<path.dip.frame+path.dip.frames){
      const delta=2*pos.distanceTo(target)*Math.tan(fov*rad/2)/height*path.dip.pixels;
      pos.add(new THREE.Vector3(0,delta,0).applyQuaternion(q));
    }
    return {position:pos.toArray(),quaternion:q.toArray(),target:target.toArray(),fov,roll,progress:p,sourceProgress:rawP,
      focusDistance:mix(a.focusDistance??pos.distanceTo(target),b.focusDistance??pos.distanceTo(target),t),
      actionTimeScale:path.actionTimeScale??1,cameraOwner:path.cameraOwner,shutter:path.shutter||0};
  }
  function update(localFrame,durationFrames=duration){
    const state=sample(localFrame/Math.max(1,durationFrames-1),{localFrame,durationFrames});
    camera.position.fromArray(state.position);camera.quaternion.fromArray(state.quaternion);
    camera.fov=state.fov;camera.aspect=width/height;camera.updateProjectionMatrix();camera.updateMatrixWorld();
    return state;
  }
  return {sample,update};
}
