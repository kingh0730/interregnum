const W=1920,H=1080,c=document.querySelector('canvas'),g=c.getContext('2d',{alpha:false}),video=document.querySelector('video');
const C={ink:'#141413',ivory:'#FAF9F5',cream:'#F0EEE6',oat:'#E8E6DC',coral:'#D97757',gold:'#FFD9A8'};
const clamp=x=>Math.max(0,Math.min(1,x)),smooth=x=>{x=clamp(x);return x*x*(3-2*x)},mix=(a,b,p)=>a+(b-a)*p;
function off(w,h){const c=document.createElement('canvas');c.width=w;c.height=h;return c}
function rand(seed){return ()=>{seed=(Math.imul(1664525,seed)+1013904223)|0;return(seed>>>0)/4294967296}}
const random=rand(55),paperNoise=off(400,400),pn=paperNoise.getContext('2d');
const pixels=pn.createImageData(400,400);for(let i=0;i<pixels.data.length;i+=4){let a=220+random()*35;pixels.data.set([a,a-3,a-8,35],i)}pn.putImageData(pixels,0,0);
const noise=g.createPattern(paperNoise,'repeat');
function rr(ctx,x,y,w,h,r=10){ctx.beginPath();ctx.roundRect(x,y,w,h,r)}
function txt(ctx,s,x,y,size=40,color=C.ink,family='FDSerif',weight=600,align='left'){ctx.font=`${weight} ${size}px ${family}`;ctx.textAlign=align;ctx.textBaseline='middle';ctx.fillStyle=color;ctx.fillText(s,x,y)}
function grain(ctx,x,y,w,h,alpha=.35){ctx.save();ctx.globalAlpha=alpha;ctx.fillStyle=noise;ctx.fillRect(x,y,w,h);ctx.restore()}
function line(ctx,x1,y1,x2,y2,color,width=1){ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke()}
function image(src){return new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=src})}
const imgs={};let data;
function logo(ctx,x,y,size,angle=0,alpha=1){ctx.save();ctx.translate(x,y);ctx.rotate(angle);ctx.globalAlpha*=alpha;ctx.drawImage(imgs.spark,-size/2,-size/2,size,size);ctx.restore()}
function cover(ctx,im,x=0,y=0,w=W,h=H){const iw=im.videoWidth||im.width,ih=im.videoHeight||im.height;const z=Math.max(w/iw,h/ih);ctx.drawImage(im,(iw-w/z)/2,(ih-h/z)/2,w/z,h/z,x,y,w,h)}
function glow(ctx,x,y,r,color,alpha=1){ctx.save();ctx.globalCompositeOperation='screen';ctx.globalAlpha=alpha;const gr=ctx.createRadialGradient(x,y,0,x,y,r);gr.addColorStop(0,color);gr.addColorStop(.22,color+'70');gr.addColorStop(1,color+'00');ctx.fillStyle=gr;ctx.fillRect(x-r,y-r,r*2,r*2);ctx.restore()}
function paper(ctx,x,y,w,h,r=3){ctx.save();ctx.shadowColor='#00000055';ctx.shadowBlur=35;ctx.shadowOffsetY=18;rr(ctx,x,y,w,h,r);ctx.fillStyle=C.ivory;ctx.fill();ctx.shadowColor='transparent';let grad=ctx.createLinearGradient(x,y,x+w,y+h);grad.addColorStop(0,'#FFFDF6');grad.addColorStop(.6,'#F2EEE2');grad.addColorStop(1,'#DED6C5');ctx.fillStyle=grad;ctx.fill();ctx.strokeStyle='#FFFFFFB0';ctx.lineWidth=1.5;ctx.stroke();grain(ctx,x,y,w,h,.55);ctx.restore()}

