import turtle
from typing import Tuple

class Text(turtle.Turtle):
    __text_align__ = 'center'
    __font__ = ('Courier', 24, 'normal')

    def __init__(self, text: str, color: str = 'aqua', starting_point: Tuple = (0,0)) -> None:
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(starting_point)
        self.update_text(text)

    def update_text(self, text):
        self.clear()
        self.write(text, align=self.__text_align__, font=self.__font__)