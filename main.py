# import colorgram
#
# colors = colorgram.extract('image.jpg', 100)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random as r

t.colormode(255)
pointer = t.Turtle()
pointer.pensize(200)
pointer.hideturtle()
pointer.speed(0)

color_list = [(198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5),
              (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10),
              (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61),
              (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169),
              (78, 234, 201), (50, 234, 244), (3, 66, 40), (222, 86, 44), (174, 178, 231), (5, 246, 222), (251, 7, 48),
              (235, 169, 164), (10, 80, 111), (14, 51, 246), (244, 14, 14)]

# pointer.setposition(-440,-300)

pointer.penup()

y = -300
for _ in range(16):
    pointer.setposition(-380, y)
    y += 40

    for _ in range(14):
        pointer.penup()
        pointer.color(r.choice(color_list))
        pointer.forward(50)
        pointer.dot(20)




screen = t.Screen()
screen.exitonclick()
