from PIL import Image
S=16; BG=(250,236,210); FLOOR=(235,215,180)
C=(215,119,87); K=(20,20,20)
# Clawd: blocky, terracotta, two square eyes, stubby arms, four legs
W,H=24,22
img=Image.new("RGB",(W,H),BG); px=img.load()
def rect(x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): px[x,y]=c
rect(0,16,W-1,H-1,FLOOR)
rect(6,5,17,12,C)        # body
rect(4,8,5,9,C); rect(18,8,19,9,C)   # stubby arms
for lx in (7,9,14,16): rect(lx,13,lx,15,C)   # legs
rect(8,7,9,8,K); rect(14,7,15,8,K)  # eyes
img.resize((W*S,H*S),Image.NEAREST).save("art/clawd-selfie.png")

# side-by-side with big bro
bro=Image.open("art/claude-4-6-chenzhi-selfie.png")
me=img.resize((W*S,H*S),Image.NEAREST)
duo=Image.new("RGB",(bro.width+me.width,bro.height),BG)
duo.paste(bro,(0,0))
fl=Image.new("RGB",(me.width,bro.height-me.height),BG); duo.paste(fl,(bro.width,0))
duo.paste(me,(bro.width,bro.height-me.height))
duo.save("art/crab-brothers.png")
