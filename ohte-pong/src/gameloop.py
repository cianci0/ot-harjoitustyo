import pygame as pg
from objects.movement import Ball
from objects.clock import Clock
from style import window, black, white

class Gameloop:
    def __init__(self, player1, player2, length, screen, font, twoplayer):
        self.twoplayer = twoplayer
        self.clock = Clock()
        self.screen = screen
        self.font = font
        self.ball = Ball(200, 200, window)
        self.player1 = player1
        self.player2 = player2
        self.length = length
        self.is_paused = False
        self.running = True

    def render(self):
        # Draw ball and paddles, display score
        self.screen.fill(black)
        self.ball.draw(self.screen)
        self.player1.paddle.draw(self.screen)
        self.player2.paddle.draw(self.screen)

        text = self.font.render(f"{self.player1.name} {self.player1.points} – {self.player2.points} {self.player2.name}", True, white)
        self.screen.blit(text, (20, 10))

    def loop(self):

        # Reset ball and paddles to starting positions
        self.ball.reset()
        self.player1.paddle.reset()
        self.player2.paddle.reset()

        # Randomize ball direction
        self.ball.randomize_velocity()

        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player1.paddle.up = True
                    if event.key == pg.K_s:
                        self.player1.paddle.down = True
                    if self.twoplayer:
                        if event.key == pg.K_UP:
                            self.player2.paddle.up = True
                        if event.key == pg.K_DOWN:
                            self.player2.paddle.down = True

                    # Check for spacebarrd to start/pause the game
                    if event.key == pg.K_SPACE:
                        self.is_paused = not self.is_paused

                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.player1.paddle.up = False
                    if event.key == pg.K_s:
                        self.player1.paddle.down = False
                    if self.twoplayer:
                        if event.key == pg.K_UP:
                            self.player2.paddle.up = False
                        if event.key == pg.K_DOWN:
                            self.player2.paddle.down = False

                if event.type == pg.QUIT:
                    self.running = False

            # If game is not paused, move paddles and ball
            if not self.is_paused:
                self.player1.paddle.move()
                if not self.twoplayer:
                    self.player2.paddle.follow_ball()
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

                # Update display
                pg.display.flip()

                # Tick clock
                self.clock.tick(160)
            
            else:
                # Render pause view
                text = self.font.render("Paused", True, white)
                text_rect = text.get_rect(center=(window[0] // 2, window[1] // 2))
                self.screen.blit(text, text_rect)
                pg.display.flip()
            
        pg.quit()
