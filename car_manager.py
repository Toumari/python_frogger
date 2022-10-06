COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.up()
        self.shapesize(1,2.5)
        self.color(random.choice(COLORS))
        self.goto(random.randint(260, 1000),random.randint(-220, 250))
        self.speed = 0.1
        self.move()
    
    def move(self):
        self.setheading(180)
        self.forward(MOVE_INCREMENT)
        if self.xcor() < -320:
            self.clear()
            self.goto(random.randint(260,1000), random.randint(-220, 250))


    def increase_difficulty(self):
        self.speed *= 0.9