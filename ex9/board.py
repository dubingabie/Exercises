
#################################################################
# FILE : board.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


class Board:
    """
    an object class for the a board of 7x7 cells and one target cell
    """
    def __init__(self) -> None:
        self.car_dict = dict()
        self.board = list()
        for i_row in range(7):
            row = list()
            for i_col in range(7):
                row.append(None)
            if i_row == 3:
                row.append(None)
            self.board.append(row)

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ""
        for i_row in range(len(self.board)):
            for i_col in range(6):
                board_str += self.board[i_row][i_col] if self.board[i_row][i_col] else "_"
            if i_row == self.target_location()[0]:
                board_str += "E"
            else:
                board_str += "*"
            board_str += "\n"
        return board_str

    def cell_list(self) -> list:
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = list()
        for i_row in range(len(self.board)):
            for i_col in range(len(self.board[i_row])):
                cell_lst.append((i_row, i_col))
        return cell_lst

    def possible_moves(self) -> list:
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = list()
        for car in self.car_dict.values():
            for move in car.possible_moves().keys():
                if self.can_move_car(car, move):
                    moves_lst.append((car.get_name(), move, car.possible_moves()[move]))
        return moves_lst

    def target_location(self) -> tuple:
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return 3, 7

    def cell_content(self, coordinate: tuple):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        return self.board[coordinate[0]][coordinate[1]] if self.board[coordinate[0]][coordinate[1]] else None

    def can_add(self, car) -> bool:
        """
        checks if the given car can be placed on the board
        :param car: car object of the car that is checked
        :param car_location: a list of tuples that contains all of the cells the car is in
        :return: True if the car can be added to the board and else if otherwise
        --note: i need to check if the game can add a car at the target location
        """
        is_allowed = car.get_name() not in self.car_dict.keys()
        if is_allowed:
            for cell in car.car_coordinates():
                if 0 > cell[0] or cell[0] >= len(self.board) or 0 > cell[1] or cell[1] >= len(self.board):
                    is_allowed = False
                    break
                if self.board[cell[0]][cell[1]] is not None:
                    is_allowed = False
                    break
        return is_allowed

    def add_car(self, car) -> bool:
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        car_location = car.car_coordinates()
        placement_success = self.can_add(car)
        if placement_success:
            self.car_dict[car.get_name()] = car
            for cell in car.car_coordinates():
                self.board[cell[0]][cell[1]] = car.get_name()
        return placement_success

    def can_move_car(self, car, movekey: str) -> bool:
        """
        checks if the given car can be moved to the specified location
        :param car: car object of the car that is checked
        :param movekey: a string type containing the specified movment direction
        :return: True if movement is allowed and False otherwise
        """
        req_cell = car.movement_requirements(movekey)[0]
        is_allowed = True
        if 0 > req_cell[0] or req_cell[0] >= len(self.board) or 0 > req_cell[1] or req_cell[1] >= len(self.board[req_cell[0]]):
            is_allowed = False
        if self.cell_content(req_cell) is not None:
            is_allowed = False
        return is_allowed

    def move_car(self, name, movekey: str) -> bool:
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        move_success = name in self.car_dict.keys() and movekey in self.car_dict[name].possible_moves()
        if move_success:
            car = self.car_dict[name]
            if self.can_move_car(car, movekey):
                car.move(movekey)
                self.redraw_board()
            else:
                move_success = False
        return move_success

    def redraw_board(self) -> None:
        """
        this functions redraws the board after a movement of a car
        :return: None
        """
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                self.board[row][column] = None
        for car_name in self.car_dict.keys():
            car_coordinates = self.car_dict[car_name].car_coordinates()
            for cell in car_coordinates:
                self.board[cell[0]][cell[1]] = car_name

