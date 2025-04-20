from turtle import getscreen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = getscreen()


screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("black")
screen.title("Pong-game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.y_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -335 or ball.distance(r_paddle) < 50 and ball.xcor() > 335:
        ball.x_bounce()



    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()