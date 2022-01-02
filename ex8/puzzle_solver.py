
#################################################################
# FILE : puzzle_solver.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex8 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

from typing import List, Tuple, Set, Optional
from copy import deepcopy

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def get_range(picture: Picture, row: int, col: int, is_white: bool) -> Tuple[int,int,int,int]:
    """ this function calculates the beginning and the end of the seen cells
        from the specified cell in the picture
        :param: a picture type containing the a picture of the board
        :param: an int containing the row index of the current cell
        :param: an int containing the column index of the current cell
        :param: a bool type that specifies if the unknown cells are counted
                as white cells
        :returns: a tuple containing:
                  an int containing the row index of the start of the seen white cells sequence
                  an int containing the row index of the end of the seen white cells sequence
                  an int containing the column index of the start of the seen white cells sequence
                  an int containing the column index of the end of the seen white cells sequence"""
    row_start, row_end, col_start, col_end = 0, len(picture), 0, len(picture[0])
    for i_row in range(len(picture)):
        if i_row <= row and picture[i_row][col] == 0 or (picture[i_row][col] == -1 and not is_white):
            row_start = i_row + 1
        if i_row > row and picture[i_row][col] == 0 or (picture[i_row][col] == -1 and not is_white):
            row_end = i_row
            break
    for i_col in range(len(picture[0])):
        if i_col <= col and picture[row][i_col] == 0 or (picture[row][i_col] == -1 and not is_white):
            col_start = i_col + 1
        if i_col > col and picture[row][i_col] == 0 or (picture[row][i_col] == -1 and not is_white):
            col_end = i_col
            break
    return row_start, row_end, col_start, col_end


def get_seen_cells(row_start: int, row_end: int, col_start: int, col_end: int) -> int:
    """this functions calculates the amount of seen white cells from a certain cell and returns it
       :param: an int containing the row index of the start of the seen white cells sequence
       :param: an int containing the row index of the end of the seen white cells sequence
       :param: an int containing the column index of the start of the seen white cells sequence
       :param: an int containing the column index of the end of the seen white cells sequence
       :returns an int containing the amount of the seen white cells"""
    seen_cells = (row_end - row_start) + (col_end - col_start)
    if seen_cells == 0:
        seen_cells += 1
    else:
        seen_cells -= 1
    return seen_cells


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """ this function calculates the amount of seen white cells from the specified cell
        while counting the unknown cells as white
        :param: a picture type containing the a picture of the board
        :param: an int containing the row index of the current cell
        :param: an int containing the column index of the current cell
        :returns an int containing the amount of the seen white cells"""
    seen_cells = 0
    if picture[row][col] != 0:
        seen_cells = get_seen_cells(*get_range(picture, row, col, True))
    return seen_cells


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """ this function calculates the amount of seen white cells from the specified cell
        while not counting the unknown cells as white
        :param: a picture type containing the a picture of the board
        :param: an int containing the row index of the current cell
        :param: an int containing the column index of the current cell
        :returns an int containing the amount of the seen white cells"""
    seen_cells = 0
    if picture[row][col] == 1:
        seen_cells = get_seen_cells(*get_range(picture, row, col, False))
    return seen_cells


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """this function checks if the partial picture violates the constraints set
       :param: a picture containing the current partial picture of the board
       :param: a set containing tuples that specify the row , column and seen cells of each constraint
       :return: 0 if the constraints are violated outright
                1 if none of the constraints are violated
                2 if some of the constraints are not violated but are not kept outright"""
    check_value = 1
    for constraint in constraints_set:
        max_seen = max_seen_cells(picture, constraint[0], constraint[1])
        min_seen = min_seen_cells(picture, constraint[0], constraint[1])
        if max_seen < constraint[2] or constraint[2] < min_seen:
            check_value = 0
            break
        if max_seen == min_seen == constraint[2]:
            continue
        else:
            check_value = 2
    return check_value


