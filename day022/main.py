from turtle import Turtle, Screen
from paddle import Paddle

turtle = Turtle()
screen = Screen()
# paddle = Paddle()

screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setpos(350, 0)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(fun=up, key="Up")
    screen.onkey(fun=down, key="Down")

screen.exitonclick()
