/** Real outline extrusion. No external imports or raster text.
 * Supply THREE and SVGLoader from the caller's same Three installation.
 * svgPaths={left:raw title-left.svg,right:raw title-right.svg}; sparkSVG=raw brand/spark.svg.
 * Or preparse each SVG with SVGLoader.parse and supply {paths}; cap defaults 1340.
 * Optional camera+fitCamera fit settled title at 180px nominal cap height at 1080p.
 * update(frame,duration) uses shot-local frames (30fps); deterministic and seekable.
 */
const clamp=x=>Math.max(0,Math.min(1,x));
export function titleSlamDescriptor(frame,duration=21){
 const f=Math.max(0,frame),u=clamp(f/5),remainder=(Math.exp(-5*u)*Math.cos(7*u)-Math.exp(-5)*Math.cos(7))/(1-Math.exp(-5)*Math.cos(7));
 const decay=1-clamp(f/20),shakeAmplitude=14*decay;
 return {scale:f>=5?1:1+2*remainder,shakeAmplitude,shakePixels:[Math.sin(f*9.13)*shakeAmplitude,Math.cos(f*7.71)*shakeAmplitude],shockRadius:.15+f*.20,shockOpacity:1-clamp(f/12),parallax:clamp((f-duration*.65)/(duration*.35)),capHeightPixelsAt1080:180,depth:.35};
}
export function createTitleSlam({THREE:T,scene,svgPaths,sparkSVG,SVGLoader,camera=null,width=1920,height=1080,capHeight=2,fitCamera=true,position=[0,0,0]}){
 if(!T||!scene||!SVGLoader||!svgPaths?.left||!svgPaths?.right||!sparkSVG)throw new Error('TitleSlam requires THREE, scene, SVGLoader, svgPaths.left/right, sparkSVG');
 const root=new T.Group();root.name='OPUS55:TitleSlam';root.position.set(...position);scene.add(root);
 const word=new T.Group();root.add(word);const owned=[];const own=x=>(owned.push(x),x);
 const face=own(new T.MeshBasicMaterial({color:'#FAF9F5'})),side=own(new T.MeshBasicMaterial({color:'#D97757'})),bevel=own(new T.MeshBasicMaterial({color:'#191919'}));
 const coralFace=own(new T.MeshBasicMaterial({color:'#D97757'}));const materials=[face,side,bevel];
 const parse=svg=>typeof svg==='string'?new SVGLoader().parse(svg):svg;
 const attr=(svg,key,fallback)=>typeof svg==='string'?Number(svg.match(new RegExp(`${key}="([0-9.]+)"`))?.[1]||fallback):fallback;
 const counts={shapes:0,triangles:0,face:0,side:0,bevel:0};
 function geometry(shape,unitsPerWorld){
  let g=new T.ExtrudeGeometry(shape,{depth:.35*unitsPerWorld,bevelEnabled:true,bevelThickness:.008*unitsPerWorld,bevelSize:.008*unitsPerWorld,bevelSegments:2,steps:1,curveSegments:18});
  if(g.index){const unindexed=g.toNonIndexed();g.dispose();g=unindexed;}
  // Three puts bevel and vertical walls in one material group. Split by normals.
  g.clearGroups();const normal=g.attributes.normal;let runStart=0,last=-1;
  for(let i=0;i<normal.count;i+=3){const z=(Math.abs(normal.getZ(i))+Math.abs(normal.getZ(i+1))+Math.abs(normal.getZ(i+2)))/3;const type=z>.9999?0:z<.0001?1:2;counts[['face','side','bevel'][type]]++;if(type!==last){if(last!==-1)g.addGroup(runStart,i-runStart,last);runStart=i;last=type;}}
  if(last!==-1)g.addGroup(runStart,normal.count-runStart,last);counts.shapes++;counts.triangles+=normal.count/3;return own(g);
 }
 function build(svg,unitsPerWorld,mats=materials){const group=new T.Group();for(const p of parse(svg).paths)for(const shape of SVGLoader.createShapes(p))group.add(new T.Mesh(geometry(shape,unitsPerWorld),mats));group.scale.set(1/unitsPerWorld,-1/unitsPerWorld,1/unitsPerWorld);return group;}
 const leftCap=attr(svgPaths.left,'data-cap-height',1340),rightCap=attr(svgPaths.right,'data-cap-height',1340);
 const leftWidth=attr(svgPaths.left,'data-advance',7984)/leftCap*capHeight,rightWidth=attr(svgPaths.right,'data-advance',1400)/rightCap*capHeight;
 const gap=capHeight*.13,sparkSize=capHeight*.25,totalWidth=leftWidth+rightWidth+2*gap+sparkSize;
 const left=build(svgPaths.left,leftCap/capHeight);left.position.set(-totalWidth/2,capHeight/2,0);word.add(left);
 // Exact supplied logo path. Center and normalize its actual outline bounds, retaining all rays.
 const sparkViewBox=typeof sparkSVG==='string'?sparkSVG.match(/viewBox="([^"]+)"/)?.[1]?.trim().split(/[ ,]+/).map(Number):null;const sparkUnits=Math.max(sparkViewBox?.[2]||100,sparkViewBox?.[3]||100)/sparkSize;const spark=build(sparkSVG,sparkUnits,[coralFace,side,bevel]);const sb=new T.Box3().setFromObject(spark),ss=new T.Vector3(),sc=new T.Vector3();sb.getSize(ss);sb.getCenter(sc);const sparkScale=sparkSize/Math.max(ss.x,ss.y);
 const sparkWrapper=new T.Group();sparkWrapper.add(spark);sparkWrapper.scale.set(sparkScale,sparkScale,1);spark.position.x-=sc.x;spark.position.y-=sc.y;sparkWrapper.position.set(-totalWidth/2+leftWidth+gap+sparkSize/2,-capHeight/2+sparkSize*.6,0);word.add(sparkWrapper);
 const right=build(svgPaths.right,rightCap/capHeight);right.position.set(-totalWidth/2+leftWidth+2*gap+sparkSize,capHeight/2,0);word.add(right);
 const ringMaterial=own(new T.MeshBasicMaterial({color:'#D97757',transparent:true,opacity:1,side:T.DoubleSide,depthWrite:false}));const ring=new T.Mesh(own(new T.RingGeometry(.975,1,128)),ringMaterial);ring.position.z=-.05;root.add(ring);
 const worldHeight=capHeight*1080/180,worldPerPixel=worldHeight/height;
 if(camera&&fitCamera){if(camera.isPerspectiveCamera){camera.aspect=width/height;camera.position.set(position[0],position[1],position[2]+worldHeight/(2*Math.tan(camera.fov*Math.PI/360)));camera.lookAt(...position);}else if(camera.isOrthographicCamera){camera.top=worldHeight/2;camera.bottom=-worldHeight/2;camera.left=-worldHeight*width/height/2;camera.right=-camera.left;camera.position.set(position[0],position[1],position[2]+15);camera.lookAt(...position);}camera.updateProjectionMatrix();}
 const metadata={text:'OPUS 5✱5',sourceText:'OPUS 5.5',font:'Newsreader',weight:800,opticalSize:72,capHeight,capHeightPixelsAt1080:180,totalWidth,worldHeight,depth:.35,geometry:counts,spark:'Exact supplied SVG, no unicode asterisk substitution',settledWidthFraction:totalWidth/(worldHeight*width/height)};
 return {root,metadata,update(frame,duration=21){const d=titleSlamDescriptor(frame,duration);word.scale.setScalar(d.scale);word.position.set(d.shakePixels[0]*worldPerPixel+d.parallax*.14,d.shakePixels[1]*worldPerPixel,0);word.rotation.y=-.08*d.parallax;ring.scale.setScalar(d.shockRadius*capHeight);ringMaterial.opacity=d.shockOpacity;return d;},dispose(){scene.remove(root);for(const x of owned)x.dispose();}};
}
