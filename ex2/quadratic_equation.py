
#################################################################
# FILE : quadratic_equation.py
# WRITER : Gaberiel Dubin, dubingabie , 209386481
# EXERCISE : intro2cse ex2 2021`
# DESCRIPTION: A simple program that calculates the value of
#               of a quadratic equation
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
#################################################################
import math


def quadratic_equation(a, b, c):
    """ a functions that receives the coefficients of a quadratic equation
        and returns the solution or solutions of that equation using the root formula"""
    first_root = None
    second_root = None
    delta = (b**2) - (4*a*c)
    if delta == 0:
        first_root = -b / (2*a)
    elif delta > 0:
        delta = math.sqrt(delta)
        first_root = (-b + delta) / (2*a)
        second_root = (-b - delta) / (2*a)
    return first_root, second_root


def quadratic_equation_user_input():
    """ a function that receives three coefficients of a quadratic equation from the user
        calls the "quadratic_equation" function with those coefficients as parameters and prints out
        to the user the solution or solutions """
    coefficients_list = input("Insert coefficients a, b, and c: ").split(" ", -1)
    if int(coefficients_list[0]) == 0:
        print("The parameter 'a' may not equal 0")
    else:
        roots = quadratic_equation(float(coefficients_list[0]),
                                   float(coefficients_list[1]), float(coefficients_list[2]))
        if roots[0] is not None and roots[1] is not None:
            print(f"The equation has 2 solutions: {roots[0]} and {roots[1]}")
        elif roots[0] is not None and roots[1] is None:
            print(f"The equation has 1 solution: {roots[0]}")
        else:
            print("The equation has no solutions")




