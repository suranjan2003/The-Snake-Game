
from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_cobras = []
        self.create_snake()
        self.head = self.all_cobras[0]

    def create_snake(self):
        for snake_index in positions:
            self.grow_tail(snake_index)

    def reset(self):
        for i in self.all_cobras:
            i.goto(2000, 2000)
        self.all_cobras.clear()
        self.create_snake()
        self.head = self.all_cobras[0]

    def grow_tail(self,snake_index):
        cobra = Turtle(shape='square')
        cobra.color('yellow')
        cobra.penup()
        cobra.goto(snake_index)
        self.all_cobras.append(cobra)

    def extend(self):
        self.grow_tail(self.all_cobras[-1].position())

    def move(self):
        for seg_num in range(len(self.all_cobras) - 1, 0, -1):
            new_x = self.all_cobras[seg_num - 1].xcor()
            new_y = self.all_cobras[seg_num - 1].ycor()
            self.all_cobras[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



