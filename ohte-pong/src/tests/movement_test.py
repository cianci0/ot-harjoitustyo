import unittest
from objects.movement import Ball, Paddle, NPCPaddle

class TestObject(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(200, 200, (400, 400))
        self.paddle = Paddle(10, 175, 400)
        self.npc = NPCPaddle(10, 175, 400, self.ball)
    
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

    def test_ball_collision_returns_false(self):
        paddle_right = Paddle(375, 175, 400)
        a = self.ball.check_collision_paddle(self.paddle, paddle_right)
        self.assertFalse(a)

    def test_ball_collision_with_ceiling(self):
        ball = Ball(200, 0, (400, 400))
        ball.check_collision_ceiling_floor()
        self.assertEqual(ball.velocity[1], -1)

    def test_ball_collision_with_ceiling_returns_false(self):
        ball = Ball(200, 200, (400, 400))
        ball.check_collision_ceiling_floor()
        self.assertEqual(ball.velocity[1], 1)

    def test_ball_collision_with_left_wall(self):
        ball = Ball(0, 200, (400, 400))
        a = ball.check_collision_wall()
        self.assertEqual(a, 1)

    def test_ball_collision_with_right_wall(self):
        ball = Ball(400, 200, (400, 400))
        a = ball.check_collision_wall()
        self.assertEqual(a, 2)
    
    def test_ball_collision_with_wall_returns_false(self):
        ball = Ball(200, 200, (400, 400))
        a = ball.check_collision_wall()
        self.assertEqual(a, None)

    def test_ball_reset_works(self):
        self.ball.move()
        self.ball.reset()
        self.assertEqual((self.ball.x, self.ball.y), (200, 200))

    def test_ball_velocity_increase_works(self):
        self.ball.increase_velocity()
        self.assertEqual(self.ball.velocity, [2, 2])

    def test_ball_randomize_velocity_works(self):
        self.ball.randomize_velocity()
        self.assertTrue(self.ball.velocity[0] in (self.ball.speed, -self.ball.speed) and self.ball.velocity[1] in (self.ball.speed, -self.ball.speed))

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
        self.assertEqual((self.paddle.x, self.paddle.y, self.paddle.up, self.paddle.down), (10, 175, False, False))

    def test_paddle_velocity_increase_works(self):
        self.paddle.increase_velocity()
        self.assertEqual(self.paddle.velocity, 3)

    def test_npcpaddle_constructor_works(self):
        self.assertNotEqual(self.npc, None)

    def test_npcpaddle_doesnt_move_when_level_with_ball(self):
        self.npc.follow_ball()
        self.assertEqual((self.npc.up, self.npc.down), (False, False))

    def test_npcpaddle_follows_ball_up(self):
        self.ball.y = 100
        self.npc.follow_ball()
        self.assertEqual(self.npc.up, True)

    def test_npcpaddle_follows_ball_down(self):
        self.ball.y = 300
        self.npc.follow_ball()
        self.assertEqual(self.npc.down, True)