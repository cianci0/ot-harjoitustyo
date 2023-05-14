import unittest
import numpy as np
import pygame as pg
from unittest.mock import MagicMock, patch
import gameloop
from objects.movement import Paddle
from objects.player import Player
from style import WINDOW

class TestObject(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("1")
        self.player2 = Player("2")
        self.gameloop = gameloop.Gameloop(self.player1, self.player2, 10, False)
        pg.display.set_mode((WINDOW), flags=pg.HIDDEN)
        self.ball = gameloop.Ball(200, 200, (400, 400))

    def tearDown(self):
        pg.quit()

    def test_gameloop_constructor(self):
        self.assertNotEqual(self.gameloop, None)
        self.tearDown()        

    def test_gameloop_rendering(self):
        self.player1.paddle = Paddle(0, 0, 400)
        self.player2.paddle = Paddle(7, 7, 400)
        arr1 = pg.surfarray.array2d(self.gameloop.screen)
        self.gameloop.render()
        arr2 = pg.surfarray.array2d(self.gameloop.screen)
        self.assertFalse(np.array_equal(arr1, arr2))
        self.tearDown()

    def test_gameloop_display_score_oneplayer(self):
        arr1 = pg.surfarray.array2d(self.gameloop.screen)
        self.gameloop.display_score()
        arr2 = pg.surfarray.array2d(self.gameloop.screen)
        self.assertFalse(np.array_equal(arr1, arr2))
        self.tearDown()

    def test_gameloop_display_score_twoplayer(self):
        self.gameloop.twoplayer = True
        arr1 = pg.surfarray.array2d(self.gameloop.screen)
        self.gameloop.display_score()
        arr2 = pg.surfarray.array2d(self.gameloop.screen)
        self.assertFalse(np.array_equal(arr1, arr2))
        self.tearDown()

    def test_change_theme(self):
        self.gameloop.is_paused = False
        a = self.gameloop.light
        b = self.gameloop.dark
        self.gameloop.change_theme()
        self.assertNotEqual((a, b), (self.gameloop.light, self.gameloop.dark))
        self.tearDown()

    def test_change_theme_returns_False(self):
        self.gameloop.is_paused = True
        a = self.gameloop.change_theme()
        self.assertFalse(a)
        self.tearDown()

    def test_event_loop_w(self):
        self.player1.paddle = Paddle(10, 175, 400)
        self.player2.paddle = Paddle(375, 175, 400)

        keydown = pg.event.Event(pg.KEYDOWN, {"key": pg.K_w})
        pg.event.get = MagicMock(return_value=[keydown])
        self.gameloop.event_loop()
        self.assertTrue(self.gameloop.player1.paddle.up)

        quit = pg.event.Event(pg.QUIT)
        pg.event.get = MagicMock(return_value=[quit])

        self.tearDown()

    def test_event_loop_s(self):
        self.player1.paddle = Paddle(10, 175, 400)
        self.player2.paddle = Paddle(375, 175, 400)

        keydown = pg.event.Event(pg.KEYDOWN, {"key": pg.K_s})
        pg.event.get = MagicMock(return_value=[keydown])
        self.gameloop.event_loop()
        self.assertTrue(self.gameloop.player1.paddle.down)

        quit = pg.event.Event(pg.QUIT)
        pg.event.get = MagicMock(return_value=[quit])

        self.tearDown()

    def test_event_loop_arrow_up(self):
        self.player1.paddle = Paddle(10, 175, 400)
        self.player2.paddle = Paddle(375, 175, 400)
        self.gameloop.twoplayer = True

        keydown = pg.event.Event(pg.KEYDOWN, {"key": pg.K_UP})
        pg.event.get = MagicMock(return_value=[keydown])
        self.gameloop.event_loop()
        self.assertTrue(self.gameloop.player2.paddle.up)

        quit = pg.event.Event(pg.QUIT)
        pg.event.get = MagicMock(return_value=[quit])

        self.tearDown()
    
    def test_event_loop_arrow_down(self):
        self.player1.paddle = Paddle(10, 175, 400)
        self.player2.paddle = Paddle(375, 175, 400)
        self.gameloop.twoplayer = True

        keydown = pg.event.Event(pg.KEYDOWN, {"key": pg.K_DOWN})
        pg.event.get = MagicMock(return_value=[keydown])
        self.gameloop.event_loop()
        self.assertTrue(self.gameloop.player2.paddle.down)

        quit = pg.event.Event(pg.QUIT)
        pg.event.get = MagicMock(return_value=[quit])

        self.tearDown()
