// Kitchen touch-screen case v6: generator. Run: node --stack-size=30000 case.mjs   (no installs needed)
// Front view coordinates: x right, y up, z toward the viewer. z=0 is the back face of the plate (wall side).
import {Solid,box,zcyl,zprism,xprism,yprism,rrect,rect,circ,extrude,stlBinary} from './csg.mjs';
import fs from 'fs';
export const P = {
  W:235, H:142, T:8, fit:0.4, wall:6, wing:18, backT:2.6, rear:34, plateT:4, bez:4, R:8,
  so_h:3,            // screen standoff height behind the screen (ESTIMATE: brass posts in the maker's photo)
  holeX:6, holeTop:7, holeBot:5,   // M2.5 mount holes from the screen edge (from the maker's diagram)
  zb:[15,24.8,25.1,34.9,35.2,45],  // hinge stack: body / door / body knuckles (3 x 9.8 mm + 0.3 gaps = 30 = M3x30 pin)
  barrelR:3.9, doorBarrelR:3.8, socketR:4.2, axisOff:0.9,
  spk:[-60,62],      // speaker centres, front view x (from the maker's diagram)
};
const {W,H,T,fit,wall,wing,backT,rear,plateT,bez,R,so_h}=P;
export const hx=W/2+fit, hy=H/2+fit, ox=hx+wing+wall, oy=hy+wall;
export const zS=backT+rear, zTop=zS+T+0.4;
const sel=(...a)=>a.reduce((s,x)=>s.union(x));
const subAll=(s,list)=>list.reduce((a,c)=>a.sub(c),s);

// ---- doors: local frame (u along the door from the hinge axis, v across, + = outward) ----
export const DOORS = {
  A:{ax:-(ox-wall/2), ay:-55, t:[0,1],  n:[-1,0], L:110, latch:[0,48],  name:'door_A_left'},
  C:{ax: (ox-wall/2), ay: 55, t:[0,-1], n:[1,0],  L:110, latch:[0,48],  name:'door_C_right'},
  B:{ax:-36, ay:-(oy-wall/2), t:[-1,0], n:[0,-1], L:76,  latch:[40,66], name:'door_B_bottom'},
};
const W2=(d,u,v)=>[d.ax+d.t[0]*u+d.n[0]*v, d.ay+d.t[1]*u+d.n[1]*v];
const polyUV=(d,pts)=>pts.map(([u,v])=>W2(d,u,v));
const zb=P.zb;
function doorCuts(d){ // things cut from the body
  const c=[];
  c.push(zprism(polyUV(d,rect(0,d.L+0.3,-wall/2-0.05,wall/2+0.05)),zb[0]-0.3,zTop+1));        // opening through the wall
  const [cx,cy]=W2(d,0,P.axisOff);
  c.push(zcyl(cx,cy,P.socketR,zb[1],zb[4],32));                                               // socket for the door knuckle
  return c;
}
function doorBodyAdds(d){ const [cx,cy]=W2(d,0,P.axisOff); return [zcyl(cx,cy,P.barrelR,zb[0],zb[1],32), zcyl(cx,cy,P.barrelR,zb[4],zb[5],32)]; }
function doorHoles(d){ const [cx,cy]=W2(d,0,P.axisOff); return [zcyl(cx,cy,2.7,zb[0]-1,zb[1]+0.1,24), zcyl(cx,cy,3.4,zb[4]-0.1,zb[5]+1,24)]; }
export function doorSolid(d, extras){
  const [cx,cy]=W2(d,0,P.axisOff), hv=wall/2-0.1;
  let s=zprism(polyUV(d,rect(4.4,d.L-0.2,-hv,hv)),zb[0],zb[5]-0.2);
  s=s.union(zprism(polyUV(d,rect(0,4.5,-hv,hv)),zb[2],zb[3]));
  s=s.union(zcyl(cx,cy,P.doorBarrelR,zb[2],zb[3],32));
  s=s.sub(zcyl(cx,cy,3.4,zb[2]-1,zb[3]+1,24));
  for(const lu of d.latch){ const [lx,ly]=W2(d,lu,0); s=s.sub(zcyl(lx,ly,1.1,zb[5]-0.2-9,zb[5]+1,14)); }
  return extras?extras(s,d):s;
}
const doorVents=(s,d)=>{ // vent slots through the door thickness (vertical slots)
  for(let i=0;i<6;i++){ const u=10+i*(d.L-20)/5; const p=polyUV(d,rect(u-1.4,u+1.4,-wall,wall)); s=s.sub(zprism(p,zb[0]+6,zb[5]-8)); } return s; };
