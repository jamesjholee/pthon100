import colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('download.jpeg', 25)
for color in colors:
    rgb_colors.append(color.rgb)

for rgb in rgb_colors:
    new_colors = rgb[0], rgb[1], rgb[2]
    rgb_colors.append(new_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = rgb_colors
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()