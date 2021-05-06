from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
import CollisionDC
import Player

###################### Drawing ######################

def drawScene(objects):
    for item in objects:
        item.draw()
        item.update()

######################

