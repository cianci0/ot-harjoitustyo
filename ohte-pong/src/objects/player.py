class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.paddle = None

    def increase_points(self):
        self.points += 1