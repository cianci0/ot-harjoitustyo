import unittest
import numpy as np
import pygame as pg
import gameloop
from objects.movement import Paddle
from objects.player import Player
from style import window

class TestObject(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.font = pg.font.SysFont("Comic Sans", 24)
        self.screen = pg.display.set_mode(window)
        self.player1 = Player("1")
        self.player2 = Player("2")
        self.ball = gameloop.Ball(200, 200, (400, 400))
        self.gameloop = gameloop.Gameloop(self.player1, self.player2, 10, False)

    def test_gameloop_constructor_works(self):
        self.assertNotEqual(self.gameloop, None)

    def test_gameloop_clock_tick_works(self):
        a = self.gameloop.clock.get_ticks()
        self.gameloop.clock.tick(160)
        b = self.gameloop.clock.get_ticks()
        self.assertNotEqual(a, b)

    def test_gameloop_rendering_works(self):
        self.player1.paddle = Paddle(0, 0, 400)
        self.player2.paddle = Paddle(7, 7, 400)
        arr1 = pg.surfarray.array2d(self.screen)
        self.gameloop.render()
        arr2 = pg.surfarray.array2d(self.screen)
        self.assertFalse(np.array_equal(arr1, arr2))

    def test_gameloop_display_score_oneplayer(self):
        arr1 = pg.surfarray.array2d(self.screen)
        self.gameloop.display_score()
        arr2 = pg.surfarray.array2d(self.screen)
        self.assertFalse(np.array_equal(arr1, arr2))

    def test_gameloop_display_score_twoplayer(self):
        self.gameloop.twoplayer = True
        arr1 = pg.surfarray.array2d(self.screen)
        self.gameloop.display_score()
        arr2 = pg.surfarray.array2d(self.screen)
        self.assertFalse(np.array_equal(arr1, arr2))
        
