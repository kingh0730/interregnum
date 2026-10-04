/** Deterministic Three.js set pieces for OPUS55 §8.6.
 * createEffect(name,{THREE,scene,camera,renderer,assets,width,height})
 * update(localFrame, normalizedShotProgress); rendering remains caller-owned.
 * Textures must be preloaded THREE.Texture; URLs are also accepted (await ready).
 * TokenTunnel: glyphAtlas, glyphColumns=8, glyphRows=8; optional silhouette.
 * Shatter: egg; ToastShatter: toast. GlassCrack: plate.
 * Mosaic: mosaicAtlas, mosaicHero (finished final S37 frame), mosaicColumns=30, mosaicRows=20, sparkSVG.
 * diagnosticMissingHero:true explicitly permits non-final standalone geometry previews.
 * Optional sparkContains(x,y), x/y normalized 0..1, replaces SVG in non-DOM QA.
 * Bloom is compositor-owned: threshold .8, intensity .6. HDR emission supplied.
 */
export const PALETTE = Object.freeze({clay:'#D97757',ivory:'#FAF9F5',paper:'#F0EEE6',slate:'#191919',grey:'#B0AEA5',sky:'#6A9BCB',olive:'#788C5D',fig:'#C46686'});
export const EFFECT_NAMES=['TokenTunnel','Shatter','ToastShatter','GlassCrack','InkBloom','Mosaic','SpeedLines'];
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
export function seededRandom(seed=5505){return ()=>{seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t^=t+Math.imul(t^t>>>7,61|t);return ((t^t>>>14)>>>0)/4294967296;};}
/** Exact convex half-plane clipping, not triangle fragments pretending to be Voronoi. */
export function voronoiCells(count=240,seed=55){
 const rnd=seededRandom(seed), sites=Array.from({length:count},()=>[rnd()*2-1,rnd()*2-1]);
 return sites.map((s,i)=>{let poly=[[-1,-1],[1,-1],[1,1],[-1,1]];
  sites.forEach((t,j)=>{if(i===j||!poly.length)return;const nx=t[0]-s[0],ny=t[1]-s[1],c=(t[0]**2+t[1]**2-s[0]**2-s[1]**2)/2;const out=[];
   for(let k=0;k<poly.length;k++){const a=poly[k],b=poly[(k+1)%poly.length],da=a[0]*nx+a[1]*ny-c,db=b[0]*nx+b[1]*ny-c;if(da<=1e-9)out.push(a);if((da<0)!==(db<0)){const u=da/(da-db);out.push([a[0]+u*(b[0]-a[0]),a[1]+u*(b[1]-a[1])]);}}poly=out;});
  return {site:s,polygon:poly};});
}
// Texture samples tagged SRGBColorSpace decode on upload in Three r170.
// Shader uniforms and samples are linear; encode only the final framebuffer output.
const outputShader=fragment=>fragment.replace(/}\s*$/, '\n#include <colorspace_fragment>\n}');
const quadVertex=`varying vec2 vUv;void main(){vUv=uv;gl_Position=vec4(position.xy,0.,1.);}`;
const noiseGLSL=`float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453123);}float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*noise(p);p=mat2(.8,-.6,.6,.8)*p*2.03;a*=.5;}return v;}vec2 curl(vec2 p){float e=.025;return vec2(fbm(p+vec2(0,e))-fbm(p-vec2(0,e)),-fbm(p+vec2(e,0))+fbm(p-vec2(e,0)))/(2.*e);}`;
export function createEffect(name,{THREE:T,scene,camera,renderer,assets={},width=1920,height=1080}){
 if(!EFFECT_NAMES.includes(name))throw new Error(`Unknown effect: ${name}`);
 const root=new T.Group();root.name=`OPUS55:${name}`;scene.add(root);
 const owned=[], pending=[],rnd=seededRandom(5505),aspect=width/height;
 const own=x=>(owned.push(x),x);const color=x=>new T.Color(x);
 const texture=key=>{const value=assets[key];if(value?.isTexture)return value;if(typeof value!=='string')throw new Error(`${name} requires assets.${key}`);let tx;pending.push(new Promise((ok,no)=>{tx=new T.TextureLoader().load(value,ok,undefined,no);}));tx.colorSpace=T.SRGBColorSpace;return own(tx);};
 const plane=(fragment,uniforms,transparent=false)=>{const material=own(new T.ShaderMaterial({vertexShader:quadVertex,fragmentShader:outputShader(fragment),uniforms,transparent,depthTest:false,depthWrite:false}));const mesh=new T.Mesh(own(new T.PlaneGeometry(2,2)),material);mesh.frustumCulled=false;root.add(mesh);return mesh;};
 const setCamera=(z,fov=45,x=0,y=0)=>{camera.position.set(x,y,z);camera.lookAt(0,0,0);if(camera.isPerspectiveCamera){camera.fov=fov;camera.aspect=aspect;camera.updateProjectionMatrix();}};
 let tick=()=>{};const metadata={name,deterministic:true,bloom:{threshold:.8,intensity:.6}};
 function atlasMesh(count,map,columns,rows,additive=false){
  const geometry=own(new T.PlaneGeometry(1,1));geometry.setAttribute('tile',new T.InstancedBufferAttribute(Float32Array.from({length:count},(_,i)=>i%(columns*rows)),1));
  const material=own(new T.ShaderMaterial({uniforms:{atlas:{value:map},grid:{value:new T.Vector2(columns,rows)},tint:{value:color(PALETTE.ivory)},emission:{value:1}},vertexShader:`attribute float tile;uniform vec2 grid;varying vec2 vUv;void main(){vUv=(vec2(mod(tile,grid.x),grid.y-1.-floor(tile/grid.x))+uv)/grid;gl_Position=projectionMatrix*modelViewMatrix*instanceMatrix*vec4(position,1.);}`,fragmentShader:outputShader(`uniform sampler2D atlas;uniform vec3 tint;uniform float emission;varying vec2 vUv;void main(){vec4 c=texture2D(atlas,vUv);if(c.a<.01)discard;gl_FragColor=vec4(c.rgb*tint*emission,c.a);}`),transparent:true,depthWrite:!additive,side:T.DoubleSide,blending:additive?T.AdditiveBlending:T.NormalBlending}));
  const mesh=new T.InstancedMesh(geometry,material,count);mesh.frustumCulled=false;root.add(mesh);return mesh;
 }
 if(name==='TokenTunnel'){
  const mesh=atlasMesh(6000,texture('glyphAtlas'),assets.glyphColumns||8,assets.glyphRows||8,true),dummy=new T.Object3D();metadata.instances=6000;
  const path=new T.CatmullRomCurve3([new T.Vector3(0,0,8),new T.Vector3(-2,1,-10),new T.Vector3(2,-1,-30),new T.Vector3(-1,2,-60),new T.Vector3(0,0,-100)]);
  const particles=Array.from({length:6000},()=>({u:rnd(),angle:rnd()*Math.PI*2,r:2+rnd()*6,size:.055+rnd()*.22,roll:rnd()*6.28}));
  tick=(f,p)=>{const travel=p*.67;const c=path.getPoint(travel),target=path.getPoint(Math.min(.999,travel+.07));camera.position.copy(c);camera.lookAt(target);camera.fov=48+40*ease(p);camera.updateProjectionMatrix();
   particles.forEach((v,i)=>{const pt=path.getPoint(v.u);dummy.position.set(pt.x+Math.cos(v.angle+p*.25)*v.r,pt.y+Math.sin(v.angle+p*.25)*v.r,pt.z);dummy.quaternion.copy(camera.quaternion);dummy.rotateZ(v.roll);dummy.scale.set(v.size,v.size,1);dummy.updateMatrix();mesh.setMatrixAt(i,dummy.matrix);});mesh.instanceMatrix.needsUpdate=true;mesh.material.uniforms.tint.value.copy(color(PALETTE.grey)).lerp(color(PALETTE.clay),ease(p));mesh.material.uniforms.emission.value=1.4;};
 }else if(name==='Shatter'||name==='ToastShatter'){
  const count=name==='Shatter'?240:40,tex=texture(name==='Shatter'?'egg':'toast'),cells=voronoiCells(count);metadata.shards=count;metadata.gravity=.3;
  const key=new T.PointLight(PALETTE.clay,65,30,2);key.position.set(-3,4,6);root.add(key);root.add(new T.AmbientLight(PALETTE.ivory,1.5));
  const shards=cells.map(({site,polygon})=>{const [cx,cy]=site,positions=[],uvs=[];for(let j=1;j<polygon.length-1;j++)for(const [x,y] of [polygon[0],polygon[j],polygon[j+1]]){positions.push((x-cx)*aspect*3,(y-cy)*3,0);uvs.push((x+1)/2,(y+1)/2);}const g=own(new T.BufferGeometry());g.setAttribute('position',new T.Float32BufferAttribute(positions,3));g.setAttribute('uv',new T.Float32BufferAttribute(uvs,2));g.computeVertexNormals();const m=own(new T.MeshStandardMaterial({map:tex,roughness:.88,metalness:0,side:T.DoubleSide,transparent:true}));const obj=new T.Mesh(g,m);root.add(obj);return {obj,x:cx*aspect*3,y:cy*3,z:rnd()*4+1,rx:rnd()*5-2.5,ry:rnd()*5-2.5,rz:rnd()*3-1.5};});
  tick=(f,p)=>{setCamera(8-p*.8,45);const t=p*2.6;shards.forEach(s=>{s.obj.position.set(s.x*(1+t*.95),s.y*(1+t*.95)-.5*.3*t*t,s.z*t);s.obj.rotation.set(s.rx*t,s.ry*t,s.rz*t);s.obj.material.opacity=1-ease((p-.78)/.22);});};
 }else if(name==='GlassCrack'){
  const tex=texture('plate'),cells=voronoiCells(90,20),positions=[];
  cells.forEach(({polygon})=>polygon.forEach((a,i)=>{const b=polygon[(i+1)%polygon.length];positions.push(a[0]*aspect*3,a[1]*3,0,b[0]*aspect*3,b[1]*3,0);}));
  const ribbons=[];for(let i=0;i<positions.length;i+=6){const ax=positions[i],ay=positions[i+1],bx=positions[i+3],by=positions[i+4],len=Math.hypot(bx-ax,by-ay)||1,dx=-(by-ay)/len*.008,dy=(bx-ax)/len*.008;for(const v of [[ax+dx,ay+dy],[ax-dx,ay-dy],[bx+dx,by+dy],[ax-dx,ay-dy],[bx-dx,by-dy],[bx+dx,by+dy]])ribbons.push(v[0],v[1],0);}const g=own(new T.BufferGeometry());g.setAttribute('position',new T.Float32BufferAttribute(ribbons,3));const mat=own(new T.MeshBasicMaterial({color:PALETTE.clay,transparent:true,opacity:0,side:T.DoubleSide,blending:T.NormalBlending}));const lines=new T.Mesh(g,mat);root.add(lines);
  const uniforms={plate:{value:tex},progress:{value:0},aspect:{value:aspect}};
  const bg=plane(`varying vec2 vUv;uniform sampler2D plate;uniform float progress,aspect;${noiseGLSL}void main(){vec2 p=vUv-.5;float r=length(p*vec2(aspect,1.));vec2 shift=normalize(p+vec2(.0001))*sin(r*70.-progress*8.)*.018*progress;vec3 c=texture2D(plate,vUv+shift).rgb;float light=smoothstep(.82,1.,progress);gl_FragColor=vec4(mix(c,vec3(1.),light),1.);}`,uniforms);bg.renderOrder=-5;
  tick=(f,p)=>{uniforms.progress.value=p;mat.opacity=ease(p*4)*(1-ease((p-.8)/.2));mat.color.copy(color(PALETTE.clay)).multiplyScalar(1.4);lines.scale.setScalar(1+p*.4);setCamera(7-9*Math.pow(p,2),40+40*p);};
 }else if(name==='InkBloom'){
  metadata.sourceFrames=90;metadata.method='analytic backwards curl-noise dye advection; deterministic random-access shader';
  const u={time:{value:0},progress:{value:0},aspect:{value:aspect},clay:{value:color(PALETTE.clay)},sky:{value:color(PALETTE.sky)},olive:{value:color(PALETTE.olive)},fig:{value:color(PALETTE.fig)},paper:{value:color(PALETTE.paper)}};
  plane(`varying vec2 vUv;uniform float time,progress,aspect;uniform vec3 clay,sky,olive,fig,paper;${noiseGLSL}float dye(vec2 p,vec2 origin,float seed){vec2 q=p;for(int i=0;i<9;i++){q-=curl(q*2.+seed+time*.07)*(.008+progress*.018);}float d=length(q-origin);float edge=.045+progress*.65+fbm(q*9.+seed)*.12;return 1.-smoothstep(edge-.065,edge+.045,d);}void main(){vec2 p=(vUv-.5)*vec2(aspect,1.)/(1.+progress*.35);float a=dye(p,vec2(-.40,.15),1.),b=dye(p,vec2(.36,.18),4.),c=dye(p,vec2(-.25,-.26),8.),d=dye(p,vec2(.31,-.25),14.);float total=a+b+c+d;vec3 pigment=(clay*a+sky*b+olive*c+fig*d)/max(total,.0001);vec3 col=mix(paper,pigment,clamp(total,0.,1.)*.94);col+=(hash(gl_FragCoord.xy)-.5)/255.;col=mix(col,vec3(1.),smoothstep(.87,1.,progress));gl_FragColor=vec4(col,1.);}`,u);
  tick=(f,p)=>{u.time.value=p*89/30;u.progress.value=p;};
 }else if(name==='SpeedLines'){
  metadata.lines=32;const u={time:{value:0},aspect:{value:aspect},ink:{value:color(PALETTE.clay)},progress:{value:0}};
  plane(`varying vec2 vUv;uniform float time,aspect,progress;uniform vec3 ink;void main(){vec2 p=(vUv-.5)*vec2(aspect,1.);float r=length(p);float a=atan(p.y,p.x);float slot=(a+3.14159265)/6.2831853*32.;float id=floor(slot);float width=.025+.025*sin(id*4.13);float ray=1.-smoothstep(width,width+.012,abs(fract(slot)-.5));float start=.16+.22*(.5+.5*sin(id*2.37+time*15.));float len=.35+.25*sin(id*1.8+time*8.);float mask=smoothstep(start,start+.035,r)*(1.-smoothstep(start+len,start+len+.1,r));gl_FragColor=vec4(ink*1.2,ray*mask*.72);}`,u,true);
  tick=(f,p)=>{u.time.value=f/30;u.progress.value=p;};
 }else if(name==='Mosaic'){
  const atlas=texture('mosaicAtlas');let contains=assets.sparkContains;
  if(!contains){if(typeof assets.sparkSVG!=='string')throw new Error('Mosaic needs raw assets.sparkSVG or sparkContains');if(typeof document==='undefined')throw new Error('SVG mask sampling needs browser canvas or sparkContains');const doc=new DOMParser().parseFromString(assets.sparkSVG,'image/svg+xml'),svg=doc.documentElement;const box=(svg.getAttribute('viewBox')||'0 0 100 100').split(/[ ,]+/).map(Number);const paths=[...doc.querySelectorAll('path')].map(p=>new Path2D(p.getAttribute('d')));const ctx=document.createElement('canvas').getContext('2d');contains=(x,y)=>paths.some(path=>ctx.isPointInPath(path,box[0]+x*box[2],box[1]+y*box[3]));}
  const hasHero=!!assets.mosaicHero;if(!hasHero&&!assets.diagnosticMissingHero)throw new Error('Mosaic requires assets.mosaicHero; diagnosticMissingHero:true is permitted only for explicit standalone diagnostics');
  const heroWidth=.26,heroHeight=heroWidth/aspect,heroZ=.08,fov=40,startDistance=heroZ+heroHeight/(2*Math.tan(fov*Math.PI/360)),endDistance=110,tileCount=hasHero?599:600;
  const points=[];for(let tries=0;points.length<tileCount&&tries<100000;tries++){const x=rnd(),y=rnd(),wx=(x-.5)*10,wy=(.5-y)*10;const overlapsHero=hasHero&&Math.abs(wx)<heroWidth+.012&&Math.abs(wy)<heroHeight+.012;if(contains(x,y)&&!overlapsHero)points.push([x,y]);}if(points.length!==tileCount)throw new Error('Spark mask rejection sampler failed to place mosaic tiles');
  const mesh=atlasMesh(tileCount,atlas,assets.mosaicColumns||30,assets.mosaicRows||20,false),dummy=new T.Object3D();metadata.tiles=600;metadata.atlasTiles=tileCount;metadata.heroTile=hasHero;metadata.diagnosticMissingHero=!hasHero;metadata.mask='provided spark SVG paths, normalized viewBox';
  points.forEach(([x,y],i)=>{dummy.position.set((x-.5)*10,(.5-y)*10,(rnd()-.5)*.11);dummy.rotation.set(0,0,(rnd()-.5)*.09);dummy.scale.set(heroWidth,heroHeight,1);dummy.updateMatrix();mesh.setMatrixAt(i,dummy.matrix);});mesh.instanceMatrix.needsUpdate=true;mesh.material.uniforms.emission.value=1;
  if(hasHero){if(!contains(.5,.5))throw new Error('Mosaic spark mask has no center for hero tile');const hero=new T.Mesh(own(new T.PlaneGeometry(heroWidth,heroHeight)),own(new T.MeshBasicMaterial({map:texture('mosaicHero'),toneMapped:false,transparent:false,side:T.DoubleSide})));hero.name='MosaicFinishedHero';hero.position.z=heroZ;hero.renderOrder=10;root.add(hero);}
  metadata.projection={fov,startDistance,endDistance,heroWidth,heroHeight,heroZ,startHeroViewportFraction:1,endSparkHeightFraction:10/(2*endDistance*Math.tan(fov*Math.PI/360)),curve:'exponential positive camera pull-out'};
  metadata.bloom={enabled:false,reason:'Finished source tiles retain their baked light; no second bloom pass'};
  metadata.grade='Hero and atlas already finished; emission1, no second tone map. Caller bypasses global finish for this shot.';
  tick=(f,p)=>{root.rotation.z=.10*p;root.rotation.y=.08*Math.sin(p*Math.PI);setCamera(startDistance*Math.pow(endDistance/startDistance,p),fov);};
 }
 return {root,metadata,ready:Promise.all(pending),update(frame,progress){tick(frame,clamp(progress));},dispose(){scene.remove(root);for(const x of owned)x.dispose();}};
}
/** Minimal standalone setup; caller supplies actual production textures and renders each frame. */
export function createEffectPreview(name,{THREE,renderer,assets,width=960,height=540}){
 const scene=new THREE.Scene();scene.background=new THREE.Color(name==='TokenTunnel'?PALETTE.slate:PALETTE.paper);const camera=new THREE.PerspectiveCamera(45,width/height,.01,1000);camera.position.z=8;
 const effect=createEffect(name,{THREE,scene,camera,renderer,assets,width,height});return {...effect,scene,camera,render(frame,totalFrames=90){effect.update(frame,frame/Math.max(1,totalFrames-1));renderer.render(scene,camera);}};
}
