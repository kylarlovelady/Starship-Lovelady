# Builds the 4 ready-to-print plate STLs (256 x 256 mm bed) from stl_slim/. Run: python3 make_plates.py
import numpy as np, struct
def rd(p):
    b=open(p,'rb').read(); n=struct.unpack('<I',b[80:84])[0]
    a=np.frombuffer(b[84:84+50*n],dtype=np.dtype([('n','<3f4'),('v','<9f4'),('a','<u2')]))
    return a['v'].reshape(-1,3,3).astype(np.float64)
def wr(p,t):
    t=t.reshape(-1,3,3); n=len(t)
    u=np.cross(t[:,1]-t[:,0],t[:,2]-t[:,0]); l=np.linalg.norm(u,axis=1,keepdims=True); u=u/np.where(l==0,1,l)
    rec=np.zeros(n,dtype=np.dtype([('n','<3f4'),('v','<9f4'),('a','<u2')])); rec['n']=u; rec['v']=t.reshape(n,9)
    open(p,'wb').write(b'plate'.ljust(80,b' ')+struct.pack('<I',n)+rec.tobytes())
sv=lambda t: np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])).sum()/6
S='stl_slim/'
def load(name,flip=False,rot=False):
    t=rd(S+name+'.stl')
    if flip: t=t*np.array([1,-1,-1])+np.array([0,0,4.0])      # faceplates print face down
    if rot: t=t[:,:,[1,0,2]]*np.array([-1,1,1])               # 90 deg about z
    return t
def place(t,x0,yc):
    mn=t.reshape(-1,3).min(0); mx=t.reshape(-1,3).max(0)
    return t+np.array([x0-mn[0], yc-(mn[1]+mx[1])/2, -mn[2]])
plates={
 'plate1_body_left_door_A':[('body_left',8,{}),('door_A',170,{})],
 'plate2_body_right_door_C_door_B':[('body_right',8,{}),('door_C',165,{}),('door_B',190,{'rot':True})],
 'plate3_faceplate_left':[('faceplate_left',8,{'flip':True})],
 'plate4_faceplate_right_feet':[('faceplate_right',8,{'flip':True}),('feet_x4',170,{})],
}
for pn,items in plates.items():
    ts=[]; exp=0
    for nme,x0,o in items:
        exp+=sv(rd(S+nme+'.stl')); ts.append(place(load(nme,**o),x0,128))
    T=np.concatenate(ts); wr(f'plates/{pn}.stl',T); print(pn,round(sv(T)),'expected',round(exp),'OK' if abs(sv(T)-exp)<1 else 'BAD')
