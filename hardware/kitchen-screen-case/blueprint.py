import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
scr_w,scr_h,scr_t=235,142,8; fit=.4; wall=2.4; lip=2.0; bez=4; back_t=2.6; rear=34; foot=4; pocket=17
ow=scr_w+2*(fit+wall); oh=scr_h+2*(fit+wall); zs=back_t+rear; zf=zs+scr_t+lip+.6
BG='#0b1730'; LN='#5ce1ff'; AC='#ffd166'; TX='#e8f6ff'; GR='#7be0a0'; OR='#ff9f5c'; PK='#ff7a9c'
fig=plt.figure(figsize=(18,11),facecolor=BG)
def dh(ax,x0,x1,y,t): ax.annotate('',xy=(x0,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text((x0+x1)/2,y+3,t,color=AC,ha='center',fontsize=10)
def dv(ax,x,y0,y1,t): ax.annotate('',xy=(x,y0),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text(x+3,(y0+y1)/2,t,color=AC,va='center',fontsize=10,rotation=90)
def setup(ax,t,xl,yl): ax.set_facecolor(BG); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis('off'); ax.set_title(t,color=TX,fontsize=13,loc='left')
def box(ax): ax.add_patch(FancyBboxPatch((-ow/2,-oh/2),ow,oh,boxstyle='round,pad=0,rounding_size=5',fc='#10223e',ec=LN,lw=2))
ax=fig.add_axes([0.02,0.53,0.58,0.39]); setup(ax,'FRONT VIEW: thin and symmetric',(-150,150),(-95,95)); box(ax)
ax.add_patch(Rectangle((-(scr_w-2*bez)/2,-(scr_h-2*bez)/2),scr_w-2*bez,scr_h-2*bez,fc='#06101f',ec=LN,lw=1,ls='--'))
ax.text(0,0,'SCREEN 235 x 142 x 8',color=TX,ha='center',fontsize=11); dh(ax,-ow/2,ow/2,-oh/2-9,f'{ow:.1f} mm'); dv(ax,ow/2+8,-oh/2,oh/2,f'{oh:.1f} mm'); ax.text(0,oh/2+6,'only 2.4 mm walls; 4 mm lip',color=AC,ha='center',fontsize=9)
ax=fig.add_axes([0.02,0.05,0.58,0.44]); setup(ax,'BACK VIEW (wall side): everything is open space behind the screen',(-150,150),(-95,95)); box(ax)
mx=lambda x:-x
xe=mx(-(scr_w/2+fit))
ax.add_patch(Rectangle((xe,-45),pocket+wall,100,fc='#16305a',ec=GR,ls='--')); ax.text(xe+9,-52,'port pocket\n17 mm',color=GR,fontsize=8,ha='center')
for n,d in {'switch':25,'audio':53,'USB-C touch+power':72,'HDMI-IN':106}.items(): y=scr_h/2-d; ax.add_patch(Rectangle((xe-3,y-4),6,8,fc=GR,ec=GR)); ax.text(xe-6,y,n,color=GR,fontsize=8,va='center',ha='right')
ax.add_patch(Rectangle((-37.5,-35),82,54,fc='none',ec=AC,ls=':')); ax.text(3,-8,'screen driver board\n(avoid: bumps)',color=AC,fontsize=8,ha='center')
ax.add_patch(Rectangle((52,-40),62,92,fc='#16305a',ec=PK,lw=2,ls='--')); ax.text(83,6,'Pi kit case\n(tape here, portrait,\nclose to the ports;\nfit to be tested)',color=TX,ha='center',fontsize=8)
for i in range(7): x=mx(-105+i*9); ax.plot([x-2,x+2],[oh/2-1,oh/2-5],color=LN,lw=2.5); ax.plot([x-2,x+2],[-oh/2+1,-oh/2+5],color=LN,lw=2.5)
ax.text(mx(-78),oh/2+4,'warm air out (top slots)',color=LN,fontsize=8,ha='center'); ax.text(mx(-78),-oh/2-7,'cool air in (bottom slots)',color=LN,fontsize=8,ha='center')
for c in (scr_w/2-54,scr_w/2-175): ax.add_patch(Rectangle((mx(c)-13,oh/2-wall),26,wall,fc=AC)); ax.text(mx(c),oh/2-wall-5,'speaker slot',color=AC,fontsize=8,ha='center')
for i in range(-3,4): ax.add_patch(Rectangle((mx(-83+i*8)-1.5,-36),3,84,fc=LN,alpha=.35))
ax.text(83,60,'fan grille in the plate',color=LN,fontsize=8,ha='center')
for sx in(-1,1): ax.add_patch(Circle((sx*75,60),4.5,fc=BG,ec=LN)); ax.text(sx*75,66,'keyhole',color=TX,ha='center',fontsize=8)
ax=fig.add_axes([0.62,0.40,0.36,0.52]); setup(ax,'SIDE SECTION',(-14,66),(-95,95))
ax.add_patch(Rectangle((0,-oh/2),zf,oh,fc='#10223e',ec=LN,lw=2)); 
ax.add_patch(Rectangle((zs,-scr_h/2),scr_t,scr_h,fc='#1d3b66',ec=AC)); ax.text(zs+scr_t/2,0,'screen',color=TX,rotation=90,va='center',ha='center',fontsize=9)
ax.add_patch(Rectangle((back_t,-oh/2+wall),zs-back_t,oh-2*wall,fc=BG,ec='none')); ax.add_patch(Rectangle((back_t+1,-40),31,92,fc='#16305a',ec=PK,ls='--')); ax.text(back_t+16,56,'Pi kit case 31 mm',color=TX,ha='center',fontsize=8)
ax.add_patch(Rectangle((-foot,-oh/2+16),foot,14,fc=LN))
dh(ax,0,zf,-oh/2-6,f'{zf:.1f} mm'); dh(ax,-foot,zf,-oh/2-22,f'{zf+foot:.1f} mm from the wall'); ax.text(zf-4,-oh/2-36,'FRONT',color=TX,fontsize=9); ax.text(-12,-oh/2-36,'WALL',color=TX,fontsize=9)
fig.text(0.625,0.33,'CHANGES (v4)\n- No cable bay: symmetric, 2.4 mm walls on all four sides\n- Only a thin pocket on the back of the left wall (17 mm) for the\n  plugs; you cannot see it from the front\n- Pi stays in its kit case, taped on, not part of the model\n- Cables: 90-degree HDMI adapter and the right-angle USB-C both exit\n  toward the back, then run flat behind the screen to the Pi\n- Case is 31 mm Pi + 8 mm screen + plate = 47 mm thick\n  (a bare Pi would save about 9 mm)\n\nTO TEST WITH THE REAL PARTS\n- Pi case position vs the screen driver board and the plugs\n- hole positions, bezel width, plug length',color=TX,fontsize=9,va='top',family='monospace')
fig.text(0.02,0.995,'KITCHEN SCREEN CASE v4  |  thin frame  |  GeekPi 10.1 + Pi 5 kit case  |  ASA black  |  mm',color=AC,fontsize=14,weight='bold',va='top')
fig.savefig('blueprint.png',dpi=105,facecolor=BG); print(ow,oh,zf)
