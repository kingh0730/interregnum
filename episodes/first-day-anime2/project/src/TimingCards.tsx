import React from 'react';
import {AbsoluteFill, Audio, staticFile, useCurrentFrame} from 'remotion';
import {heldFrame, shotAt, sync} from './sync';

/** Diagnostic composition. Production output must never use these cards. */
export const TimingCards: React.FC = () => {
  const actual=useCurrentFrame();
  const frame=heldFrame(actual);
  const shot=shotAt(frame)!;
  return <AbsoluteFill style={{background:shot.id==='S10'?'#F0EEE6':'#D97757',color:'#191919',padding:96,fontFamily:'sans-serif'}}>
    <Audio src={staticFile('first-day.mp3')}/>
    <div style={{fontSize:40}}>TIMING TEST / NOT FINAL ART</div>
    <div style={{fontSize:180,marginTop:100}}>{shot.id}</div>
    <div style={{fontSize:60}}>Frame {frame} / {sync.frames} · {(frame/sync.fps).toFixed(3)} s</div>
    <div style={{fontSize:44,marginTop:40}}>{shot.f0}–{shot.f1-1}</div>
    <div style={{position:'absolute',bottom:96,left:96,width:(1920-192)*frame/sync.frames,height:12,background:'#FAF9F5'}}/>
  </AbsoluteFill>;
};
