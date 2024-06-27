import turtle
from turtle import Turtle, Screen


class Wall(Turtle):
    def __init__(self, i):
        super().__init__()
        self.wall = Turtle(shape='square')
        self.wall.color('brown')
        self.wall.penup()
        self.x = i

    def up_wall(self, i):
        self.wall.goto(i * 20, 280)

    def down_wall(self, i):
        self.wall.goto(i * 20, -300)

    def left_wall(self, i):
        self.wall.goto(-300, i * 20)

    def right_wall(self, i):
        self.wall.goto(280, i * 20)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('HighScoreTrack.txt', mode='r') as file:
            content = file.read(7)
            self.high_score = int(content)
        self.color('white')
        self.penup()
        self.goto(x=-180, y=290)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open('HighScoreTrack.txt', mode='w') as file:
            file.write(str(self.high_score))



   # def game_over(self):
    #    self.goto(0, 0)
     #   self.write(f"GAME OVER", False, align="center", font=("Arial", 15, "normal"))
