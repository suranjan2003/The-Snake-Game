# the snake game

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Wall
import time


screen = Screen()
screen.setup(600, 630)
image = 'graSS.gif'
screen.bgpic(image)
#screen.bgcolor('black')
screen.title('my snake game')
screen.tracer(0)

for i in range(-14, 14):
    wall = Wall(i)
    wall.up_wall(i)
    wall = Wall(i)
    wall.down_wall(i)

for i in range(-15, 15):
    wall = Wall(i)
    wall.left_wall(i)
    wall = Wall(i)
    wall.right_wall(i)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

move_move = True
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while move_move:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # eat food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # if snake hits the wall
    if snake.head.xcor() > 260 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.all_cobras:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()