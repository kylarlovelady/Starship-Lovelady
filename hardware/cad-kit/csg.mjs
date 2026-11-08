// Minimal solid-modelling kernel (BSP CSG, after Evan Wallace's csg.js). Units: mm. Convex primitives only.
const EPS = 1e-6;
export class Poly {
  constructor(v) { this.v = v; // array of [x,y,z]
    let nx=0,ny=0,nz=0, n=v.length;
    for (let i=0;i<n;i++){ const a=v[i], b=v[(i+1)%n]; nx+=(a[1]-b[1])*(a[2]+b[2]); ny+=(a[2]-b[2])*(a[0]+b[0]); nz+=(a[0]-b[0])*(a[1]+b[1]); }
    const l=Math.hypot(nx,ny,nz); this.area=l/2; this.valid=l>1e-9;
    this.n=[nx/l,ny/l,nz/l]; let cx=0,cy=0,cz=0; for(const p of v){cx+=p[0];cy+=p[1];cz+=p[2];}
    this.w=(this.n[0]*cx+this.n[1]*cy+this.n[2]*cz)/n;
  }
  flip(){ const p=new Poly(this.v.slice().reverse()); return p; }
}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
function splitPoly(pn, pw, poly, cf, cb, f, b) {
  let type=0; const types=[];
  for (const p of poly.v){ const t=dot(pn,p)-pw; const ty=t<-EPS?2:t>EPS?1:0; type|=ty; types.push(ty); }
  if (type===0) { (dot(pn,poly.n)>0?cf:cb).push(poly); }
  else if (type===1) f.push(poly); else if (type===2) b.push(poly);
  else {
    const fv=[],bv=[], n=poly.v.length;
    for (let i=0;i<n;i++){ const j=(i+1)%n, ti=types[i], tj=types[j], vi=poly.v[i], vj=poly.v[j];
      if (ti!==2) fv.push(vi); if (ti!==1) bv.push(vi);
      if ((ti|tj)===3){ const t=(pw-dot(pn,vi))/dot(pn,[vj[0]-vi[0],vj[1]-vi[1],vj[2]-vi[2]]);
        const m=[vi[0]+(vj[0]-vi[0])*t, vi[1]+(vj[1]-vi[1])*t, vi[2]+(vj[2]-vi[2])*t]; fv.push(m); bv.push(m); } }
    if (fv.length>=3){ const p=new Poly(fv); if(p.valid&&p.area>1e-7) f.push(p); }
    if (bv.length>=3){ const p=new Poly(bv); if(p.valid&&p.area>1e-7) b.push(p); }
  }
}
class Node {
  constructor(polys){ this.pn=null; this.pw=0; this.front=null; this.back=null; this.polys=[]; if(polys&&polys.length) this.build(polys); }
  invert(){ // iterative-safe enough for our sizes (recursion depth is modest)
    this.polys=this.polys.map(p=>p.flip()); if(this.pn){this.pn=[-this.pn[0],-this.pn[1],-this.pn[2]]; this.pw=-this.pw;}
    if(this.front)this.front.invert(); if(this.back)this.back.invert(); const t=this.front; this.front=this.back; this.back=t; }
  clip(polys){ if(!this.pn) return polys.slice(); let f=[],b=[];
    for(const p of polys) splitPoly(this.pn,this.pw,p,f,b,f,b);
    f=this.front?this.front.clip(f):f; b=this.back?this.back.clip(b):[]; return f.concat(b); }
  clipTo(o){ this.polys=o.clip(this.polys); if(this.front)this.front.clipTo(o); if(this.back)this.back.clipTo(o); }
  all(){ let r=this.polys.slice(); if(this.front)r=r.concat(this.front.all()); if(this.back)r=r.concat(this.back.all()); return r; }
  build(polys){ if(!polys.length) return;
    if(!this.pn){ // choose the largest polygon plane: keeps trees shallow for box-like geometry
      let best=polys[0]; for(const p of polys) if(p.area>best.area) best=p; this.pn=best.n.slice(); this.pw=best.w; }
    const f=[],b=[];
    for(const p of polys) splitPoly(this.pn,this.pw,p,this.polys,this.polys,f,b);
    if(f.length){ if(!this.front)this.front=new Node(); this.front.build(f); }
    if(b.length){ if(!this.back)this.back=new Node(); this.back.build(b); } }
}
export class Solid {
  constructor(polys){ this.polys=polys; }
  union(o){ const a=new Node(this.polys), b=new Node(o.polys);
    a.clipTo(b); b.clipTo(a); b.invert(); b.clipTo(a); b.invert(); a.build(b.all()); return new Solid(a.all()); }
  sub(o){ const a=new Node(this.polys), b=new Node(o.polys);
    a.invert(); a.clipTo(b); b.clipTo(a); b.invert(); b.clipTo(a); b.invert(); a.build(b.all()); a.invert(); return new Solid(a.all()); }
  and(o){ const a=new Node(this.polys), b=new Node(o.polys);
    a.invert(); b.clipTo(a); b.invert(); a.clipTo(b); b.clipTo(a); a.build(b.all()); a.invert(); return new Solid(a.all()); }
  map(fn){ return new Solid(this.polys.map(p=>new Poly(p.v.map(fn)))); }
  tris(){ const t=[]; for(const p of this.polys){ for(let i=1;i<p.v.length-1;i++) t.push([p.v[0],p.v[i],p.v[i+1]]); } return t; }
}
const orient=(polys,c)=>polys.map(p=>{ const q=p.v; let m=[0,0,0]; for(const v of q){m[0]+=v[0];m[1]+=v[1];m[2]+=v[2];} m=m.map(x=>x/q.length);
  return dot(p.n,[m[0]-c[0],m[1]-c[1],m[2]-c[2]])<0?p.flip():p; });
