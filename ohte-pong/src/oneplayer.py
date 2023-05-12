from objects.movement import Paddle, NPCPaddle
from objects.player import Player
from style import WINDOW
from gameloop import Gameloop
from db.score_database import insert_score


def start(player1, player2, length):
    player1 = Player(player1)
    player2 = Player(player2)
    gameloop = Gameloop(player1, player2, length, False)
    player1.paddle = Paddle(10, 175, WINDOW[1])
    player2.paddle = NPCPaddle(375, 175, WINDOW[1], gameloop.ball)

    scores = gameloop.loop()

    for score in scores:
        insert_score(score[0], score[1])
    
    return True
