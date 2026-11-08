// Builds viewer.html (self-contained interactive 3D page) from the generated parts.
import fs from 'fs';
import {buildAll,DOORS,P,ox,oy,zS,zTop,hx,hy} from './case.mjs';
const parts=buildAll(); const data={parts:{},doors:{},meta:{ox,oy,zS,zTop,hx,hy,P:{W:P.W,H:P.H,T:P.T}}};
const names=['body_left','body_right','faceplate_left','faceplate_right','door_A','door_B','door_C'];
const key={door_A:'A',door_B:'B',door_C:'C'};
for(const n of names){ const t=parts[n].cleanTris(); const a=new Int16Array(t.length*9); let i=0; for(const tri of t) for(const v of tri){ a[i++]=Math.round(v[0]*100); a[i++]=Math.round(v[1]*100); a[i++]=Math.round(v[2]*100); }
  data.parts[n]={n:t.length,b64:Buffer.from(a.buffer).toString('base64')}; }
for(const k of 'ABC'){ const d=DOORS[k]; data.doors['door_'+k]={pivot:[d.ax+d.n[0]*P.axisOff, d.ay+d.n[1]*P.axisOff],n:d.n}; }
const tpl=fs.readFileSync('viewer.template.html','utf8');
fs.writeFileSync('viewer.html',tpl.replace('__DATA__',JSON.stringify(data)));
console.log('viewer.html',(fs.statSync('viewer.html').size/1e6).toFixed(2),'MB');
