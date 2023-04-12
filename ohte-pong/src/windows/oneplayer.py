# Yksinpelinäkymä

import pygame
import random
from objects.playingfield import PlayingField
from objects.ball import Ball
from objects.paddle import Paddle
from objects.player import Player
from objects.npc import Npc


field = PlayingField()

ball = Ball(200, 200)
ball_velocity = (random.choice((-1, 1)), random.choice((-1, 1)))

left_paddle = Paddle(10, 175)
right_paddle = Npc(375, 175)

player = Player("nimi")

