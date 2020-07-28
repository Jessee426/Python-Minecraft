from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+200,y+100,z+200,5)
mc.setBlocks(x+1,y+1,z+1,x+199,y+99,z+199,0)

