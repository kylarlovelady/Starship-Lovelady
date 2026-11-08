# Blueprint v6 for the kitchen screen case. Run: python3 blueprint.py  (needs matplotlib)
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
W,H,T=235,142,8; fit=.4; wall=6; wing=18; backT=2.6; rear=34; plateT=4; foot=4
hx=W/2+fit; hy=H/2+fit; ox=hx+wing+wall; oy=hy+wall; zS=backT+rear; zTop=zS+T+.4
BG='#0b1730'; LN='#5ce1ff'; AC='#ffd166'; TX='#e8f6ff'; GR='#7be0a0'; OR='#ff9f5c'; PK='#ff7a9c'
fig=plt.figure(figsize=(18,11.5),facecolor=BG)
def dh(ax,x0,x1,y,t): ax.annotate('',xy=(x0,y),xytext=(x1,y),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text((x0+x1)/2,y+2.5,t,color=AC,ha='center',fontsize=10)
def dv(ax,x,y0,y1,t): ax.annotate('',xy=(x,y0),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color=AC,lw=1.2)); ax.text(x+3,(y0+y1)/2,t,color=AC,va='center',fontsize=10,rotation=90)
def setup(ax,t,xl,yl): ax.set_facecolor(BG); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis('off'); ax.set_title(t,color=TX,fontsize=13,loc='left')
def outline(ax): ax.add_patch(FancyBboxPatch((-ox,-oy),2*ox,2*oy,boxstyle='round,pad=0,rounding_size=8',fc='#10223e',ec=LN,lw=2))
topX=[-125,-75,-25,25,75,125]; botX=[-125,-104,-74,25,75,125]
pts=[(x,oy-3) for x in topX]+[(x,-(oy-3)) for x in botX]+[(-(ox-3),y) for y in (-66,0,48,66)]+[((ox-3),y) for y in (-66,-48,0,66)]
# FRONT
ax=fig.add_axes([0.02,0.52,0.60,0.42]); setup(ax,'FRONT VIEW: faceplate screws on with 20 black M2.5 x 12 screws; side bays hold the ports',(-160,160),(-96,96)); outline(ax)
ax.add_patch(Rectangle((-113.5,-67),227,134,fc='#06101f',ec=LN,lw=1,ls='--'))
ax.add_patch(Rectangle((-W/2,-H/2),W,H,fc='none',ec=GR,lw=1,ls=':')); ax.text(0,0,'SCREEN 235 x 142 x 8\nwindow 227 x 134',color=TX,ha='center',va='center',fontsize=11)
for x,y in pts: ax.add_patch(Circle((x,y),2.5,fc='#222',ec=AC,lw=1))
ax.plot([-ox+.5,-ox+.5],[-55,55],color=OR,lw=5); ax.plot([ox-.5,ox-.5],[-55,55],color=OR,lw=5); ax.plot([-112,-36],[-oy+.5,-oy+.5],color=OR,lw=5)
ax.text(-ox-3,0,'DOOR A\n(ports)',color=OR,fontsize=9,ha='right',va='center'); ax.text(ox+3,0,'DOOR C\n(spare)',color=OR,fontsize=9,ha='left',va='center'); ax.text(-74,-oy-8,'DOOR B (Pi side)',color=OR,fontsize=9,ha='center')
dh(ax,-ox,ox,oy+9,f'{2*ox:.1f} mm'); dv(ax,ox+30,-oy,oy,f'{2*oy:.1f} mm')

# BACK (mirror x)
mx=lambda x:-x
ax=fig.add_axes([0.02,0.05,0.60,0.44]); setup(ax,'BACK VIEW (wall side, mirrored): plate, vents, keyholes, hinge pins',(-160,160),(-96,96)); outline(ax)
for i in range(7): x=mx(-107+i*9); ax.add_patch(Rectangle((x-1.5,-48),3,94,fc=LN,alpha=.45))
ax.text(mx(-80),52,'fan grille under the Pi',color=LN,fontsize=8,ha='center')
ax.add_patch(Rectangle((mx(-50),-49),64,95,fc='none',ec=PK,lw=2,ls='--')); ax.text(mx(-82),-3,'Pi kit case\n(taped to screen,\nposition to confirm)',color=TX,ha='center',fontsize=8)
for sx in(-1,1): ax.add_patch(Circle((sx*75,58),4.5,fc=BG,ec=LN)); ax.text(sx*75,48,'keyhole',color=TX,ha='center',fontsize=8)
for i in range(5): x=mx(-112+i*8.5); ax.plot([x-2.5,x+2.5],[oy+0.5,oy-5],color=LN,lw=2.5)
ax.text(mx(-90),oy+4,'exhaust louvers',color=LN,fontsize=8,ha='center')
for c in (-60,62): ax.add_patch(Rectangle((mx(c)-13,oy-wall),26,wall,fc=AC)); ax.text(mx(c),oy-wall-5,'speaker slot',color=AC,fontsize=8,ha='center')
for sx in(-1,1):
  for sy in(-1,1): ax.add_patch(Circle((sx*(ox-16),sy*(oy-16)),7,fc='none',ec=OR,ls='--'))
