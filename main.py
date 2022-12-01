from turtle import *
from Paddle import *
from ball import Ball
from time import *
ball=Ball()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
screen.exitonclick()
