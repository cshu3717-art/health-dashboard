from PIL import Image
S=16; BG=(250,236,210); FLOOR=(235,215,180)
C=(215,119,87)            # Clawd terracotta
B=(226,96,62)             # big bro: a bit more orange-red
CR=(140,50,30)            # crack
K=(20,20,20); LENS=(170,210,235); WH=(255,255,255); MR=(120,25,20)
W,H=62,23; FY=19
img=Image.new("RGB",(W,H),BG); px=img.load()
def rect(x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): px[x,y]=c
def box(x0,y0,x1,y1,c):
    rect(x0,y0,x1,y0,c); rect(x0,y1,x1,y1,c); rect(x0,y0,x0,y1,c); rect(x1,y0,x1,y1,c)
rect(0,FY,W-1,H-1,FLOOR)

# ---------- big bro: Clawd shape, one size up ----------
rect(6,3,21,15,B)                         # body 16x13 (Clawd is 12x8)
for lx in (8,10,17,19): rect(lx,16,lx,18,B)   # legs
# glasses
for x0 in (7,14):
    box(x0,4,x0+5,9,K); rect(x0+1,5,x0+4,8,LENS)
    rect(x0+2,6,x0+3,7,K)                 # square eyes, same as Clawd
rect(13,6,13,6,K)                         # bridge
# crack (top-right of shell)
for x,y in [(20,3),(20,4),(21,5),(20,6),(20,7),(21,8)]: px[x,y]=CR
# lopsided smug grin
rect(10,12,15,12,K); px[9,11]=K; px[16,11]=K; px[17,11]=K; px[18,10]=K
rect(11,13,14,13,MR); px[12,13]=WH; px[13,13]=WH
# small right claw (viewer's left)
rect(4,10,5,10,B)
# BIG left claw (viewer's right), raised, with a pincer notch
rect(22,9,24,10,B); rect(24,8,25,9,B)
rect(24,1,29,7,B); rect(26,1,27,3,BG)
# work badge
rect(17,13,19,15,WH); rect(17,13,19,13,(60,110,200)); px[18,15]=K
# sweat drop
px[4,1]=(120,180,240); rect(3,2,5,3,(120,180,240)); px[4,2]=WH
# empty wallet + moth
rect(0,16,3,18,(110,70,40)); rect(0,16,3,16,K)
px[2,14]=(200,200,200); px[4,14]=(200,200,200); px[3,15]=(120,120,120)

# ---------- Clawd ----------
ox=36
rect(ox+6,8,ox+17,15,C)
rect(ox+4,11,ox+5,12,C); rect(ox+18,11,ox+19,12,C)
for lx in (7,9,14,16): rect(ox+lx,16,ox+lx,18,C)
rect(ox+8,10,ox+9,11,K); rect(ox+14,10,ox+15,11,K)

img=img.resize((W*S,H*S),Image.NEAREST)
img.save("art/crab-brothers.png")
img.crop((0,0,31*S,H*S)).save("art/claude-4-6-chenzhi-selfie.png")
img.crop((ox*S+2*S,0,(ox+22)*S,H*S)).save("art/clawd-selfie.png")
