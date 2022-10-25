from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.choose_location()

    def choose_location(self):
        num_x = randint(-250, 250)
        num_y = randint(-250, 250)
        self.goto(num_x, num_y)

