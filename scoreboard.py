FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.up()
        self.hideturtle()
        self.goto(-200,240)
        self.write(f"Level {self.level}", align="center",font=FONT)
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font=FONT)
    
    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-200,240)
        self.write(f"Level {self.level}", align="center",font=FONT)
