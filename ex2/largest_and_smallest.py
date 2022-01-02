#################################################################
# FILE : largest_and_smallest.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: a simple program that returns the largest and smallest number out of a series of three numbers
#               and checks its own functionality
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: in the function "check_largest_and_smallest" i chose the inputs
#       (1, 6, 17)->(17, 1) to determine if the order of the parameters
#       doesn't affect the function and (-1,0,-3)->(0, -3)
#       to determine the function works on negative numbers

#################################################################


def largest_and_smallest(parameter1, parameter2, parameter3):
    """ a function that receives three parameters and
        returns the largest and smallest of the three"""
    largest_value = parameter1
    smallest_value = parameter2
    if parameter1 < parameter2:
        largest_value = parameter2
        smallest_value = parameter1
    if parameter3 > largest_value:
        largest_value = parameter3
    elif parameter3 < smallest_value:
        smallest_value = parameter3
    return largest_value, smallest_value


def check_largest_and_smallest():
    """ a function that checks the functionality
        of the largest and smallest function """
    check_correctness = True
    if largest_and_smallest(17, 1, 6) != (17, 1):
        check_correctness = False
    elif largest_and_smallest(1, 17, 6) != (17, 1):
        check_correctness = False
    elif largest_and_smallest(1, 1, 2) != (2, 1):
        check_correctness = False
    elif largest_and_smallest(1, 6, 17) != (17, 1):
        check_correctness = False
    elif largest_and_smallest(-1, 0, -3) != (0, -3):
        check_correctness = False
    return check_correctness

