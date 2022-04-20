from typing import Tuple

from classes.ball import Ball
from classes.paddle import Paddle
from constants.window import WINDOW_HEIGHT

def move(element: Paddle | Ball, new_coord: Tuple = (None, None)):
    '''Move element

    Allows to move either a ball or paddle to a new set of coordinates
    '''
    x_cor = element.xcor()
    y_cor = element.ycor()
    x, y = new_coord

    if x is not None:
        x_cor += x

    if y is not None: 
        y_cor += y

    element.setx(x_cor)
    element.sety(y_cor)
    
def move_paddle(paddle: Paddle, y: int = Paddle.__move__):
    '''Move a paddle instance.

    If y is not provided, it moves up by default.
    '''

    new_y_cor = paddle.ycor() + y
    max_movement_range = (WINDOW_HEIGHT / 2) - (paddle.__height__ / 2) + 10 # adding 10 because it's a bit off in the window

    if new_y_cor >= -max_movement_range and new_y_cor <= max_movement_range:
        move(paddle, (0, y))

def move_paddle_up(paddle: Paddle):
    move_paddle(paddle)

def move_paddle_down(paddle: Paddle):
    move_paddle(paddle, y=-paddle.__move__)