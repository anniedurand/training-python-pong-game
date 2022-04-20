from typing import Tuple

from classes.ball import Ball
from functions.sound import play_sound

def bounce_ball(ball: Ball, new_coord: Tuple = (None, None)):
    '''Bounce a ball instance.

    Sets new coordinates and reverses movement
    '''
    x, y = new_coord
    x_collided = x is not None
    y_collided = y is not None

    if x_collided or y_collided:
        # play bounce sound
        play_sound('sounds/bounce.wav')

        if x_collided:
            ball.setx(x)
            ball.dx *= -1

        if y_collided:
            ball.sety(y)
            ball.dy *= -1
    

def vertical_bounce(ball: Ball, y: int):
    '''Bounces ball vertically

    Reverses y direction
    '''
    bounce_ball(ball, (None, y))

def horizontal_bounce(ball: Ball, x: int = 0, reset_position: bool = False):
    '''Bounces ball horizontally

    Optionally resets the ball's coordinates to center of the window and reverses x direction
    '''
    if reset_position:
        ball.goto(0,0)

    bounce_ball(ball, (x, None))