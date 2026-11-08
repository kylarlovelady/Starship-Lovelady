// Fit and collision checks for v6 (every number is a volume in mm^3 that SHOULD be ~0).
import {buildBody,buildFace,doorSolid,DOORS,P,hx,hy,ox,oy,zS,zTop} from './case.mjs';
import {box} from './csg.mjs';
const body=buildBody(), face=buildFace().map((v)=>[v[0],v[1],v[2]+zTop]);
const vol=s=>{ let v=0; for(const [p,q,r] of s.tris()) v+=(p[0]*(q[1]*r[2]-q[2]*r[1])-p[1]*(q[0]*r[2]-q[2]*r[0])+p[2]*(q[0]*r[1]-q[1]*r[0]))/6; return v; };
const rows=[]; const chk=(name,a,b,note='')=>{ const v=Math.max(0,vol(a.and(b))); rows.push([name,v,note]); };
const doors={}; for(const k of 'ABC') doors[k]=doorSolid(DOORS[k]);
const W2=(d,u,v)=>[d.ax+d.t[0]*u+d.n[0]*v, d.ay+d.t[1]*u+d.n[1]*v];
const rot=(s,cx,cy,deg)=>{ const a=deg*Math.PI/180,c=Math.cos(a),sn=Math.sin(a); return s.map(p=>[cx+(p[0]-cx)*c-(p[1]-cy)*sn, cy+(p[0]-cx)*sn+(p[1]-cy)*c, p[2]]); };
for(const k of 'ABC'){ const d=DOORS[k]; const [cx,cy]=W2(d,0,P.axisOff);
  for(const deg of [0,5,15,30,60,90,110]) chk(`door ${k} open ${deg} deg vs case body`,rot(doors[k],cx,cy,deg),body, deg===0?'closed: only clearance gaps':'swinging out'); }
chk('screen (235x142x8) vs case body', box(-117.5,117.5,-71,71,zS,zS+P.T), body);
chk('screen vs faceplate', box(-117.5,117.5,-71,71,zS,zS+P.T), face);
chk('Pi kit case keep-out (64x95x31) vs body', box(-114,-50,-49,46,zS-31,zS), body, 'default spot, left strip');
for(const c of P.spk) chk(`speaker pad at x=${c} (30x17x12) vs body`, box(c-15,c+15,45,62,zS-12,zS), body);
chk('driver board bump (82x54x6) vs body', box(-43,39,-35,19,zS-6,zS), body);
chk('USB-C right-angle plug zone (x -135..-117.9, y -8..1) vs body', box(-135,-hx,-8,1,zS,zS+7), body);
chk('USB-C zone vs door A', box(-135,-hx,-8,1,zS,zS+7), doors.A);
chk('cable run up the wing (x -134..-119, y -8..50, z 8..30) vs body', box(-134,-119,-8,50,8,30), body);
for(const [k,v,n] of rows) console.log((v<0.5?'PASS ':'FAIL ')+k.padEnd(66)+' '+v.toFixed(1).padStart(10)+' mm3 '+(n||''));
// negative control: a door pushed 3 mm down into the wall must collide, proving the test can fail
{ const v=Math.max(0,vol(doors.A.map(p=>[p[0],p[1],p[2]-3]).and(body))); console.log((v>50?'PASS ':'FAIL ')+'control: door A pushed 3 mm down collides'.padEnd(66)+' '+v.toFixed(1).padStart(10)+' mm3'); }
