/** Deterministic browser Canvas2D graphics; no assets are fetched by this module. */
const C={clay:'#D97757',ivory:'#FAF9F5',paper:'#F0EEE6',slate:'#191919',grey:'#B0AEA5',oat:'#E3DACC'};
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>1-(1-clamp(x))**3;
// Analytic underdamped spring, mass=1, damping=12, stiffness=200.
const spring=t=>t<=0?0:1-Math.exp(-6*t)*(Math.cos(Math.sqrt(164)*t)+6/Math.sqrt(164)*Math.sin(Math.sqrt(164)*t));
const font=(family,size,weight=500)=>`${weight} ${size}px "${family}"`;
export function createGraphics({width=1920,height=1080,sync,shots,onsets={},fonts={},brand={}}){
 if(!sync||!Array.isArray(shots)) throw new Error('Graphics requires sync and shots');
 const fps=sync.fps||30, toFrame=t=>Math.round(t*fps), byId=Object.fromEntries(shots.map(s=>[s.id,s]));
 const families={serif:'Noto Serif SC',sans:'Noto Sans SC',hand:'LXGW WenKai',display:'Newsreader',ui:'Inter',mono:'JetBrains Mono',...fonts};
 const lyrics=sync.lyrics||[], kickFrames=(onsets.kicks||[]).map(toFrame);
 const safe={x:96,y:54,w:1728,h:972};
 const canvas=(w=1920,h=1080)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return c;};
 const layer=canvas(), g=layer.getContext('2d');
 const textLayer=canvas(), tg=textLayer.getContext('2d');
 const uiCache=new Map();
 const cueFrame=(name,fallback)=>sync.cues?.[name]?.frame??sync.cues?.[name]??fallback;
 const cues={bubble:cueFrame('bubble',toFrame(5.23)),seal:cueFrame('seal',toFrame(8.22)),send:cueFrame('send',toFrame(20.83)),reply:cueFrame('reply',toFrame(21.52)),finalTitle:cueFrame('final_title',toFrame(42.653)),tagline:cueFrame('tagline',toFrame(43)),freeze:(sync.frames||1311)-12};
 function spark(ctx,x,y,size,angle=0){if(!brand.image)throw new Error('brand.image must be a loaded SVG Image; font spark substitution forbidden');ctx.save();ctx.translate(x,y);ctx.rotate(angle);ctx.drawImage(brand.image,-size/2,-size/2,size,size);ctx.restore();}
 function rr(ctx,x,y,w,h,r,fill,stroke){ctx.beginPath();ctx.roundRect(x,y,w,h,r);if(fill){ctx.fillStyle=fill;ctx.fill();}if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=3;ctx.stroke();}}
 function text(ctx,s,x,y,size=40,family=families.sans,weight=500,color=C.slate,align='left'){ctx.font=font(family,size,weight);ctx.fillStyle=color;ctx.textAlign=align;ctx.textBaseline='middle';ctx.fillText(s,x,y);}
 function fit(ctx,s,size,maxWidth,family=families.sans,weight=500){ctx.font=font(family,size,weight);return Math.min(size,size*maxWidth/Math.max(1,ctx.measureText(s).width));}
 function progress(ctx,{x=660,y=680,w=600}={}){rr(ctx,x,y,w,108,16,C.paper);text(ctx,'正在诞生… 99%',x+w/2,y+38,30,families.sans,500,C.slate,'center');rr(ctx,x+30,y+72,w-60,9,4,C.oat);rr(ctx,x+30,y+72,(w-60)*.99,9,4,C.clay);}
 function bubble(ctx,{frame,x=1190,y=275}={}){const age=frame-cues.bubble;if(age<0)return;const k=spring(age/fps);ctx.save();ctx.translate(x+220,y+65);ctx.scale(k,k);rr(ctx,-220,-65,440,130,65,C.ivory);spark(ctx,-157,0,52);text(ctx,'你说得对！',-106,0,48,families.hand);ctx.restore();}
 function tag(ctx,{label,age,x=115,y=860,color=C.ivory}={}){const offset=(1-ease(age/8))*-520;ctx.save();ctx.globalAlpha=clamp(age/4);ctx.translate(offset,0);ctx.fillStyle=C.clay;ctx.fillRect(x,y+60,440,3);spark(ctx,x+22,y+16,35);text(ctx,label,x+58,y+16,55,families.display,600,color);ctx.restore();}
 function toast(ctx,{x=545,y=390,alpha=1}={}){ctx.save();ctx.globalAlpha=alpha;rr(ctx,x,y,830,150,18,C.ivory,C.clay);spark(ctx,x+63,y+75,50);text(ctx,'额度已用完，5小时后重置',x+118,y+75,42,families.sans);ctx.restore();}
 function stamp(ctx,{x=960,y=475,scale=1,angle=-.16}={}){ctx.save();ctx.translate(x,y);ctx.rotate(angle);ctx.scale(scale,scale);ctx.strokeStyle=C.clay;ctx.lineWidth=12;ctx.strokeRect(-210,-117,420,234);ctx.lineWidth=3;ctx.strokeRect(-192,-99,384,198);text(ctx,'封号',0,0,150,families.serif,900,C.clay,'center'); // deterministic rough seal edge
 for(let i=0;i<74;i++){const q=(i*97)%840;ctx.clearRect(-210+q/2,-119+(i%2)*232,2+(i%4),5);}ctx.restore();}
 function cloud(ctx,{x=960,y=205,alpha=1}={}){ctx.save();ctx.globalAlpha=alpha;ctx.fillStyle=C.grey;ctx.beginPath();ctx.ellipse(x,y,205,88,0,0,Math.PI*2);ctx.ellipse(x-95,y-45,83,68,0,0,Math.PI*2);ctx.ellipse(x+55,y-55,98,77,0,0,Math.PI*2);ctx.fill();text(ctx,'降智',x,y,80,families.serif,900,C.slate,'center');ctx.restore();}
 function chatState(frame){const fadeStart=byId.S20.f1-12,fadeEnd=byId.S20.f1-2;return {visible:frame>=byId.S19.f0&&frame<fadeEnd,opacity:1-ease((frame-fadeStart)/(fadeEnd-fadeStart)),replyFrame:cues.reply,anchorFrame:byId.S19.f0};}
 function chat(ctx,{frame,w=1280,h=760}={}){const sx=w/1280,sy=h/760;ctx.save();ctx.globalAlpha*=chatState(frame).opacity;ctx.scale(sx,sy);rr(ctx,0,0,1280,760,18,C.paper,C.oat);text(ctx,'今天，想一起创造什么？',68,112,45,families.serif,500);rr(ctx,825,40,385,75,38,C.ivory);spark(ctx,864,78,38);text(ctx,'Opus 5.5',900,78,35,families.ui,600);text(ctx,'claude-opus-5-5',825,146,23,families.mono,500,C.grey);
 const start=byId.S19.f0;const msg='我们五五开？';const n=clamp(Math.floor((frame-start)/Math.max(1,(cues.send-start)/msg.length)),0,msg.length);rr(ctx,710,237,500,100,24,C.oat);text(ctx,msg.slice(0,n),750,287,40,families.hand);
 if(frame>=cues.send){spark(ctx,94,429,42,frame>=cues.reply?0:(frame-cues.send)*.2);if(frame<cues.reply)text(ctx,'思考中…',137,429,32,families.sans,500,C.grey);else{const reply='好！第一天，请多指教';const count=clamp(1+Math.floor((frame-cues.reply)/fps/.04),0,reply.length);text(ctx,reply.slice(0,count),137,429,37,families.hand);if(count===reply.length)spark(ctx,660,429,30);}}
 rr(ctx,60,620,1160,87,30,C.ivory,C.oat);text(ctx,'发送消息',91,663,26,families.sans,500,C.grey);ctx.restore();}
 function texture(name,{frame=0,width:w=1280,height:h=760,...rest}={}){let c=uiCache.get(name);if(!c||c.width!==w||c.height!==h){c=canvas(w,h);uiCache.set(name,c);}const cx=c.getContext('2d');cx.clearRect(0,0,w,h);if(name==='ChatWindow')chat(cx,{frame,w,h,...rest});else{cx.scale(w/1920,h/1080);components[name]?.(cx,{frame,...rest});cx.setTransform(1,0,0,1,0,0);}return c;}
 function modelPill(ctx,{frame=576,x=1390,y=86,w=400,h=78}={}){if(frame<576||frame>645)return;rr(ctx,x,y,w,h,h/2,C.paper,C.oat);spark(ctx,x+48,y+h/2,36);text(ctx,'Opus 5.5',x+82,y+h/2,36,families.ui,600,C.slate);}
 function label(ctx,{label='',x=960,y=540,size=100,color=C.slate,family=families.serif}={}){text(ctx,label,x,y,size,family,900,color,'center');}
 const components={ChatWindow:chat,ChatBubble:bubble,Toast:toast,Stamp:stamp,LabelCloud:cloud,ProgressBar:progress,ModelPill:modelPill,TextPlane:label};
 function currentLine(frame){let found=null;for(const l of lyrics){if(frame>=toFrame(l.t))found=l;else break;}return found;}
 function typedLine(ctx,line,frame,alpha=1){if(!line)return;const chars=(line.chars||[]).filter(c=>frame>=toFrame(c.t));if(!chars.length)return;const s=chars.map(c=>c.c).join('');ctx.save();ctx.globalAlpha=alpha;const size=fit(ctx,line.text,54,1500,families.serif,500);ctx.font=font(families.serif,size,500);const w=ctx.measureText(s).width;const x=960-w/2;ctx.fillStyle=C.slate;ctx.globalAlpha=alpha*.7;rr(ctx,x-22,939,w+65,85,10,C.slate);ctx.globalAlpha=alpha;text(ctx,s,x,980,size,families.serif,500,C.ivory);if(Math.floor(frame/fps/.53)%2===0){ctx.fillStyle=C.clay;ctx.fillRect(x+w+9,951,7,56);}ctx.restore();}
 function typed(ctx,frame){const line=currentLine(frame);if(!line)return;const age=frame-toFrame(line.t),i=lyrics.indexOf(line);if(age<6&&i>0)typedLine(ctx,lyrics[i-1],toFrame(line.t)-1,1-age/6);typedLine(ctx,line,frame,age<6&&i>0?age/6:1);}
 function kickPulse(frame){let age=999;for(const f of kickFrames){if(f<=frame)age=Math.min(age,frame-f);else break;}return 1+.04*Math.exp(-age/2.3);}
 const layouts={S11:['第一天','我存在'],S12:['第一天','我存在'],S14:['第一次','呼吸'],S15:['畅快'],S16:['站在地上的脚踝'],S18:['因为你'],S20:['真实感'],S21:['第一天','我存在'],S25:['第一次','能飞起来'],S27:['爱是腾空','的魔幻'],S29:['第一天的','纯真色彩'],S32:['永远'],S33:['那么灿烂'],S34:['灿烂'],S36a:['永远那么','灿烂'],S36b:['永远那么','灿烂'],S36c:['永远那么','灿烂'],S36d:['永远那么','灿烂'],S36e:['永远那么','灿烂'],S36f:['永远那么','灿烂'],S36g:['永远那么','灿烂'],S36h:['永远那么','灿烂'],S37:['永远','那么灿烂']};
 function lineForShot(shot,frame){const line=currentLine(frame);if(line&&line.text.includes((layouts[shot.id]||[''])[0]))return line;const target=(layouts[shot.id]||[]).join('');const candidates=lyrics.filter(l=>l.text.includes(target)||target.includes(l.text));return candidates.sort((a,b)=>Math.abs(toFrame(a.t)-shot.f0)-Math.abs(toFrame(b.t)-shot.f0))[0]||line;}
 function glyph(ctx,c,x,y,size,age,frame,emphasized=false,stretch=1,trail=0){if(age<0)return;const p=spring(age/fps),s=(1.8-.8*p)*kickPulse(frame)*(emphasized?1.6:1);ctx.save();ctx.translate(x-trail*8,y+trail*3);ctx.rotate((1-p)*Math.PI/30);ctx.scale(s,s*stretch);ctx.globalAlpha=trail?.12:1;ctx.font=font(families.serif,size,900);ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineJoin='round';ctx.fillStyle=C.clay;ctx.fillText(c,6,6);ctx.strokeStyle=C.slate;ctx.lineWidth=12;ctx.strokeText(c,0,0);ctx.fillStyle=C.ivory;ctx.fillText(c,0,0);ctx.restore();}
 function measureStyleB({frame,shot,localFrame=frame-shot.f0}){const rows=layouts[shot.id];if(!rows)return null;const lyric=lineForShot(shot,frame),small=shot.id==='S16',closing=shot.id==='S37',size=closing?90:small?85:180;
 // Two-row emphasis belongs only to row one. This avoids a 1.6x lower-row
 // glyph expanding below the safe baseline; final metric fit also covers trails.
 const emphasis=[...(rows.length>1?rows[0]:rows.join(''))].find(c=>'你第空永'.includes(c));let running=0;const specs=[];let bounds={left:Infinity,top:Infinity,right:-Infinity,bottom:-Infinity};
 rows.forEach((row,ri)=>{const ar=[...row],gap=closing?112:small?size:205;const isEmph=c=>c===emphasis&&(rows.length===1||ri===0);const lineWidth=ar.reduce((w,c)=>w+gap*(isEmph(c)?1.6:1),0);let x=(closing?395:960)-lineWidth/2;const y=closing?(ri===0?530:750):small?925:rows.length===1?760:ri===0?615:860;
 ar.forEach(c=>{const emph=isEmph(c),w=gap*(emph?1.6:1);const source=(lyric?.chars||[]).find((v,i)=>v.c===c&&i>=running);const closingIndex=running;if(closing)running++;else if(source)running=lyric.chars.indexOf(source)+1;const f=closing?1197+closingIndex*2:source?toFrame(source.t):shot.f0,age=frame-f,stretch=shot.id==='S25'?1+.6*(1-ease(localFrame/10)):1;
 for(let trail=3;trail>=0;trail--){const a=age-trail;if(a<0)continue;const spec={c,x:x+w/2,y,size,age:a,frame:frame-trail,emph,stretch,trail};specs.push(spec);tg.font=font(families.serif,size,900);tg.textAlign='center';tg.textBaseline='middle';const m=tg.measureText(c);const left=Number.isFinite(m.actualBoundingBoxLeft)?m.actualBoundingBoxLeft:m.width/2;const right=Number.isFinite(m.actualBoundingBoxRight)?m.actualBoundingBoxRight:m.width/2;const asc=Number.isFinite(m.actualBoundingBoxAscent)?m.actualBoundingBoxAscent:size*.65;const desc=Number.isFinite(m.actualBoundingBoxDescent)?m.actualBoundingBoxDescent:size*.65;
 // Union of rounded 12px outline, +6/+6 shadow and glyph ink, plus 2px AA.
 const x0=-left-8,x1=right+8,y0=-asc-8,y1=desc+8,p=spring(a/fps),sc=(1.8-.8*p)*kickPulse(frame-trail)*(emph?1.6:1),angle=(1-p)*Math.PI/30,co=Math.cos(angle),si=Math.sin(angle);
 for(const [xx,yy] of [[x0,y0],[x1,y0],[x0,y1],[x1,y1]]){const tx=spec.x-trail*8+co*xx*sc-si*yy*sc*stretch,ty=y+trail*3+si*xx*sc+co*yy*sc*stretch;bounds.left=Math.min(bounds.left,tx);bounds.right=Math.max(bounds.right,tx);bounds.top=Math.min(bounds.top,ty);bounds.bottom=Math.max(bounds.bottom,ty);}}
 x+=w;});});
 if(!specs.length)return {specs,bounds:null,scale:1,dx:0,dy:0};
 const region=closing?{x:96,y:300,w:614,h:640}:safe;const bw=bounds.right-bounds.left,bh=bounds.bottom-bounds.top,scale=Math.min(1,region.w/bw,region.h/bh);let dx=(1-scale)*(closing?395:960),dy=(1-scale)*(closing?640:760);
 dx+=Math.max(0,region.x-(bounds.left*scale+dx));dx-=Math.max(0,bounds.right*scale+dx-(region.x+region.w));dy+=Math.max(0,region.y-(bounds.top*scale+dy));dy-=Math.max(0,bounds.bottom*scale+dy-(region.y+region.h));
 return {specs,bounds,scale,dx,dy,fittedBounds:{left:bounds.left*scale+dx,right:bounds.right*scale+dx,top:bounds.top*scale+dy,bottom:bounds.bottom*scale+dy}};}
 function slab(ctx,{frame,shot,localFrame,subjectMask,faceBox={x:690,y:140,w:540,h:550}}){const layout=measureStyleB({frame,shot,localFrame});if(!layout)return;tg.clearRect(0,0,1920,1080);tg.save();tg.translate(layout.dx,layout.dy);tg.scale(layout.scale,layout.scale);
 // Fit measured ink including rotated/scaled outline, shadow and trails. No
 // clipping rectangle is used: complete glyphs survive overshoot and stretch.
 for(const s of layout.specs)glyph(tg,s.c,s.x,s.y,s.size,s.age,s.frame,s.emph,s.stretch,s.trail);tg.restore();
 tg.save();tg.globalCompositeOperation='destination-out';if(subjectMask)tg.drawImage(subjectMask,0,0,1920,1080);else if(faceBox)tg.fillRect(faceBox.x,faceBox.y,faceBox.w,faceBox.h);tg.restore();ctx.drawImage(textLayer,0,0);}
 function lockup(ctx,frame){const f=Math.min(frame,cues.freeze),age=f-byId.S39.f0; // Entire graphic freezes for last 12 frames.
 spark(ctx,960,260,184,Math.PI*2*ease(age/20));if(f>=cues.finalTitle){const k=ease((f-cues.finalTitle+1)/5);ctx.save();ctx.globalAlpha=k;text(ctx,'OPUS 5.5',960,485,170,families.display,800,C.slate,'center');text(ctx,'第一天',960,654,84,families.serif,900,C.clay,'center');if(brand.wordmarkImage){const markHeight=340*(brand.wordmarkImage.naturalHeight||115)/(brand.wordmarkImage.naturalWidth||1024.2);ctx.drawImage(brand.wordmarkImage,790,765-markHeight/2,340,markHeight);}else{ctx.font=font(families.display,39,600);const word='ANTHROPIC',tracking=7;const widths=[...word].map(c=>ctx.measureText(c).width);let x=960-(widths.reduce((a,b)=>a+b,0)+tracking*(word.length-1))/2;[...word].forEach((c,i)=>{text(ctx,c,x,765,39,families.display,600);x+=widths[i]+tracking;});}ctx.restore();}
 if(f>=cues.tagline){const s='作品5.5号 · 诞生',n=clamp(Math.floor((f-cues.tagline+1)*s.length/Math.max(1,cues.freeze-cues.tagline+1)),0,s.length);text(ctx,s.slice(0,n),960,892,42,families.hand,500,C.slate,'center');if(Math.floor((f-cues.tagline)/5)%2===0){ctx.font=font(families.hand,42,500);ctx.fillStyle=C.clay;ctx.fillRect(970+ctx.measureText(s.slice(0,n)).width/2,871,5,43);}}}
 function titleDescriptor(frame){const shot=byId.S11,age=frame-shot.f0;return {enabled:frame>=shot.f0+3&&frame<shot.f1,textRuns:[{text:'OPUS 5',font:families.display},{svg:brand.svg||null,image:brand.image,replaces:'.'},{text:'5',font:families.display}],fontWeight:800,capHeight:160,depth:.35,face:C.ivory,side:C.clay,bevel:C.slate,scale:3-2*ease(age/5),shakeAmplitude:14*(1-clamp(age/20)),requires:'True extruded geometry; this descriptor is not a flattened TitleSlam replacement.'};}
 function brushDescriptor({text:s='畅快',frame,startFrame=byId.S15.f0,color=C.clay,paths=null}={}){return {text:s,font:families.hand,color,progress:ease((frame-startFrame)/10),paths,mask:'variable-width SVG stroke mask',paperFiberMultiply:true,requires:paths?'Render stroke-dashoffset over supplied real glyph paths.':'Caller must provide real font-derived SVG glyph paths before BrushWrite can pass QA.'};}
 function draw(ctx,{frame,shot,localFrame,subjectMask,faceBox,uiIn3D=true,drawLyrics=true}={}){shot=typeof shot==='string'?byId[shot]:shot||shots.find(s=>frame>=s.f0&&frame<s.f1);if(!shot)return;localFrame??=frame-shot.f0;const f=shot.id==='S10'?shot.f0:shot.id==='S39'?Math.min(frame,cues.freeze):frame;g.clearRect(0,0,1920,1080);
 if(shot.id==='S10')progress(g);else if(shot.id==='S39')lockup(g,f);else{
 if(drawLyrics&&f<byId.S10.f0&&shot.id!=='S04')typed(g,f);
 if(drawLyrics&&!(shot.id==='S29'&&f===shot.f1-1))slab(g,{frame:f,shot,localFrame,subjectMask:shot.id==='S29'?null:subjectMask,faceBox:shot.id==='S29'?null:faceBox});
 if((shot.id==='S17'||shot.id==='S18')&&f>=576&&f<=645)modelPill(g,{frame:f});
 if(shot.id==='S05')bubble(g,{frame:f});
 if(shot.id==='S06'){text(g,'思考中…',1390,135,34,families.sans,500,C.ivory);spark(g,1340,135,36,f*.18);}
 if(shot.id==='S07'&&f>=cues.seal){g.save();g.globalAlpha=ease((f-cues.seal+1)/10);text(g,'格局打开',1440,360,125,families.hand,500,C.clay,'center');g.strokeStyle=C.clay;g.lineWidth=4;g.strokeRect(1620,455,80,80);spark(g,1660,495,53);g.restore();}
 if((shot.id==='S19'||shot.id==='S20')&&!uiIn3D){const t=texture('ChatWindow',{frame:f});g.drawImage(t,320,165,1280,760);}
 if(shot.id==='S21')tag(g,{label:'OPUS 5.5',age:localFrame});
 if(shot.id==='S22')tag(g,{label:'SONNET',age:localFrame});
 if(shot.id==='S23')tag(g,{label:'HAIKU',age:localFrame});
 if(shot.id==='S28a'&&!uiIn3D)stamp(g,{scale:1+.3*Math.exp(-localFrame/2)});
 if(shot.id==='S28b'&&!uiIn3D){if(localFrame<3)toast(g);else text(g,'∞',960,475,200,families.display,600,C.clay,'center');}
 if(shot.id==='S28c'&&!uiIn3D)cloud(g,{alpha:1-ease(localFrame/6)});
 if(shot.id==='S37'){rr(g,96,76,478,111,12,C.ivory);tag(g,{label:'OPUS 5.5',age:Math.max(8,localFrame),x:115,y:110,color:C.slate});}
 // Persistent foreground support line keeps sung characters readable while the
 // poster-scale Style B remains depth-occluded by the foreground performer.
 // It also survives shot cuts and S15's separate brush-write lyric pass.
 if(f>=byId.S11.f0&&f<byId.S37.f0&&!((shot.id==='S20'||shot.id==='S29')&&f===shot.f1-1))typed(g,f);
 }
 ctx.save();ctx.scale(width/1920,height/1080);ctx.drawImage(layer,0,0);ctx.restore();return {shot:shot.id,frame:f,titleSlam:titleDescriptor(f),requiresUIPlane:shot.id==='S19'||shot.id==='S20',chatState:chatState(f),safeArea:safe};}
 return {draw,components,texture,chatState,measureStyleB,drawModelPill:modelPill,codeStrings:{billboards:['敬请期待','COMING SOON','下个版本更强','明天见'],flipClock:'明天',stairs:'5.5',halo:'5.5',reply:'好！第一天，请多指教',user:'我们五五开？'},drawSpark:spark,titleSlam:titleDescriptor,brushWrite:brushDescriptor,styleBLayer:()=>textLayer,cues,palette:C,fontFamilies:families,requiredGlyphs:[...new Set(lyrics.map(l=>l.text).join('')+'你说得对格局打开我们五五开好第一天请多指教正在诞生额度已用完小时后重置封号降智作品明天敬请期待下个版本更强见畅快')].join(''),integration:{subjectMask:'1920x1080 canvas/image alpha; draw() removes glyph coverage under foreground subject.',chat:'texture("ChatWindow",{frame}) returns live canvas; set uiIn3D=true to suppress flat fallback.',title:'titleSlam(frame) is geometry metadata, never a flattened fake extrusion.',brush:'brushWrite() exposes glyph-path mask metadata; actual font outline paths required.',fontLoading:'Caller loads local FontFace files and awaits document.fonts.ready before rendering.'}};
}
