from turtle import Turtle,Screen
import time
from food import Food
from Score import Score

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.score = Score()
        self.food = Food()
        self.snake_body = []
        self.screen = Screen()
        self.screen.tracer(0)
        x=0
        for i in range(3):
            box = Turtle("square")
            box.up()
            box.color("white")
            box.goto(x,0)
            x-=20
            self.snake_body.append(box)
        self.screen.listen()
    def move_up(self):
        if self.snake_body[0].heading()!=DOWN:
            self.snake_body[0].setheading(UP)
    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
    def add_body(self,x,y):
        box = Turtle("square")
        box.up()
        box.color("white")
        box.goto(x,y)
        self.snake_body.append(box)
    def extend_snake(self):
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.add_body(x,y)

    def sna_move(self):
        game_continue = True
        while game_continue:
            self.screen.update()
            time.sleep(0.1)
            for j in range(len(self.snake_body)-1,0,-1):
                x_position = self.snake_body[j-1].xcor()
                y_position = self.snake_body[j-1].ycor()
                self.snake_body[j].goto(x_position,y_position)
            self.screen.onkey(self.move_up,"Up")
            self.screen.onkey(self.move_down,"Down")
            self.screen.onkey(self.move_left,"Left")
            self.screen.onkey(self.move_right,"Right")
            self.snake_body[0].forward(20)
            if self.snake_body[0].distance(self.food) < 15:
                self.extend_snake()
                self.score.increase_score()
                self.food.refresh()
            if self.snake_body[0].xcor() > 280 or self.snake_body[0].xcor() < -280 or self.snake_body[0].ycor() > 280 or self.snake_body[0].ycor() < -280:
                self.score.game_over()

                game_continue = False
            for _ in self.snake_body[1:]:
                if self.snake_body[0].distance(_) < 10:
                    self.score.game_over()
                    game_continue = False