

import turtle
# Create screen once
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(300, 400)
polygon = turtle.Turtle()
number_of_sides = 6
side_length = 70
angle = 360 / number_of_sides
for i in range(number_of_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()


import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
number_of_sides = 6
side_lenght = 70
angle = 360.0/number_of_sides

for i in range(number_of_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()