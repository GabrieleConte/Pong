from turtle import *
from Paddle import *
from ball import Ball
from time import *
from scoreboard import *
scoreboard=Scoreboard()
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
    sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
