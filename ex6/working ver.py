
import requests
import bs4
import sys
import urllib.parse
import pickle
import copy

def load_dict_file(file_name):
    with open(file_name, 'rb') as f:
        d = pickle.load(f)
    return d

def pages_with_words_in_query(query, words_dict):
    query_list = []
    for i in query.split():
        if words_dict.get(i):
            query_list.append(i)
    if not query_list:
        return []
    pages_list = [*words_dict.get(query_list[0])]
    if len(pages_list) > 1:
        for query_word in query_list[1:]:
            for page in pages_list:
                if page not in words_dict.get(query_word):
                    pages_list.remove(page)
    return pages_list

def sort_pages_by_ranking_dict(ranking_dict, pages_list, max_results):
    sorted_pages = pages_list
    sorted_pages = sorted(sorted_pages, key = lambda x: -ranking_dict.get(x))
    return sorted_pages[0:max_results]

def combined_scores(query, sorted_pages_list, ranking_dict, words_dict):
    combined_score_dict = {}
    for page in sorted_pages_list:
        min_occurances = 0
        for i, query_word in enumerate(query.split()):
            if query_word in words_dict and page in words_dict[query_word]:
                current_occurances = words_dict[query_word][page]
            else:
                continue
            if i == 0:
                min_occurances = current_occurances
            else:
                min_occurances = current_occurances if current_occurances < min_occurances else min_occurances
        combined_score_dict[page] = ranking_dict.get(page) * min_occurances
    return dict(sorted(combined_score_dict.items(), key=lambda item: item[1], reverse =True))

def run_query(query, ranking_dict, words_dict, max_results):
    ranking_dict = load_dict_file(ranking_dict)
    words_dict = load_dict_file(words_dict)
    sorted_pages_list = sort_pages_by_ranking_dict(ranking_dict, pages_with_words_in_query(query, words_dict), int(max_results))
    combined_scores_dict = combined_scores(query, sorted_pages_list, ranking_dict, words_dict)
    for result in combined_scores_dict:
        print(result, combined_scores_dict[result])

if __name__ == "__main__":
    run_query("broom wand cape", "page_rank_dict.pickle", "words_dict.pickle", 4)