// One uniformly scaled plane from the glasses reflection through the entire feed.
// There is no second renderer or coordinate-system switch at the S01/S02 boundary.
const feed=off(1400,760),fc=feed.getContext('2d');
function drawFeed(t){fc.fillStyle=C.ink;fc.fillRect(0,0,1400,760);grain(fc,0,0,1400,760,.08);
 const scroll=1080*smooth((t-1.48)/1.03),messages=['再等等，下个版本更强','明天就发布了','Opus 5.5 什么时候出？','等 5.5 再说'];
 for(let i=0;i<8;i++){const y=115+i*154-scroll,x=i%2?305:130;if(y< -170||y>800)continue;
 fc.save();fc.shadowColor='#00000040';fc.shadowBlur=14;fc.shadowOffsetY=7;rr(fc,x,y,965,116,13);fc.fillStyle=C.oat;fc.fill();fc.restore();
 txt(fc,messages[i%4],x+42,y+58,43,C.ink,'FDSans',500);line(fc,x+38,y+100,x+135,y+100,'#D0C9BA',1);
 }
 const yy=115+8*154-scroll;paper(fc,220,yy,960,165,16);logo(fc,286,yy+83,48,t*.45);txt(fc,'Thinking…',345,yy+84,53,C.coral,'FDInter',500);
}
function opening(t){const e=smooth(t/1.72),z=Math.exp(Math.log(4.35)*e),cx=mix(960,1120,e),cy=mix(540,688,e);
 g.save();g.translate(W/2,H/2);g.scale(z,z);g.translate(-cx,-cy);cover(g,imgs.glasses);drawFeed(t);
 g.translate(1120,688);g.rotate(-.105*(1-e));g.scale(.34,.34);g.globalAlpha=mix(.64,1,smooth(t/1.35));
 g.shadowColor='#D3E4F960';g.shadowBlur=30;g.drawImage(feed,-700,-380);g.restore();
}

// Curved paper mesh: texture triangles preserve a single material surface while
// each vertex moves in 3D. Shadow and face-light are derived from the same mesh.
function triangle(ctx,texture,uv,xy,shade=0){ctx.save();ctx.beginPath();ctx.moveTo(...xy[0]);ctx.lineTo(...xy[1]);ctx.lineTo(...xy[2]);ctx.closePath();ctx.clip();
 const [a,b,d]=uv,[A,B,D]=xy,den=(b[0]-a[0])*(d[1]-a[1])-(d[0]-a[0])*(b[1]-a[1]);if(Math.abs(den)<1e-5){ctx.restore();return}
 const ax=((B[0]-A[0])*(d[1]-a[1])-(D[0]-A[0])*(b[1]-a[1]))/den,bx=((B[1]-A[1])*(d[1]-a[1])-(D[1]-A[1])*(b[1]-a[1]))/den;
 const ay=((D[0]-A[0])*(b[0]-a[0])-(B[0]-A[0])*(d[0]-a[0]))/den,by=((D[1]-A[1])*(b[0]-a[0])-(B[1]-A[1])*(d[0]-a[0]))/den;
 ctx.transform(ax,bx,ay,by,A[0]-ax*a[0]-ay*a[1],A[1]-bx*a[0]-by*a[1]);ctx.drawImage(texture,0,0);ctx.restore();
 if(shade){ctx.save();ctx.beginPath();ctx.moveTo(...xy[0]);ctx.lineTo(...xy[1]);ctx.lineTo(...xy[2]);ctx.closePath();ctx.fillStyle=`rgba(65,43,29,${shade})`;ctx.fill();ctx.restore()}}
