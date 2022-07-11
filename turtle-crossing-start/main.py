import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")


car_manager= CarManager()


scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.car_move()
    scoreboard.update_level()

    # detect collusion with cars
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            screen.update()
            scoreboard.game_over()

    # detect hitting the egde
    if player.ycor() >= 290:
        player.goto(0, -280)
        scoreboard.level += 1
        car_manager.speed_up()






screen.exitonclick()
