#################################################################
# FILE : search.py
# WRITER : Nitay Shoshana , nitay (cse) nitay.shoshana (huji) , 315315408
# EXERCISE : intro2cs2 ex6 2021
# DESCRIPTION: Exercise 6 cse
# STUDENTS I DISCUSSED THE EXERCISE WITH: 
# WEB PAGES I USED: 
# NOTES: 
#################################################################

import pickle

def min_word_score(query_word_list, page, words_dict):
    """
    gets the minimum query word score in a page
    :param query_word_list: a list of the query words
    :param page: current proccesed page
    :param words_dict: a dict that specifies which words appears in pages which are the keys, and how many times
    :return: the minimum number of appearances of the least appearant word
    """
    word_scores = []
    for w in query_word_list:
        if w in words_dict:
            if page in words_dict[w]:
                word_scores.append(words_dict[w][page])
            else:
                return 0
    if word_scores:
        return min(word_scores)
    return 0

def sec_elem(s):
    """
    :param s: a generic subscriptable element
    :return: the element in index 1 of that element
    """
    return s[1]

def sort_tuple_list(t_list):
    """
    sorts descending a tuple list by the key in index 1 (second element)
    :param t_list: a tuple list
    """
    return sorted(t_list, key=sec_elem, reverse=True)

def pretty_print_tuple_list(tuple_list):
    """
    prints a tuple list in a relatively good looking format
    :param tuple_list: a list of tuples (?)
    :return: None
    """
    for t in tuple_list:
        print(t[0], t[1])

def get_pages_scores_filtered(query, rank_dict, w_dict):
    """
    trims and filters all ranked scores to match the starting creteria
    :param query: query string
    :param rank_dict: ranking dictionary (see page_rank.page_rank)
    :param w_dict: a wording dictionary (see word_dict)
    :return: a list of tuples, sorted and trimed by the rules
    """
    pages_scores_filtered = []
    for page, score in rank_dict.items():
        word_query_score = min_word_score(query.split(), page, w_dict)
        if word_query_score == 0:
            continue
        pages_scores_filtered.append((page, score, word_query_score))
    return sort_tuple_list(pages_scores_filtered)

# def load_search_dicts_from_pickle(rank_dict_path, word_dict_path):
#     """
#     loads ranking dict and wording dict from pickle files
#     :param rank_dict_path:
#     :param word_dict_path:
#     :return: tuple of those dicts
#     """
#     return ph.load_dict_from_pickle(rank_dict_path), ph.load_dict_from_pickle(word_dict_path)


def open_dict_file(dict_file_name):
    with open(dict_file_name, "rb") as file:
        dict_file = pickle.load(file)
    return dict_file

def search(query: str, rank_dict_path: str, word_dict_path: str, max_results: int):
    """
    searches a query in the Moogle search engine
    :param query: a query string seperated by spaces
    :param rank_dict_path: a path to a ranking dict pickle file
    :param word_dict_path: a path to a wording dict pickle file
    :param max_results: maximum number of retured results to user
    """
    word_dict = open_dict_file(word_dict_path)
    rank_dict = open_dict_file(rank_dict_path)
    pages_scores_filtered = get_pages_scores_filtered(query, rank_dict, word_dict)
    pages_scores_sorted = []
    for page, score , word_query_score in pages_scores_filtered[:max_results]:
        pages_scores_sorted.append((page, score * word_query_score))
    pages_scores_sorted = sort_tuple_list(pages_scores_sorted)
    pretty_print_tuple_list(pages_scores_sorted)

if __name__ == "__main__":
    search("scar", "page_rank_dict.pickle", "words_dict.pickle", 4)