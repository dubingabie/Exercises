#################################################################
# FILE : hangman.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import hangman_helper_original as helper


# pattern management
def letter_location(word, letter):
    """ a functions that finds all of the appearances of a char in a string
        :param : a string and a char
        :return : a list that contains the indexes of all of the appearances of that char in the string"""
    word = list(word)
    letter_location_list = list()
    for i in range(len(word)):
        if word[i] == letter:
            letter_location_list.append(i)
    return letter_location_list


def update_word_pattern(word, pattern, letter):
    """ a function that updates the hangman pattern according to the users lguess
        :param : a string containing a word
                 a string containg the hangman pattern
                 a char containg the guessed letter
        :return : the updated hangman pattern"""
    update_list = letter_location(word, letter)
    for i in range(len(update_list)):
        pattern = pattern[:update_list[i]] + letter + pattern[update_list[i]+1:]
    return pattern


# input management


def calculate_score_addition(letter_appearance):
    """ a function that calculates the addition to the user's score after a correct guess
        :param : receives the amount of times the letters the user has guessed appear in the word
        :returns : returns the ammount of points that should be added to the users score"""
    return (letter_appearance*(letter_appearance+1)) // 2


def letter_guess(letter_input, score, word, pattern, wrong_guess_list):
    """a function that that manages the input of a letter into the hangman game
          :param : a char contain the letter the user has inputted
                   an int containing the current score of the user
                   a string containing the current word the user has to guess
                   a string containing the current pattern
                   a list containing all of the letters the user has guessed up to the current point
          :returns : a string containing the current pattern as a result of the users guess
                     an int containing the user's updated score
                     a list containing the letters the user has guessed wrongly after the current turn"""
    output_message = ""
    if len(letter_input) != 1 or ord(letter_input) not in range(97, 122):
        output_message = "The letter you entered is invalid."
    elif letter_input in wrong_guess_list or letter_input in pattern:
        output_message = "The letter you entered was already chosen."
    else:
        updated_pattern = update_word_pattern(word, pattern, letter_input)
        score -= 1
        if pattern != updated_pattern:
            letter_appearance = pattern.count("_") - updated_pattern.count("_")
            score += calculate_score_addition(letter_appearance)
            pattern = updated_pattern
        else:
            wrong_guess_list.append(letter_input)
    return pattern, score, wrong_guess_list, output_message


def word_guess(word_input, word, pattern, score):
    """a function that checks if the word the user has guessed is the correct word
          :param : a string containing the word the user has inputted
                   a string containing the current word the user has to guess
                   a string containing the current pattern
                   an int containing the current score of the user
          :returns : a string containing the updated pattern
                     an int containing the updated score"""
    score -= 1
    if word_input == word:
        letter_appearance = pattern.count("_")
        score += calculate_score_addition(letter_appearance)
        pattern = word
    return pattern, score


