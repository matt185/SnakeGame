import time
from turtle import Screen
from components.snake import Snake
from components.food import Food
from components.score_board import Scoreboard

# create the game board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create game element
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# set the snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    # detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # detect collision with the body

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
