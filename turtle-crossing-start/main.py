import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
score = Scoreboard()

screen.setup(width=800, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    player.move()
    car.create_car()
    car.move()

    if player.ycor() > 270:
        player.reset_position()
        score.point()
        car.update_speed()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False




screen.exitonclick()