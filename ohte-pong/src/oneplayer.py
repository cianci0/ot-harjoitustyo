from objects.movement import Paddle, NPCPaddle
from objects.player import Player
from style import window
from gameloop import Gameloop


def start(p1, p2, length):
    # Initiate players and gameloop
    player1 = Player(p1)
    player2 = Player(p2)
    gameloop = Gameloop(player1, player2, length, False)

    # Initiate paddles
    player1.paddle = Paddle(10, 175, window[1])
    player2.paddle = NPCPaddle(375, 175, window[1], gameloop.ball)

    gameloop.loop()
    return
