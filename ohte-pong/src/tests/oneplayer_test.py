import unittest
from db.score_database import clear, get_top3
import pygame as pg
from oneplayer import OnePlayer

class TestObject(unittest.TestCase):
    def setUp(self):
        self.oneplayer = OnePlayer("balotelli", "botti")
        self.oneplayer.db = "test_db"

    def tearDown(self):
        pg.quit()

    def test_oneplayer_constructor(self):
        self.assertNotEqual(self.oneplayer, None)

    def test_oneplayer_start(self):
        self.oneplayer.start()
        self.assertNotEqual(self.oneplayer.gameloop, None)
        self.tearDown()

    def test_oneplayer_start_insert_scores(self):
        clear("test_db")
        self.oneplayer.scores = [("balotelli", 45), ("cassano", 99), ("ronaldo", 7)]
        self.oneplayer.insert_scores()
        scores = get_top3("test_db")
        self.assertEqual((scores[0], scores[2]), (("cassano", 99), ("ronaldo", 7)))
    