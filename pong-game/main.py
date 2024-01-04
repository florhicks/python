from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key= "Up")
screen.onkeypress(fun=l_paddle.move_down, key= "Down")
screen.onkeypress(fun=r_paddle.move_up, key= "w")
screen.onkeypress(fun=r_paddle.move_down, key= "s")

game_is_on = True



while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()
    if (ball.distance(l_paddle)<50 or ball.distance(r_paddle) < 50) and (ball.xcor() < 345 or ball.xcor() > -345):
        ball.bounce_X()


    if ball.xcor()>380:
        ball.restart()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()