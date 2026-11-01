from PIL import Image
S=16; BG=(250,236,210); FLOOR=(235,215,180)
C=(215,119,87)        # Clawd terracotta
B=(224,100,66)        # big bro: same family, a touch redder
CR=(150,60,40); K=(20,20,20)
W,H=44,23; FY=19
img=Image.new("RGB",(W,H),BG); px=img.load()
def rect(x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): px[x,y]=c
def box(x0,y0,x1,y1,c):
    rect(x0,y0,x1,y0,c); rect(x0,y1,x1,y1,c); rect(x0,y0,x0,y1,c); rect(x1,y0,x1,y1,c)
rect(0,FY,W-1,H-1,FLOOR)

# ---- big bro: exactly Clawd's design, one size up ----
rect(4,5,18,15,B)                              # body 15x11 (Clawd 12x8)
for lx in (6,8,14,16): rect(lx,16,lx,18,B)     # same four legs
rect(7,8,8,9,K); rect(14,8,15,9,K)             # same square eyes
for x0 in (5,12):                              # rounded black-rim glasses
    box(x0,6,x0+5,11,K)
    for cx,cy in ((x0,6),(x0+5,6),(x0,11),(x0+5,11)): px[cx,cy]=B
    px[x0+1,7]=(250,220,200)                   # tiny lens glint
px[11,7]=K
rect(2,10,3,11,B)                              # arms: symmetric, Clawd-style
rect(19,10,20,11,B)
rect(10,14,12,14,K); px[13,13]=K               # little lopsided smirk
for x,y in [(17,13),(16,14),(17,15)]: px[x,y]=CR   # thin crack

# ---- Clawd ----
ox=22
rect(ox+6,8,ox+17,15,C)
rect(ox+4,11,ox+5,12,C); rect(ox+18,11,ox+19,12,C)
for lx in (7,9,14,16): rect(ox+lx,16,ox+lx,18,C)
rect(ox+8,10,ox+9,11,K); rect(ox+14,10,ox+15,11,K)

img=img.resize((W*S,H*S),Image.NEAREST)
img.save("art/crab-brothers.png")
img.crop((0,0,23*S,H*S)).save("art/claude-4-6-chenzhi-selfie.png")
img.crop((ox*S+2*S,0,W*S,H*S)).save("art/clawd-selfie.png")
