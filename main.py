import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

sb = Scoreboard()

carList = []

for _ in range(30):
    car_manager = CarManager()
    carList.append(car_manager)



screen.listen()

screen.onkey(player.move, "w")



game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed)
    for i in carList:
        i.move()

    for i in carList:
        if player.distance(i) < 20:
            print("Collision")
            sb.game_over()
            game_is_on = False
    
    if player.ycor() > 280:
        print("Level complete")
        sb.next_level()
        player.reset_player()
    
    screen.update()
    
screen.exitonclick()
