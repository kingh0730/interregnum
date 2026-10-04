import {write,rounded,family} from './text.js';
import {vector} from './vectors.js';
const{hash01,clamp,easeOutExpo,lerp,smoothstep}=window.RT;
const P={ink:'#141413',ivory:'#FAF9F5',cream:'#F0EEE6',oat:'#E8E6DC',coral:'#D97757'};
export function impact(ctx,u,frame,W,H,spark){
 const sc=H/1080;ctx.fillStyle=frame<2?'#FFFFFF':P.coral;ctx.fillRect(0,0,W,H);if(frame<2)return;
 const j=frame<6?((hash01(frame,33)-.5)*28*sc):0;ctx.save();ctx.translate(W/2+j,H/2-j*.5);
 ctx.save();ctx.globalAlpha=.28;vector(ctx,spark,0,0,H*.99,u*1.4,P.ink);ctx.restore();
 for(let i=0;i<12;i++){let a=i*Math.PI/6+u*.3;ctx.strokeStyle=P.ivory;ctx.lineWidth=2*sc;ctx.beginPath();ctx.moveTo(Math.cos(a)*H*.51,Math.sin(a)*H*.51);ctx.lineTo(Math.cos(a)*W,Math.sin(a)*W);ctx.stroke();}
 const zoom=1+.35*(1-easeOutExpo(clamp(u*3,0,1)));ctx.scale(zoom,zoom);
 if(frame<7){write(ctx,'Opus 5.5',-4*sc,H*.1,H*.38,'#6A9BCC','Lora-SemiBold');write(ctx,'Opus 5.5',4*sc,H*.1,H*.38,P.ink,'Lora-SemiBold');}
 write(ctx,'Opus 5.5',0,H*.1,H*.38,P.ivory,'Lora-SemiBold');write(ctx,'第一天 · First Day',0,H*.24,H*.045,P.ivory);ctx.restore();
 write(ctx,'额度',W*.80,H*.067,H*.018,P.ivory,'NotoSansSC-Bold','right');rounded(ctx,W*.815,H*.047,W*.14,H*.015,4*sc,P.oat);rounded(ctx,W*.815,H*.047,W*.14,H*.015,4*sc,P.ivory);
 const travel=(u-.72)/.28;if(travel>0){ctx.fillStyle=P.ivory;ctx.beginPath();ctx.moveTo(-W,0);ctx.lineTo(W*travel,0);for(let i=0;i<=80;i++)ctx.lineTo(W*travel+(hash01(i,24)-.5)*38*sc,H*i/80);ctx.lineTo(-W,H);ctx.closePath();ctx.fill();}
}
export function thinking(ctx,x,y,w,h,t,W,H,spark){rounded(ctx,x,y,w,h,h*.2,P.oat);vector(ctx,spark,x+h*.5,y+h*.5,h*.5,t*.7);ctx.save();ctx.beginPath();ctx.rect(x+h,y,w-h,h);ctx.clip();let z=(t*120*H/1080)%(w*2);let g=ctx.createLinearGradient(x-w+z,0,x+z,0);g.addColorStop(0,P.ink);g.addColorStop(.5,P.coral);g.addColorStop(1,P.ink);write(ctx,'Thinking…',x+h,y+h*.65,h*.4,g,'Poppins','left');ctx.restore();}
export function feed(ctx,u,t,W,H,spark){let sc=H/1080;ctx.fillStyle=P.cream;ctx.fillRect(0,0,W,H);let words=['再等等，下个版本更强','明天就发布了','Opus 5.5 什么时候出？','等 5.5 再说'];let travel=(Math.exp(u*3)-1)/(Math.exp(3)-1)*H*3.8;for(let i=0;i<10;i++){let y=H*.15+i*H*.27-travel;rounded(ctx,W*(i%2?.2:.12),y,W*.67,H*.19,22*sc,P.oat);write(ctx,words[i%4],W*(i%2?.24:.16),y+H*.11,H*.043,P.ink,'NotoSansSC-Bold','left');}thinking(ctx,W*.28,lerp(H*1.6,H*.44,smoothstep(.65,1,u)),W*.44,H*.13,t,W,H,spark);}
export function stop(ctx,u,t,W,H,localFrame=0){let sc=H/1080;ctx.save();ctx.translate(W/2,H/2);ctx.scale(1+.04*u,1+.04*u);ctx.translate(-W/2,-H/2);rounded(ctx,W*.23,H*.27,W*.54,H*.44,8*sc,'#242423');rounded(ctx,W*.245,H*.285,W*.51,H*.405,3*sc,P.ink);let chars=[...'你好，我是 Opus 5.5。'].slice(0,localFrame).join('');write(ctx,chars,W*.5,H*.51,H*.055,P.ivory);ctx.font=`${H*.055}px ${family('NotoSerifSC-SemiBold')}`;if(localFrame>=16?localFrame%2===0:Math.floor(t*30/8)%2===0){ctx.fillStyle=P.ivory;ctx.fillRect(W*.5+ctx.measureText(chars).width/2+9*sc,H*.455,3*sc,H*.06);}write(ctx,'额度',W*.3,H*.61,H*.025,P.ivory,'NotoSansSC-Bold','left');rounded(ctx,W*.36,H*.59,W*.34,H*.02,5*sc,'#383835');rounded(ctx,W*.36,H*.59,W*.34*clamp(u*1.15,0,1),H*.02,5*sc,P.coral);ctx.restore();}
export function endcard(ctx,t,W,H,logos){ctx.fillStyle=P.ivory;ctx.fillRect(0,0,W,H);vector(ctx,logos.spark,W/2,H*.3,H*.15);write(ctx,'Opus 5.5',W/2,H*.56,H*.13,P.ink,'Lora-SemiBold');write(ctx,'第一天 · First Day',W/2,H*.66,H*.038,P.ink);write(ctx,'你好，世界。',W/2,H*.79,H*.03,P.coral);vector(ctx,logos.anthropic,W*.94,H*.91,H*.065);}