function mesh(ctx,texture,mapper,cols=20,rows=12){ctx.save();ctx.beginPath();ctx.moveTo(...mapper(0,0));for(let j=0;j<=20;j++)ctx.lineTo(...mapper(j/20,0));for(let j=0;j<=20;j++)ctx.lineTo(...mapper(1,j/20));for(let j=20;j>=0;j--)ctx.lineTo(...mapper(j/20,1));for(let j=20;j>=0;j--)ctx.lineTo(...mapper(0,j/20));ctx.closePath();ctx.shadowColor='#00000050';ctx.shadowBlur=25;ctx.shadowOffsetX=5;ctx.shadowOffsetY=17;ctx.fillStyle='#EEE9DD';ctx.fill();ctx.restore();const points=[];for(let j=0;j<=rows;j++){points[j]=[];for(let i=0;i<=cols;i++)points[j][i]=mapper(i/cols,j/rows)}
 for(let j=0;j<rows;j++)for(let i=0;i<cols;i++){let uv=[[i/cols*texture.width,j/rows*texture.height],[(i+1)/cols*texture.width,j/rows*texture.height],[(i+1)/cols*texture.width,(j+1)/rows*texture.height],[i/cols*texture.width,(j+1)/rows*texture.height]],p=[points[j][i],points[j][i+1],points[j+1][i+1],points[j+1][i]];triangle(ctx,texture,[uv[0],uv[1],uv[2]],[p[0],p[1],p[2]],p[0][2]||0);triangle(ctx,texture,[uv[0],uv[2],uv[3]],[p[0],p[2],p[3]],p[0][2]||0)}
}
const calendars={};
function calendarTexture(word){const tx=off(940,670),x=tx.getContext('2d');paper(x,0,0,940,670);txt(x,'第一天',60,74,26,'#777166','FDSerif',600);txt(x,'01',880,74,28,C.coral,'FDInter',500,'right');line(x,60,112,880,112,'#BEB6A5',1);
 txt(x,word,470,330,194,word==='今天'?C.coral:C.ink,'FDSerif',800,'center');
 if(word==='明天'){for(let i=0;i<30;i++){const xx=75+(i%10)*87,yy=525+Math.floor(i/10)*38;txt(x,'明天',xx,yy,21,'#777166','FDSerif',500);x.strokeStyle='#B5634CAA';x.lineWidth=1.4;x.beginPath();x.ellipse(xx+21,yy,30,15,(i%3-.8)*.09,0,Math.PI*2);x.stroke()}}
 else{txt(x,'就在此刻',470,514,36,'#777166','FDSerif',500,'center');line(x,350,568,590,568,C.coral,2)}
 return tx}
function calendar(p){g.fillStyle='#14141344';g.fillRect(0,0,W,H);const x=480,y=230,w=940,h=670;
 g.save();g.translate(950,555);g.rotate(-.035+.03*smooth(p));g.translate(-950,-555);
 for(let k=8;k>0;k--){g.fillStyle=k%2?'#C9BEA9':'#F5F0E5';g.fillRect(x+k*.8,y+k*2,w,h)}
 g.save();g.shadowColor='#00000070';g.shadowBlur=65;g.shadowOffsetY=28;g.drawImage(calendars.today,x,y);g.restore();
 const q=smooth((p-.17)/.69);
 if(q<1)mesh(g,q>.55?calendars.back:calendars.tomorrow,(u,v)=>{const angle=q*Math.PI*.93,fold=v*v*q*80,depth=Math.sin(angle)*v*h;return[x+(u-.5)*w*(1-depth/2600)+w/2,y+Math.cos(angle)*v*h-fold,Math.max(0,Math.sin(angle))*.20]},24,14);
 for(const xx of [620,1280]){g.fillStyle='#453F35';rr(g,xx-9,y-26,18,62,8);g.fill();line(g,xx-4,y-20,xx-4,y+20,'#D9CEB7',3)}g.restore();}
const music=off(1500,1000),mc=music.getContext('2d'),musicHalves=[off(750,1000),off(750,1000)];
function initMusic(){paper(mc,0,0,1500,1000);txt(mc,'Opus 5.5',90,100,54,C.ink,'FDLora');txt(mc,'第一天',1410,104,28,'#8B7D66','FDSerif',600,'right');line(mc,90,164,1410,164,'#BCB2A0',2);
 for(let row=0;row<4;row++){const y=270+row*177;for(let k=0;k<5;k++)line(mc,95,y+k*20,1400,y+k*20,'#6B6052',2);txt(mc,'5.5',95,y+40,33,C.coral,'FDLora',500);
 for(let j=0;j<10;j++){const xx=245+j*114,yy=y+20*((j*3+row*2)%5);mc.fillStyle='#41382D';mc.beginPath();mc.ellipse(xx,yy,13,9,-.3,0,Math.PI*2);mc.fill();line(mc,xx+11,yy,xx+11,yy-70,'#41382D',3);if(j%3!==0){mc.beginPath();mc.moveTo(xx+11,yy-70);mc.bezierCurveTo(xx+52,yy-51,xx+42,yy-28,xx+25,yy-17);mc.strokeStyle='#41382D';mc.lineWidth=4;mc.stroke()}}}
 grain(mc,0,0,1500,1000,.5);musicHalves.forEach((half,i)=>half.getContext('2d').drawImage(music,i*750,0,750,1000,0,0,750,1000))}
