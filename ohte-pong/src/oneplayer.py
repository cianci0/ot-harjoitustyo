from objects.movement import Paddle, NPCPaddle
from objects.player import Player
from style import WINDOW
from gameloop import Gameloop
from db.score_database import insert_score

class OnePlayer:
    """ Class for single-player game initialization

        Attributes:
        player1_name: string value for player 1 name
        player2_name: string value for player 2 name
        gameloop: NoneType. OnePlayer object gets assigned a Gameloop object in start() -function
        length: meaningless integer value necessary for Gameloop initialization
        scores: list object that holds player scores obtained in one instance of initialization
        db: string value that holds the name of the variable in score_database.py that connects to the database in which scores will be stored

        Methods:
        insert_scores(self): Insert scores one-by-one into database
        start(self): Initalize Player-objects, assign paddles to them and start game loop. Returns True
    """
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
