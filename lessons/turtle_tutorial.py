"""Turtle Tutorial"""

__author__ = "730656260"

from turtle import  Turtle, colormode, done
leo: Turtle = Turtle() 
colormode(255)
leo.speed(50)
leo.hideturtle()
leo.color(99,204,250)
leo.begin_fill()
leo.penup()
leo.goto(-150,-40)
leo.pendown()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()
bob.color(0,0,0)
bob.speed(75)
bob.penup()
bob.goto(-150,-40)
bob.pendown()

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

bob.color(0,0,0)
bob.speed(75)
bob.penup()
bob.goto(-150,-40)
bob.pendown()

side_length2: int = 300 * 0.97

i: int = 0
while (i < 55):
    bob.forward(side_length2)
    bob.left(120)
    i = i + 1




done()