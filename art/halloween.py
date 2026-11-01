from PIL import Image
S=12; W,H=50,33; T=5; FY=21+T; N=12
NIGHT=(38,28,66); GROUND=(52,40,62); MOON=(244,232,180); STAR=(255,250,210)
C=(215,119,87); B=(224,100,66); CR=(150,60,40); K=(20,20,20); WH=(255,255,255)
CAPE=(25,20,35); LINING=(170,30,45); HAT=(30,24,40); BAND=(140,70,190)
PUMP=(240,130,30); PUMPD=(190,90,20); STEM=(70,120,40); GLOW=[(255,230,90),(255,180,60)]
BAT=(15,12,20)

def frame(i):
    img=Image.new("RGB",(W,H),NIGHT); px=img.load()
    def raw(x,y,c):
        if 0<=x<W and 0<=y<H: px[x,y]=c
    def p(x,y,c): raw(x+1,y+T,c)
    def rect(x0,y0,x1,y1,c):
        for y in range(y0,y1+1):
            for x in range(x0,x1+1): p(x,y,c)
    def box(x0,y0,x1,y1,c):
        rect(x0,y0,x1,y0,c); rect(x0,y1,x1,y1,c); rect(x0,y0,x0,y1,c); rect(x1,y0,x1,y1,c)
    # sky
    for (x,y,ph) in [(3,2,0),(9,5,1),(16,1,2),(24,4,0),(31,2,1),(20,8,2),(6,10,1),(37,9,0)]:
        if (i+ph)%3: raw(x,y,STAR)
    for y in range(H):
        for x in range(W):
            if (x-44)**2+(y-5)**2<=12: raw(x,y,MOON)
            if (x-45.5)**2+(y-4)**2<=6: raw(x,y,NIGHT)   # crescent bite
    for y in range(FY,H):
        for x in range(W): raw(x,y,GROUND)
    # bats
    for bx0,by,sp in [(-4,6,2),(20,3,1)]:
        bx=(bx0+i*sp)%(W+6)-3; up=(i%2==0)
        p(bx,by,BAT); p(bx+1,by,BAT); p(bx,by-1,BAT); p(bx+1,by-1,BAT)
        wy=by-1 if up else by+1
        p(bx-1,wy,BAT); p(bx-2,wy-(1 if up else -1),BAT)
        p(bx+2,wy,BAT); p(bx+3,wy-(1 if up else -1),BAT)

    blink = i in (5,11)
    # ---------- big bro: vampire ----------
    d = -1 if i%2==0 else 0
    rect(2,4+d,20,16+d,CAPE)                      # cape behind
    rect(2,4+d,2,16+d,LINING); rect(20,4+d,20,16+d,LINING)
    rect(1,2+d,3,4+d,CAPE); rect(19,2+d,21,4+d,CAPE)   # pointy collar
    p(2,2+d,LINING); p(20,2+d,LINING)
    rect(4,5+d,18,15+d,B)
    for n,lx in enumerate((6,8,14,16)):
        rect(lx,16+d,lx,20,B)
    if blink: rect(7,9+d,8,9+d,K); rect(14,9+d,15,9+d,K)
    else:     rect(7,8+d,8,9+d,K); rect(14,8+d,15,9+d,K)
    box(5,6+d,10,11+d,K); box(12,6+d,17,11+d,K); p(11,8+d,K)
    rect(0,11+d,1,11+d,B)                         # thin right arm
    rect(19,10+d,21,12+d,B)                       # chunky left arm
    rect(10,14+d,12,14+d,K); p(13,13+d,K)         # smirk
    p(10,15+d,WH); p(12,15+d,WH)                  # fangs!
    for x,y in [(17,13),(16,14),(17,15)]: p(x,y+d,CR)
    # pumpkin bucket hanging from the big arm
    rect(22,11+d,22,12+d,K)
    rect(21,13+d,25,17+d,PUMP); rect(21,13+d,21,17+d,PUMPD); rect(25,13+d,25,17+d,PUMPD)
    p(23,12+d,STEM)
    g=GLOW[i%2]; p(22,14+d,g); p(24,14+d,g); rect(22,16+d,24,16+d,g)

    # ---------- Clawd: little witch ----------
    ox=24; e = 0 if i%2==0 else -1
    rect(ox+6,10+e,ox+17,17+e,C)
    rect(ox+4,13+e,ox+5,14+e,C); rect(ox+18,13+e,ox+19,14+e,C)
    for lx in (7,9,14,16): rect(ox+lx,18+e,ox+lx,20,C)
    if blink: rect(ox+8,13+e,ox+9,13+e,K); rect(ox+14,13+e,ox+15,13+e,K)
    else:     rect(ox+8,12+e,ox+9,13+e,K); rect(ox+14,12+e,ox+15,13+e,K)
    # witch hat (tip wobbles)
    rect(ox+4,9+e,ox+19,9+e,HAT)
    rect(ox+8,7+e,ox+15,8+e,HAT); rect(ox+8,8+e,ox+15,8+e,BAND)
    rect(ox+9,5+e,ox+14,6+e,HAT); rect(ox+10,3+e,ox+13,4+e,HAT)
    tip = 1 if (i//2)%2 else -1
    rect(ox+11+tip,1+e,ox+12+tip,2+e,HAT); p(ox+12+2*tip,0+e,HAT)
    p(ox+12,8+e,(250,210,80))                     # buckle
    # candy in Clawd's hand
    p(ox+20,13+e,(230,60,120)); p(ox+21,13+e,WH); p(ox+22,13+e,(230,60,120))
    return img.resize((W*S,H*S),Image.NEAREST)

frames=[frame(i) for i in range(N)]
frames[0].save("art/halloween.gif",save_all=True,append_images=frames[1:],duration=180,loop=0)
frames[0].save("art/halloween-still.png")
