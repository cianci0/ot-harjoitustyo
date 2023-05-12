import unittest
from objects.clock import Clock

class TestObject(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_clock_tick(self):
        a = self.clock.get_ticks()
        self.clock.tick(200)
        b = self.clock.get_ticks()
        self.assertTrue(a < b)

    def test_clock_get_ticks(self):
        self.assertNotEqual(self.clock.get_ticks(), None)