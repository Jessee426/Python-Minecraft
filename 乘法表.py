from mcpi.minecraft import Minecraft
mc=Minecraft.create()
list123=[]
list456=[]
list789=[]
for i in range(1,4):
    list123.append(i*1)
for i in range(1,4):
    list456.append(i*2)
for i in range(1,4):
    list789.append(i*3)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,2,str(list123),str(list456),str(list789))               