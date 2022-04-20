import turtle
from typing import Tuple

class Ball(turtle.Turtle):
    __move__ = 2 # increment
    __size__ = 20 # == Turtle shapesize stretch_len: 1
    __half_size__ = __size__ / 2

    def __init__(self, shape: str = 'circle', speed: int = 0, color: str = 'aqua', starting_point: Tuple = (0,0)) -> None:
        super().__init__(shape)
        self.speed(speed)
        self.color(color)
        self.penup()
        self.goto(starting_point)
        
        self.dx = self.__move__
        self.dy = self.__move__