import * as T from 'three';
import {Pose,neutral,COLORS} from './rig';
import {lerp,clamp,hash} from './vendor/pdoom/util';
const sphere=new T.SphereGeometry(1,28,20), cyl=new T.CylinderGeometry(1,1,1,20),shoeGeo=new T.SphereGeometry(1,24,16);
const mat=(c:string,rough=.55,metal=0)=>new T.MeshStandardMaterial({color:c,roughness:rough,metalness:metal});
const skin=mat('#f4d2b9',.62),white=mat('#fffcf1',.38),black=mat('#272934',.45),iris=mat('#684b43',.3),pupil=mat('#171822',.25),blush=mat('#ecae9f',.8),gold=mat('#dcb55f',.3,.65);
function ell(parent:T.Object3D,m:T.Material,x:number,y:number,z:number,sx:number,sy:number,sz:number){let o=new T.Mesh(sphere,m);o.position.set(x,y,z);o.scale.set(sx,sy,sz);parent.add(o);return o;}
function box(parent:T.Object3D,m:T.Material,x:number,y:number,z:number,sx:number,sy:number,sz:number){let o=new T.Mesh(new T.BoxGeometry(sx,sy,sz,1,1,1),m);o.position.set(x,y,z);parent.add(o);return o;}
function tube(parent:T.Object3D,points:T.Vector3[],radius:number,m:T.Material){const c=new T.CatmullRomCurve3(points);const o=new T.Mesh(new T.TubeGeometry(c,20,radius,7,false),m);parent.add(o);return o;}
function torus(parent:T.Object3D,m:T.Material,x:number,y:number,z:number,r:number,w:number){let o=new T.Mesh(new T.TorusGeometry(r,w,8,32),m);o.position.set(x,y,z);parent.add(o);return o;}
function bone(parent:T.Object3D,m:T.Material,r:number){const o=new T.Mesh(cyl,m);o.userData.radius=r;parent.add(o);return o;}
function connect(o:T.Mesh,a:T.Vector3,b:T.Vector3,r?:number){o.position.copy(a).add(b).multiplyScalar(.5);const d=b.clone().sub(a);o.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),d.clone().normalize());o.scale.set(r||o.userData.radius,d.length(),r||o.userData.radius);}
function solve(a:T.Vector3,b:T.Vector3,l1:number,l2:number,bend:T.Vector3){const d=b.clone().sub(a);let D=Math.min(d.length(),l1+l2-.001);d.normalize();const t=(D*D+l1*l1-l2*l2)/(2*D);const n=bend.clone().addScaledVector(d,-bend.dot(d)).normalize();return a.clone().addScaledVector(d,t).addScaledVector(n,Math.sqrt(Math.max(.0001,l1*l1-t*t)));}
export class Doll{
 group=new T.Group();body=new T.Group();head=new T.Group();legs:any[]=[];arms:any[]=[];root=new T.Group();shadow=new T.Group();bodyVisible=true;index:number;h:number;phase=0;
 constructor(index:number){this.index=index;this.h=[2.22,2.52,2.63,2.03,1.91,2.40,2.30,2.16,2.38,2.1,2.17,2.2,2.2,2.17,2.25,2.55,2.38,2.48][index]||2.3;this.group.add(this.root);this.root.add(this.body);const lead=index%6;
 const cloth=mat(index<6?['#ede8df','#cf8065','#25252d','#275596','#f5d4b2','#827ba9'][index]:COLORS[index%15]);const pants=mat(lead===4?'#f9e5ce':lead===3?'#29476b':'#343540');const accent=mat(COLORS[index%15],.38);const hair=mat(['#392d2b','#e8cfac','#242328','#332b2a','#40302c','#777da8'][lead],.64);
 // Soft sculpted torso with a real back and layered clothing.
 ell(this.body,cloth,0,1.34,0,.32,.46,.22);ell(this.body,cloth,0,1.62,0,.36,.21,.23);
 ell(this.body,skin,0,1.82,0,.10,.17,.10);this.body.add(this.head);this.head.position.set(0,2.09,0);
 const face=ell(this.head,skin,0,0,.025,lead===2?.235:.268,lead===2?.31:.29,.25);
 ell(this.head,skin,-.259,-.015,0,.06,.085,.045);ell(this.head,skin,.259,-.015,0,.06,.085,.045);
 // Eye whites, colored irises, deep pupils, tiny specular glints and quiet mouth.
 for(const side of [-1,1]){const ex=side*.105;ell(this.head,white,ex,.018,.237,.080,.068,.024);ell(this.head,iris,ex,.011,.256,.042,.050,.012);ell(this.head,pupil,ex,.010,.266,.024,.037,.008);ell(this.head,white,ex-.013,.031,.274,.012,.014,.006);ell(this.head,blush,side*.171,-.07,.218,.05,.016,.010);tube(this.head,[new T.Vector3(ex-.066,.085,.235),new T.Vector3(ex,.099+(lead===2&&side<0?.025:0),.247),new T.Vector3(ex+.059,.088,.235)],.012,hair);}
 ell(this.head,skin,0,-.057,.275,.025,.023,.020);tube(this.head,[new T.Vector3(-.034,-.137,.24),new T.Vector3(0,-.145,.249),new T.Vector3(.034,-.133,.24)],.007,mat('#ae6c65'));
 // Sculpted cap and curved locks: three-dimensional silhouettes, not a portrait card.
 ell(this.head,hair,0,.115,-.068,.29,.23,.247);
 for(let j=0;j<10;j++){const u=(j-4.5)/4.5;const x=u*.26;const endy=lead===1?-.10+.05*Math.sin(j):.015+.06*Math.sin(j*1.8);tube(this.head,[new T.Vector3(x*.55,.315,-.01),new T.Vector3(x,.26,.16),new T.Vector3(x*.91,endy,.22)],lead===1?.045:.041,(lead===2&&j>6)?white:hair);}
 if(lead===0){for(let s of [-1,1])for(let j=0;j<4;j++)tube(this.head,[new T.Vector3(s*.24,.18,.0),new T.Vector3(s*(.28+j*.008),-.02,.04),new T.Vector3(s*.23,-.21-j*.025,.04)],.045,hair);for(let j=0;j<8;j++)ell(this.body,hair,-.27+Math.sin(j*2)*.024,1.85-j*.06,.19,.045,.055,.04);for(let j=0;j<3;j++){const o=torus(this.body,hair,-.27+Math.cos(j*2.1)*.034,1.40+Math.sin(j*2.1)*.034,.24,.047,.017);o.scale.set(1,.7,1);}const bag=ell(this.body,white,0,1.43,-.27,.25,.22,.10);for(let j=-1;j<=1;j++)ell(this.body,accent,j*.065,1.44,-.367,.019,.019,.006);torus(this.body,white,0,1.77,0,.18,.063).rotation.x=Math.PI/2;}
 if(lead===1){for(let j=0;j<9;j++){const ang=j/9*Math.PI*2;const ray=ell(this.head,accent,-.22+Math.cos(ang)*.060,.14+Math.sin(ang)*.060,.21,.014,.040,.012);ray.rotation.z=ang-Math.PI/2;}for(let s of [-1,1])ell(this.body,cloth,s*.255,.93,-.04,.14,.40,.20);box(this.body,mat('#f0ddbd'),0,1.4,.214,.21,.59,.012);for(let j=0;j<4;j++)ell(this.body,accent,.09,1.18+j*.1,.231,.015,.015,.01);const pen=box(this.head,gold,.26,.1,.13,.018,.23,.018);pen.rotation.z=-.16;box(this.body,mat('#594233'),-.27,1.14,.24,.18,.27,.055);}
 if(lead===2){const stripe=box(this.body,white,0,1.43,.223,.10,.61,.013);stripe.rotation.z=-.65;ell(this.body,black,0,1.76,0,.20,.11,.20);const towel=box(this.body,mat('#9eacba'),-.28,1.51,.24,.14,.49,.07);tube(this.body,[new T.Vector3(.15,1.75,.21),new T.Vector3(.12,1.34,.25),new T.Vector3(.25,1.18,.24)],.01,black);const scope=bone(this.body,gold,.035);connect(scope,new T.Vector3(.25,1.20,.24),new T.Vector3(.25,1.04,.24));}
 if(lead===3){const whale=mat('#3266b1',.65);ell(this.head,whale,0,.15,-.105,.365,.35,.29);ell(this.head,white,0,-.055,.009,.31,.29,.26);this.head.add(face);face.position.z=.065; // face forward of hood
 for(let s of [-1,1]){const fin=ell(this.head,whale,s*.365,.04,-.02,.14,.035,.08);fin.rotation.z=s*.30;ell(this.head,black,s*.17,.36,.08,.018,.018,.012);}ell(this.head,gold,0,.40,.135,.080,.080,.035);ell(this.head,white,0,.40,.170,.055,.055,.012);}
 if(lead===4){for(let s of [-1,1]){ell(this.head,hair,s*.27,.14,-.04,.12,.12,.11);torus(this.head,accent,s*.27,.14,.051,.085,.017);}for(let y=1.15;y<1.65;y+=.12)torus(this.body,cloth,0,y,0,.30,.043).rotation.x=Math.PI/2;for(let y=1.18;y<1.65;y+=.13)ell(this.body,mat('#a46c72'),0,y,.24,.025,.027,.01);}
 if(lead===5){const peach=mat('#e6b8a6',.58);for(let j=0;j<5;j++)tube(this.head,[new T.Vector3(.08+j*.04,.30,.0),new T.Vector3(.23+j*.014,.1,.19),new T.Vector3(.29+j*.016,-.38,.02)],.044,peach);for(let s of [-1,1])ell(this.body,s<0?cloth:peach,s*.24,1.05,-.06,.17,.40,.19);for(let j=0;j<8;j++)ell(this.body,gold,Math.sin(j*3)*.27,1+j*.09,.24,.009,.015,.008);const star=new T.Shape();for(let j=0;j<8;j++){const a=j*Math.PI/4,rad=j%2?.055:.13;const x=Math.sin(a)*rad,y=Math.cos(a)*rad;j?star.lineTo(x,y):star.moveTo(x,y);}const st=new T.Mesh(new T.ExtrudeGeometry(star,{depth:.045,bevelEnabled:true,bevelSegments:2,steps:1,bevelSize:.01,bevelThickness:.01}),gold);st.position.set(.29,1.15,.23);this.body.add(st);}
 // Ensemble details intentionally differ from leads.
 if(index===6){torus(this.head,white,0,.12,.02,.281,.025).rotation.x=Math.PI/2;}
 if(index===7){const sc=mat('#dce3f1');tube(this.body,[new T.Vector3(-.15,1.8,.22),new T.Vector3(.24,1.7,.20),new T.Vector3(.40,1.5,.02),new T.Vector3(.85,1.35,-.1)],.06,sc);}
 if(index===9)ell(this.head,gold,0,.34,0,.25,.08,.16);
 if(index===10)for(let s of [-1,1])torus(this.head,accent,s*.10,.01,.277,.085,.011);
 if(index===13)for(let s of [-1,1])ell(this.head,white,s*.21,.36,-.06,.05,.18,.05);
 if(index===15){const robe=ell(this.body,mat('#314b6c'),0,1.0,-.05,.38,.57,.28);}
 // Four two-bone chains. Rounded cuff and ankle forms hide all joints.
 for(const side of [-1,1]){
  const shoe=ell(this.root,white,side*.16,.075,.08,.14,.085,.23);const sole=ell(this.root,white,side*.16,.028,.08,.145,.025,.235);const trim=ell(this.root,accent,side*.16,.11,.18,.085,.014,.03);
  const upper=bone(this.root,pants,.12),lower=bone(this.root,pants,.095),knee=ell(this.root,pants,0,0,0,.118,.12,.118);
  this.legs.push({side,upper,lower,knee,shoe,sole,trim});
  const ua=bone(this.root,cloth,.12),la=bone(this.root,cloth,.10),el=ell(this.root,cloth,0,0,0,.115,.115,.115),handGroup=new T.Group();this.root.add(handGroup);ell(handGroup,skin,0,0,0,.065,.08,.045);for(let j=0;j<4;j++)ell(handGroup,skin,(j-1.5)*.023,-.066,.003,.014,.05,.018);ell(handGroup,skin,side*.06,-.01,.012,.028,.042,.028);this.arms.push({side,upper:ua,lower:la,elbow:el,hand:handGroup});
 }
 const scl=this.h/2.55;this.root.scale.setScalar(scl);this.pose(neutral());
 }
 pose(p:Pose,shadow=true){const c=p.crouch*2,j=p.jump*2.55;this.body.position.y=-c+j;this.body.rotation.z=p.lean*.5;this.head.rotation.z=-p.lean*.3;this.head.rotation.y=p.turn*.5;
 for(const l of this.legs){const lift=Math.max(0,-l.side*p.step)*2.6;const hip=new T.Vector3(l.side*.17,1.04-c+j,0);const ankle=new T.Vector3(l.side*(.16+Math.abs(p.step)*.15),.15+lift+j,.025);const knee=solve(hip,ankle,.48,.47,new T.Vector3(0,0,1));connect(l.upper,hip,knee);connect(l.lower,knee,ankle);l.knee.position.copy(knee);l.shoe.position.set(ankle.x,.077+lift+j,.09);l.sole.position.set(ankle.x,.028+lift+j,.09);l.trim.position.set(ankle.x,.117+lift+j,.18);}
 for(const a of this.arms){const shoulder=new T.Vector3(a.side*.31,1.65-c+j,0);const wrist=new T.Vector3(a.side*lerp(.48,.55,p.raise),lerp(1.13,2.23,p.raise)-c+j,.06);wrist.lerp(new T.Vector3(a.side*.09,1.49-c+j,.35),p.hand);const elbow=solve(shoulder,wrist,.34,.32,new T.Vector3(a.side*.8,0,.3));connect(a.upper,shoulder,elbow);connect(a.lower,elbow,wrist);a.elbow.position.copy(elbow);a.hand.position.copy(wrist);a.hand.rotation.z=-a.side*p.raise*.4;}
 this.root.rotation.y=p.turn;
 }
}