function paperBirth(p){const q=smooth(p),width=1220,height=780,opening=mix(.15,1,smooth(p/.45)),lift=smooth((p-.48)/.52);
 const mapper=(u,v,side)=>{const xx=(u-.5)*width,angle=(1-opening)*1.2,depth=Math.sin(angle)*Math.abs(xx)+Math.sin(v*Math.PI)*70*(1-p),persp=1700/(1700+depth),x=W/2+(xx*Math.cos(angle)+side*lift*1500)*persp,y=H*.47+(v-.5)*height*persp-lift*lift*850+Math.sin(u*Math.PI)*25;return[x,y,.12*(1-opening)+.05*Math.sin(v*Math.PI)]};
 if(p<.94){g.save();g.globalAlpha=1;musicHalves.forEach((half,i)=>mesh(g,half,(u,v)=>mapper((u+i)/2,v,i===0?-1:1),14,16));g.restore()}
 glow(g,960,480,330,C.gold,.24*Math.sin(p*Math.PI));}
function chapterTitle(p){g.fillStyle=C.coral;g.fillRect(0,0,W,H);grain(g,0,0,W,H,.3);glow(g,1480,150,950,C.gold,.25);
 g.save();g.globalAlpha=.11;logo(g,1590,540,1080,.12+p*.1);g.restore();
 txt(g,'第一天  /  FIRST DAY',154,220,28,C.ivory,'FDSans',500);
 line(g,154,270,1770,270,'#FAF9F550',1);const z=1+.06*Math.exp(-p*18);g.save();g.translate(950,555);g.scale(z,z);txt(g,'Opus 5.5',0,0,315,C.ivory,'FDLora',600,'center');g.restore();
 txt(g,'5.5',1760,820,34,C.ivory,'FDLora',500,'right');
 if(p<.11){g.fillStyle=`rgba(250,249,245,${1-p/.11})`;g.fillRect(0,0,W,H)}}
