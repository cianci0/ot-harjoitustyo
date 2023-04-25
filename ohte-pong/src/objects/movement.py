from random import choice
import pygame
from style import white

class Ball:
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

    def randomize_velocity(self):
        self.velocity = [choice([-self.speed, self.speed]), choice([-self.speed, self.speed])]

    def increase_velocity(self):
        self.speed += 1
        self.velocity[0] = self.speed
        self.velocity[1] = self.speed

    # Check if ball collides with paddles. If so, change direction accordingly
    def check_collision_paddle(self, paddle_left, paddle_right):
        if self.x == paddle_left.x + 10 and self.y in range(paddle_left.y, paddle_left.y + paddle_left.height):
            self.velocity[0] *= -1
        elif self.x == paddle_right.x and self.y in range(paddle_right.y, paddle_right.y + paddle_right.height):
            self.velocity[0] *= -1

    # Check if ball collides with ceiling or floor. If so, change direction accordingly
    def check_collision_ceiling_floor(self):
        if self.y <= 0 or self.y >= self.window_height:
            self.velocity[1] *= -1

    def check_collision_wall(self):
        if self.x <= 0:
            # Ball has reached left wall
            return 1
        elif self.x >= self.window_width:
            # Ball has reached right wall
            return 2

    def reset(self):
        self.x = self.x_orig
        self.y = self.y_orig

    def draw(self, screen):
        pygame.draw.circle(screen, (white), (self.x, self.y), self.diameter)


class Paddle:
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

    def increase_velocity(self):
        self.velocity += 1

    def draw(self, screen):
        pygame.draw.rect(screen, (white), (self.x, self.y, self.width, self.height))

# NPC opponent
class NPCPaddle(Paddle):
    def __init__(self, x, y, window_height, ball):
        super().__init__(x, y, window_height)
        self.ball = ball

    def follow_ball(self):
        # Follow ball movement
        if self.ball.y < self.y + self.height // 2:
            self.up = True
            self.down = False
        elif self.ball.y > self.y + self.height // 2:
            self.up = False
            self.down = True
        else:
            self.up = False
            self.down = False
