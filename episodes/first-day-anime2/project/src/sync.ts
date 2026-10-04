import syncData from '../helper/sync.json';
import shotData from '../helper/shots.json';
import onsets from '../helper/onsets.json';

export const sync = syncData;
export const shots = shotData;
export const beatFrame = (u: number) => Math.round((sync.offset + u * sync.beat) * sync.fps);
export const nearestKick = (seconds: number) => onsets.kicks.reduce((a,b) => Math.abs(a-seconds) < Math.abs(b-seconds) ? a : b);
export const lyricChars = () => sync.lyrics.flatMap((line,index) => line.chars.map(char => ({...char, line:index, frame:Math.round(char.t*sync.fps)})));
export const shotAt = (frame:number) => shots.find(shot => frame>=shot.f0 && frame<shot.f1);
export const snapToGrid = (frame:number) => [0,...sync.eighths,...onsets.kicks].map(t=>Math.round(t*sync.fps)).reduce((a,b)=>Math.abs(a-frame)<Math.abs(b-frame)?a:b);
export const heldFrame = (frame:number) => {
  const stop=shots.find(s=>s.id==='S10')!;
  if(frame>=stop.f0 && frame<stop.f1) return stop.f0;
  return Math.min(frame,sync.frames-12);
};
