import unittest
from objects.player import Player

class TestObject(unittest.TestCase):
    def setUp(self):
        self.player = Player("")

    def test_player_constructor_works(self):
        self.assertNotEqual(self.player, None)

    def test_player_increase_points_works(self):
        self.player.increase_points()
        self.assertEqual(self.player.points, 1)