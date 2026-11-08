import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
scr_w,scr_h,scr_t=235,142,8; fit=0.5; wall=5.5; back_t=3.2; rear=6; lip=2.4; bez=4; bay=30
pod_w,pod_h,pod_d=104,72,24; pod_y=-14; kx=150; ky=52; hin=7
ow=scr_w+2*(fit+wall)+bay; oh=scr_h+2*(fit+wall); fd=lip+scr_t+0.6; bd=back_t+rear; tot=fd+bd+pod_d
sx0=bay/2; pod_x=-ow/2+8+pod_w/2
BG='#0b1730'; LN='#5ce1ff'; AC='#ffd166'; TX='#e8f6ff'; GR='#7be0a0'
ports={'switch':25,'audio':53,'USB-C touch+power':72,'HDMI':106}
fig=plt.figure(figsize=(17,11),facecolor=BG)
def dim_h(ax,x0,x1,y,t,c=AC): ax.annotate('',xy=(x0,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',color=c,lw=1.2)); ax.text((x0+x1)/2,y+3,t,color=c,ha='center',fontsize=10)
def dim_v(ax,x,y0,y1,t): ax.annotate('',xy=(x,y0),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text(x+3,(y0+y1)/2,t,color=AC,va='center',fontsize=10,rotation=90)
def setup(ax,title,xl,yl): ax.set_facecolor(BG); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis('off'); ax.set_title(title,color=TX,fontsize=13,loc='left')
def case(ax,m=1):
    ax.add_patch(FancyBboxPatch((-ow/2,-oh/2),ow,oh,boxstyle='round,pad=0,rounding_size=6',fc='#10223e',ec=LN,lw=2))
X=lambda x,m: m*x
# FRONT
ax=fig.add_axes([0.03,0.50,0.64,0.42]); setup(ax,'FRONT VIEW',(-160,160),(-95,95)); case(ax)
ax.add_patch(Rectangle((sx0-(scr_w-2*bez)/2,-(scr_h-2*bez)/2),scr_w-2*bez,scr_h-2*bez,fc='#06101f',ec=LN,lw=1,ls='--'))
for i in range(5): ax.add_patch(Rectangle((-ow/2+wall+6+i*4.6,-26),2.2,52,fc=BG,ec=LN,lw=0.8))
ax.text(sx0,0,'SCREEN 235 x 142 x 8',color=TX,ha='center',fontsize=11); ax.text(-ow/2+wall+bay/2-2,-40,'cable bay\n(ports behind)',color=GR,ha='center',fontsize=8)
dim_h(ax,-ow/2,ow/2,-oh/2-9,f'{ow:.0f} mm'); dim_v(ax,ow/2+8,-oh/2,oh/2,f'{oh:.0f} mm')
for i,(x,y) in enumerate([(sx0+sx*(scr_w/2-hin),sy*(scr_h/2-hin)) for sx in(-1,1) for sy in(-1,1)]): ax.add_patch(Circle((x,y),1.6,fc=AC,ec=AC))
ax.text(sx0+(scr_w/2-hin)+2,scr_h/2-hin+6,'M2.5 screen screws (4)',color=AC,fontsize=8,ha='right')
# BACK (mirrored: how it looks from the wall side)
ax=fig.add_axes([0.03,0.03,0.64,0.42]); setup(ax,'BACK VIEW (looking at the wall side)',(-160,160),(-95,95)); case(ax)
mx=lambda x:-x
ax.add_patch(FancyBboxPatch((mx(pod_x)-pod_w/2,pod_y-pod_h/2),pod_w,pod_h,boxstyle='round,pad=0,rounding_size=5',fc='#16305a',ec=AC,lw=2))
ax.text(mx(pod_x),pod_y,'Pi 5 + cooler\nUSB side toward the screen\nair in at bottom, out at top',color=TX,ha='center',va='center',fontsize=10)
for i in range(-4,5):
    x=mx(pod_x)+i*9; ax.plot([x-2,x+2],[pod_y+pod_h/2+4,pod_y+pod_h/2-4],color=LN,lw=2); ax.plot([x-2,x+2],[pod_y-pod_h/2+4,pod_y-pod_h/2-4],color=LN,lw=2)
for sx in(-1,1): ax.add_patch(Circle((sx*kx/2,ky),4.5,fc=BG,ec=LN)); ax.text(sx*kx/2,ky+8,'wall keyhole',color=TX,ha='center',fontsize=8)
for x,y in [(mx(sx0+sx*(scr_w/2-hin)),sy*(scr_h/2-hin)) for sx in(-1,1) for sy in(-1,1)]: ax.add_patch(Circle((x,y),1.6,fc=AC,ec=AC))
# screen edge ports (they are on the bay side, which is the right side in this view)
xe=mx(sx0-scr_w/2)
for n,d in ports.items():
    y=scr_h/2-d; ax.add_patch(Rectangle((xe-2,y-4),4,8,fc=GR,ec=GR)); ax.text(xe+6,y,n,color=GR,fontsize=8,va='center')
for c in (sx0+(scr_w/2-54), sx0+(scr_w/2-175)):
    ax.add_patch(Rectangle((mx(c)-13,oh/2-wall),26,wall,fc=LN)); 
ax.text(mx(sx0+(scr_w/2-54)),oh/2-wall-5,'speaker sound slot',color=LN,fontsize=8,ha='center')
ax.text(mx(pod_x)+pod_w/2-62,pod_y-pod_h/2-9,'power cord exits here',color=AC,fontsize=9)
dim_h(ax,mx(pod_x)-pod_w/2,mx(pod_x)+pod_w/2,pod_y+pod_h/2+16,f'pod {pod_w}'); 
# SIDE
ax=fig.add_axes([0.69,0.40,0.29,0.50]); setup(ax,'SIDE SECTION',(-10,70),(-95,95))
ax.add_patch(Rectangle((0,-oh/2),fd,oh,fc='#10223e',ec=LN,lw=2)); ax.add_patch(Rectangle((lip,-scr_h/2),scr_t,scr_h,fc='#1d3b66',ec=AC)); ax.text(lip+scr_t/2,0,'screen',color=TX,rotation=90,va='center',ha='center',fontsize=9)
ax.add_patch(Rectangle((fd,-oh/2),bd,oh,fc='#0e1a35',ec=LN,lw=2)); ax.add_patch(Rectangle((fd+bd,pod_y-pod_h/2),pod_d,pod_h,fc='#16305a',ec=AC,lw=2)); ax.text(fd+bd+pod_d/2,pod_y,'Pi pod',color=TX,rotation=90,va='center',ha='center',fontsize=9)
dim_h(ax,0,fd+bd,-oh/2-6,f'{fd+bd:.1f} mm'); dim_h(ax,0,tot,-oh/2-22,f'{tot:.1f} mm at the pod'); ax.text(-8,-oh/2-36,'FRONT',color=TX,fontsize=9); ax.text(tot-14,-oh/2-36,'WALL',color=TX,fontsize=9)
fig.text(0.685,0.34,'CABLES (all short):\n1 USB-A to USB-C, 1 ft: Pi to the screen port\n   "Touch & Power" (one cable does both)\n2 Micro-HDMI to HDMI (Alvin\'s): Pi to HDMI-IN\n3 Pi power cord: out the bottom notch\nThe 2nd SUNGUY cable is a spare.\n\nFROM THE MAKER\'S DIAGRAM\n235 x 142 x 8 mm, ports on one short edge\nM2.5 mounting points near the corners\n(positions are estimates: check with a\nruler, then tell me)\n\nBUILD\nBlack ASA, 0.2 mm, 4 walls\nM2.5 x 12 screws x4 hold the screen\nM3 x 10 screws x4 join the two parts',color=TX,fontsize=9.5,va='top',family='monospace')
fig.text(0.03,0.995,'KITCHEN SCREEN CASE v2  |  GeekPi 10.1 + Raspberry Pi 5  |  ASA, black  |  mm',color=AC,fontsize=14,weight='bold',va='top')
fig.savefig('blueprint.png',dpi=110,facecolor=BG); print(ow,oh,fd+bd,tot)
