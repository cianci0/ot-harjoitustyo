from objects.movement import Paddle, NPCPaddle
from objects.player import Player
from style import WINDOW
from gameloop import Gameloop
from db.score_database import insert_score

class OnePlayer:
    def __init__(self, player1, player2):
        self.player1_name = player1
        self.player2_name = player2
        self.gameloop = None
        self.length = 69
        self.scores = []
        self.db = "db"

    def insert_scores(self):
        for score in self.scores:
            insert_score(score[0], score[1], self.db)

    def start(self):
        player1 = Player(self.player1_name)
        player2 = Player(self.player2_name)
        self.gameloop = Gameloop(player1, player2, self.length, False)
        player1.paddle = Paddle(10, 175, WINDOW[1])
        player2.paddle = NPCPaddle(375, 175, WINDOW[1], self.gameloop.ball)

        self.scores = self.gameloop.loop()

        self.insert_scores()

        return True
