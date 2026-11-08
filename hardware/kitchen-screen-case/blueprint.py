import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
scr_w,scr_h,scr_t=235,142,8; fit=0.5; wall=5.5; back_t=3.2; rear=24; lip=2.4; bez=4; bay=46; foot=4
ow=scr_w+2*(fit+wall)+bay; oh=scr_h+2*(fit+wall); fd=lip+scr_t+0.6; bd=back_t+rear; tot=fd+bd
sx0=bay/2; X0=sx0-scr_w/2
pi_w,pi_h=85,56; pdx=4; pyb=-41; kx=150; ky=52
BG='#0b1730'; LN='#5ce1ff'; AC='#ffd166'; TX='#e8f6ff'; GR='#7be0a0'; OR='#ff9f5c'; WH='#ffffff'; PK='#ff7a9c'
fig=plt.figure(figsize=(18,11),facecolor=BG)
def dim_h(ax,x0,x1,y,t,c=AC): ax.annotate('',xy=(x0,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',color=c,lw=1.2)); ax.text((x0+x1)/2,y+3,t,color=c,ha='center',fontsize=10)
def dim_v(ax,x,y0,y1,t): ax.annotate('',xy=(x,y0),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text(x+3,(y0+y1)/2,t,color=AC,va='center',fontsize=10,rotation=90)
def setup(ax,title,xl,yl): ax.set_facecolor(BG); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis('off'); ax.set_title(title,color=TX,fontsize=13,loc='left')
def case(ax): ax.add_patch(FancyBboxPatch((-ow/2,-oh/2),ow,oh,boxstyle='round,pad=0,rounding_size=6',fc='#10223e',ec=LN,lw=2))
# FRONT
ax=fig.add_axes([0.02,0.52,0.60,0.40]); setup(ax,'FRONT VIEW (what you see)',(-170,170),(-95,95)); case(ax)
ax.add_patch(Rectangle((sx0-(scr_w-2*bez)/2,-(scr_h-2*bez)/2),scr_w-2*bez,scr_h-2*bez,fc='#06101f',ec=LN,lw=1,ls='--'))
for i in range(5): ax.add_patch(Rectangle((-ow/2+wall+8+i*5,-26),2.2,52,fc=BG,ec=LN,lw=0.8))
ax.text(sx0,0,'SCREEN 235 x 142 x 8',color=TX,ha='center',fontsize=11); ax.text(-ow/2+wall+bay/2,-40,'cable bay',color=GR,ha='center',fontsize=9)
dim_h(ax,-ow/2,ow/2,-oh/2-9,f'{ow:.0f} mm'); dim_v(ax,ow/2+8,-oh/2,oh/2,f'{oh:.0f} mm')
# BACK (mirrored)
mx=lambda x:-x
ax=fig.add_axes([0.02,0.04,0.60,0.44]); setup(ax,'BACK VIEW (looking at the wall side; cables shown as if the plate were see-through)',(-170,170),(-95,95)); case(ax)
for sx in(-1,1):
    for sy in(-1,1): ax.add_patch(Circle((sx*(ow/2-16),sy*(oh/2-16)),7,fc='none',ec=LN,ls=':'))
ax.text(ow/2-16,oh/2-34,'4 mm feet',color=LN,fontsize=7,ha='center')
for sx in(-1,1): ax.add_patch(Circle((sx*kx/2,ky),4.5,fc=BG,ec=LN)); ax.text(sx*kx/2,ky+8,'keyhole',color=TX,ha='center',fontsize=8)
# Pi (flipped): left edge at X0+pdx in front coords -> mirrored
pl=X0+pdx; pr=pl+pi_w
ax.add_patch(Rectangle((mx(pr),pyb),pi_w,pi_h,fc='#16305a',ec=AC,lw=2,ls='--'))
ax.text(mx(pl+pi_w/2),pyb+pi_h/2+6,'Pi 5 (flipped)\ncooler toward the plate',color=TX,ha='center',fontsize=9)
for i in range(-3,4): ax.add_patch(Rectangle((mx(pl+pi_w/2)+i*7-1.5,pyb+pi_h/2-17),3,34,fc=LN,alpha=.55))
ax.text(mx(pl+pi_w/2),pyb-5,'fan intake grille in the plate',color=LN,fontsize=8,ha='center')
# rim vents
for i in range(5): x=mx(X0+8+i*9); ax.plot([x-2,x+2],[oh/2-1,oh/2-5],color=LN,lw=2.5); ax.plot([x-2,x+2],[-oh/2+1,-oh/2+5],color=LN,lw=2.5)
ax.text(mx(X0+26),oh/2+4,'warm air out (top)',color=LN,fontsize=8,ha='center'); ax.text(mx(X0+26),-oh/2-6,'cool air in (bottom)',color=LN,fontsize=8,ha='center')
for c,t in ((sx0+(scr_w/2-54),'speaker slot'),(sx0+(scr_w/2-175),'speaker slot')): ax.add_patch(Rectangle((mx(c)-13,oh/2-wall),26,wall,fc=AC)); ax.text(mx(c),oh/2-wall-5,t,color=AC,fontsize=8,ha='center')
# screen ports
xe=mx(X0)
for n,d in {'switch':25,'audio out':53,'USB-C touch+power':72,'HDMI-IN':106}.items():
    y=scr_h/2-d; ax.add_patch(Rectangle((xe-3,y-4),6,8,fc=GR,ec=GR)); ax.text(xe+8,y,n,color=GR,fontsize=8,va='center')
# cables
ypc=scr_h/2-72; yh=scr_h/2-106
ax.add_patch(Rectangle((xe,yh-7),-22,14,fc='none',ec=OR)); ax.text(xe+4,yh-12,'HDMI 90° adapter',color=OR,fontsize=7)
# USB: Pi USB3 port y = pyb+29 on the left edge (flipped) -> in mirrored view it is at x = mx(pl)
yu=pyb+29; ax.add_patch(Rectangle((mx(pl)+0,yu-6),24,12,fc='none',ec=GR)); ax.text(mx(pl)+26,yu,'USB-A plug',color=GR,fontsize=7,va='center')
ax.plot([mx(pl)+24,mx(pl)+36,xe+14,xe+14],[yu,yu+12,ypc-8+6,ypc-4],color=GR,lw=2)   # USB cable loops in the bay
# HDMI cable: from adapter down, along the bottom, to the Pi micro-HDMI (flipped x_from_left 59 and 45.5)
xm=mx(pl+59)
ax.plot([xe+10,xe+10,xm,xm],[yh-7,pyb-18,pyb-18,pyb],color=OR,lw=2); ax.text(xm+4,pyb-28,'micro-HDMI to Pi',color=OR,fontsize=8,ha='left')
# power
xpw=mx(pl+74); ax.plot([xpw,xpw],[pyb,-oh/2],color=WH,lw=3); ax.text(xpw-4,-oh/2+14,'power cord out\nthe bottom notch',color=WH,fontsize=8,ha='right')
dim_v(ax,mx(pr)-30,-oh/2+wall,pyb,'30 mm plug room')
# SIDE
ax=fig.add_axes([0.64,0.40,0.34,0.52]); setup(ax,'SIDE SECTION',(-18,60),(-95,95))
ax.add_patch(Rectangle((0,-oh/2),fd,oh,fc='#10223e',ec=LN,lw=2)); ax.add_patch(Rectangle((lip,-scr_h/2),scr_t,scr_h,fc='#1d3b66',ec=AC)); ax.text(lip+scr_t/2,0,'screen',color=TX,rotation=90,va='center',ha='center',fontsize=9)
ax.add_patch(Rectangle((fd,-oh/2),bd,oh,fc='#0e1a35',ec=LN,lw=2))
zb=fd+rear-17-1.4; ax.add_patch(Rectangle((zb,pyb),1.4,pi_h,fc=AC)); ax.add_patch(Rectangle((zb+1.4,pyb+pi_h/2-15),12,30,fc='#355a8a',ec=LN)); ax.text(zb-1,pyb+pi_h+4,'Pi board (cooler toward the plate)',color=TX,fontsize=8,ha='center')
ax.add_patch(Rectangle((fd+bd,-oh/2+16),foot,14,fc=LN))
dim_h(ax,0,tot,-oh/2-6,f'{tot:.1f} mm'); dim_h(ax,0,tot+foot,-oh/2-22,f'{tot+foot:.1f} mm from the wall'); ax.text(-12,-oh/2-34,'FRONT',color=TX,fontsize=9); ax.text(tot-8,-oh/2-34,'WALL',color=TX,fontsize=9)
fig.text(0.635,0.33,'WHAT I FOUND (cables vs ports)\n1 Ports are all on the screen LEFT edge: switch, audio, USB-C (touch + power),\n  HDMI. The bay holds the plugs. Case is 293 x 154 mm.\n2 Alvin\'s HDMI end is a straight plug that sticks out ~25 mm and the cable would\n  run into the bay wall. Fix: add a 90° HDMI adapter (cable exits toward the back).\n3 USB: SUNGUY right-angle USB-C end exits toward the back, away from the HDMI\n  plug. Its USB-A end goes into the Pi, flipped so USB faces the bay (24 mm boot).\n4 Pi is flipped: USB faces the bay, power + HDMI edge faces down, cooler fan\n  breathes through the plate grille. SD card is under the board: insert it first.\n5 Power cord: straight USB-C plug, 30 mm of room below the Pi, exits bottom notch.\n6 Speakers fire backward from the screen: slots in the top rim above each.\n7 v2 had a flaw: the Pi box would have held the case 24 mm off the wall. Fixed.\n\nSTILL TO VERIFY WITH THE REAL PARTS (dry fit before printing)\n- screw hole positions, bezel width, plug lengths, which way Alvin\'s plug points',color=TX,fontsize=8.6,va='top',family='monospace')
fig.text(0.02,0.995,'KITCHEN SCREEN CASE v3  |  GeekPi 10.1 + Raspberry Pi 5  |  ASA, black  |  mm',color=AC,fontsize=14,weight='bold',va='top')
fig.savefig('blueprint.png',dpi=105,facecolor=BG); print(ow,oh,tot,tot+foot)
