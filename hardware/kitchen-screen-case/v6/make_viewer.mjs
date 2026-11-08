// Builds viewer.html (self-contained interactive 3D page) from the STL files of both variants.
import fs from 'fs';
import {DOORS,P,ox,oy,hx,hy} from './case.mjs';
const names=['body_left','body_right','faceplate_left','faceplate_right','door_A','door_B','door_C'];
const variants={standard:{dir:'stl',rear:34},slim:{dir:'stl_slim',rear:23}}; const data={variants:{}};
for(const [v,cfg] of Object.entries(variants)){
  const parts={}; for(const n of names){ const b=fs.readFileSync(`${cfg.dir}/${n}.stl`); const c=b.readUInt32LE(80); const a=new Int16Array(c*9); let o=84,i=0;
    for(let t=0;t<c;t++){ o+=12; for(let k=0;k<9;k++){ a[i++]=Math.round(b.readFloatLE(o)*100); o+=4; } o+=2; } parts[n]={n:c,b64:Buffer.from(a.buffer).toString('base64')}; }
  const zS=P.backT+cfg.rear, doors={}; for(const k of 'ABC'){ const d=DOORS[k]; doors['door_'+k]={pivot:[d.ax+d.n[0]*P.axisOff,d.ay+d.n[1]*P.axisOff],n:d.n}; }
  data.variants[v]={parts,doors,meta:{ox,oy,hx,hy,zS,zTop:zS+P.T+0.4,backT:P.backT,P:{W:P.W,H:P.H,T:P.T}}};
}
fs.writeFileSync('viewer.html',fs.readFileSync('viewer.template.html','utf8').replace('__DATA__',JSON.stringify(data)));
console.log('viewer.html',(fs.statSync('viewer.html').size/1e6).toFixed(2),'MB');
