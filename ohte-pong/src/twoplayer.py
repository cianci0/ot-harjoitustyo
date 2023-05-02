from objects.movement import Paddle
from objects.player import Player
from style import window
from gameloop import Gameloop


def start(p1, p2, length):
    # Initiate players and paddles
    player1 = Player(p1)
    player2 = Player(p2)
    player1.paddle = Paddle(10, 175, window[1])
    player2.paddle = Paddle(375, 175, window[1])

    gameloop = Gameloop(player1, player2, length, True)

    gameloop.loop()
    return
