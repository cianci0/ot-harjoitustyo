from random import choice
import pygame as pg
from style import WHITE

class Ball:
    """Ball class

       Attributes:
       x: integer value for x-coordinate
       x_orig: integer value to store original x-coordinate
       y: integer value for y-coordinate
       y_orig: integer value to store original y-coordinate
       diameter: integer value for ball diameter
       speed: integer value for ball velocity (pixels per iteration)
       velocity: list value for directional velocity. velocity[0] = speed on x-axis, velocity[1] = speed on y-axis
       window_width: integer value for width of the window that the ball exists in
       window_height: integer value for height of the window that the ball exists in

       Methods:
       move(self): Move ball
       randomize_velocity(self): Randomize ball direction
       check_collision_paddle(self, paddle_left, paddle_right): Check if ball collides with paddles. Returns True if so, otherwise returns False
       check_collision_ceiling_floor(self): Check if ball collides with ceiling or floor and change ball direction accordingly
       check_collision_wall(self): Check if ball collides with walls. Returns 1 if ball collides with left wall and 2 if it collides with right wall
       reset(self): Reset ball to starting position
       draw(self, screen): Render ball on screen

    """
    
    def __init__(self, x, y, window):
        self.x = self.x_orig = x
        self.y = self.y_orig = y
        self.diameter = 5
        self.speed = 1
        self.velocity = [1, 1]
        self.window_width, self.window_height = window[0], window[1]

    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def randomize_velocity(self, twoplayer):
        if twoplayer:
            self.velocity = [choice([-self.speed, self.speed]),
                            choice([-self.speed, self.speed])]
        else:
            self.velocity = [-1, choice([-self.speed, self.speed])]

    def check_collision_paddle(self, paddle_left, paddle_right):
        if self.x == paddle_left.x + 10 and self.y in range(paddle_left.y, paddle_left.y + paddle_left.height):
            self.velocity[0] *= -1
            return True
        elif self.x == paddle_right.x and self.y in range(paddle_right.y, paddle_right.y + paddle_right.height):
            self.velocity[0] *= -1
            return True
        return False

    def check_collision_ceiling_floor(self):
        if self.y <= 0 or self.y >= self.window_height:
            self.velocity[1] *= -1

    def check_collision_wall(self):
        if self.x <= 0:
            return 1
        elif self.x >= self.window_width:
            return 2

    def reset(self):
        self.x = self.x_orig
        self.y = self.y_orig

    def draw(self, screen):
        pg.draw.circle(screen, (WHITE), (self.x, self.y), self.diameter)


class Paddle:
    """Paddle class

       Attributes:
       x: integer value for x-coordinate
       x_orig: integer value for starting x-coordinate that doesn't change
       y: integer value for y-coordinate
       y_orig: integer value for starting y-coordinate that doesn't change
       width: integer value for paddle width
       height: integer value for paddle height
       up: Boolean value; True if paddle is being instructed to move up, otherwise False
       down: Boolean value; True if paddle is being instructed to move down, otherwise False
       velocity: integer value for speed on y-axis (pixels per tick)
       boundary: integer value for height of the window that the paddle exists in

       Methods:
       move(self): Move paddle
       reset(self): Reset paddle to starting position
       draw(self, screen): Render paddle on screen
    """
    def __init__(self, x, y, window_height):
        self.x = self.x_orig = x
        self.y = self.y_orig = y
        self.width = 10
        self.height = 50
        self.up = False
        self.down = False
        self.velocity = 2
        self.boundary = window_height

    def move(self):
        if self.down and self.y + self.velocity <= self.boundary - self.height:
            self.y += self.velocity
        elif self.up and self.y - self.velocity >= 0:
            self.y -= self.velocity

    def reset(self):
        self.x = self.x_orig
        self.y = self.y_orig
        self.up = False
        self.down = False

    def draw(self, screen):
        pg.draw.rect(
            screen, (WHITE), (self.x, self.y, self.width, self.height))


class NPCPaddle(Paddle):
    """Class for non-player character paddle that inherits the Paddle class.

       Attributes:
       x: integer value for x-coordinate
       x_orig: integer value for starting x-coordinate that doesn't change
       y: integer value for y-coordinate
       y_orig: integer value for starting y-coordinate that doesn't change
       width: integer value for paddle width
       height: integer value for paddle height
       up: Boolean value; True if paddle is being instructed to move up, otherwise False
       down: Boolean value; True if paddle is being instructed to move down, otherwise False
       velocity: integer value for speed on y-axis (pixels per tick)
       boundary: integer value for height of the window that the paddle exists in
       ball: Ball object for NPCPaddle to follow

       Methods:
       move(self): Move paddle
       reset(self): Reset paddle to starting position
       draw(self, screen): Render paddle on screen
       follow_ball(self): Follow ball
    """
    def __init__(self, x, y, window_height, ball):
        super().__init__(x, y, window_height)
        self.ball = ball

    def follow_ball(self):
        if self.ball.y < self.y + self.height // 2:
            self.up = True
            self.down = False
        elif self.ball.y > self.y + self.height // 2:
            self.up = False
            self.down = True
        else:
            self.up = False
            self.down = False
