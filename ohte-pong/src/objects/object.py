class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ball(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.diameter = 10

class Paddle(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 10
        self.height = 50

def move(object: Object, velocity):
    object.x += velocity[0]
    object.y += velocity[1]