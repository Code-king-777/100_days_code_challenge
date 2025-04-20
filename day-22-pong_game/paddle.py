from turtle import *


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.screen = getscreen()
        self.paddle = Turtle()



        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 50
        self.goto(self.x_pos, new_y)

    def go_down(self):
        new_y = self.ycor() - 50
        self.goto(self.x_pos, new_y)

