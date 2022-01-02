#################################################################
# FILE : math_print.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that prints: the golden ratio,
#               6 to the power of 2, the value of pi, the value of e,
#               and the surface area of squares with sides the length of 1 to 10.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################

import math


def golden_ratio():
    # a function that prints out the golden ratio using the math class
    print(float((1+math.sqrt(5))/2))


def six_squared():
    # a function that prints out 6 to the power of 2 using the math class.
    print(int(math.pow(6, 2)))


def hypotenuse():
    # a function that prints out the value of the hypotenuse
    # in a right triangle with the sides of 5 and 12.
    print(math.sqrt(math.pow(5, 2) + math.pow(12, 2)))


def pi():
    # a function that prints out the value of pi
    print(math.pi)

def e():
    # a function that prints out the value of e
    print(math.e)


def squares_area():
    # a function that prints out the area of squares with the sides of 1 to 10.
    area_output = ""
    for index in range(1, 11):
        # a for loop that uses its index to the power of 2 in order to
        # calculate the area of the squares
        area_output += str(int(math.pow(index,2))) + " "
    print(area_output[:len(area_output)-1])  # prints out area_output string without the last space


if __name__ == "__main__":
    # calling each function
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()


