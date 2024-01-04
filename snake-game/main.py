import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
scoreboard = Scoreboard()


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food ( .distance puede ser usado con una instancia de turtle)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
        scoreboard.score_counter()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset()


    # detect collision with tail, if head collides with any segment in the tail, game over
    for part in snake.snake[1:]:
        if snake.head.distance(part)< 10:
            scoreboard.reset_scoreboard()
            snake.reset()


screen.exitonclick()