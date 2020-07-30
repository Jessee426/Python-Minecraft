from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(10000):
    r=random.randrange(1,7)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z=z+4
    elif r==2: 
        mc.setBlocks(x,y,z,x,y,z-4,20)
        z=z-4
    elif r==3:     
        mc.setBlocks(x,y,z,x-4,y,z,133)
        x=x+4
    elif r==4: 
        mc.setBlocks(x,y,z,x+4,y,z,41) 
        x=x-4
    elif r==5:
       
        mc.setBlocks(x,y,z,x,y+4,z,41) 
        y=y+4
    else:
        mc.setBlocks(x,y,z,x,y-4,z,41) 
        y=y-4