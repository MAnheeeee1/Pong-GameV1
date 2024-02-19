from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle = Turtle("square")
scoreboard_l = Scoreboard("left")
scoreboard_r = Scoreboard("right")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()
screen.update()
screen.listen()
screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")
screen.onkey(fun=l_paddle.paddle_up, key="w")
screen.onkey(fun=l_paddle.paddle_down, key="s")



game_is_on = True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    #Detect collison with paddle
    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    elif game_ball.xcor() > 380 or game_ball.xcor() < -380:
        if game_ball.xcor() > 380:
            #Reset game with ball boucning toward left
            print("Hit right border")
            game_ball.goto(0,0)
            game_ball.bounce_x()
            game_ball.move_speed = 0.1
            game_ball.move()
            scoreboard_l.l_score += 1
            scoreboard_l.update_board("left")
        elif game_ball.xcor() < -380:
            print("Hit left border")
            game_ball.goto(0, 0)
            game_ball.x_move *= -1
            game_ball.move_speed = 0.1
            game_ball.move()
            scoreboard_r.r_score += 1
            scoreboard_r.update_board("right")
            #Reset game with ball bounxing toward right




screen.exitonclick()

