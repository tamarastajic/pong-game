from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# ~~~~~~~~~~~~~ Needed Functions ~~~~~~~~~~~~~
def reset_position():
    """Resets the position of the ball and paddles."""
    ball.reset_position()
    l_paddle.reset_position()
    r_paddle.reset_position()


def write_score():
    """Writes the current score on the screen."""
    score.write_score(l_paddle.score, r_paddle.score, game_screen)


# ~~~~~~~~~~~~~ Creating Screen, Scoreboard and Ball ~~~~~~~~~~~~~
game_screen = Screen()
game_screen.tracer(0)

score = ScoreBoard()

ball = Ball()

# ~~~~~~~~~~~~~ Setting up the game screen ~~~~~~~~~~~~~
game_screen.screensize(canvheight=600, canvwidth=800)
game_screen.bgcolor("black")
game_screen.title("My Pong Game")

# ~~~~~~~~~~~~~ Placing Paddles ~~~~~~~~~~~~~
r_paddle = Paddle(x_location=450, y_location=0)
l_paddle = Paddle(x_location=-450, y_location=0)

game_screen.update()

# ~~~~~~~~~~~~~ Game Loop ~~~~~~~~~~~~~
while True:
    # Listening to certain key inputs
    game_screen.listen()
    game_screen.onkey(key="W", fun=l_paddle.move_up)
    game_screen.onkey(key="S", fun=l_paddle.move_down)
    game_screen.onkey(key="Up", fun=r_paddle.move_up)
    game_screen.onkey(key="Down", fun=r_paddle.move_down)

    # Moving the ball
    ball.move(game_screen)
    time.sleep(ball.move_speed)

    # Showing the current score.
    write_score()

    # Checking if there was a collision with the top or bottom wall.
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Checking if there was a collision with the paddles.
    if ball.distance(r_paddle) < 75 and ball.xcor() > 420 or ball.distance(l_paddle) < 75 and ball.xcor() < -420:
        ball.bounce_x()

    # Detecting if the ball went out of bounds and who got points.
    if ball.xcor() > 430:
        l_paddle.score += 1
        reset_position()
    elif ball.xcor() < -430:
        r_paddle.score += 1
        reset_position()

    # Showing the new score.
    write_score()
    game_screen.update()

    # Exiting if score is 100.
    if l_paddle.score == 100 or r_paddle.score == 100:
        break

game_screen.exitonclick()
