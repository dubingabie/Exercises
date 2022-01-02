
#################################################################
# FILE : shapes.py
# WRITER : Gaberiel Dubin, dubingabie , 209386481
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: the calculates the surface area of three different shapes
#               a triangle, a rectangle and a circle.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import math


def circle_area():
    """ a function that receives the length of radius of a circle
        from the user as keyboard input and calculates its
        surface area """
    radius = float(input())
    return math.pi * (radius**2)


def rectangle_area():
    """ a function that receives the length of the two sides of a
        rectangle from the user as keyboard input
        and calculates and returns its surface area """
    a_side = float(input())
    b_side = float(input())
    return a_side * b_side


def triangle_area():
    """ a function that receives the length of a side of an even sided
        triangle from the user as keyboard input and calculates
        and returns its surface area """
    side = float(input())
    return ((3**0.5)/4)*(side**2)


def shape_area():
    """ a function that lets the user chose the area of which shape he wants to calculate
        (a circle, a rectangle or a triangle) and calls upon the relevant function
        that calculates the surface area of each shape and then returns the area of the shape  """
    shape_parameter = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    area = None
    if shape_parameter == 1:
        area = circle_area()
    elif shape_parameter == 2:
        area = rectangle_area()
    elif shape_parameter == 3:
        area = triangle_area()
    return area
