from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
screen.colormode(255)

direction = [0, 90, 180, 270]

# for i in range(3, 11):
#     angle = 360 / i
#     tim.color(randint(0, 255),
#               randint(0, 255),
#               randint(0, 255))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)
# tim.pensize(10)
tim.speed("fastest")
setheading = 5
for _ in range(int(360 / 5)):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    tim.circle(100)
    tim.setheading(setheading)
    setheading += 5

screen.exitonclick()
