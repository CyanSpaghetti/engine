from window import *
from gameObject import *

objectlist = []
player = gameObject("Player", transform(0, 0, 0))
objectlist.append(player)
balls = gameObject("Balls", transform(0, 0, 0))
objectlist.append(balls)
w = window(640, 480, "Window", objectlist)
