from turtle import getscreen
from snake import Snake
from food import Food
from score import Score
import time

screen = getscreen()
screen.bgcolor("black")
screen.screensize(canvwidth=600,canvheight=600)
screen.title("snake_game_by_satya")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        score.reset_score()
        snake.reset()


    for segment in snake.snakes[1:]:
        if segment == snake.head:
            pass

        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()










screen.exitonclick()