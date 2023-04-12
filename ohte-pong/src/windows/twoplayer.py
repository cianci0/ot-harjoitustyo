# Kaksinpelinäkymä

import pygame
import random
from objects.playingfield import PlayingField
from objects.paddle import move, Ball, Paddle

field = PlayingField()

ball = Ball(200, 200)
ball_velocity = (random.choice((-1, 1)), random.choice((-1, 1)))

left_paddle = Paddle(10, 175)
right_paddle = Paddle(375, 175)