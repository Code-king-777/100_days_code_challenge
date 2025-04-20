from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-360,260)
        self.write(f"LEVEL:{self.score}" , False ,"left", FONT )

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER " , False ,"center", ("Courier", 24, "bold") )

