# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()
drawing = open("drawing.txt", "r")

text = drawing.read()
coords = text.split("\n")
del coords[-1]

for i in range(len(coords)):
    if(coords[i] == "UP"):
        t.penup()
    elif(coords[i] == "DOWN"):
        t.pendown()
    else:
        point = coords[i].split()
        t.goto(int(point[0]), int(point[1]))

drawing.close()

# wait
turtle.Screen().exitonclick()