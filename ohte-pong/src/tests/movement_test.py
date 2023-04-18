import unittest
from objects.movement import *

class TestObject(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(200, 200, (400, 400))
        self.paddle = Paddle(10, 175, 400)
    
    def test_ball_constructor_works(self):
        self.assertNotEqual(self.ball, None)

    def test_ball_movement_works(self):
        self.ball.move()
        self.assertEqual((self.ball.x, self.ball.y), (201, 201))

    def test_ball_collision_with_left_paddle(self):
        ball = Ball(20, 200, (400, 400))
        paddle_right = Paddle(375, 175, 400)
        ball.check_collision_paddle(self.paddle, paddle_right)
        self.assertEqual(ball.velocity[0], -1)

    def test_ball_collision_with_right_paddle(self):
        ball = Ball(375, 200, (400, 400))
        paddle_right = Paddle(375, 175, 400)
        ball.check_collision_paddle(self.paddle, paddle_right)
        self.assertEqual(ball.velocity[0], -1)

    def test_ball_collision_with_ceiling(self):
        ball = Ball(200, 0, (400, 400))
        ball.check_collision_ceiling_floor()
        self.assertEqual(ball.velocity[1], -1)

    def test_ball_collision_with_left_wall(self):
        ball = Ball(0, 200, (400, 400))
        a = ball.check_collision_wall()
        self.assertEqual(a, 1)

    def test_ball_collision_with_right_wall(self):
        ball = Ball(400, 200, (400, 400))
        a = ball.check_collision_wall()
        self.assertEqual(a, 2)

    def test_ball_reset_works(self):
        self.ball.move()
        self.ball.reset()
        self.assertEqual((self.ball.x, self.ball.y), (200, 200))

    def test_paddle_constructor_works(self):
        self.assertNotEqual(self.paddle, None)

    def test_paddle_movement_up_works(self):
        self.paddle.up = True
        self.paddle.move()
        self.assertEqual((self.paddle.x, self.paddle.y), (10, 173))

    def test_paddle_movement_down_works(self):
        self.paddle.down = True
        self.paddle.move()
        self.assertEqual((self.paddle.x, self.paddle.y), (10, 177))

    def test_paddle_doesnt_move_at_bottom_border(self):
        self.paddle = Paddle(10, 400, 400)
        self.paddle.down = True
        self.paddle.move()
        self.assertEqual((self.paddle.x, self.paddle.y), (10, 400))

    def test_paddle_reset_works(self):
        self.paddle.down = True
        self.paddle.move()
        self.paddle.reset()
        self.assertEqual((self.paddle.x, self.paddle.y), (10, 175))
