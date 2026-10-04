const{hash01,smoothstep}=window.RT;
export class PaperMeadow{
 constructor(W,H,figures){this.W=W;this.H=H;this.figures=figures;this.canvas=document.createElement('canvas');this.canvas.width=W*2;this.canvas.height=H*2;this.x=this.canvas.getContext('2d',{alpha:false});}
 render(t,u){let W=this.W*2,H=this.H*2,x=this.x,truck=u*W*.13,q=Math.floor(t*12)/12,phase=q*9;x.setTransform(1,0,0,1,0,0);x.fillStyle='#FAF9F5';x.fillRect(0,0,W,H);
  // Plane 1: paper sky and flat coral sun.
  x.fillStyle='#D97757';x.beginPath();x.arc(W*.79-truck*.1,H*.21,H*.16,0,Math.PI*2);x.fill();x.strokeStyle='#141413';x.lineWidth=H*.002;for(let i=0;i<8;i++){let px=hash01(i,66)*W-truck*.08,py=H*(.05+.35*hash01(i,67));x.beginPath();x.moveTo(px-10,py);x.lineTo(px+10,py);x.moveTo(px,py-10);x.lineTo(px,py+10);x.stroke();}
  // Plane 2: distant hand-drawn hills.
  for(let j=0;j<3;j++){x.save();x.translate(-truck*(.18+j*.05),0);x.strokeStyle=j===0?'#788C5D':'#141413';x.lineWidth=H*.002;x.beginPath();x.moveTo(-W,H*(.62+j*.08));x.bezierCurveTo(W*.1,H*(.31+j*.08),W*.45,H*(.81+j*.03),W*1.3,H*(.49+j*.09));x.stroke();x.restore();}
  // Plane 3: middle meadow, loosely inked stems and coral petals.
  for(let i=0;i<150;i++){let px=hash01(i,68)*W*1.4-truck*.4,py=H*(.58+.4*hash01(i,69)),h=H*(.007+.025*hash01(i,70));x.strokeStyle='#141413';x.lineWidth=H*.0018;x.beginPath();x.moveTo(px,py);x.quadraticCurveTo(px+h*.2,py-h*.4,px+h*.5,py-h);x.stroke();if(i%5===0){x.fillStyle='#D97757';for(let k=0;k<5;k++){let a=k*Math.PI*2/5;x.beginPath();x.ellipse(px+h*.5+Math.cos(a)*h*.18,py-h+Math.sin(a)*h*.18,h*.16,h*.08,a,0,Math.PI*2);x.fill();}}}
  // Plane 4: generated line-art character cutouts, stepped animation on twos/threes.
  x.save();x.translate(W*.03-truck*.14,H*.008*Math.sin(phase));x.rotate(.006*Math.sin(phase));x.drawImage(this.figures,0,0,W,H);x.restore();
  // Plane 5: close grasses sweep rapidly across the camera.
  x.strokeStyle='#141413';for(let i=0;i<70;i++){let px=hash01(i,72)*W*1.7-truck*.95,py=H*(.99+.15*hash01(i,73)),h=H*(.04+.11*hash01(i,74));x.lineWidth=H*(.0015+.002*hash01(i,75));x.beginPath();x.moveTo(px,py);x.quadraticCurveTo(px+h*.12,py-h*.6,px+h*.4,py-h);x.stroke();}
  let wipe=u<.07?1-u/.07:u>.93?(u-.93)/.07:0;if(wipe>0){x.fillStyle='#F0EEE6';x.beginPath();x.moveTo(0,0);x.lineTo(W*wipe,0);for(let i=0;i<=80;i++)x.lineTo(W*wipe+(hash01(i,99)-.5)*H*.025,H*i/80);x.lineTo(0,H);x.closePath();x.fill();}
  return this.canvas;
 }
}
