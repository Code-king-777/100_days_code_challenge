from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0,295)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f" SCORE: {self.score}     HIGH SCORE:{self.high_score}", False,ALIGNMENT ,FONT )

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
