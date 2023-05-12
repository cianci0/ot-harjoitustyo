from objects.movement import Paddle
from objects.player import Player
from style import WINDOW
from gameloop import Gameloop


def start(p1, p2, length):
    player1 = Player(p1)
    player2 = Player(p2)
    player1.paddle = Paddle(10, 175, WINDOW[1])
    player2.paddle = Paddle(375, 175, WINDOW[1])
    gameloop = Gameloop(player1, player2, length, True)
    gameloop.loop()

    return True
