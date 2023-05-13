import unittest
import pygame as pg
from twoplayer import TwoPlayer

class TestObject(unittest.TestCase):
    def setUp(self):
        self.twoplayer = TwoPlayer("balotelli", "cassano", 10)

    def tearDown(self):
        pg.quit()

    def test_twoplayer_constructor(self):
        self.assertNotEqual(self.twoplayer, None)

    def test_twoplayer_start(self):
        self.twoplayer.start()
        self.assertNotEqual(self.twoplayer.gameloop, None)
        self.tearDown()
