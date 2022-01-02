#################################################################
# FILE : hello_turtle.py
# WRITER : Gaberiel Dubin, dubingabie , 209386481
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that prints 3 adjacent
#                                   flowers using the turtle package
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import turtle


def draw_petal():
    # a function that draws a deltoid shaped petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    # a functions that draws a flower made up from 4 petals and a stem
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    # a function that calls up the draw_flower function
    # and moves in position to draw the next flower
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    # a function that draws 3 adjacent flowers using draw_flower_and_advance
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    for index in range(0,3):
        # a for loop that is used instead of repeating the code 3 times
        draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()

