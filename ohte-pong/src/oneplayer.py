# Single-player view

import os
import pygame as pg
from objects.movement import Paddle, NPCPaddle
from objects.player import Player
from style import window
from gameloop import Gameloop


def start(p1, p2, length):
    # Initialize and center pygame window, set caption
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption("Pong")
    screen = pg.display.set_mode(window)
    font = pg.font.SysFont("Comic Sans", 24)

    # Initiate players and gameloop
    player1 = Player(p1)
    player2 = Player(p2)
    gameloop = Gameloop(player1, player2, length, screen, font, False)

    # Initiate paddles
    player1.paddle = Paddle(10, 175, window[1])
    player2.paddle = NPCPaddle(375, 175, window[1], gameloop.ball)

    gameloop.loop()
    return
