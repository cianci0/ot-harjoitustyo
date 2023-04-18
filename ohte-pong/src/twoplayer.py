import os
import pygame
from objects.movement import Paddle
from objects.player import Player
from style import window
from gameloop import Gameloop

# Initialize and center pygame window, set caption
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Pong")

# Initiate players with placeholder names for now
player1 = Player("balotelli")
player2 = Player("cassano")

# Initiate paddles
player1.paddle = Paddle(10, 175, window[1])
player2.paddle = Paddle(375, 175, window[1])

gameloop = Gameloop(player1, player2)
gameloop.loop()