def sort_hint_list(hint_list):
    sorted_hint_list = list()
    for i in range(helper.HINT_LENGTH):
        sorted_hint_list.append(hint_list[i*len(hint_list)//helper.HINT_LENGTH])
    return sorted_hint_list


def get_hints(word_list, pattern, wrong_guess_list, score):
    """ a functions that displays hints when the user asks for them
          :param : a list containing the list of all the possible words
                   a string containing the current pattern
                   a list containing all of the letters the user has guessed wrongly
                   an int containing the current score of the user
          :returns : an int containing the updated score of the user"""
    score -= 1
    hint_list = filter_words_list(word_list, pattern, wrong_guess_list)
    if len(hint_list) > helper.HINT_LENGTH:
        hint_list = sort_hint_list(hint_list)
    helper.show_suggestions(hint_list)
    return score


def input_manager(user_input, score, word, pattern, wrong_guess_list, word_list):
    """a function that receives input from the user and handles it according to the game rules
        :param : a tuple that contains a number that signifies the type of input (letter, word, hint)
                 and the input of the user
                 an int that contains the current score of the user
                 a string that contains the current score of the user
                 a string that contains the current pattern
                 a list that contains all of the letters the user has guessed incorrectly
                 a list containing all of the possible words
        :returns : an in containing the updated score of the user
                   a string containing the updated pattern after the guess
                   a list containing all of the letters the user has guessed incorrectly
                   after the current guess
                   a string containing the appropriate output message to the user
                """
    output_message = ""
    if user_input[0] == helper.LETTER:
        pattern, score, wrong_guess_list, output_message = letter_guess(user_input[1], score, word, pattern, wrong_guess_list)
    elif user_input[0] == helper.WORD:
        pattern, score = word_guess(user_input[1], word, pattern, score)
    elif user_input[0] == helper.HINT:
        score = get_hints(word_list, pattern, wrong_guess_list, score)
    return score, pattern, wrong_guess_list, output_message


def endgame_manager(pattern, score, word, wrong_guess_list):
    """ a function that that prints out the appropriate message at the end of the game
        :param : a string containing the current pattern
                 an int containing the current score of the user
                 a string containing the word the user has to guess
                 a list containing the letters the user has guessed incorrectly"""
    end_message = "congratulations! you have guessed the word correctly"
    if pattern.count("_") > 0:
        end_message = f'you have lost the game. the word was {word}'
    helper.display_state(pattern, wrong_guess_list, score, end_message)


def run_single_game(word_list, score):
    """ a function that runs a single game of hangman
        :param : a list containing all of the possible words
                 an int containing the starting score of the user
        :returns : an int containing the user's score at the end of the game"""
    word = helper.get_random_word(word_list)
    pattern = "_" * len(word)
    wrong_guess_list = list()
    output_message = ""
    while score > 0 and pattern != word:
        helper.display_state(pattern, wrong_guess_list, score, output_message)
        user_input = helper.get_input()
        score, pattern, wrong_guess_list, output_message =\
            input_manager(user_input, score, word, pattern, wrong_guess_list, word_list)
    endgame_manager(pattern, score, word, wrong_guess_list)
    return score


def determine_play_again_message(score, num_of_games):
    """ a function that determines what message is to be displayed before the user
        is asked whether he wants to play again
        :param: an int containing the score of the user
                an int containing the number of games the user has played
        :returns : a string containing the appropriate endgame message"""
    play_again_message = f'Number of games survived: {num_of_games}. Start a new series of games?"'
    if score > 0:
        play_again_message = f'Number of games so far: {num_of_games}. Your current score: {score}. Want to continue?'
    return play_again_message


def main():
    """a function that manges the hangman game between the games"""
    word_list = helper.load_words()
    num_of_games = 1
    score = run_single_game(word_list, helper.POINTS_INITIAL)
    while helper.play_again(determine_play_again_message(score, num_of_games)):
        if score > 0:
            score = run_single_game(word_list, score)
            num_of_games += 1
        else:
            run_single_game(word_list, helper.POINTS_INITIAL)


def filter_word_length(words_list, pattern):
    """ a function that finds all of the words with same length as the pattern
        :param : a list containing all of the possible words
                 a string containing the pattern
        :returns : a list containing all of the words with the same length as the pattern"""
    filtered_list = list()
    for i in range(len(words_list)):
        if len(words_list[i]) == len(pattern):
            filtered_list.append(words_list[i])
    return filtered_list


def filter_wrong_guess_letter_words(word_list, wrong_guess_list):
    """ a function that finds all of the words that don't have letters
        from the wrongly guess letters list
        :param : a list of all of the possible words
                 a list containing all of the letters the user has wrongly guess
        :returns : a list that contains all of the words without the wrongly guessed letters"""
    filtered_list = list()
    wrong_guess_set = set(wrong_guess_list)
    for i in range(len(word_list)):
        if not bool(set(word_list[i]) & wrong_guess_set):
            filtered_list.append(word_list[i])
    return filtered_list


def get_revealed_letters_in_pattern(pattern):
    """ a function that finds the locations of the revealed letters in the pattern
        :param : a string containing the current pattern of the user
        :returns : a list containing the indexes of the revealed letters"""
    letter_location_list = list()
    for i in range(len(pattern)):
        if pattern[i] != "_":
            letter_location_list.append(i)
    return letter_location_list


def does_have_pattern_letters_in_word(letter_location_list, word, pattern):
    """a function that checks whether the word has some the letters that area
        revealed in the pattern exist in the word in other places
        :param : a list that contains the locations of the revealed letters in the pattern
                 a string containing the word that is currently being checked
                 a string containing the current pattern
        :returns : True if the word doesn't have any of the pattern letters in the places that are not yet revealed
                   False if otherwise"""
    for i in range(len(letter_location_list)):
        if word.count(pattern[letter_location_list[i]]) != pattern.count(pattern[letter_location_list[i]]):
            return False
    return True


def is_compatible_word(letter_location_list, word, pattern):
    """ a function that checks if the letters in word are matching to those in the pattern
        :param : a list that contains the locations of letters in the list
                 a string that contains the word that is currently being checked
                 a string that contains the current pattern
        :returns : True if the letters in the pattern match those in the word
                   False if otherwise"""
    for i in range(len(letter_location_list)):
        if pattern[letter_location_list[i]] != word[letter_location_list[i]]:
            return False
    return True


def filter_words_by_pattern(words_list, pattern):
    """ a function that filters a word list to the words that are compatible with those in the current pattern
        :param : a list containing all of the possible words
                 a string containing the current pattern
        :returns : a list containing all of the compatible words"""
    filtered_list = list()
    letter_location_list = get_revealed_letters_in_pattern(pattern)
    for i in range(len(words_list)):
        if is_compatible_word(letter_location_list, words_list[i], pattern):
            if does_have_pattern_letters_in_word(letter_location_list, words_list[i], pattern):
                filtered_list.append(words_list[i])
    return filtered_list


def filter_words_list(words_list, pattern, wrong_guess_list):
    """ a function that finds all of the possible hints
        :param : a list containing all of the possible words
                 a string containing the current pattern
                 a list containing all of the letters the user has guessed incorrectly"""
    hint_list = filter_word_length(words_list, pattern)
    hint_list = filter_wrong_guess_letter_words(hint_list, wrong_guess_list)
    hint_list = filter_words_by_pattern(hint_list, pattern)
    return hint_list


if __name__ == "__main__":
    main()