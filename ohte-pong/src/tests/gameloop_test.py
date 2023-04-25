import unittest
import pygame as pg
import gameloop
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
        self.gameloop = gameloop.Gameloop(self.player1, self.player2, 10, self.screen, self.font, False)

    def test_gameloop_constructor_works(self):
        self.assertNotEqual(self.gameloop, None)

    def test_gameloop_clock_tick_works(self):
        a = self.gameloop.clock.get_ticks()
        self.gameloop.clock.tick(160)
        b = self.gameloop.clock.get_ticks()
        self.assertNotEqual(a, b)