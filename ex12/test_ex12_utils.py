from ex12_utils import *

BOARD = [["D", "C", "B", "A"],
         ["G", "A", "D", "E"],
         ["T", "J", "Y", "T"],
         ["N", "M", "F", "I"]]

with open("boggle_dict.txt", "r") as words_dict:
    WORDS = words_dict.read().splitlines()


def test_find_length_n_paths_1():
    x = find_length_n_paths(
        3,
        [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'G', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ],
        ('ABC', 'CDE', 'ABCD', 'MGG', 'FKP')
    )
    assert (
            [[(0, 0), (0, 1), (0, 2)], [(3, 0), (2, 1), (1, 2)], [(1, 1), (2, 2), (3, 3)]] == x
            or
            [[(0, 0), (0, 1), (0, 2)], [(1, 1), (2, 2), (3, 3)], [(3, 0), (2, 1), (1, 2)]] == x
    )


def test_find_lenght_n_word():
    assert (
            find_length_n_words(
                3,
                [
                    ['A', 'B', 'C', 'D'],
                    ['E', 'F', 'G', 'H'],
                    ['I', 'G', 'K', 'L'],
                    ['M', 'N', 'O', 'P']
                ],
                ('ABC', 'CDE', 'ABCD')
            ) == [[(0, 0), (0, 1), (0, 2)]]
    )


def test_max_score_paths():
    # print(find_length_n_paths(4, BOARD, WORDS))
    # print(max_score_paths(BOARD, WORDS))
    assert (
            max_score_paths(
                [
                    ['A', 'B', 'C', 'D'],
                    ['E', 'F', 'G', 'H'],
                    ['I', 'G', 'K', 'L'],
                    ['M', 'N', 'O', 'P']
                ],
                ('ABC', 'CDE', 'ABCD')) == [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (0, 2)]]
    )
    # Expected return value:
