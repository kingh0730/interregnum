/** Image-based set geometry, never a character puppet. No animation or depth inference.
 * width/height are output pixels; worldHeight defaults to neutral camera's 50-degree
 * frustum at distance 10 (9.326153 units). Supplied layer z values are world units.
 */
export function createParallax({THREE,scene,plate,depth,mask,layers,width=1920,height=1080}) {
  if(!THREE||!scene)throw new Error('THREE and scene are required');
  const descriptor=plate?.isTexture||plate?.getContext||plate?.tagName?{image:plate}:(plate||{});
  const pad=descriptor.paddingFraction??.1;
  if(pad<.08)throw new Error('Use at least 8% edge padding');
  const worldHeight=descriptor.worldHeight??20*Math.tan(25*Math.PI/180);
  const worldWidth=worldHeight*width/height;
  const group=new THREE.Group();group.name='Parallax25D';
  const resources=[],meshes=[],warnings=[],layerRecords=[];
  const previousBackground=scene.background;
  const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
  function pixels(input,label){
    if(!input)throw new Error(label+' missing');
    if(input.data&&input.width&&input.height){
      const channels=input.channels??input.data.length/(input.width*input.height);
      if(![1,3,4].includes(channels))throw new Error(label+' requires 1, 3, or 4 channels');
      return {...input,channels};
    }
    if(input.getContext){const d=input.getContext('2d',{willReadFrequently:true}).getImageData(0,0,input.width,input.height);return {...d,data:d.data,width:d.width,height:d.height,channels:4};}
    if(input.width&&input.height&&typeof document!=='undefined'){
      const canvas=document.createElement('canvas');canvas.width=input.width;canvas.height=input.height;
      canvas.getContext('2d').drawImage(input,0,0);return pixels(canvas,label);
    }
    throw new Error(label+' must be readable ImageData, canvas, image, or {data,width,height,channels}');
  }
  function texture(input,label,color=true){
    if(!input)throw new Error(label+' missing');
    let tex;
    if(input.isTexture)tex=input.clone();
    else if(input.data){
      const d=pixels(input,label),rgba=new Uint8Array(d.width*d.height*4);
      for(let i=0;i<d.width*d.height;i++){
        rgba[i*4]=d.data[i*d.channels];rgba[i*4+1]=d.data[i*d.channels+(d.channels>1?1:0)];rgba[i*4+2]=d.data[i*d.channels+(d.channels>1?2:0)];rgba[i*4+3]=d.channels===4?d.data[i*4+3]:255;
      }
      tex=new THREE.DataTexture(rgba,d.width,d.height,THREE.RGBAFormat);tex.flipY=true;
    } else tex=new THREE.Texture(input);
    tex.wrapS=tex.wrapT=THREE.ClampToEdgeWrapping;
    tex.minFilter=tex.magFilter=THREE.LinearFilter;tex.generateMipmaps=false;
    tex.colorSpace=color?THREE.SRGBColorSpace:THREE.NoColorSpace;tex.needsUpdate=true;
    resources.push(tex);return tex;
  }
  function value(d,u,v){
    // ImageData starts at top left while UV v=1 is the top edge.
    const x=clamp(u)*(d.width-1),y=(1-clamp(v))*(d.height-1),x0=Math.floor(x),y0=Math.floor(y),x1=Math.min(x0+1,d.width-1),y1=Math.min(y0+1,d.height-1);
    const read=(xx,yy)=>d.data[(yy*d.width+xx)*d.channels]/(d.normalized?1:255);
    const a=read(x0,y0)*(1-x+x0)+read(x1,y0)*(x-x0),b=read(x0,y1)*(1-x+x0)+read(x1,y1)*(x-x0);
    return clamp(a*(1-y+y0)+b*(y-y0));
  }
  const mode=layers?.length?'separate-layers':depth?'depth-displaced':descriptor.diagnosticFlat?'diagnostic-flat':null;
  if(!mode)throw new Error('Real depth is required; select plate.diagnosticFlat:true explicitly for a non-final flat diagnostic');
  if(mode==='diagnostic-flat')warnings.push('DIAGNOSTIC ONLY: no supplied depth; zero parallax. Not a completed production rig.');
  const entries=layers?.length?layers:[{id:'plate',image:descriptor.image??plate,depth,mask,z:0,depthScale:descriptor.depthScale??.65}];
  if(layers?.length&&layers.length!==5)warnings.push('Layered scene supplied '+layers.length+' layers. S25 requires five independent layers.');
  let minZ=Infinity,maxZ=-Infinity;
  for(const entry of entries){
    if(!Number.isFinite(entry.z??0))throw new Error('Layer z must be finite world units');
    if(layers?.length&&entry.z===undefined)throw new Error('Each separate layer requires explicit z');
    if(layers?.length&&entry.rgba!==true&&!entry.mask&&!entry.image?.isTexture&&!(entry.image?.data&&entry.image.data.length===entry.image.width*entry.image.height*4))throw new Error('Separate layers must declare rgba:true or provide a mask/RGBA data');
    const depthPixels=entry.depth?pixels(entry.depth,'depth'):null;
    const geo=new THREE.PlaneGeometry(worldWidth*(1+2*pad),worldHeight*(1+2*pad),512,288);
    const pos=geo.attributes.position,uv=geo.attributes.uv;
    for(let i=0;i<pos.count;i++){
      const u=uv.getX(i)*(1+2*pad)-pad,v=uv.getY(i)*(1+2*pad)-pad;
      uv.setXY(i,u,v); // ClampToEdge makes overscan duplicate source edge pixels.
      const z=(entry.z??0)+(depthPixels?(value(depthPixels,u,v)-(entry.depthCenter??.5))*(entry.depthScale??.65):0);
      pos.setZ(i,z);minZ=Math.min(minZ,z);maxZ=Math.max(maxZ,z);
    }
    geo.computeVertexNormals();geo.computeBoundingBox();geo.computeBoundingSphere();
    const material=new THREE.MeshBasicMaterial({map:texture(entry.image,'plate/layer image'),transparent:true,depthWrite:!layers?.length,side:THREE.DoubleSide,toneMapped:false});
    if(entry.mask)material.alphaMap=texture(entry.mask,'mask',false);
    if(layers?.length){
      // Transparent canvases are allowed to end inside the viewport. Beyond their
      // true source rectangle, reveal the next layer instead of repeating edges.
      material.onBeforeCompile=shader=>{shader.fragmentShader=shader.fragmentShader.replace('#include <map_fragment>',
        'if(vMapUv.x<0.0||vMapUv.x>1.0||vMapUv.y<0.0||vMapUv.y>1.0) discard;\n#include <map_fragment>');};
      material.customProgramCacheKey=()=> 'parallax-source-uv-clip-v1';
    }
    const mesh=new THREE.Mesh(geo,material);mesh.name=entry.id||'layer';mesh.renderOrder=entry.renderOrder??entries.indexOf(entry);
    const sourceLayer=new THREE.Group();sourceLayer.name=(entry.id||'plate')+'-source';
    sourceLayer.add(mesh);group.add(sourceLayer);
    layerRecords.push({id:entry.id||'plate',entry,mesh,group:sourceLayer,registrationScale:1,minZ:geo.boundingBox.min.z,maxZ:geo.boundingBox.max.z});
    meshes.push(mesh);resources.push(geo,material);
  }
  // Transparent planes must paint far-to-near for the initial +Z camera.
  if(layers?.length)meshes.slice().sort((a,b)=>a.geometry.boundingBox.min.z-b.geometry.boundingBox.min.z).forEach((m,i)=>m.renderOrder=i);
  const coverageLayer=layers?.length?layerRecords.find(l=>l.entry.coverage==='background'||l.entry.opaque===true)
    ||layerRecords.find(l=>/(^|[-_])sky($|[-_])/i.test(l.id)):null;
  if(layers?.length&&!coverageLayer)throw new Error('Separate layers require an opaque:true/coverage:background layer or explicitly named sky layer');
  if(coverageLayer&&!coverageLayer.entry.opaque&&coverageLayer.entry.coverage!=='background')warnings.push('Coverage layer selected by sky name; source alpha opacity remains unverified.');
  const infiniteSky=Boolean(layers?.length&&descriptor.layerMode==='infinite-sky');
  if(infiniteSky){
    // Three's 2D background pass covers clip-space directly: no depth-dependent
    // shrinking, FOV exposure, repeated image edges, or invented disocclusions.
    coverageLayer.mesh.visible=false;
    scene.background=coverageLayer.mesh.material.map;
    warnings.push('Infinite sky uses full source UV0..1 as screen-filling background; it has no finite world anchor. Foreground alpha boundaries still require visual review.');
  }
  scene.add(group);
  const travelLimit=descriptor.maximumProjectedTravelFraction??(layers?.length?Infinity:.08);
  const bounds={worldWidth,worldHeight,paddingFraction:pad,paddedWidth:worldWidth*(1+2*pad),paddedHeight:worldHeight*(1+2*pad),minZ,maxZ,maximumProjectedTravelFraction:Number.isFinite(travelLimit)?travelLimit:null,backgroundMode:infiniteSky?'infinite-sky-screen-pass':'finite-source-plane'};
  let reference=null,referenceDistance=null;
  const anchors=[new THREE.Vector3(0,0,0)];
  for(const z of [minZ,maxZ])for(const x of [-worldWidth/2,0,worldWidth/2])for(const y of [-worldHeight/2,0,worldHeight/2])anchors.push(new THREE.Vector3(x,y,z));
  const projected=(point,cam)=>point.clone().applyMatrix4(group.matrixWorld).project(cam);
  function setReferenceCamera(camera){
    camera.updateMatrixWorld(true);
    // A generated plate already depicts frame zero. Face that initial camera instead
    // of pretending every plate was photographed at neutral (0,0,10), FOV50.
    const distance=descriptor.referenceDistance??Math.max(.5,camera.position.length());
    const cropReserve=descriptor.cropReserve??.08;
    referenceDistance=distance;
    const fittedHeight=2*distance*Math.tan(camera.fov*Math.PI/360)*(1+cropReserve);
    group.quaternion.copy(camera.quaternion);
    group.position.copy(camera.position).add(new THREE.Vector3(0,0,-distance).applyQuaternion(camera.quaternion));
    group.scale.set(fittedHeight*camera.aspect/worldWidth,fittedHeight/worldHeight,1);
    for(const layer of layerRecords){
      const z=layer.entry.z??0;
      const scale=layers?.length?(distance-z)/distance:1;
      if(scale<=0)throw new Error('Layer '+layer.id+' lies at or behind the initial camera');
      layer.registrationScale=scale;layer.group.scale.set(scale,scale,1);
      // Depth is a ray distance in the source camera, not an independent extrusion
      // of an already projected picture. Preserve every source UV at frame zero.
      const geometry=layer.mesh.geometry,positions=geometry.attributes.position,uvs=geometry.attributes.uv;
      for(let i=0;i<positions.count;i++){
        const vertexZ=positions.getZ(i),factor=(distance-vertexZ)/(distance*scale);
        if(factor<=0)throw new Error('Depth vertex lies at or behind source camera');
        positions.setXY(i,(uvs.getX(i)-.5)*worldWidth*factor,(uvs.getY(i)-.5)*worldHeight*factor);
      }
      positions.needsUpdate=true;geometry.computeVertexNormals();geometry.computeBoundingBox();geometry.computeBoundingSphere();
    }
    anchors.length=1;
    for(const layer of layerRecords.filter(l=>!infiniteSky||l!==coverageLayer))for(const z of [layer.minZ,layer.maxZ])for(const x of [-worldWidth/2,0,worldWidth/2])for(const y of [-worldHeight/2,0,worldHeight/2]){
      const factor=(distance-z)/distance;anchors.push(new THREE.Vector3(x*factor,y*factor,z));
    }
    bounds.layerRegistration=layerRecords.map(l=>({id:l.id,z:l.entry.z??0,xyScale:l.registrationScale,coverageRequired:!infiniteSky&&(l===coverageLayer||!layers?.length),renderMode:infiniteSky&&l===coverageLayer?'screen-background-at-infinity':'world-plane'}));
    group.updateMatrixWorld(true);reference=camera.clone();reference.updateMatrixWorld(true);
    bounds.initialFraming={distance,cropReserve,sourceScale:group.scale.toArray(),sourcePosition:group.position.toArray(),sourceQuaternion:group.quaternion.toArray()};
    const coverage=measureCoverage(camera);
    if(!coverage.safe)throw new Error('Initial camera cannot safely cover true source UVs: '+JSON.stringify(coverage));
    return {position:reference.position.toArray(),quaternion:reference.quaternion.toArray(),fov:reference.fov,coverage,sourceTransform:group.matrixWorld.toArray()};
  }
  function sourceScaleAtDepth(z=0){
    if(referenceDistance===null)throw new Error('Set reference camera before mapping source points');
    return (referenceDistance-z)/referenceDistance;
  }
  // For anchors parented directly to sourceGroup. Layer anchors use layerSourcePoint.
  function sourceLocalPoint(u,v,z=0){
    const factor=sourceScaleAtDepth(z);
    return new THREE.Vector3((u-.5)*worldWidth*factor,(v-.5)*worldHeight*factor,z);
  }
  function sourcePoint(u,v,z=0){
    group.updateMatrixWorld(true);
    return sourceLocalPoint(u,v,z).applyMatrix4(group.matrixWorld);
  }
  function layerSourceGroup(layerId){
    const layer=layerRecords.find(l=>l.id===layerId);
    if(!layer)throw new Error('Unknown source layer '+layerId);
    if(infiniteSky&&layer===coverageLayer)throw new Error('Infinite sky has no world-space anchor group');
    return layer.group;
  }
  function layerSourcePoint(layerId,u,v,zOffset=0){
    const layer=layerRecords.find(l=>l.id===layerId);
    if(!layer)throw new Error('Unknown source layer '+layerId);
    if(infiniteSky&&layer===coverageLayer)throw new Error('Infinite sky has no finite world point');
    group.updateMatrixWorld(true);
    const z=(layer.entry.z??0)+zOffset,factor=(referenceDistance-z)/(referenceDistance*layer.registrationScale);
    return new THREE.Vector3((u-.5)*worldWidth*factor,(v-.5)*worldHeight*factor,z).applyMatrix4(layer.group.matrixWorld);
  }
  /** Conservative heightfield coverage proof: all viewport corner rays intersect
   * both depth-extreme planes inside the true source rectangle. Any continuous
   * intervening heightfield surface then lies within those UV bounds as well.
   * Overscan/ClampToEdge is deliberately NOT counted as available source content.
   */
  function measureCoverage(camera){
    camera.updateMatrixWorld(true);group.updateMatrixWorld(true);
    if(infiniteSky)return {safe:true,uvBounds:{minU:0,maxU:1,minV:0,maxV:1},insetU:0,insetV:0,
      coverageLayer:coverageLayer.id,backgroundMode:'infinite-sky-screen-pass',foregroundCoverageRequired:false,
      foregroundOutsideUV:'transparent-discard',usesRepeatedEdgePixels:false,opacityQA:'source-sky-alpha-must-be-opaque'};
    const coverageGroup=coverageLayer?.group||group;
    const inverse=coverageGroup.matrixWorld.clone().invert();
    const worldOrigin=new THREE.Vector3().setFromMatrixPosition(camera.matrixWorld);
    const origin=worldOrigin.clone().applyMatrix4(inverse);
    const uvBounds={minU:Infinity,maxU:-Infinity,minV:Infinity,maxV:-Infinity};
    let safe=true;
    for(const nx of [-1,1])for(const ny of [-1,1]){
      const worldPoint=new THREE.Vector3(nx,ny,.5).unproject(camera);
      const direction=worldPoint.sub(worldOrigin).transformDirection(inverse);
      if(direction.z>=-1e-8){safe=false;continue;}
      for(const z of coverageLayer?[coverageLayer.minZ,coverageLayer.maxZ]:[minZ,maxZ]){
        const t=(z-origin.z)/direction.z;
        if(t<=0){safe=false;continue;}
        const factor=(referenceDistance-z)/(referenceDistance*(coverageLayer?.registrationScale??1));
        const u=(origin.x+t*direction.x)/(worldWidth*factor)+.5,v=(origin.y+t*direction.y)/(worldHeight*factor)+.5;
        uvBounds.minU=Math.min(uvBounds.minU,u);uvBounds.maxU=Math.max(uvBounds.maxU,u);
        uvBounds.minV=Math.min(uvBounds.minV,v);uvBounds.maxV=Math.max(uvBounds.maxV,v);
      }
    }
    const insetU=1/width,insetV=1/height;
    safe=safe&&Object.values(uvBounds).every(Number.isFinite)&&uvBounds.minU>=insetU&&uvBounds.maxU<=1-insetU&&uvBounds.minV>=insetV&&uvBounds.maxV<=1-insetV;
    return {safe,uvBounds,insetU,insetV,coverageLayer:coverageLayer?.id??'plate',foregroundCoverageRequired:false,foregroundOutsideUV:'transparent-discard',usesRepeatedEdgePixels:!safe};
  }
  function measure(camera){
    if(!reference)throw new Error('Call setReferenceCamera(camera) at the shot initial pose first');
    camera.updateMatrixWorld(true);group.updateMatrixWorld(true);
    let max=0;
    for(let i=0;i<anchors.length;i++){
      const p=anchors[i],a=projected(p,camera),b=projected(p,reference);
      // Depth differential isolates parallax from the intended flat-plate dolly/zoom.
      if(i){const factor=(referenceDistance-p.z)/referenceDistance;const flat=new THREE.Vector3(p.x/factor,p.y/factor,0),af=projected(flat,camera),bf=projected(flat,reference);a.sub(af);b.sub(bf);}
      max=Math.max(max,Math.abs(a.x-b.x)/2,Math.abs(a.y-b.y)*height/width/2);
    }
    return max;
  }
  function foregroundDiagnostics(camera){
    if(!layers?.length)return [];
    camera.updateMatrixWorld(true);group.updateMatrixWorld(true);
    return layerRecords.filter(layer=>layer!==coverageLayer).map(layer=>{
      const corners=[];
      for(const u of [0,1])for(const v of [0,1]){
        const point=layerSourcePoint(layer.id,u,v),view=point.clone().applyMatrix4(camera.matrixWorldInverse),ndc=point.project(camera);
        corners.push({u,v,ndc:ndc.toArray(),inFront:view.z<0});
      }
      const finite=corners.every(c=>c.ndc.every(Number.isFinite));
      const bounds=finite?{minX:Math.min(...corners.map(c=>c.ndc[0])),maxX:Math.max(...corners.map(c=>c.ndc[0])),minY:Math.min(...corners.map(c=>c.ndc[1])),maxY:Math.max(...corners.map(c=>c.ndc[1]))}:null;
      return {id:layer.id,z:layer.entry.z,registrationScale:layer.registrationScale,projectedSourceBounds:bounds,
        allSourceCornersInFront:corners.every(c=>c.inFront),allSourceCornersInsideViewport:finite&&corners.every(c=>c.inFront&&Math.abs(c.ndc[0])<=1&&Math.abs(c.ndc[1])<=1),
        boundaryPolicy:'Fragments outside source UV0..1 discard to reveal background; alpha-cut content requires visual review.',projectedCorners:corners};
    });
  }
  function constrainCamera(camera){
    if(!reference)throw new Error('Reference camera must be set before constraining');
    const requested=measure(camera),requestedCoverage=measureCoverage(camera);
    const p=camera.position.clone(),q=camera.quaternion.clone(),fov=camera.fov;
    const apply=fraction=>{
      camera.position.copy(reference.position).lerp(p,fraction);
      camera.quaternion.copy(reference.quaternion).slerp(q,fraction);
      camera.fov=reference.fov+(fov-reference.fov)*fraction;
      camera.updateProjectionMatrix();camera.updateMatrixWorld(true);
    };
    let fraction=1,actual=requested,coverage=requestedCoverage;
    const acceptable=()=>Number.isFinite(actual)&&actual<=travelLimit&&coverage.safe;
    if(!infiniteSky&&!acceptable()){
      // Search the connected safe interval from the original pose; continuous
      // bisection avoids discrete half-step jumps as a tilt reaches the border.
      let low=0,high=1;
      for(let i=0;i<18;i++){
        const mid=(low+high)/2;apply(mid);actual=measure(camera);coverage=measureCoverage(camera);
        if(acceptable())low=mid;else high=mid;
      }
      fraction=low;apply(fraction);actual=measure(camera);coverage=measureCoverage(camera);
      if(!acceptable())throw new Error('Coverage clamp failed to find a safe source pose');
    }
    return {clamped:fraction<1,retainedMoveFraction:fraction,
      requestedProjectedTravelFraction:requested,actualProjectedTravelFraction:actual,
      coverageClamped:!requestedCoverage.safe,requestedCoverage,actualCoverage:coverage,
      requestedCameraPosition:p.toArray(),actualCameraPosition:camera.position.toArray(),
      requestedCameraQuaternion:q.toArray(),actualCameraQuaternion:camera.quaternion.toArray(),
      sourceCropReserve:descriptor.cropReserve??.08,backgroundMode:bounds.backgroundMode,foregroundLayers:foregroundDiagnostics(camera),requiresVisualEdgeQA:true};
  }
  function dispose(){scene.remove(group);if(infiniteSky&&scene.background===coverageLayer.mesh.material.map)scene.background=previousBackground;for(const item of resources)item.dispose();}
  return {group,sourceGroup:group,sourceScaleAtDepth,sourceLocalPoint,sourcePoint,layerSourcePoint,layerSourceGroup,meshes,geometry:meshes[0]?.geometry,bounds,mode,warnings,setReferenceCamera,measureProjectedTravel:measure,measureCoverage,foregroundDiagnostics,constrainCamera,dispose,
    provenance:{depth:depth?.provenance??(depth?'supplied-unverified':'none'),layers:entries.map(e=>({id:e.id||'plate',depth:e.depth?.provenance??(e.depth?'supplied-unverified':'none'),z:e.z??0})),depthInferencePerformed:false},
    update(camera){
      // Sort transparent planes only; no face, hair, or body deformation.
      if(!camera||!layers?.length)return;
      camera.updateMatrixWorld(true);group.updateMatrixWorld(true);
      const center=new THREE.Vector3();
      meshes.map(mesh=>{mesh.geometry.boundingBox.getCenter(center);return {mesh,z:center.clone().applyMatrix4(mesh.matrixWorld).applyMatrix4(camera.matrixWorldInverse).z};})
        .sort((a,b)=>a.z-b.z).forEach(({mesh},i)=>mesh.renderOrder=i);
    }};
}
