from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("GT's Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# map keys to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision if head collides with any segment of tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
