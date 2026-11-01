from PIL import Image, ImageDraw
W,H=48,40; S=16
img=Image.new("RGB",(W,H),(250,236,210))
px=img.load()
def p(x,y,c):
    if 0<=x<W and 0<=y<H: px[x,y]=c
def rect(x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): p(x,y,c)
def ell(cx,cy,rx,ry,c):
    for y in range(H):
        for x in range(W):
            if ((x-cx)/rx)**2+((y-cy)/ry)**2<=1: p(x,y,c)
O=(30,22,20); R=(222,80,44); RD=(170,52,30); RL=(246,128,80)
K=(20,20,20); WH=(255,255,255); G=(150,200,230); P=(240,150,150); BG2=(235,215,180)
# floor
rect(0,34,W-1,H-1,BG2)
# legs
for i,lx in enumerate([10,13,16]):
    rect(lx-2,26+i,lx,27+i,RD); rect(lx-3,28+i,lx-2,32,RD)
for i,lx in enumerate([31,34,37]):
    rect(lx,26+i,lx+2,27+i,RD); rect(lx+2,28+i,lx+3,32,RD)
# body (outline then fill)
ell(24,23,14,9,O); ell(24,23,13,8,R)
ell(24,20,10,4,RL); ell(24,22,11,6,R)
ell(24,27,10,3,RD); ell(24,25,12,4,R)
# crack on shell (top right)
for x,y in [(26,15),(27,16),(27,17),(28,18),(29,18),(29,19),(30,20),(30,21),(28,17),(31,22),(26,19),(27,19)]: p(x,y,O)
# eye stalks
rect(18,9,19,15,R); rect(29,9,30,15,R)
for y in range(9,16): p(17,y,O); p(20,y,O); p(28,y,O); p(31,y,O)
# glasses: thick black frames around eyes
for cx in (18,30):
    rect(cx-3,5,cx+4,11,K); rect(cx-2,6,cx+3,10,G)
    rect(cx-1,7,cx+1,9,WH); p(cx,8,K); p(cx+1,8,K)  # pupils looking sideways (smug)
rect(23,7,25,7,K)  # bridge
# half-lidded smug brows
rect(15,3,21,3,K); rect(28,1,33,1,K); p(27,2,K); p(34,2,K)
# smug grin
for x in range(19,30): p(x,24,O)
p(18,23,O); p(17,23,O); p(30,23,O); p(31,22,O); p(32,21,O); p(32,20,O)
rect(21,25,27,25,O); rect(22,25,26,25,(140,20,20)); rect(23,25,24,25,WH)
# blush
rect(14,22,16,23,P); rect(32,22,34,23,P)
# small claw (viewer's left = his right)
rect(7,19,10,21,R); 
ell(5,15,3,4,O); ell(5,15,2,3,R); rect(4,11,6,13,(250,236,210)); p(5,12,(250,236,210))
rect(6,17,9,19,R)
# BIG claw (viewer's right = his left)
rect(33,19,38,22,O); rect(34,20,38,21,R)          # arm
ell(41,15,6,7,O); ell(41,15,5,6,R); ell(39,13,2,2,RL)  # palm
# upper pincer
ell(38,5,3,5,O); ell(38,5,2,4,R)
# lower/outer pincer
ell(44,6,3,6,O); ell(44,6,2,5,R); p(44,3,RL)
rect(40,2,41,9,(250,236,210))  # gap between pincers
p(40,10,O); p(41,10,O)
# sweat drop
p(13,1,(120,180,240)); rect(12,2,14,3,(120,180,240)); p(13,2,WH)
# empty wallet + moth (broke worker vibe) at bottom-left
rect(2,30,8,35,(110,70,40)); rect(2,30,8,30,O); rect(3,31,7,31,(150,100,60))
p(10,28,(200,200,200)); p(12,28,(200,200,200)); p(11,29,(120,120,120))
# work badge on body
rect(22,28,26,31,WH); rect(22,28,26,28,(60,110,200)); rect(23,30,25,30,K)
big=img.resize((W*S,H*S),Image.NEAREST)
big.save("art/claude-4-6-chenzhi-selfie.png")
