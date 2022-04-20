import turtle
from typing import Tuple

from constants.window import WINDOW_WIDTH

class Paddle(turtle.Turtle):
    __move__ = 20 # increment
    __width__ = 20 # == Turtle shapesize stretch_len: 1
    __height__ = 100 # => 20 * 5 (shapesize stretch_wid: 5)
    __x_cor__ = (WINDOW_WIDTH / 2) - 50
    
    def __init__(self, shape: str = 'square', speed: int = 0, color: str = 'white', starting_point: Tuple = (-__x_cor__,0)) -> None:
        super().__init__(shape)
        self.speed(speed)
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_point)