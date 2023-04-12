class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.diameter = 10
    
    def move(self, velocity):
        if (0 <= self.x + velocity[0] and self.x + velocity[0] + self.diameter <= 400 and 0 <= self.y + self.diameter + velocity[1] <= 400:
            self.x += velocity[0]
            self.y += velocity[1]
        else:
            return False