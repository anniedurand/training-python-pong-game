from classes.ball import Ball
from classes.paddle import Paddle

from constants.collision import BALL_PADDLE_COLLISION_MAX_RANGE

def get_ball_y_cor_is_within_paddle_height(ball: Ball, paddle: Paddle) -> bool:
    ball_is_lower_than_paddle_top = ball.ycor() < paddle.ycor() + BALL_PADDLE_COLLISION_MAX_RANGE
    ball_is_higher_than_paddle_bottom = ball.ycor() > paddle.ycor() - BALL_PADDLE_COLLISION_MAX_RANGE

    return ball_is_lower_than_paddle_top and ball_is_higher_than_paddle_bottom