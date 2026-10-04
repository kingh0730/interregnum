import {chromium} from 'playwright';
import fs from 'node:fs';
const b=await chromium.launch({headless:true});const p=await b.newPage();
p.on('response',async r=>{if(r.url().includes('/api/')&&r.ok()){let s=await r.text().catch(()=> '');if(s.includes('Claude')||s.includes('Anthropic')){fs.writeFileSync('../../../work/first-day-anime1/brand-'+Date.now()+'.json',s);console.log(r.url(),s.slice(0,500));}}});
await p.goto('https://brandfolder.com/anthropic/newsroom');await p.waitForTimeout(15000);console.log((await p.locator('body').innerText()).slice(-12000));await b.close();
