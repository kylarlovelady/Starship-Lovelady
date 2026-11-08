import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
scr_w,scr_h,scr_t=235,142,8; fit=0.5; wall=5.5; back_t=2.4; rear=6; lip=2.4; bez=4
pod_w,pod_h,pod_d=104,72,24; pod_y=-14; kx=150; ky=52
ow=scr_w+2*(fit+wall); oh=scr_h+2*(fit+wall); fd=lip+scr_t+0.6; bd=back_t+rear
tot=fd+bd+pod_d
BG='#0b1730'; LN='#5ce1ff'; AC='#ffd166'; TX='#e8f6ff'
fig=plt.figure(figsize=(16,11),facecolor=BG)
def dim_h(ax,x0,x1,y,txt):
    ax.annotate('',xy=(x0,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text((x0+x1)/2,y+3,txt,color=AC,ha='center',fontsize=10)
def dim_v(ax,x,y0,y1,txt):
    ax.annotate('',xy=(x,y0),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text(x+3,(y0+y1)/2,txt,color=AC,va='center',fontsize=10,rotation=90)
def setup(ax,title,xl,yl):
    ax.set_facecolor(BG); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis('off'); ax.set_title(title,color=TX,fontsize=13,loc='left')
# FRONT
ax=fig.add_axes([0.03,0.50,0.62,0.42]); setup(ax,'FRONT VIEW (what you see on the wall)',(-140,140),(-95,95))
ax.add_patch(FancyBboxPatch((-ow/2,-oh/2),ow,oh,boxstyle='round,pad=0,rounding_size=6',fc='#10223e',ec=LN,lw=2))
ax.add_patch(Rectangle((-(scr_w-2*bez)/2,-(scr_h-2*bez)/2),scr_w-2*bez,scr_h-2*bez,fc='#06101f',ec=LN,lw=1,ls='--'))
ax.text(0,0,'SCREEN (1024x600 touch)\nactive pixels must not be covered',color=TX,ha='center',va='center',fontsize=11)
dim_h(ax,-ow/2,ow/2,-oh/2-9,f'{ow:.0f} mm outside'); dim_v(ax,ow/2+8,-oh/2,oh/2,f'{oh:.0f} mm outside')
dim_h(ax,-(scr_w-2*bez)/2,(scr_w-2*bez)/2,oh/2+7,f'window {scr_w-2*bez:.0f} mm')
# BACK
ax=fig.add_axes([0.03,0.03,0.62,0.42]); setup(ax,'BACK VIEW (wall side): Pi pod, vents, wall keyholes',(-140,140),(-95,95))
ax.add_patch(FancyBboxPatch((-ow/2,-oh/2),ow,oh,boxstyle='round,pad=0,rounding_size=6',fc='#10223e',ec=LN,lw=2))
ax.add_patch(FancyBboxPatch((-pod_w/2,pod_y-pod_h/2),pod_w,pod_h,boxstyle='round,pad=0,rounding_size=5',fc='#16305a',ec=AC,lw=2))
for sx in (-1,1):
    ax.add_patch(Circle((sx*kx/2,ky),4.5,fc=BG,ec=LN)); ax.plot([sx*kx/2,sx*kx/2],[ky,ky-9],color=LN)
    ax.text(sx*kx/2,ky+8,'wall keyhole',color=TX,ha='center',fontsize=8)
import numpy as np
for i in range(-4,5):
    x=i*9
    ax.plot([x-1.3-3.5,x+1.3+3.5],[pod_y+pod_h/2-2,pod_y+pod_h/2-2],color=LN,lw=3) if False else None
    ax.plot([x-2,x+2],[pod_y+pod_h/2+4,pod_y+pod_h/2-4],color=LN,lw=2); ax.plot([x-2,x+2],[pod_y-pod_h/2+4,pod_y-pod_h/2-4],color=LN,lw=2)
ax.text(0,pod_y,'Pi 5 + cooler\n(bare board, board bottom to wall)\nvents: air in at bottom, out at top',color=TX,ha='center',va='center',fontsize=10)
ax.text(-pod_w/2+5,pod_y-pod_h/2-8,'power cord exits here',color=AC,ha='center',fontsize=9)
for p in [(-1,-.5),(-1,.5),(1,-.5),(1,.5)]:
    ax.add_patch(Circle((p[0]*(ow/2-wall/2),p[1]*oh/2),1.5,fc=AC,ec=AC))
ax.text(ow/2-6,0,'4x M3',color=AC,fontsize=8,rotation=90,va='center')
dim_h(ax,-pod_w/2+25,pod_w/2,pod_y-pod_h/2-16,f'pod {pod_w} mm'); dim_v(ax,pod_w/2+8,pod_y-pod_h/2,pod_y+pod_h/2,f'pod {pod_h} mm')
# SIDE SECTION
ax=fig.add_axes([0.67,0.36,0.31,0.54]); setup(ax,'SIDE SECTION (thickness)',(-10,75),(-95,95))
z0=0
ax.add_patch(Rectangle((0,-oh/2),fd,oh,fc='#10223e',ec=LN,lw=2)); ax.text(fd/2-3,oh/2+12,'frame',color=TX,ha='center',fontsize=9)
ax.add_patch(Rectangle((lip,-scr_h/2),scr_t,scr_h,fc='#1d3b66',ec=AC,lw=1)); ax.text(lip+scr_t/2,0,'screen',color=TX,rotation=90,ha='center',va='center',fontsize=9)
ax.add_patch(Rectangle((fd,-oh/2),bd,oh,fc='#0e1a35',ec=LN,lw=2)); ax.text(fd+bd/2+9,oh/2+4,'back',color=TX,ha='center',fontsize=9)
ax.add_patch(Rectangle((fd+bd,pod_y-pod_h/2),pod_d,pod_h,fc='#16305a',ec=AC,lw=2)); ax.text(fd+bd+pod_d/2,pod_y,'Pi pod',color=TX,rotation=90,ha='center',va='center',fontsize=9)
ax.text(-8,-oh/2-38,'FRONT',color=TX,fontsize=9); ax.text(fd+bd+pod_d-8,-oh/2-38,'WALL',color=TX,fontsize=9)
dim_h(ax,0,fd+bd,-oh/2-6,f'{fd+bd:.1f} mm main body'); dim_h(ax,0,tot,-oh/2-24,f'{tot:.1f} mm total at the pod')
# NOTES
fig.text(0.665,0.30,'ASSUMED (measure and tell me):\n- screen outline 235 x 142 x 8 mm\n- mounting-hole positions on the back of the screen\n- where the HDMI, touch and power ports sit on the screen edge\n- bezel width: how far the lip may overlap\n\nBUILD NOTES\n- Black ASA, 0.2 mm layers, 4 walls\n- Frame prints face-down, Back prints pod-up\n- 4 M3 screws through the back rim into the frame walls\n- Two wall screws in the keyholes (use anchors)\n- Vents: bottom in, top out (chimney). Pod must not touch\n  insulation. Do not block the vent edge with furniture.',color=TX,fontsize=10,va='top',family='monospace')
fig.text(0.03,0.995,'KITCHEN SCREEN CASE  |  GeekPi 10.1 + Raspberry Pi 5   |   ASA, black   |   units mm',color=AC,fontsize=14,weight='bold',va='top')
fig.savefig('blueprint.png',dpi=110,facecolor=BG)
print(ow,oh,fd+bd,tot)
