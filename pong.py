# Pong game based on freeCodeCamp.org tutorial - https://www.youtube.com/watch?v=XGf2GcyHPhc (original code: http://christianthompson.com/sites/default/files/Pong/pong.py)
# But optimized to use classes and reduce copied code

import turtle

from classes.ball import Ball
from classes.paddle import Paddle
from classes.score import Score

from constants.collision import MAX_BALL_PADDLE_COLLISION_X_COR, MIN_BALL_PADDLE_COLLISION_X_COR
from constants.window import WINDOW_HEIGHT, WINDOW_HORIZONTAL_LIMIT, WINDOW_VERTICAL_LIMIT, WINDOW_WIDTH

from functions.bounce import horizontal_bounce, vertical_bounce
from functions.move import move, move_paddle_down, move_paddle_up
from functions.utils import get_ball_y_cor_is_within_paddle_height

# SET UP SCREEN:
window = turtle.Screen()
window.title('My pong game')
window.bgcolor('purple')
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.tracer(0) # allows to manually speed up animation

# CREATE GAME ELEMENTS:
paddle_a = Paddle(color= 'yellow')
paddle_b = Paddle(starting_point=(Paddle.__x_cor__,0))
ball = Ball()
score = Score()


# KEYBOARD BINDINGS:

# Bindings functions
def move_paddle_a_up():
    move_paddle_up(paddle_a)

def move_paddle_a_down():
    move_paddle_down(paddle_a)

def move_paddle_b_up():
    move_paddle_up(paddle_b)

def move_paddle_b_down():
    move_paddle_down(paddle_b)

# Listeners
window.listen()
window.onkeypress(move_paddle_a_up, 'w')
window.onkeypress(move_paddle_a_down, 's')
window.onkeypress(move_paddle_b_up, 'Up') # arrow up key
window.onkeypress(move_paddle_b_down, 'Down') # arrow down key


# MAIN GAME LOOP:
while True:
    window.update()

    # Move the ball
    move(ball, (ball.dx, ball.dy))

    # Border checking
    if ball.ycor() > WINDOW_VERTICAL_LIMIT:
        vertical_bounce(ball, y=WINDOW_VERTICAL_LIMIT)

    if ball.ycor() < -WINDOW_VERTICAL_LIMIT:
        vertical_bounce(ball, y=-WINDOW_VERTICAL_LIMIT)

    if ball.xcor() > WINDOW_HORIZONTAL_LIMIT:
        score.increment_score_a()
        horizontal_bounce(ball, reset_position=True)

    if ball.xcor() < -WINDOW_HORIZONTAL_LIMIT:
        score.increment_score_b()
        horizontal_bounce(ball, reset_position=True)

    # Paddle and ball collisions
    if (ball.xcor() > MIN_BALL_PADDLE_COLLISION_X_COR and ball.xcor() < MAX_BALL_PADDLE_COLLISION_X_COR) and get_ball_y_cor_is_within_paddle_height(ball, paddle_b):
        horizontal_bounce(ball, x=MIN_BALL_PADDLE_COLLISION_X_COR)
        
    if (ball.xcor() < -MIN_BALL_PADDLE_COLLISION_X_COR and ball.xcor() > -MAX_BALL_PADDLE_COLLISION_X_COR) and get_ball_y_cor_is_within_paddle_height(ball, paddle_a):
        horizontal_bounce(ball, x=-MIN_BALL_PADDLE_COLLISION_X_COR)