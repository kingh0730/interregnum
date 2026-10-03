// The final ink point bends the actual paper texture, then catches a very small gold light.
// Pure frame-time SDF/lens pass integrated in the borrowed HDR compositor.
import * as T from 'three';
import {FSPass} from './vendor/pdoom/gl';
export class InkLens extends FSPass{
 constructor(){super(`
 uniform sampler2D src;uniform float strength,time;
 float sdInk(vec3 p){float n=snoise(p*21.0)*0.045;return length(p)-0.42-n;}
 void main(){
  vec2 centre=vec2(.5,1.-710./1440.);vec2 d=(vUv-centre)*vec2(16./9.,1.);float r=length(d);
  float mask=1.-smoothstep(.06,.22,r);vec2 uv=vUv-(vUv-centre)*strength*.0018/(dot(d,d)+.002)*mask;
  vec3 col=texture(src,uv).rgb;
  // A short signed-distance march gives the dot's gold interior a dimensional edge.
  if(r<.028){vec3 ro=vec3(d/.042,1.5),rd=vec3(0.,0.,-1.);float travel=0.;
   for(int i=0;i<24;i++){vec3 p=ro+rd*travel;float dist=sdInk(p);if(dist<.002||travel>3.)break;travel+=dist*.72;}
   vec3 p=ro+rd*travel;if(travel<3.){vec2 e=vec2(.004,0);vec3 n=normalize(vec3(sdInk(p+e.xyy)-sdInk(p-e.xyy),sdInk(p+e.yxy)-sdInk(p-e.yxy),sdInk(p+e.yyx)-sdInk(p-e.yyx)));float lit=pow(max(0.,dot(n,normalize(vec3(-.5,.8,1.)))),7.);col+=vec3(.24,.125,.025)*lit*strength;}}
  fragColor=vec4(col,1.);
 }`,{src:{value:null},strength:{value:0},time:{value:0}});}
}
