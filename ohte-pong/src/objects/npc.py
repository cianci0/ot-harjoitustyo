from ball import Ball
from paddle import Paddle

from random import randint

class Npc(Paddle):
    def __init__(self, x, y):
        super().__init__(x, y)

def npc_move(npc: Npc, ball: Ball):
    if randint(0, 99) == 99: # 1% funktion kutsukerroista botti ei liiku
        return
    if npc.y - npc.height/2 > ball.y - ball.diameter/2:
        npc.move(0, -1)
    elif npc.y - npc.height/2 < ball.y - ball.diameter/2:
        npc.move(0, 1)
