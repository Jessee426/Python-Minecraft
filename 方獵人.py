from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    hits=mc.events.PollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x, hit.pos.y,hit.pos.z
        blockID=mc.getBlock(x,y,z)
        print("恭喜你獵到ID"+str(blockID)+"方塊")
        mc.postToChat("恭喜你獵到ID"+str(blockID)+"方塊")

