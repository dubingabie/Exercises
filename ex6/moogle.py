
#################################################################
# FILE : moogle.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

import requests
import bs4
import sys
import urllib.parse
import pickle



#######################################################################################################################


def get_reference_dict(url_path: str, page_names_list: list) -> dict:
    """ a function that creates a reference dictionary from
        from one page to the pages whose names are specified in
        page_names_list
        :param : a string containing the url path to a page
                 a list containing the page names that will be checked
        :returns : a dictionary containing each page name as key and the amount of times
                    it is referenced"""
    reference_dict = dict()
    response = requests.get(url_path)
    html_code = response.text
    soup = bs4.BeautifulSoup(html_code, 'html.parser')
    for paragraph in soup.find_all("p"):
        for link in paragraph.find_all("a"):
            target_link = link.get("href")
            for name in page_names_list:
                if target_link == name:
                    if name not in reference_dict.keys():
                        reference_dict[name] = 0
                    reference_dict[name] += 1
    return reference_dict


def make_page_names_list(page_names):
    """ a function that translate a text file into a workable list
        :param : a text file
        :returns : a list containing which contains one line from the text file in each cell"""
    page_names_list = list()
    for name in page_names:
        page_names_list.append(name.replace("\n", ""))
    return page_names_list


def crawl(base_url: str, index_file: str, out_file: str):
    """ a function that receives a base link for a wiki page
        how many references between the pages in the index file supplied
        and saves them in pickle format
        :param : a string containing the base url for the page
                 a string containing the name of an index file with the names of the pages
                 a string containing the name of the pickle file that is created """
    page_names = open(index_file)
    page_names_list = make_page_names_list(page_names)
    traffic_dict = dict()
    for name in page_names_list:
        url_path = urllib.parse.urljoin(base_url, name)
        traffic_dict[name] = get_reference_dict(url_path, page_names_list)
    with open(out_file, 'wb') as file:
        pickle.dump(traffic_dict, file)


########################################################################################################################


def sum_page_links(traffic_dict: dict, page_key: str) -> int:
    """ a function that receives a traffic dictionary and page name
        and sums the amount of links that exist from the specified page
        to other pages in the traffic dictionary
        :param : a dictionary containing the number of times each page links to other pages
                 a string containing the key of the the page that is going to be checked
        :returns : an int containing the total amount of links from the specified page"""
    page_link_sum = 0
    for link_key in traffic_dict[page_key].keys():
        page_link_sum += traffic_dict[page_key][link_key]
    return page_link_sum if page_link_sum > 0 else 1


def calculate_ranking_addition(rating_dict: dict, traffic_dict: dict, page_key, link_key) -> float:
    ranking_addition = rating_dict[page_key] * \
                           (traffic_dict[page_key][link_key] / sum_page_links(traffic_dict, page_key))
    return ranking_addition


def calculate_ranking(traffic_dict: dict, ranking_dict: dict, new_ranking_dict: dict) -> dict:
    for page_key in traffic_dict.keys():
        for link_key in traffic_dict[page_key].keys():
            new_ranking_dict[link_key] += \
                calculate_ranking_addition(ranking_dict, traffic_dict, page_key, link_key)
    return new_ranking_dict


def reset_ranking_dict(traffic_dict: dict, default_value=0):
    new_ranking_dict = dict()
    for key in traffic_dict.keys():
        new_ranking_dict[key] = default_value
    return new_ranking_dict


def page_rank(iterations: int, dict_file: str, out_file: str):
    ranking_dict = dict()
    with open(dict_file, "rb") as file:
        traffic_dict = pickle.load(file)
    ranking_dict = reset_ranking_dict(traffic_dict, 1)
    for iteration in range(iterations):
        new_ranking_dict = reset_ranking_dict(traffic_dict)
        ranking_dict = calculate_ranking(traffic_dict, ranking_dict, new_ranking_dict)
    with open(out_file, 'wb') as file:
        pickle.dump(ranking_dict, file)


#######################################################################################################################


def make_url_path_dict(base_url, page_names_list):
    url_path_dict = dict()
    for name in page_names_list:
        url_path_dict[name] = urllib.parse.urljoin(base_url, name)
    return url_path_dict


