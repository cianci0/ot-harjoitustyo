from objects.movement import Paddle
from objects.player import Player
from style import WINDOW
from gameloop import Gameloop

class TwoPlayer:
    def __init__(self, player1, player2, length):
        self.player1_name = player1
        self.player2_name = player2
        self.length = length
        self.gameloop = None

    def start(self):
        player1 = Player(self.player1_name)
        player2 = Player(self.player2_name)
        player1.paddle = Paddle(10, 175, WINDOW[1])
        player2.paddle = Paddle(375, 175, WINDOW[1])
        self.gameloop = Gameloop(player1, player2, self.length, True)
        self.gameloop.loop()

        return True