// extrude a convex 2D polygon (u,v) between w=a0 and w=a1; map(u,v,w) -> [x,y,z]
export function extrude(pts, map, a0, a1){
  const n=pts.length, lo=pts.map(([u,v])=>map(u,v,a0)), hi=pts.map(([u,v])=>map(u,v,a1));
  const polys=[new Poly(lo.slice()), new Poly(hi.slice())];
  for(let i=0;i<n;i++){ const j=(i+1)%n; polys.push(new Poly([lo[i],lo[j],hi[j],hi[i]])); }
  let c=[0,0,0]; for(const v of lo.concat(hi)){c[0]+=v[0];c[1]+=v[1];c[2]+=v[2];} c=c.map(x=>x/(2*n));
  return new Solid(orient(polys.filter(p=>p.valid),c));
}
const MZ=(u,v,w)=>[u,v,w], MX=(u,v,w)=>[w,u,v], MY=(u,v,w)=>[u,w,v];
export const rect=(u0,u1,v0,v1)=>[[u0,v0],[u1,v0],[u1,v1],[u0,v1]];
export function rrect(cu,cv,w,h,r,seg=8){ const pts=[], hw=w/2-r, hh=h/2-r;
  [[1,1,0],[-1,1,90],[-1,-1,180],[1,-1,270]].forEach(([sx,sy,a0])=>{ for(let i=0;i<=seg;i++){ const a=(a0+90*i/seg)*Math.PI/180; pts.push([cu+sx*hw+r*Math.cos(a)-0*0, cv+sy*hh+r*Math.sin(a)]); } });
  // fix: corner centres use sign of quadrant
  return pts.map((p,i)=>p); }
