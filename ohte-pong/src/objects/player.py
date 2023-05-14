class Player:
    """ Class for player

        Attributes:
        name: string value for player name
        points: integer value for player points
        paddle: NoneType. Players get assigned Paddle or NPCPaddle objects outside this module

        Methods:
        increase_points(self): Increase player points by one
        reset_points(self): Reset player points to zero
    """
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.paddle = None

    def increase_points(self):
        self.points += 1

    def reset_points(self):
        self.points = 0
