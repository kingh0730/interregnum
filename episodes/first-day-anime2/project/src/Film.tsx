/** Remotion adapter around the exact standalone Three scene graph.
 * Source-compiles locally; Remotion runtime validation awaits its dependency install.
 * Production currently renders through build/render.mjs with original MP3 stream copy.
 */
import React, {useEffect, useRef, useState} from 'react';
import {AbsoluteFill, Audio, cancelRender, continueRender, delayRender, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import * as THREE from 'three';
import {SVGLoader} from 'three/examples/jsm/loaders/SVGLoader.js';
import {createFilm} from './film_runtime.mjs';
import shots from '../helper/shots.json';
import sync from '../helper/sync.json';
import onsets from '../helper/onsets.json';
import cameraPaths from '../helper/camera_paths.json';

export const Film: React.FC = () => {
  const frame=useCurrentFrame();
  const {width,height}=useVideoConfig();
  const canvas=useRef<HTMLCanvasElement>(null);
  const runtime=useRef<Promise<any>|null>(null);
  const [boot]=useState(()=>delayRender('Load production scene graph'));
  useEffect(()=>{
    let abandoned=false;
    runtime.current=(async()=>{
      const response=await fetch(staticFile('helper/asset_map.json'));
      if(!response.ok)throw new Error('Production asset map unavailable');
      const assetMap=await response.json();assetMap.resolveURL=staticFile;
      const wordmarkImage=await new Promise<HTMLImageElement>((resolve,reject)=>{
        const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=staticFile('assets/brand/anthropic-wordmark.svg');
      });
      const film=await createFilm({THREE,SVGLoader,width,height,assetMap,shots,sync,onsets,cameraPaths,brand:{wordmarkImage}});
      if(abandoned)film.dispose();return film;
    })();
    runtime.current.then(()=>continueRender(boot)).catch(cancelRender);
    return()=>{abandoned=true;runtime.current?.then(film=>film.dispose()).catch(()=>{});};
  },[width,height,boot]);
  useEffect(()=>{
    let abandoned=false;
    const handle=delayRender(`Compose source frame ${frame}`);
    (async()=>{
      const film=await runtime.current;
      if(!film)throw new Error('Scene initialization missing');
      await film.renderFrame(frame);
      if(!abandoned)canvas.current?.getContext('2d')?.drawImage(film.canvas,0,0);
      continueRender(handle);
    })().catch(cancelRender);
    return()=>{abandoned=true;};
  },[frame,width,height]);
  return <AbsoluteFill><canvas ref={canvas} width={width} height={height}/><Audio src={staticFile('first-day.mp3')}/></AbsoluteFill>;
};
