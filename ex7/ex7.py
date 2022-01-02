
#################################################################
# FILE : ex7.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex7 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

from ex7_helper import *
from typing import Any


#######################################################################################################################


def mult(x: float, y: int) -> float:
    """a function that recieves a float parameter and an int parameter and
        returns their multiplication in a float variable using recursion
        :param: a flot containing the firt number
        :param: an int containing the second number
        :returns: the result of the multiplication between the two given numbers"""
    if y == 0:
        return 0
    return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    """ a function that receives an int variable contiang a number and
        checks if it is an even number
        :param: an int containing a natural number
        :returns: true if the given number is even and false if otherwise"""
    if n == 0:
        return True
    if subtract_1(n) == 0:
        return False
    n = subtract_1(n)
    n = subtract_1(n)
    return is_even(n)


def log_mult(x: float, y: int) -> float:
    """a function receives a float type containing a number
       and an int type containg number and the returns the result
       of the multiplication between the two numbers in log(n) runtime complexity
       :param: a float containing a number
       :param: an int containing a number
       :returns: the result of the multiplication between the two numbers"""
    if x == 0 or y == 0:
        return 0
    divided_y = divide_by_2(y)
    if y == 1:
        return x
    divided_log_mult = log_mult(x, divided_y)
    if is_odd(y):
        return add(divided_log_mult, add(x, divided_log_mult))
    else:
        return add(divided_log_mult, divided_log_mult)


def is_power(b: int, x: int) -> bool:
    """a function that receives as input two int types containing numbers
       nd checks whether there exist a natural n such that
       the first number to the power of n equals to the second number
       :param: an int containing the first number
       :param: an int containing the  second numbe
       :returns: true if the second number equals to the first number
       to the power of n and false if otherwise"""
    if (b == 0 and x != 0) or (b != 0 and x == 0):
        return False
    if b == 1 and x != 1:
        return False
    if x == 1:
        return True
    return is_power_core(1, b, x)


def is_power_core(n: int, b: int, x: int) -> bool:
    """the recursive core function for the is_power function
        note: this recursive core function deosn't check the base cases
       :param: an int type that contains the recursion parameter
       :param: an int type that contains the first number
       :param: an in type that contains the second number
       :return::true if the second number equals to the first number
       to the power of n and false if otherwise """
    if n == x:
        return True
    if n >= x:
        return False
    return is_power_core(int(log_mult(n, b)), b, x)


def reverse(s: str) -> str:
    """ a function that receives a string and returns the same string revered
        :param: a string containing the string that is to be reversed
        :returns: a string containing the original string reversed"""
    return reverse_core(s, "")


def reverse_core(s: str, reverse_s: str) -> str:
    """ a recursive core function the reverse function
    :param: a string containing the string that is to be reversed
    :param: a string that the function add characters of the original string to
    :returns: a string containg the reversed string of the original string"""
    if add(len(s), -len(reverse_s)) == 0:
        return reverse_s
    reverse_s = append_to_end(reverse_s, s[subtract_1(int(add(len(s),-len(reverse_s))))])
    return reverse_core(s, reverse_s)


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """ a functions that solves the hanoi tower puzzle using the hanoi_game colass
        :param: Any type param for the use of the hanoi_game class
        :param: an int containg the number of levels in the begining of the game
        :param: Any type containing the pole that all of the discs are in
        :param: Any type containg the pole which the discs are to be moved to
        :param: Any type containg the third pole in the game"""
    if n == 0:
        return None
    if n == 1:
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)
    else:
        play_hanoi(hanoi, n-1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n-1, temp, dst, src)


def num_of_one_digits(n: int) -> int:
    """ a function that recevies an int type number
        and returns the amount of '1' digits it contains
        without using string class function
        :param: an int type containing the number
        :returns: an int type containg the amount of '1' digits
                  the original number contains"""
    count_ones = 0
    while n != 0:
        count_ones += 1 if n % 10 == 1 else 0
        n //= 10
    return count_ones


def number_of_ones(n: int) -> int:
    """a function that receives an int type containing a number
       and counts the amount of '1' digits from the one to
       the the given number
       :param: an int containing a natural number
       :returns: an int the amount of '1' digits between one and the given  umber"""
    if n <= 0:
        return 0
    return num_of_one_digits(n) + number_of_ones(subtract_1(n))


def compare_lists(l1: list[int], l2: list[int], column: int) -> bool:
    """a recursive function that checks whether the lists are identical
       note: this function doesn't check the length of the lists
       :param: a list containing int types
       :param: a list containing int types
       :param: an int that will be used as the recursion parameter
       :returns: true if the lists are identical and false if otherwise"""
    if column < 0:
        return True
    if l1[column] != l2[column]:
        return False
    return True and compare_lists(l1, l2, subtract_1(column))


def compare_2d_lists_core(l1: list[list[int]], l2:  list[list[int]], row: int) -> bool:
    """a recursive core function for compare_2d_lists_core
       note: this function doesn't check the length of the two dimensional lists
       :param: a two dimensional list containing int types
       :param: a two dimensional list containing int types
       :param: an int type that will be used as the recursion parameter
       :returns: true if the lists are identical and false if otherwise"""
    if row < 0:
        return True
    if len(l1[row]) != len(l2[row]):
        return False
    column = len(l1[row])
    return compare_lists(l1[row], l2[row], subtract_1(column)) and compare_2d_lists_core(l1, l2, subtract_1(row))


def compare_2d_lists(l1: list[list[int]], l2: list[list[int]]) -> bool:
    """a function that checks whether two 2d lists are the identical
       :param: a two dimensional list containing int types
       :param: a two dimensional list containing int types
       :returns: true if the lists are identical and false if otherwise"""
    if len(l1) != len(l2):
        return False
    row = len(l1)
    return compare_2d_lists_core(l1, l2, subtract_1(row))


def magic_list(n: int) -> list[Any]:
    """ a function that receives an int type as param
        and creates and returns a magic list with the length of the given number
        according to the specifications in ex7- question 9
        :param: an int type containing the length of the list that is to be created
        :returns: a list containing a magic list with the length of the given num"""
    if n == 0:
        return []
    lst = [magic_list(subtract_1(n))]
    return combine_lists(magic_list(subtract_1(n)), lst, n)


def combine_lists(l1: list[Any], l2: list[Any], n: int) -> list[Any]:
    """a recursive function that appends to one list
       the cells with an index the the exceeds the length of
       the original list but is lower than n
       :param: a list containing Any types
       :param: a list containing Any types
       :param: an int containing the index of the cells that are to be added
       :retruns: the combined lists according to the parameters"""
    if n <= len(l1):
        return l1
    l1.append(l2[0])
    return combine_lists(l1, l2, subtract_1(n))


if __name__ == "__main__":
    pass
