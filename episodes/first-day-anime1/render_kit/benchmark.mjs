import {openPage,renderFrame} from './lib.mjs';
const angle=process.argv[2]||'swiftshader';const frame=+(process.argv[3]||952);const c=await openPage({scale:1,angle});try{let start=Date.now();let b=await renderFrame(c.page,frame);console.log(JSON.stringify({angle,frame,seconds:(Date.now()-start)/1000,png_bytes:b.length}));}finally{await c.close();}
