from classes.ball import Ball
from classes.paddle import Paddle

MIN_BALL_PADDLE_COLLISION_X_COR = Paddle.__x_cor__ - (Paddle.__width__ / 2)
MAX_BALL_PADDLE_COLLISION_X_COR = Paddle.__x_cor__
BALL_PADDLE_COLLISION_MAX_RANGE = (Paddle.__height__ / 2) - Ball.__half_size__