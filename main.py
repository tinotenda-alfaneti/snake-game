from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import sys
import pygame
from pygame import mixer
import time

screen = Screen()
# initializing and playing sound
pygame.init()
mixer.music.load("music/background.wav")
mixer.music.play(-1)


def game():

    screen.setup(width=600, height=600)
    screen.bgcolor("blue")
    screen.title("Atarist Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    #Level selection
    level = screen.textinput("LEVEl SELECTION", "Enter the level you want. (H/M/E): ")
  
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        if level.title() == "E":
            time.sleep(0.7)
        elif level.title() == "M":
            time.sleep(0.3)
        if level.title() == "H":
            time.sleep(0.1)
        snake.move()

        # Detect distance
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                game_is_on = False
                scoreboard.game_over()


game()

end = False
while not end:
    option = screen.textinput("Game Over", "Do you want to RESTART? (y/n): ")
    if option == "y":
        screen.clear()
        game()
    else:
        end = True
        sys.exit()


screen.exitonclick()
