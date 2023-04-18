import pygame, os
from random import choice
from objects.movement import *
from style import *
from objects.player import Player
from objects.clock import Clock

class Gameloop:
    def __init__(self, player1, player2):
        self.clock = Clock()
        self.screen = pygame.display.set_mode(window)
        self.font = pygame.font.SysFont("Comic Sans", 24)
        self.ball = Ball(200, 200, window)
        self.player1 = player1
        self.player2 = player2

    def render(self):
        # Draw ball and paddles, display score
        self.screen.fill(black)
        self.ball.draw(self.screen)
        self.player1.paddle.draw(self.screen)
        self.player2.paddle.draw(self.screen)

        text = self.font.render(f"{self.player1.name} {self.player1.points} – {self.player2.points} {self.player2.name}", True, white)
        self.screen.blit(text, (20, 10))

        pygame.display.flip()

    def loop(self):

        # Reset ball and paddles to starting positions
        self.ball.reset() 
        self.player1.paddle.reset()
        self.player2.paddle.reset()

        # Randomize ball direction
        self.ball.randomize_velocity()

        while True:
            for event in pygame.event.get():
                
                # Check which keys are being pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player1.paddle.up = True

                    if event.key == pygame.K_s:
                        self.player1.paddle.down = True

                    if event.key == pygame.K_UP:
                        self.player2.paddle.up = True

                    if event.key == pygame.K_DOWN:
                        self.player2.paddle.down = True

                # Check which keys are being released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player1.paddle.up = False

                    if event.key == pygame.K_s:
                        self.player1.paddle.down = False

                    if event.key == pygame.K_UP:
                        self.player2.paddle.up = False

                    if event.key == pygame.K_DOWN:
                        self.player2.paddle.down = False

                if event.type == pygame.QUIT:
                    exit()

            # Move paddles and ball
            self.player1.paddle.move()
            self.player2.paddle.move()
            self.ball.move()

            # Check if ball has reached wall. If so, increase player score and restart game loop
            if self.ball.check_collision_wall() == 1:
                self.player2.increase_points()
                self.loop() 

            elif self.ball.check_collision_wall() == 2:
                self.player1.increase_points()
                self.loop()
            
            # Check if ball collides with ceiling or floor
            self.ball.check_collision_ceiling_floor()

            # Check if ball collides with paddles
            self.ball.check_collision_paddle(self.player1.paddle, self.player2.paddle)

            # Draw ball and paddles, display score
            self.render()

            # Tick clock
            self.clock.tick(160)
