
#################################################################
# FILE : game.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


import sys
import helper
from board import Board
from car import Car


class Game:
    """
    game object class which manages the rush hour game
    """
    def __init__(self, board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self) -> bool:
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        :returns: True if the game will continue for another turn and False if otherwise
        """
        keep_playing = True
        user_input = input("Please enter your input").split(",")
        if user_input[0] in "Y,B,O,G,W,R" and user_input[0] in self.board.car_dict.keys() \
                and user_input[1] in "u,d,l,r" and user_input[1] in self.board.car_dict[user_input[0]].possible_moves():
            self.board.move_car(*user_input)
        elif user_input[0] == "!":
            keep_playing = False
        else:
            print("illegal input, please try again")
        return keep_playing

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        target_cell = self.board.target_location()
        keep_playing = True
        while self.board.board[target_cell[0]][target_cell[1]] is None and keep_playing:
            print(self.board)
            keep_playing = self.__single_turn()


if __name__ == "__main__":
    file_path = sys.argv[1]
    car_dict = helper.load_json(file_path)
    board = Board()
    for car in car_dict.keys():
        if car_dict[car][0] <= 4 or car_dict[car][0] >= 2 and car in "Y,B,O,G,W,R":
            board.add_car(Car(car, *car_dict[car]))
    Game(board).play()