def make_words_in_page_dict(url_path):
    words_in_page_dict = dict()
    response = requests.get(url_path)
    html_code = response.text
    soup = bs4.BeautifulSoup(html_code, 'html.parser')
    for paragraph in soup.find_all("p"):
        text_content = paragraph.text
        words_list = text_content.split()
        for word in words_list:
            if word not in words_in_page_dict:
                words_in_page_dict[word] = 0
            words_in_page_dict[word] += 1
    return words_in_page_dict


def words_dict(base_url, index_file, out_file):
    page_names = open(index_file)
    page_names_list = make_page_names_list(page_names)
    url_path_dict = make_url_path_dict(base_url, page_names_list)
    words_dict = dict()
    for page_name in url_path_dict.keys():
        words_in_page_dict = make_words_in_page_dict(url_path_dict[page_name])
        for word in words_in_page_dict.keys():
            if word not in words_dict:
                words_dict[word] = dict()
            words_dict[word][page_name] = words_in_page_dict[word]
    with open(out_file, "wb") as file:
        pickle.dump(words_dict, file)


########################################################################################################################

def open_dict_file(file_name):
    with open(file_name, 'rb') as file:
        dict_file = pickle.load(file)
    return dict_file

def make_query_list(query, words_dict):
    query_list = list()
    for query_index in query.split():
        if words_dict.get(query_index):
            query_list.append(query_index)
    return query_list

def get_pages_with_query_words(query, words_dict):
    query_list = make_query_list(query, words_dict)
    pages_list = list()
    if query_list:
        pages_list = [*words_dict.get(query_list[0])]
        if len(pages_list) > 1:
            for query_word in query_list[1:]:
                for page_mame in pages_list:
                    if page_mame not in words_dict.get(query_word):
                        pages_list.remove(page_mame)
    return pages_list


def sort_pages_by_ranking_dict(ranking_dict, pages_list, max_results):
    sorted_pages = sorted(pages_list, key = lambda x: -ranking_dict.get(x))
    return sorted_pages[0:max_results]


def result_score_dict(query, sorted_pages_list, ranking_dict, words_dict):
    result_score_dict = dict()
    for page_name in sorted_pages_list:
        min_word_appearances = 0
        for query_index, query_word in enumerate(query.split()):
            if query_word in words_dict and page_name in words_dict[query_word]:
                current_word_appearances = words_dict[query_word][page_name]
            else:
                continue
            if query_index == 0:
                min_word_appearances = current_word_appearances
            else:
                min_word_appearances = current_word_appearances \
                    if current_word_appearances < min_word_appearances else min_word_appearances
        result_score_dict[page_name] = ranking_dict.get(page_name) * min_word_appearances
    return dict(sorted(result_score_dict.items(), key=lambda item: item[1], reverse = True))


def search(query, ranking_dict, words_dict, max_results):
    ranking_dict = open_dict_file(ranking_dict)
    words_dict = open_dict_file(words_dict)
    pages_list = get_pages_with_query_words(query, words_dict)
    sorted_pages_list = sort_pages_by_ranking_dict(ranking_dict, pages_list, int(max_results))
    result_scores_dict = result_score_dict(query, sorted_pages_list, ranking_dict, words_dict)
    for result in result_scores_dict:
        print(result, result_scores_dict[result])


if __name__ == "__main__":
    # if sys.argv[1] == "search" and len(sys.argv) == 6:
    #     search(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    # elif sys.argv[1] == "words_dict" and len(sys.argv) == 5:
    #     words_dict(sys.argv[2], sys.argv[3],sys.argv[4])
    # elif sys.argv[1] == "page_rank" and len(sys.argv) == 5 :
    #     page_rank(int(sys.argv[2]), sys.argv[3], sys.argv[4])
    # elif sys.argv[1] == "crawl" and len(sys.argv) == 5:
    #     crawl(sys.argv[2], sys.argv[3], sys.argv[4])
    # search("wand","page_rank_dict.pickle","words_dict.pickle",4)
    print(open_dict_file("words_dict.pickle"))