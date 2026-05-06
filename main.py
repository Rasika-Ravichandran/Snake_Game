from turtle import Turtle,Screen
from Snake import Snake
cutie = Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
cutie.penup()
snake = Snake()

snake.sna_move()




screen.exitonclick()

