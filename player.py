STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.color('green')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def move(self):
        print("Moving")
        self.forward(MOVE_DISTANCE)
        
    def reset_player(self):
        self.goto(STARTING_POSITION)
    
