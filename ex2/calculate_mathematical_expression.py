#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: a program that can calculate the result of a simple mathematical
#               using string input or parameter input
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def calculate_mathematical_expression(first_number, second_number,
                                      operand, result=None):
    """ a function that receives number type parameters
        and a string type that contains a mathematical operand
        (+,-,*,:) and then calculates the mathematical expressions created by
        the first parameter , the operand and the second number and returns it"""
    if operand == "*":
        result = first_number * second_number
    elif operand == ":" and second_number != 0:
        result = first_number / second_number
    elif operand == "+":
        result = first_number + second_number
    elif operand == "-":
        result = first_number - second_number
    return result


def calculate_from_string(expression):
    """a function that receives a string type parameter
    that contains a mathematical expression and separates it using the split function
    and calls upon the "calculate_mathematical_expression" function
     with the parameters contained in the string and returns the result"""
    word_list = expression.split(" ", -1)  
    return calculate_mathematical_expression(float(word_list[0]),
                                             float(word_list[2]),
                                             word_list[1])