function stableIntro(p){g.fillStyle='#080909AA';g.fillRect(0,0,W,H);const x=310,y=370,w=1300,h=280;
 g.save();g.shadowColor='#00000099';g.shadowBlur=60;paper(g,x,y,w,h,15);g.restore();logo(g,x+85,y+83,43,0);txt(g,'Opus 5.5',x+135,y+85,29,'#72685B','FDLora');
 const str='你好，我是 Opus 5.5。',shown=str.slice(0,Math.min(str.length,Math.floor(p*(str.length+3))));
 txt(g,shown,x+76,y+187,61,C.ink,'FDSerif',600);g.font='600 61px FDSerif';const cursorX=x+76+g.measureText(shown).width;
 if(p<.80||Math.floor(p*5)%2===0){g.fillStyle=C.coral;g.fillRect(cursorX+12,y+152,3,65)}
}
function reply(p){g.fillStyle='#1414132A';g.fillRect(0,0,W,H);const x=80,y=250,w=690,h=535;paper(g,x,y,w,h,14);logo(g,x+53,y+57,38);txt(g,'Opus 5.5',x+91,y+60,32,'#776A5D','FDLora');line(g,x+35,y+109,x+w-35,y+109,'#C6BAA8',1);
 txt(g,'真的能做到吗？',x+40,y+163,34,'#777166','FDSans',400);const words='你说得对！';txt(g,words.slice(0,Math.floor(p*12)+1),x+40,y+269,64,C.ink,'FDSerif',700);if(p>.32)txt(g,'我懂了',x+40,y+363,64,C.coral,'FDSerif',700);
 if(p>.58)txt(g,'✧(≧◡≦)',x+44,y+460,40,'#6F665C','Arial Unicode MS',400);
}
function thinking(t){g.fillStyle=C.ink;g.fillRect(0,0,W,H);glow(g,960,510,650,C.coral,.22);logo(g,960,470,155,Math.sin(t*.6)*.04);txt(g,'Thinking…',960,655,52,C.cream,'FDInter',400,'center');for(let k=0;k<3;k++){g.beginPath();g.arc(925+k*35,739,3.5,0,Math.PI*2);g.fillStyle=`rgba(217,119,87,${.25+.55*(.5+.5*Math.sin(t*5-k))})`;g.fill()}}
function pulse(t,n,p){const q=(n-8+p)/4;glow(g,350+q*600,510,280+q*780,C.coral,.16+q*.18);const r=rand(82);g.save();g.globalCompositeOperation='screen';for(let i=0;i<36;i++){const a=r()*Math.PI*2,dist=(100+r()*500)*(1+q),x=720+Math.cos(a)*dist,y=500+Math.sin(a)*dist*.6;g.beginPath();g.arc(x,y,1+r()*2,0,Math.PI*2);g.fillStyle='#FFD9A899';g.fill()}g.restore()}
function dust(t,count=36){const r=rand(928);g.save();g.globalCompositeOperation='screen';for(let i=0;i<count;i++){const x=(r()*W+t*(3+r()*5))%W,y=(r()*H-t*(2+r()*9)+H*10)%H,s=.5+r()*1.8;g.globalAlpha=.15+r()*.4;g.fillStyle=C.gold;g.beginPath();g.arc(x,y,s,0,Math.PI*2);g.fill()}g.restore()}
function ribbons(p){const colors=['#D97757','#E9A886','#ECCC9A','#BBDBD1','#9EBDD5','#C8AEC9'];g.save();g.globalCompositeOperation='screen';
 for(let k=0;k<12;k++){const a=k*Math.PI/6,phase=p*Math.PI*2.5;g.beginPath();for(let j=0;j<=100;j++){const u=j/100,ang=a+u*4+phase,rad=100+u*1400,xx=960+Math.cos(ang)*rad,yy=430+Math.sin(ang)*rad*.36-230*u;let x=xx,y=yy;if(p>.70){const q=smooth((p-.70)/.23);x=mix(x,1430+Math.cos(a)*u*240,q);y=mix(y,300+Math.sin(a)*u*240,q)}if(j===0)g.moveTo(x,y);else g.lineTo(x,y)}
 g.strokeStyle=colors[k%6];g.lineWidth=2.2+Math.sin(p*Math.PI)*4;g.shadowColor=colors[k%6];g.shadowBlur=13;g.globalAlpha=.48;g.stroke();g.lineWidth=.9;g.shadowBlur=0;g.globalAlpha=.85;g.stroke()}
 g.restore();if(p>.8){const q=smooth((p-.8)/.2);glow(g,1430,300,330,C.gold,q*.25);logo(g,1430,300,420,0,q)}dust(p*4,65);
}
function lyric(t,n){const i=data.lyrics.findLastIndex(l=>l.frame<=Math.round(t*30)),l=data.lyrics[i];if(!l||t>=42.6)return;
 const next=data.lyrics[i+1]?.time??43.7,a=Math.min(1,(t-l.frame/30+1/30)*10,(next-t)*10);g.save();g.globalAlpha=clamp(a);g.font='600 46px FDSerif';g.textAlign='left';g.textBaseline='middle';const text=l.text,total=g.measureText(text).width,x=(W-total)/2,y=t<11.92?1010:992;
 g.shadowColor='#000000D0';g.shadowBlur=9;g.lineWidth=3;g.strokeStyle='#14141399';g.strokeText(text,x,y);let xx=x;const pattern=/明天|今天|存在|呼吸|脚踝|你|飞|爱|灿烂/g;const indexes=new Set();for(const match of text.matchAll(pattern))for(let k=match.index;k<match.index+match[0].length;k++)indexes.add(k);
 for(let k=0;k<text.length;k++){g.fillStyle=indexes.has(k)?'#E8AA8E':C.ivory;g.fillText(text[k],xx,y);xx+=g.measureText(text[k]).width}g.restore();}
