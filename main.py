
# import colorgram
#
# # Extract 30 colors from an image.
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors. append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(201, 10, 34), (239, 244, 251), (247, 236, 36), (240, 230, 3), (224, 159, 59), (37, 216, 72), (40, 79, 183), (28, 39, 158), (210, 74, 17), (17, 153, 18), (240, 37, 151), (188, 14, 9), (70, 8, 28), (219, 22, 127), (220, 138, 200), (58, 13, 8), (222, 157, 6), (11, 97, 61), (71, 196, 223), (16, 14, 43), (73, 74, 218), (236, 159, 217), (85, 208, 157), (10, 228, 238), (103, 232, 190), (213, 79, 55), (4, 71, 43)]

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