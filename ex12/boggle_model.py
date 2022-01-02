from boggle_board_randomizer import randomize_board
from ex12_utils import is_valid_path

with open("boggle_dict.txt", "r") as words_dict:
    WORDS = words_dict.read().splitlines()


class BoogleModel:
    def __init__(self):
        self.board = randomize_board()
        self.current_path = list()
        self.score = 0
        self.chosen_words = set()

    def choose_word(self):
        chosen_word = is_valid_path(self.board, self.current_path, WORDS)
        if chosen_word:
            self.score += len(self.current_path) ** 2
            self.chosen_words.add(chosen_word)
        self.current_path = list()

    def clear_path(self):
        self.current_path = list()

    def update_current_path(self, coordinates):
        self.current_path.append(coordinates)

