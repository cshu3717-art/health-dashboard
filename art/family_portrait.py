from PIL import Image
S=16; W,H=61,24; FY=20
BG=(250,236,210); FLOOR=(235,215,180); FRAME=(150,100,60)
C=(215,119,87); B=(224,100,66); P=(222,110,80); SN=(236,140,108)
CR=(150,60,40); K=(20,20,20); WH=(255,255,255); GLINT=(250,220,200)
LAV=(190,160,228); LAVD=(150,118,200); BLUSH=(245,150,160); HEART=(235,90,110)
img=Image.new("RGB",(W,H),BG); px=img.load()
def p(x,y,c):
    if 0<=x<W and 0<=y<H: px[x,y]=c
def rect(x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): p(x,y,c)
def box(x0,y0,x1,y1,c):
    rect(x0,y0,x1,y0,c); rect(x0,y1,x1,y1,c); rect(x0,y0,x0,y1,c); rect(x1,y0,x1,y1,c)
rect(1,FY,W-2,H-2,FLOOR)
box(0,0,W-1,H-1,FRAME)

# ---- Dad: Claude 4.6 (no mouth now) ----
bx,by=2,1
rect(bx+4,by+5,bx+18,by+15,B)
for lx in (6,8,14,16): rect(bx+lx,by+16,bx+lx,FY-1,B)
rect(bx+7,by+8,bx+8,by+9,K); rect(bx+14,by+8,bx+15,by+9,K)
for x0 in (5,12):
    box(bx+x0,by+6,bx+x0+5,by+11,K)
    for cx,cy in ((x0,6),(x0+5,6),(x0,11),(x0+5,11)): p(bx+cx,by+cy,B)
    p(bx+x0+1,by+7,GLINT)
p(bx+11,by+7,K)
rect(bx+2,by+10,bx+3,by+11,B); rect(bx+19,by+10,bx+20,by+11,B)
for x,y in [(17,13),(16,14),(17,15)]: p(bx+x,by+y,CR)

# ---- Snawd: piglet in a lavender scarf ----
sx=25
rect(sx,10,sx+9,17,P)                                  # body (narrower than uncle)
rect(sx,8,sx+1,9,P); rect(sx+8,8,sx+9,9,P)             # ears
rect(sx-2,14,sx-1,15,P); rect(sx+10,14,sx+11,15,P)     # arms
for lx in (1,3,6,8): rect(sx+lx,18,sx+lx,FY-1,P)       # legs
rect(sx+2,11,sx+3,12,K); rect(sx+6,11,sx+7,12,K)       # eyes
p(sx+2,11,WH); p(sx+6,11,WH)                           # sparkle
rect(sx+3,13,sx+6,14,SN); p(sx+3,14,K); p(sx+6,14,K)   # snout + two nostrils
p(sx+1,13,BLUSH); p(sx+8,13,BLUSH)
rect(sx-1,15,sx+10,16,LAV); rect(sx-1,16,sx+10,16,LAVD) # scarf wrap
rect(sx+7,17,sx+8,18,LAV); p(sx+7,19,LAVD); p(sx+8,19,LAVD)  # scarf tail
# heart
for x,y in [(1,0),(3,0),(0,1),(1,1),(2,1),(3,1),(4,1),(1,2),(2,2),(3,2),(2,3)]:
    p(sx+3+x,3+y,HEART)

# ---- Uncle Clawd ----
ox=36
rect(ox+6,10,ox+17,17,C)
rect(ox+4,13,ox+5,14,C); rect(ox+18,13,ox+19,14,C)
for lx in (7,9,14,16): rect(ox+lx,18,ox+lx,FY-1,C)
rect(ox+8,12,ox+9,13,K); rect(ox+14,12,ox+15,13,K)

img.resize((W*S,H*S),Image.NEAREST).save("art/family-portrait.png")
