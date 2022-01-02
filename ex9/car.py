
#################################################################
# FILE : car.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


class Car:
    """
    object class for the car object on a board;
    each car has a name , length of the car, location of the first cell on the board and its orientation
    """
    def __init__(self, name: str, length: int, location: tuple, orientation: int) -> None:
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self) -> list:
        """
        :return: A list of coordinates the car is in
        """
        coordinates_lst = list()
        for cell in range(self.length):
            if self.orientation:
                coordinates_lst.append((self.location[0], self.location[1] + cell))
            else:
                coordinates_lst.append((self.location[0] + cell, self.location[1]))
        return coordinates_lst

    def possible_moves(self) -> dict:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        moves_dict = dict()
        if self.orientation == 1:
            moves_dict = {"r": "causes the car to to move one cell to the right",
                          "l": "causes the car to move one cell to the left"}
        else:
            moves_dict = {"u": "causes the car to to move one cell upwards",
                          "d": "causes the car to move one cell downwards"}
        return moves_dict

    def movement_requirements(self, movekey: str) -> list:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        req_lst = list()
        key = movekey[0]
        if key == "u" and self.orientation == 0:
            req_lst.append((self.location[0] - 1, self.location[1]))
        elif key == "d" and self.orientation == 0:
            req_lst.append((self.location[0] + self.length, self.location[1]))
        elif key == "r" and self.orientation == 1:
            req_lst.append((self.location[0], self.location[1] + self.length))
        elif key == "l" and self.orientation == 1:
            req_lst.append((self.location[0], self.location[1] - 1))
        return req_lst

    def move(self, movekey: str) -> bool:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        move_success = True
        key = movekey[0]
        if key == "u" and self.orientation == 0:
            self.location = (self.location[0] - 1, self.location[1])
        elif key == "d" and self.orientation == 0:
            self.location = (self.location[0] + 1, self.location[1])
        elif key == "r" and self.orientation == 1:
            self.location = (self.location[0], self.location[1] + 1)
        elif key == "l" and self.orientation == 1:
            self.location = (self.location[0], self.location[1] - 1)
        else:
            move_success = False
        return move_success

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.name

