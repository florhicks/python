from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("pink")
        self.goto(0, 0)
        self.direction = 1
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        # if self.ycor() > 290 or self.ycor() < -290:
        #     self.bounce_Y()
        # if self.xcor() > 390 or self.xcor() < -390:
        #     self.bounce_X()
        y_position = self.ycor() + self.y_move
        x_position = self.xcor() + self.x_move
        self.goto(x_position, y_position)

    def bounce_Y(self):
        self.y_move *= -1

    def bounce_X(self):
        self.x_move *= -1
        self.ball_speed *=0.9

    def restart(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_X()
