from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1500, height=700)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Paddle(-730, 0)
r_paddle = Paddle(730, 0)
r_paddle.speed("fastest")
l_paddle.speed("fastest")

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

count_user1 = 0
count_user2 = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    if count_user1 == 3:
        scoreboard.winner_user1()
        break
    elif count_user2 == 3:
        scoreboard.winner_user2()
        break

    ball.move()

    # Detect collision with ball
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 725 or ball.distance(l_paddle) < 50 and ball.xcor() < -725:
        ball.bounce_paddle()

    # Detect collision with wall
    if ball.xcor() > 740:
        scoreboard.user_1()
        count_user1 += 1
        print(count_user1)
        ball.reset_position()

    elif ball.xcor() < -740:
        scoreboard.user_2()
        count_user2 += 1
        print(count_user2)
        ball.reset_position()

screen.exitonclick()