ax.text(0,-oy+10,'feet 4 mm (or rubber pads)',color=OR,fontsize=8,ha='center')
ax.add_patch(Rectangle((36,-oy),76,6,fc='none',ec=OR,lw=2)); ax.text(74,-oy-8,'door B: intake slots, M3 hinge pin',color=OR,fontsize=8,ha='center')
ax.add_patch(Rectangle((ox-6,-55),6,110,fc='none',ec=OR,lw=2)); ax.add_patch(Rectangle((-ox,-55),6,110,fc='none',ec=OR,lw=2))
for (x,y) in [(-(ox-3),-55),(ox-3,55),(-36,-(oy-3))]: ax.add_patch(Circle((mx(x),y),3.4,fc=AC,ec=AC)); 
ax.text(-30,0,'split line x = 0:\ntwo printed halves,\n4 x M2.5 x 20 bolts\ninside top and bottom walls',color=TX,fontsize=8,ha='center',alpha=.7)
# SIDE section
ax=fig.add_axes([0.64,0.40,0.34,0.54]); setup(ax,'SIDE SECTION (through the Pi strip)',(-14,66),(-96,96))
zf=zTop+plateT
ax.add_patch(Rectangle((0,-oy),zf,2*oy,fc='#10223e',ec=LN,lw=2)); ax.add_patch(Rectangle((backT,-oy+wall),zTop-backT,2*oy-2*wall,fc=BG,ec='none'))
ax.add_patch(Rectangle((zS,-H/2),T,H,fc='#1d3b66',ec=AC)); ax.text(zS+T/2,0,'screen',color=TX,rotation=90,va='center',ha='center',fontsize=9)
ax.add_patch(Rectangle((zS-31,-49),31,95,fc='#16305a',ec=PK,ls='--')); ax.text(zS-15,52,'Pi kit case 31',color=TX,ha='center',fontsize=8)
ax.add_patch(Rectangle((zTop,-oy),plateT,2*oy,fc='#10223e',ec=OR,lw=1.5)); ax.text(zTop+2,oy+3,'faceplate 4',color=OR,fontsize=8,ha='center')
ax.add_patch(Rectangle((-foot,-oy+8),foot,14,fc=LN)); 
dh(ax,0,zf,-oy-6,f'{zf:.0f} mm'); dh(ax,-foot,zf,-oy-20,f'{zf+foot:.0f} mm from the wall'); ax.text(-12,-oy-30,'WALL',color=TX,fontsize=9); ax.text(zf-8,-oy-30,'FRONT',color=TX,fontsize=9)
fig.text(0.645,0.33,'v6 CHANGES\n- Faceplate screws on (20 x M2.5 x 12), pocket for each hinge pin head\n- Doors A, C (side bays) and B (bottom): vertical hinges, your M3 x 30\n  as the pin, 3 knuckles (9.8 mm each), pin goes in from the front\n  under the faceplate; latch = 2 faceplate screws into the door edge\n- Screen held by 4 corner tabs behind it (M2.5, length at dry fit)\n- Split in two halves (each under 144 mm) so any printer can make it\n- Right bay mirrors the left; 36 mm wider than v5 but symmetric\n\nCHECKED (see viewer): doors swing clear, screen/Pi/speakers/plugs fit,\nall meshes watertight\n\nTO CONFIRM AT THE NOV 10 DRY FIT\n- screw hole positions and standoff height (3 mm assumed)\n- HDMI adapter + straight plug needs about 50 mm; bay gives 36 to 37\n  -> add a short flexible right-angle HDMI extension if it is tight\n- Pi kit case size and where it sits on the back',color=TX,fontsize=8.6,va='top',family='monospace')
fig.text(0.02,0.995,'KITCHEN SCREEN CASE v6  |  GeekPi 10.1 + Pi 5 kit case  |  black ASA  |  mm',color=AC,fontsize=14,weight='bold',va='top')
fig.savefig('blueprint.png',dpi=105,facecolor=BG); print('ok')
