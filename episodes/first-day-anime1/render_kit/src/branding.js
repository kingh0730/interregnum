import {vector} from './vectors.js';import {tracked} from './media.js';import {write} from './text.js';
// Landmark positions are in the source 1672 x 941 plate. Every overlay stays vector at output resolution.
export const landmarks={
 S16:{pin:[875,171,22],eyes:[[802,210,6],[839,198,6]]},
 S17:{pin:[970,140,48],brooch:[809,667,51],eyes:[[697,234,21],[894,220,21]]},
 S20:{tag:[533,252,16]},
 S20end:{tag:[541,304,16]},
 S21:{pin:[794,56,27],brooch:[751,209,20],eyes:[[680,129,7],[744,98,7]],tag:[775,722,9]},
 S23:{pin:[564,99,40],brooch:[352,443,29],eyes:[[430,194,11],[515,244,11]]},
 S24:{pin:[714,80,27],brooch:[628,262,23],eyes:[[587,153,8],[645,125,8]]},
 S25:{pin:[813,206,22],brooch:[790,289,14]},
 S42:{pin:[746,80,40],brooch:[714,348,28]},
 S29:{pin:[946,125,38],brooch:[872,585,35],eyes:[[609,300,16],[780,225,16]]},
 S32:{pin:[611,110,20],brooch:[529,181,17]},
 S44:{pin:[577,94,27],brooch:[475,258,22],eyes:[[479,134,9],[537,148,9]],tag:[419,609,9]}
};
export function brand(ctx,id,W,H,logos,project=null,time=null){const m=landmarks[id]||(id==='S36'?landmarks.S29:null);if(!m)return;let pos=(a,key)=>{let tr=time===null?null:tracked(id,key,time);let u=tr?tr[0]:a[0]/1672,v=tr?tr[1]:a[1]/941,size=tr?tr[2]:a[2]/1672;if(size<=0||!Number.isFinite(u)||u<0||u>1||v<0||v>1)return[-10000,-10000,0];return project?project(u,v,size):[u*W,v*H,size*W];};ctx.save();if(m.pin){let[x,y,z]=pos(m.pin,'pin');vector(ctx,logos.spark,x,y,z);}if(m.brooch){let[x,y,z]=pos(m.brooch,'brooch');vector(ctx,logos.anthropic,x,y,z,0,'#FAF9F5');}for(let [ei,eye] of (m.eyes||[]).entries()){let[x,y,z]=pos(eye,`eye${ei}`);vector(ctx,logos.spark,x,y,z,0,'#141413');}if(m.tag){let[x,y,z]=pos(m.tag,'tag');write(ctx,'5.5',x,y+z*.25,z,'#141413','Lora-SemiBold');}ctx.restore();}
