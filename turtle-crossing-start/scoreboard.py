
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("pink")
        self.goto(-200, 250)
        self.level = 1
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"PLAYER, YOUR GAME IS NOW OVER", align="center", font=FONT)