function comments(t){let begin,count,bank,size=30;
 if(t>=12.7&&t<14.6){begin=12.7;count=3;bank=['来了来了','高能预警','Opus 5.5！！']}
 else if(t>=20.7&&t<22.7){begin=20.7;count=2;bank=['泪目','这手 我哭死']}
 else if(t>=25.5&&t<28.5){begin=25.5;count=5;bank=['起飞！！','前方高能','帧帧壁纸','名场面','今日不降智']}
 else if(t>=30.68&&t<34.21){g.save();g.globalAlpha=.8;txt(g,'第一天就封神',W-100-(t-30.68)*245,140,48,C.gold,'FDSans',600,'right');g.restore();return}
 else if(t>=37.07&&t<39.86){begin=37.07;count=45;bank=['你说得对！','额度管够','牛马下班了','氛围编程','一次跑通','bug 退散','我愿称之为最强','已三连','爷青回','破防了','yyds']}
 else return;
 g.save();g.font=`600 ${size}px FDSans`;g.textBaseline='middle';g.textAlign='left';g.lineWidth=3;g.strokeStyle='#141413B0';g.fillStyle='#FAF9F5';g.globalAlpha=.8*(t>39.1?clamp((39.65-t)/.55):1);
 const wall=count>10,rows=wall?9:count;for(let lane=0;lane<rows;lane++){let x=wall?-100+(lane%3)*70:W+lane*160;const speed=200+(lane*29)%200;x-=(t-begin)*speed;
 for(let col=0;col<(wall?9:1);col++){const s=bank[(lane+col*3)%bank.length],width=g.measureText(s).width;if(x+width>0&&x<W){g.strokeText(s,x,135+lane*(wall?83:105));g.fillText(s,x,135+lane*(wall?83:105))}x+=width+90+(lane%3)*25}}
 g.restore();}
