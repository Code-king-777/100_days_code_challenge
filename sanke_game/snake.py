from turtle import *



STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.created_snake()
        self.head = self.snakes[0]



    def created_snake(self):

        for tur in STARTING_POSITION:
            self.add_segment(tur)


    def add_segment(self,tur):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(tur)
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.created_snake()
        self.head = self.snakes[0]


    def move(self):
        for snakes_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snakes_num - 1].xcor()
            new_y = self.snakes[snakes_num - 1].ycor()
            self.snakes[snakes_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)