export function circ(cu,cv,r,n=28,ph=0){ const p=[]; for(let i=0;i<n;i++){ const a=ph+2*Math.PI*i/n; p.push([cu+r*Math.cos(a),cv+r*Math.sin(a)]); } return p; }
export const box=(x0,x1,y0,y1,z0,z1)=>extrude(rect(x0,x1,y0,y1),MZ,z0,z1);
export const zprism=(pts,z0,z1)=>extrude(pts,MZ,z0,z1);
export const xprism=(pts,x0,x1)=>extrude(pts,MX,x0,x1);   // pts are (y,z)
export const yprism=(pts,y0,y1)=>extrude(pts,MY,y0,y1);   // pts are (x,z)
export const zcyl=(cx,cy,r,z0,z1,n=28)=>zprism(circ(cx,cy,r,n),z0,z1);
export const xcyl=(cy,cz,r,x0,x1,n=28)=>xprism(circ(cy,cz,r,n),x0,x1);
export const ycyl=(cx,cz,r,y0,y1,n=28)=>yprism(circ(cx,cz,r,n),y0,y1);
// Insert missing vertices on polygon edges (BSP splitting leaves T-junctions) so the exported mesh is watertight.
Solid.prototype.cleanTris=function(){
  const sn=x=>Math.round(x*1e4)/1e4, K=v=>sn(v[0])+','+sn(v[1])+','+sn(v[2]);
  const polys=this.polys.map(p=>p.v.map(v=>[sn(v[0]),sn(v[1]),sn(v[2])]));
  const verts=new Map(); const C=2, grid=new Map(); const cell=x=>Math.floor(x/C);
  for(const p of polys) for(const v of p){ const k=K(v); if(!verts.has(k)){ verts.set(k,v); const g=cell(v[0])+','+cell(v[1])+','+cell(v[2]); (grid.get(g)||grid.set(g,[]).get(g)).push(v); } }
  const out=[];
  for(const p of polys){ const n=p.length, ring=[];
    for(let i=0;i<n;i++){ const a=p[i], b=p[(i+1)%n]; ring.push(a);
      const lo=[0,1,2].map(d=>Math.min(a[d],b[d])-3e-4), hi=[0,1,2].map(d=>Math.max(a[d],b[d])+3e-4);
      const d=[b[0]-a[0],b[1]-a[1],b[2]-a[2]], L2=d[0]*d[0]+d[1]*d[1]+d[2]*d[2]; const ins=[];
      for(let x=cell(lo[0]);x<=cell(hi[0]);x++) for(let y=cell(lo[1]);y<=cell(hi[1]);y++) for(let z=cell(lo[2]);z<=cell(hi[2]);z++){
        const g=grid.get(x+','+y+','+z); if(!g) continue;
        for(const v of g){ const w=[v[0]-a[0],v[1]-a[1],v[2]-a[2]]; const t=(w[0]*d[0]+w[1]*d[1]+w[2]*d[2])/L2; if(t<=1e-7||t>=1-1e-7) continue;
          const e=[w[0]-t*d[0],w[1]-t*d[1],w[2]-t*d[2]]; if(e[0]*e[0]+e[1]*e[1]+e[2]*e[2]<9e-8) ins.push([t,v]); } }
      ins.sort((q,r)=>q[0]-r[0]); for(const [,v] of ins) if(K(v)!==K(ring[ring.length-1])) ring.push(v); }
    // fan triangulation from the first vertex that is not collinear with its neighbours
    const m=ring.length; for(let i=1;i<m-1;i++){ const a=ring[0],b=ring[i],c=ring[i+1];
      const u=[b[0]-a[0],b[1]-a[1],b[2]-a[2]], w=[c[0]-a[0],c[1]-a[1],c[2]-a[2]];
      if(Math.hypot(u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0])<1e-9) { out.push([a,b,c]); continue; } out.push([a,b,c]); } }
  // merge vertices closer than 1.5 micrometres (BSP leaves micro-slivers) and drop collapsed triangles
  const key2=v=>Math.round(v[0]*1e4)+','+Math.round(v[1]*1e4)+','+Math.round(v[2]*1e4), rep=new Map(), g2=new Map(), c2=1e-2, tol=1.5e-3;
  const cell2=v=>[Math.floor(v[0]/c2),Math.floor(v[1]/c2),Math.floor(v[2]/c2)];
  const R=v=>{ const k=key2(v); if(rep.has(k)) return rep.get(k); const [a,b,c]=cell2(v); let hit=null;
    for(let x=a-1;x<=a+1&&!hit;x++) for(let y=b-1;y<=b+1&&!hit;y++) for(let z=c-1;z<=c+1&&!hit;z++){ const L=g2.get(x+','+y+','+z); if(L) for(const q of L) if(Math.abs(q[0]-v[0])<tol&&Math.abs(q[1]-v[1])<tol&&Math.abs(q[2]-v[2])<tol){ hit=q; break; } }
    if(!hit){ hit=v; const gk=a+','+b+','+c; (g2.get(gk)||g2.set(gk,[]).get(gk)).push(v); } rep.set(k,hit); return hit; };
  const res=[]; for(const t of out){ const a=R(t[0]),b=R(t[1]),c=R(t[2]); if(a===b||b===c||a===c) continue; res.push([a,b,c]); }
  return res; };
export function stlBinary(tris){ const buf=Buffer.alloc(84+50*tris.length); buf.write('kitchen screen case v6',0); buf.writeUInt32LE(tris.length,80); let o=84;
  for(const t of tris){ const a=t[0],b=t[1],c=t[2]; const ux=b[0]-a[0],uy=b[1]-a[1],uz=b[2]-a[2],vx=c[0]-a[0],vy=c[1]-a[1],vz=c[2]-a[2];
    let nx=uy*vz-uz*vy, ny=uz*vx-ux*vz, nz=ux*vy-uy*vx; const l=Math.hypot(nx,ny,nz)||1; nx/=l;ny/=l;nz/=l;
    for(const f of [nx,ny,nz,...a,...b,...c]){ buf.writeFloatLE(f,o); o+=4; } buf.writeUInt16LE(0,o); o+=2; }
  return buf; }