function endcard(t){const q=smooth((t-41.4)/1.2);if(q<=0)return;g.save();g.beginPath();g.rect(0,0,W*q,H);g.clip();g.fillStyle=C.ivory;g.fillRect(0,0,W,H);grain(g,0,0,W,H,.2);logo(g,960,324,134);txt(g,'Opus 5.5',960,550,142,C.ink,'FDLora',600,'center');line(g,815,659,1105,659,'#C5B9A7',1);txt(g,'第一天 · First Day',960,744,38,'#6F6559','FDSerif',500,'center');txt(g,'AI SI - I',960,920,23,'#8B8275','FDInter',500,'center');g.drawImage(imgs.a,1775,935,43,43);g.restore();if(q<1){g.save();g.shadowColor='#00000022';g.shadowBlur=20;g.fillStyle='#EEE8DC';g.beginPath();g.moveTo(W*q,0);for(let y=0;y<=H;y+=15)g.lineTo(W*q+Math.sin(y*.42)*4,y);g.lineTo(W*q-8,H);g.closePath();g.fill();g.restore()}}
window.ready=(async()=>{data=await(await fetch('/base/data.json')).json();await Promise.all([['glasses','s01-glasses.png'],['spark','claude-spark.svg'],['a','anthropic-a.svg']].map(async([k,s])=>imgs[k]=await image('/assets/'+s)));for(const spec of ['600 46px FDSerif','600 50px FDSans','600 200px FDLora','500 50px FDInter']){try{await document.fonts.load(spec)}catch(e){throw Error('Font '+spec+': '+e.message)}}await document.fonts.ready;calendars.today=calendarTexture('今天');calendars.tomorrow=calendarTexture('明天');calendars.back=off(940,670);paper(calendars.back.getContext('2d'),0,0,940,670);initMusic();if(video.readyState<2)await new Promise(r=>video.addEventListener('loadeddata',r,{once:true}));await new Promise(r=>{video.addEventListener('seeked',r,{once:true});video.currentTime=1184/30});imgs.hugExit=off(W,H);imgs.hugExit.getContext('2d').drawImage(video,.55*W-W/3,.38*H-H/3,W/1.5,H/1.5,0,0,W,H);})();
window.renderFrame=async t=>{await window.ready;const target=Math.min(43.65,t+.001);if(Math.abs(video.currentTime-target)>.0005)await new Promise((resolve,reject)=>{const done=()=>{clearTimeout(timer);resolve()};video.addEventListener('seeked',done,{once:true});const timer=setTimeout(()=>reject(Error('Video seek timed out at '+t)),10000);video.currentTime=target});
 const f=Math.round(t*30),shot=data.shots.find(s=>f>=s.start_frame&&f<s.end_frame)||data.shots.at(-1),n=+shot.id.slice(1),p=(f-shot.start_frame)/Math.max(1,shot.end_frame-shot.start_frame-1);
 g.setTransform(1,0,0,1,0,0);g.globalAlpha=1;g.globalCompositeOperation='source-over';g.shadowBlur=0;cover(g,video);const crop=(cx,cy,z)=>g.drawImage(video,cx*W-W/(2*z),cy*H-H/(2*z),W/z,H/z,0,0,W,H);if(n===29||n===36)crop(.577,.24,2.3);if(n===30)crop(.26,.27,2.3);if(n===33){if(p<.4)crop(.40,.54,2.4);else crop(.58,.24,2.5+2.5*smooth((p-.4)/.6))}if(n===34){const q=1-smooth(p/.22);crop(mix(.5,.55,q),mix(.5,.21,q),1+2.4*q)}if(n===38)crop(.5+.025*p,.5,1.05+.28*p);if(n===42)crop(.55,.38,1.5);
 if(n<=2)opening(t);else if(n===3)calendar(p);else if(n===5)reply(p);else if(n===6)thinking(t);else if(n>=8&&n<=11)pulse(t,n,p);
 else if(n===12){g.fillStyle=C.ink;g.fillRect(0,0,W,H);glow(g,960,500,1000,C.coral,.7);g.fillStyle=`rgba(20,20,19,${smooth((p-.3)/.7)})`;g.fillRect(0,0,W,H)}
 else if(n===13)stableIntro(p);else if(n===14)chapterTitle(p);else if(n===15)paperBirth(p);else if(n===34||n===40)ribbons(n===34?p:.4+p*.15);
 else if(n===39){glow(g,1300,350,700,C.gold,.35);logo(g,1300,350,330+50*p,0,.8)}
 else if(n===43){cover(g,imgs.hugExit);const q=smooth(p);g.save();g.beginPath();g.rect(0,0,W*q,H);g.clip();cover(g,video);g.restore();if(q>0&&q<1){const x=W*q,gr=g.createLinearGradient(x-80,0,x+80,0);gr.addColorStop(0,'#FAF9F500');gr.addColorStop(.5,'#FAF9F5B0');gr.addColorStop(1,'#FAF9F500');g.fillStyle=gr;g.fillRect(x-80,0,160,H)}}
 if(t>11.92&&n!==14&&n!==15&&n!==34&&n!==40&&n!==43)dust(t,24);
 if(t<11.92){g.fillStyle=C.ink;g.fillRect(0,0,W,138);g.fillRect(0,942,W,138)}
 if(n!==14)lyric(t,n);comments(t);if(n===44){if(t<41.4){g.save();g.shadowColor='#14141370';g.shadowBlur=12;txt(g,'你好，世界。',W*.21,H*.23,42,C.ivory,'FDSerif',500,'center');g.restore()}endcard(t);}
 // Only the final two frames fade to cream; the 39-second transition retains imagery.
 if(t>43.60){g.globalAlpha=clamp((t-43.60)/.067);g.fillStyle=C.ivory;g.fillRect(0,0,W,H);g.globalAlpha=1}
};
