import pygame as pg, os
from objects.movement import Ball
from objects.clock import Clock
from style import window, black, white

class Gameloop:
    """Class for handling game loop

        Attributes:
        screen: pygame.display object to display the game.
        font: pygame.font.SysFont object to display player names and scores.
        twoplayer: Boolean value; True in case of two-player game, otherwise False.
        clock: Clock object to monitor time.
        ball: Ball object
        player1: Player object that controls the left-hand paddle.
        player2: Player object that controls the right-hand side paddle.
        length: integer that determines game length if twoplayer is True.
        is_paused: Boolean value; True if the game is paused at any given moment, otherwise False.
        ended: Boolean value; True if the game has ended and exited, otherwise False.
        running: Boolean value that determines whether game loop is running or not.
        rally_length: integer that keeps track of the length of the current rally.
    """

    def __init__(self, player1, player2, length, twoplayer):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        pg.display.set_caption("Pong")
        self.screen = pg.display.set_mode(window)
        self.font = pg.font.SysFont("Comic Sans", 24)
        self.twoplayer = twoplayer
        self.clock = Clock()
        self.ball = Ball(200, 200, window)
        self.player1 = player1
        self.player2 = player2
        self.length = length
        self.is_paused = True
        self.ended = False
        self.running = True
        self.rally_length = 0

    def display_score(self):
        if self.twoplayer:
            text = self.font.render(f"{self.player1.name} {self.player1.points} – {self.player2.points} {self.player2.name}", True, white)
        else:
            text = self.font.render(f"Pisteet: {self.rally_length}", True, white)
        self.screen.blit(text, (20, 10))

    def render(self):
        # Draw ball and paddles, display score
        self.screen.fill(black)
        self.ball.draw(self.screen)
        self.player1.paddle.draw(self.screen)
        self.player2.paddle.draw(self.screen)

    def end(self, player):
        running = True
        self.screen.fill(black)
        while running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.ended = False
                        return True
                if event.type == pg.QUIT:
                    self.ended = True
                    return False
            if self.twoplayer:
                text = self.font.render(f"Pelaaja {player} voitti!", True, white)
                text_rect = text.get_rect(center=(window[0] // 2, window[1] // 2))
                self.screen.blit(text, text_rect)
                pg.display.flip()
            elif self.twoplayer is False:
                text = self.font.render(f"Peli päättyi, sait {self.rally_length} pistettä", True, white)
                text_rect = text.get_rect(center=(window[0] // 2, window[1] // 2))
                self.screen.blit(text, text_rect)
                pg.display.flip()
 
    
    def loop(self):
        self.ball.reset()
        self.player1.paddle.reset()
        self.player2.paddle.reset()
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

            if not self.is_paused:
                self.player1.paddle.move()
                if not self.twoplayer:
                    self.player2.paddle.follow_ball()
                self.player2.paddle.move()
                self.ball.move()

                if self.ball.check_collision_wall() == 1:
                    if self.twoplayer is False:
                        if self.end(666) == True:
                            self.rally_length = 0
                            self.loop()
                        self.running = False
                    self.player2.increase_points()
                    self.rally_length = 0
                    if self.player2.points == self.length:
                        if self.end(2) is False:
                            self.running = False
                        self.player1.reset_points()
                        self.player2.reset_points()
                    self.loop()

                elif self.ball.check_collision_wall() == 2:
                    self.player1.increase_points()
                    if self.player1.points == self.length:
                        if self.end(1) is False:
                            self.running = False
                        self.player1.reset_points()
                        self.player2.reset_points()
                    self.rally_length = 0
                    self.loop()

                self.ball.check_collision_ceiling_floor()

                if self.ball.check_collision_paddle(self.player1.paddle, self.player2.paddle):
                    self.rally_length += 1

                self.render()
                self.display_score()
                pg.display.flip()
                self.clock.tick(160)
            
            else:
                if not self.ended:
                    text = self.font.render("Paused", True, white)
                    text_rect = text.get_rect(center=(window[0] // 2, window[1] // 2))
                    self.screen.blit(text, text_rect)
                    pg.display.flip()
            
        # Hide pygame window
        self.screen = pg.display.set_mode(window, flags=pg.HIDDEN)
        return True