def make_picture(n: int, m: int) -> Picture:
    """ this function makes a picture with n rows and m columns
        that is full of unkown cells
        :param: an int containing the amount of rows in the picture
        :param: an int containing the amount of columns in the picture
        :returns: a picture of the specified size full of unkown cells"""
    picture: Picture = list()
    for row in range(n):
        picture.append(list())
        for column in range(m):
            picture[row].append(-1)
    return picture


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """ this functions returns one possible solution of a puzzle of the given size and constraints
        :param: a set containing all of the constraints of the puzzle
        :param: an int containing the number of rows in the puzzle board
        :param: an int containing the number of columns in the puzzle board
        :returns: a possible solution to the puzzle of the given solutions and None if there are no solutions"""
    picture = make_picture(n, m)
    solution_list: list[Picture] = list()
    solve_puzzle_core(picture, constraints_set, 0, 0, solution_list)
    return solution_list[0] if len(solution_list) >= 1 else None


def solve_puzzle_core(picture: Picture, constraints_set: Set[Constraint],
                      i_row: int, i_col: int, solution_list: list[Picture]) -> None:
    """this functions adds all of the possible solutions of the puzzle to a list
       :param: a picture type containing the puzzle board
       :param: a set containing the constraints of the given puzzle
       :param: an int containing the current row index
       :param: an int containing hte current column index
       :param: a picture list which all of the possible solutions will be added to"""
    constraint_check = check_constraints(picture, constraints_set)
    if constraint_check == 0:
        return
    if i_col == len(picture[i_row]):
        i_row += 1
        i_col = 0
    if i_row == len(picture):
        if constraint_check == 1:
            solution_list.append(deepcopy(picture))
        return
    for value in range(2):
        picture[i_row][i_col] = value
        solve_puzzle_core(picture, constraints_set, i_row, i_col+1, solution_list)
    picture[i_row][i_col] = -16


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """ this functions returns the amount of possible solutions to a puzzle of
        the given size and constraints
        :param: a set containing the constraints
        :param: an int containing the amount of rows on the given puzzle board
        :param: an int containing the amount of columns on the given puzzle board
        :returns: an int containing the amount of possible solutions to a puzzle of
                  the given specifications"""
    picture = make_picture(n, m)
    solution_list: list[Picture] = list()
    solve_puzzle_core(picture, constraints_set, 0, 0, solution_list)
    return len(solution_list)


def get_solution_list(constraints_set: Set[Constraint], n: int, m: int) -> list[Picture]:
    """this functions receieves a constraint set and returns the list of all of the
       possible solutions
       :param: a set containing the constraints
       :param: an int containing the amount of rows on the given puzzle board
       :param: an int containing the amount of columns on the given puzzle board
       :returns: a list containing all of the possible solutions of the given specifications"""
    picture = make_picture(n, m)
    solution_list: list[Picture] = list()
    solve_puzzle_core(picture, constraints_set, 0, 0, solution_list)
    return solution_list


def get_all_constraints(picture: Picture) -> set[Constraint]:
    """ this function generates a set of all of the possible constraints for a puzzle board
        :param: a picture type containing a puzzle board
        :returns: a set of all of the possible constraints"""
    all_constraints_set = set()
    for row in range(len(picture)):
        for column in range(len(picture[row])):
            all_constraints_set.add((row, column, max_seen_cells(picture, row, column)))
    return all_constraints_set


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """ this function generates a constraint set from the given puzzle board which
        its only solution
        :param: a picture type containing the puzzle board
        :returns: a set of constraints of which the puzzle board is the only solution"""
    constraints_set = get_all_constraints(picture)
    minimal_constraints_set = deepcopy(constraints_set)
    n, m = len(picture), len(picture[0])
    for constraint in constraints_set:
        solutions = get_solution_list(minimal_constraints_set, n, m)
        updated_solutions = get_solution_list(minimal_constraints_set - {constraint}, n, m)
        if 0 < len(updated_solutions) <= len(solutions) and picture in updated_solutions:
            minimal_constraints_set.remove(constraint)
    return minimal_constraints_set

