from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
while True:
      mc.executeCommand("time add 1000")
      time.sleep(0.01)