const doorBcord=(s,d)=>{ s=doorVents(s,d); return s; };

// ---- faceplate screw layout (centre lines of the walls) ----
const topX=[-125,-75,-25,25,75,125], botX=[-125,-104,-74,25,75,125], sideY=[-66,0,48,66];
export const fpts=[ ...topX.map(x=>[x,oy-wall/2]), ...botX.map(x=>[x,-(oy-wall/2)]),
  ...sideY.map(y=>[-(ox-wall/2),y]), ...[-66,-48,0,66].map(y=>[(ox-wall/2),y]) ];

export function buildBody(log=()=>{}){
  let b=zprism(rrect(0,0,2*ox,2*oy,R,10),0,zTop);
  const cut=[];
  cut.push(zprism(rrect(0,0,2*hx,2*hy,2,6),backT,zTop+1));
  cut.push(box(-(ox-wall),-hx+1,-hy,hy,backT,zTop+1), box(hx-1,ox-wall,-hy,hy,backT,zTop+1));
  b=subAll(b,cut); log('cavities');
  // screen tabs with 45-degree gussets (support-free), seam columns
  const adds=[];
  const zt1=zS-so_h, zt0=zt1-3;
  for(const sx of [-1,1]) for(const sy of [-1,1]){
    const x0=sx>0?hx-16:-hx-4, x1=sx>0?hx+4:-hx+16; const y0=sy>0?hy-14:-hy-0.5, y1=sy>0?hy+0.5:-hy+14;
    adds.push(box(x0,x1,y0,y1,zt0,zt1));
    const yw=sy>0?hy:-hy, ys=sy>0?-14:14;  // wedge below the tab: triangle in (y,z)
    adds.push(xprism([[yw+sy*0.5,zt0],[yw+sy*0.5,zt0-14],[yw+ys,zt0]],x0,x1));
  }
  for(const sy of [-1,1]){ const y0=sy>0?hy-10:-hy-0.5, y1=sy>0?hy+0.5:-hy+10; adds.push(box(-10,10,y0,y1,backT-0.3,33.5)); }
  b=sel(b,...adds); log('tabs+columns');
  for(const k of ['A','B','C']){ b=sel(b,...doorBodyAdds(DOORS[k])); }
  const cuts2=[];
  for(const k of ['A','B','C']) cuts2.push(...doorCuts(DOORS[k]));
  b=subAll(b,cuts2); log('doors cut');
  // after the openings: add the barrels back (they were added before the cuts, so re-add) and cut pin holes
  for(const k of ['A','B','C']) b=sel(b,...doorBodyAdds(DOORS[k]));
  const holes=[];
  for(const k of ['A','B','C']) holes.push(...doorHoles(DOORS[k]));
  // tab screw holes (M2.5 clearance + head counterbore from the back)
  for(const sx of [-1,1]) for(const sy of [-1,1]){ const x=sx*(W/2-P.holeX), y=sy>0?H/2-P.holeTop:-(H/2-P.holeBot);
    holes.push(zcyl(x,y,1.4,zt0-1,zt1+1,18), zcyl(x,y,2.7,zt0-1,zt0+1.4,18)); }
  // seam bolts (M2.5 x 20): clearance in the left half, pilot in the right; heads counterbored on the left face
  for(const sy of [-1,1]) for(const z of [12,26]){ const y=sy*(hy-5); holes.push(extrude(circ(y,z,1.4,16),(u,v,w)=>[w,u,v],-11,10.5), extrude(circ(y,z,2.7,16),(u,v,w)=>[w,u,v],-11,-7.5)); }
  // fan grille in the plate, under the Pi
  for(let i=0;i<7;i++){ const x=-107+i*9; holes.push(box(x-1.5,x+1.5,-48,46,-1,backT+1)); }
  // keyholes
  for(const sx of [-1,1]){ const x=sx*75,y=58; holes.push(zcyl(x,y,4.5,-1,backT+1,24), box(x-2.5,x+2.5,y-9,y,-1,backT+1)); }
  // top exhaust louvers (slanted), speaker slots
  for(let i=0;i<5;i++){ const cx=-112+i*8.5, cy=oy-wall/2; const a=20*Math.PI/180, hl=(wall+4)/2, hw=1.3;
    const pts=[[-hw,-hl],[hw,-hl],[hw,hl],[-hw,hl]].map(([u,v])=>[cx+u*Math.cos(a)-v*Math.sin(a), cy+u*Math.sin(a)+v*Math.cos(a)]);
    holes.push(zprism(pts,10,30)); }
  for(const c of P.spk) holes.push(box(c-13,c+13,oy-wall-1,oy+1,zS-12,zS-1));
  // faceplate pilot holes in the wall tops and later the door latch holes are in the doors
  for(const [x,y] of fpts) holes.push(zcyl(x,y,1.1,zTop-10,zTop+1,14));
  b=subAll(b,holes); log('holes');
  return b;
}
export function buildFace(){
  const wx=W-2*bez, wy=H-2*bez;
  let f=zprism(rrect(0,0,2*ox,2*oy,R,10),0,plateT);
  f=f.sub(zprism(rrect(0,0,wx,wy,2,6),-1,plateT+1));
  // accent groove around the window
  const ring=zprism(rrect(0,0,wx+6,wy+6,3,8),plateT-0.6,plateT+1).sub(zprism(rrect(0,0,wx+4,wy+4,2.5,8),plateT-1,plateT+2));
  f=f.sub(ring);
  for(const [x,y] of fpts){ f=f.sub(zcyl(x,y,1.4,-1,plateT+1,14)).sub(zcyl(x,y,2.5,plateT-2.2,plateT+1,16)); }
  for(const k of ['A','B','C']){ const d=DOORS[k]; const [cx,cy]=W2(d,0,P.axisOff); f=f.sub(zcyl(cx,cy,3.3,-1,3.2,18)); }  // pockets for the M3 pin heads
  return f;
}
const half=(s,sign)=> s.and(box(sign<0?-400:0.1, sign<0?-0.1:400,-300,300,-50,100));
export function buildAll(log=()=>{}){
  const body=buildBody(log), face=buildFace();
  const out={};
  out.body_left=half(body,-1); out.body_right=half(body,1);
  out.faceplate_left=half(face,-1); out.faceplate_right=half(face,1);
  out.door_A=doorSolid(DOORS.A); out.door_C=doorSolid(DOORS.C,doorVents); out.door_B=doorSolid(DOORS.B,doorBcord);
  out.feet_x4=[[-1,-1],[1,-1],[-1,1],[1,1]].map(([i,j])=>zcyl(i*18,j*18,7,0,4,32)).reduce((a,c)=>a.union(c));
  return out;
}
const meshStats=(s)=>{ const t=s.tris(); let vol=0; let mn=[1e9,1e9,1e9],mx=[-1e9,-1e9,-1e9];
  for(const [p,q,r] of t){ vol+=(p[0]*(q[1]*r[2]-q[2]*r[1])-p[1]*(q[0]*r[2]-q[2]*r[0])+p[2]*(q[0]*r[1]-q[1]*r[0]))/6; for(const v of [p,q,r]) for(let i=0;i<3;i++){mn[i]=Math.min(mn[i],v[i]);mx[i]=Math.max(mx[i],v[i]);} }
  return {tris:t.length,volume:vol,min:mn,max:mx}; };
export {meshStats};
if (process.argv[1] && process.argv[1].endsWith('case.mjs')) {
  const t0=Date.now(); const log=m=>console.error(`[${((Date.now()-t0)/1000).toFixed(1)}s] ${m}`);
  const parts=buildAll(log); fs.mkdirSync('stl',{recursive:true}); const info={};
  for(const [k,s] of Object.entries(parts)){ const t=s.cleanTris(); fs.writeFileSync(`stl/${k}.stl`,stlBinary(t)); info[k]=meshStats(s); log(`${k}: ${t.length} tris`); }
  fs.writeFileSync('parts_info.json',JSON.stringify(info,null,1));
  fs.writeFileSync('_parts.mjs.json',JSON.stringify(Object.fromEntries(Object.entries(parts).map(([k,s])=>[k,s.cleanTris()]))));
}
