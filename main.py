from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

PUM = 16

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
food.choose_location()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.10)
    snake.move()

    if snake.head.distance(food) < PUM:
        food.choose_location()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



















screen.exitonclick()
