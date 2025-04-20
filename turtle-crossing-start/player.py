from turtle import *
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.screen = Screen()


    def movement(self):
        self.forward(MOVE_DISTANCE)

    def move(self):
        self.screen.listen()
        self.screen.onkey(self.movement,"Up")

    def reset_position(self):
        self.goto(STARTING_POSITION)