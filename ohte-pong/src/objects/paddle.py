class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 50

    def move(self, velocity):
        if 0 <= self.y + velocity[1] and self.y + velocity[1] + self.height <= 400:
            self.y += velocity[1]
        else:
            return False
