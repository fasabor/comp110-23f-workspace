"""A Pokeball with stars that appear randomly."""

__author__ = "730656260"

from turtle import Turtle, done
import random


def main() -> None:
    """Main function that calls upon the other ones to create a scene."""
    pb: Turtle = Turtle()
    pb.speed(50)
    pb.hideturtle()
    draw_background(pb, "orange")
    white_circle(pb, 0, -200, 200)
    red_semi_circle(pb, 200, 0, 200)
    middle_circle1(pb, 0, 50, 50)
    middle_circle2(pb, 0, 25, 25)
    middle_lines(pb, 50, 0)
    random_star(pb)
    done()


def white_circle(pb: Turtle, x: float, y: float, radius: float) -> None:
    """Function that creates the baseline white circle."""
    pb.penup()
    pb.pensize(3)
    pb.color("black", "white")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.circle(radius)
    pb.end_fill()


def red_semi_circle(pb: Turtle, x: float, y: float, radius: float) -> None:
    """Function that creates the red semi circle to create the bottom half of the image."""
    pb.penup()
    pb.pensize(3)
    pb.color("black", "red")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.left(90)
    pb.circle(radius, 180)
    pb.right(90)
    pb.end_fill()


def middle_circle1(pb: Turtle, x: float, y: float, radius: float) -> None:
    """Function that creates the outer middle circle that has a ridge for the button."""
    pb.penup()
    pb.pensize(10)
    pb.color("black", "white")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.circle(radius)
    pb.end_fill()


def middle_circle2(pb: Turtle, x: float, y: float, radius: float) -> None:
    """Function that creates the 2nd middle circle, 'aka', the button."""
    pb.penup()
    pb.pensize(5)
    pb.color("black", "white")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.circle(radius)
    pb.end_fill()


def left_line(pb: Turtle, x: float, y: float) -> None:
    """Function that creates the black middle line crease for opening on the left side."""
    pb.penup()
    pb.pensize(10)
    pb.color("black")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.forward(150)
    pb.end_fill()


def right_line(pb: Turtle, x: float, y: float) -> None:
    """Function that creates the black middle line crease for opening on the right side."""
    pb.penup()
    pb.pensize(10)
    pb.color("black")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    pb.backward(150)
    pb.end_fill()    


def middle_lines(pb: Turtle, x: int, y: int) -> None:
    """Function that calls both the left and right line functions to create the middle line."""
    left_line(pb, -x, 0)
    right_line(pb, x, 0)


def draw_background(pb: Turtle, color: str) -> None:
    """Function that creates the background for the scene."""
    pb.speed(0)
    pb.penup()
    pb.goto(-800, 450)
    pb.pendown()
    pb.color(color)
    pb.begin_fill()
    i: int = 0
    while (i < 4):
        if i % 2 == 0:
            pb.forward(2000) 
            pb.right(90)
        else:
            pb.forward(2000) 
            pb.right(90)
        i += 1
    pb.end_fill()
   

def draw_star(pb: Turtle, x: float, y: float, size: float) -> None:
    """Function that draws a star on the scene."""
    pb.penup()
    pb.pensize(3)
    pb.color("yellow")
    pb.goto(x, y)
    pb.pendown()
    pb.begin_fill()
    s: int = 0
    while (s < 5):
        pb.forward(size)
        pb.right(-144)
        s += 1
    pb.end_fill()


def random_star(pb: Turtle) -> None:
    """Function that randomly makes one star out of three appear."""
    z: float = random.randrange(1, 4)
    if z == 1:
        draw_star(pb, 50, 275, 100)
    elif z == 2:
        draw_star(pb, 250, 225, 100)
        draw_star(pb, -150, 225, 100)
    elif z == 3:
        draw_star(pb, 50, 275, 100)
        draw_star(pb, -150, 225, 100)
        draw_star(pb, 250, 225, 100)


if __name__ == "__main__":
    main()