import unittest
from objects.object import move, Ball, Paddle

class TestObject(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(200, 200)
        self.paddle = Paddle(200, 200)
    
    def test_ball_constructor_works(self):
        self.assertNotEqual(self.ball, None)

    def test_paddle_constructor_works(self):
        self.assertNotEqual(self.paddle, None)

    def test_ball_movement_works(self):
        move(self.ball, (1,-1))
        self.assertEqual((self.ball.x, self.ball.y), (201, 199))

    def test_paddle_movement_works(self):
        move(self.paddle, (1,-1))
        self.assertEqual((self.paddle.x, self.paddle.y), (201, 199))
