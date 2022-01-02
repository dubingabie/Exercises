from copy import deepcopy

MOVES_LIST = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, 1), (1, -1), (1, 0), (1, 1)]


def is_valid_path(board, path, words):
    """
    this function checks if the path given is valid according to the game rules
    and returns the word if it is valid according to the game rules
    :param board: a two dimensional list containing the game board
    :param path: a list of tuples that contains the cells on the board which the user chose
    :param words: a list that contains all of the legal words of the game
    :return: a string containing the word the player chose if the path is valid and None otherwise
    """
    word = None
    if is_path_legal(path):
        path_word = get_word_in_path(path, board)
        if path_word in words:
            word = path_word
    return word


def is_path_legal(path) -> bool:
    """
    this function checks if a path on the board is legal according to the game rules
    :param path: a list of tuples that contains the cells on the board which the user chose
    :return: True if the path is legal and False otherwise
    """
    is_legal = True
    if not is_in_range(path[0]) or len(path) != len(set(path)):
        is_legal = False
    else:
        for i in range(1, len(path)):
            if not is_in_range(path[i]):
                is_legal = False
                break
            if (path[i][0] - path[i-1][0]) > 1 or (path[i][1] - path[i-1][1]) > 1:
                is_legal = False
                break
    return is_legal


def get_word_in_path(path, board) -> str:
    """
    this function returns the word created from the letters in the cells on the path
    :param board: a two dimensional list containing the board
    :param path: the tuple list containing the cells which the user chose by the order they were chosen
    :return: a string containing the word made up by the path
    """
    word_str = ""
    for cell in path:
        word_str += board[cell[0]][cell[1]]
    return word_str


def find_length_n_paths(n, board, words):
    """
    this function finds all of the n length paths for legal words on the board
    :param n: an int that contains the length of the paths that are to be found
    :param board: a two dimensional list containing the game board
    :param words: a list that contains all of the legal words
    :return: a list that contains lists of tuples with all of the legal paths
    """
    all_paths_lst = list()
    cur_path = list()
    for row in range(4):
        for col in range(4):
            cur_path.append((row, col))
            filtered_words = filter_words_list(cur_path, board, words)
            __find_length_n_paths_core(cur_path, all_paths_lst, n-1, board, filtered_words)
            cur_path = list()
    return all_paths_lst


def __find_length_n_paths_core(cur_path, all_paths_lst, n, board, words):
    """
    this is a backtracking recursive core function for the find_length_n_paths function
    :param cur_path: a list of tuples containing the current path
    :param all_paths_lst: a list that contains lists of tuples with all of the legal n length paths found
    :param n: an in that contains the amount of the cells that are to be added to the path
    :param board: a two dimensional list containing the game board
    :param words: a list that contains all of the legal words
    :return: None
    """
    if n == 0:
        if is_valid_path(board, cur_path, words) and cur_path not in all_paths_lst:
            all_paths_lst.append(deepcopy(cur_path))
        return
    for possible_move in MOVES_LIST:
        next_move = (cur_path[-1][0] + possible_move[0], cur_path[-1][1] + possible_move[1])
        if is_in_range(next_move):
            cur_path.append(next_move)
            if is_path_in_words_list(cur_path, board, words):
                filtered_words = filter_words_list(cur_path, board, words)
                __find_length_n_paths_core(cur_path, all_paths_lst, n-1, board, filtered_words)
            cur_path.pop()


def is_path_in_words_list(path, board, words) -> bool:
    """
    this function checks if there are words that match the current path
    :param path: a tuple list that contains the current path
    :param board: a two dimensional list that contains the current game board
    :param words: a list of the legal words
    :return: True if there are words that match the current path and False otherwise
    """
    path_word = get_word_in_path(path, board)
    is_path_in_legal_words = False
    for word in words:
        if path_word == word[:len(path_word)]:
            is_path_in_legal_words = True
            break
    return is_path_in_legal_words


def filter_words_list(path, board, words):
    """
    this function filters the words list according to the current path
    :param path: a tuple list containing the current path
    :param board: a two dimensional list contain the current game board
    :param words: a list containing all of the currently legal words
    :return: a filtered word list according to the current path
    """
    cur_word = get_word_in_path(path, board)
    return list(filter(lambda word: word[:len(cur_word)] == cur_word, words))


def is_in_range(coordinates):
    """
    this function checks if the given tuple is in range
    :param coordinates: a tuple that contains the (y,x) coordinates of the cell on the board
    :return: True if the cell is in the board and False otherwise
    """
    return (0 <= coordinates[0] <= 3) and (0 <= coordinates[1] <= 3)


def find_length_n_words(n, board, words):
    """
    this function finds all of the legal paths to words with n letters
    :param n: an int that contains the length of words in the paths
    :param board: a two dimensional list containing the game board
    :param words: a list that contains the length of all of legal words
    :return: a list that contains all of the paths to n length words
    """
    all_n_length_paths = list()
    for path_len in range(1, n+1):
        cur_n_length_paths = find_length_n_paths(path_len, board, words)
        for cur_path in cur_n_length_paths:
            if cur_path not in all_n_length_paths:
                all_n_length_paths.append(cur_path)
    return list(filter(lambda path: len(get_word_in_path(path, board)) == n, all_n_length_paths))


def max_score_paths(board, words):
    """
    this function finds the paths that give the player the highest score addition
    :param board: a two dimensional list of the current game board
    :param words: a list of all of the legal words
    :return: a list of the pats that grant the player the highest score addition
    """
    max_score_dict = dict()
    for path_length in range(16, 0, -1):
        cur_n_length_paths = find_length_n_paths(path_length, board, words)
        for path in cur_n_length_paths:
            path_word = get_word_in_path(path, board)
            if path_word not in max_score_dict.keys():
                max_score_dict[path_word] = path
    return list(max_score_dict.values())

