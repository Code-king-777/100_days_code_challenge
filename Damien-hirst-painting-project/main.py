import random
import colorgram as cg
from turtle import Turtle,getscreen
# colour =  cg.extract('Damien-Hirst-Ellipticine-2007-White-Frame.jpg',108)
#
#
# rgb_colours = []
# for color in colour:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r,g,b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)


tim = Turtle()
screen = getscreen()
screen.colormode(255)
colour_list = [(229, 238, 249), (173, 71, 45), (27, 33, 65), (243, 233, 71), (56, 87, 147), (220, 139, 92), (51, 38, 30), (132, 32, 47), (126, 160, 208), (224, 80, 52), (210, 82, 124), (41, 49, 128), (139, 33, 26), (148, 55, 76), (63, 30, 39), (88, 111, 206), (125, 183, 133), (33, 48, 39), (197, 135, 158), (73, 76, 40), (70, 106, 56), (164, 187, 238), (154, 138, 68), (41, 76, 59), (241, 161, 152), (227, 171, 187), (156, 202, 220), (40, 78, 81), (246, 230, 3), (111, 162, 85), (172, 206, 180), (83, 142, 163)]


#
tim.pensize(10)
# tim_position = tim.pos()


tim.hideturtle()
x = 0
y = 0


tim.speed("fastest")
for nm in range(10):
    tim.hideturtle()
    tim.penup()
    tim.setposition(x - 200, y - 200)
    tim.pendown()
    m = 0
    while m < 10 :
        m += 1
        new_colours = random.choices(colour_list)
        tim.color(new_colours[0])
        tim.circle(4)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    y += 50

screen.exitonclick()
