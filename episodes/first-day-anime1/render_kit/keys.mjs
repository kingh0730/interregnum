import fs from 'node:fs';import path from 'node:path';import {openPage,renderFrame} from './lib.mjs';
for(const key of ['S25front','S25back']){const c=await openPage({scale:1,key});try{const png=await renderFrame(c.page,720,1);fs.writeFileSync(path.resolve(import.meta.dirname,`../assets/plates/${key}-composite.png`),png);}finally{await c.close();}}
