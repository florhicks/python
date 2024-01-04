from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)


    def add_part(self,position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake.append(snake_part)

    def extent(self):
        self.add_part(self.snake[-1].position())

    def move(self):
        for part_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_number - 1].xcor()
            new_y = self.snake[part_number - 1].ycor()
            self.snake[part_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for part in self.snake:
            part.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
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

