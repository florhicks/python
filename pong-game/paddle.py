import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.goto(x_position, 0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.y_position=self.ycor()

    def move_up(self):
        self.y_position= self.ycor()+20
        self.goto(self.xcor(),self.y_position)

    def move_down(self):
        self.y_position = self.ycor() - 20
        self.goto(self.xcor(), self.y_position)