from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
   
    mc.setBlock(x,y,z,38)
    time.sleep(2)
