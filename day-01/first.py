from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

a = 5
b = 4
print (a)

print (mc.getPlayerEntityIds())

x = -217
y = 160
z = 367

#mc.player.setTilePos(-217, 160, 367)
mc.entity.setPos(235, x, y, z)

time.sleep(5)

x = 217
y = 160
z = 367

mc.entity.setPos(235, x, y, z)

