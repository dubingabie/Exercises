
#################################################################
# FILE : ex11.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex11 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


import itertools
from copy import deepcopy

class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root: Node):
        self.root = root

    def diagnose(self, symptoms):
        """
        this function diagnoses the illness according to a list of symptoms
        :param symptoms: a list of strings containing sympotms
        :return: if an illness was diagnosed it returns a string and None if otherwise
        """
        pointer = self.root
        return self.__diagnose_core(pointer, symptoms)

    def __diagnose_core(self, pointer, symptoms):
        """
        this is a recursive core function the the diagnose function
        :param pointer: a point the root of the Diagnoser object tree
        :param symptoms: a a list of strings containing sympotms
        :return: if an illness was diagnosed it returns a string and None if otherwise
        """
        if pointer is None:
            return None
        if pointer.positive_child is None and pointer.negative_child is None:
            return pointer.data
        if pointer.data in symptoms:
            pointer = pointer.positive_child
        else:
            pointer = pointer.negative_child
        return self.__diagnose_core(pointer, symptoms)

    def calculate_success_rate(self, records):
        """
        this function tests the success rate of the Diagnoser object
        :param records: a list of record objects
        :return: the success rate of the Diagnoser in diagnosing the ilness
        """
        num_of_records = len(records)
        if num_of_records == 0:
            raise ValueError("records list is empty")
        correct_diagnosis = 0
        for record in records:
            if record.illness == self.diagnose(record.symptoms):
                correct_diagnosis += 1
        return correct_diagnosis / num_of_records

    def all_illnesses(self):
        """
        this function returns all of the illnesses this diagnoser can diagnose according to the sympotms
        :return: a list of str types containing all of the illnesses this Diagnoser object can diagnose
        """
        illnesses_lst = list()
        pointer = self.root
        self.__all_illnesses_core(pointer, illnesses_lst)
        return illnesses_lst

    def __all_illnesses_core(self, pointer, illnesses_lst):
        """
        a recursive core function the all_illneses function
        :param pointer: a pointer the the Diagnoser root
        :param illnesses_lst: an list which all of the illnesses to the tree will be added to
        :return: None
        """
        if pointer is None:
            return
        if pointer.positive_child is None and pointer.negative_child is None and pointer.data not in illnesses_lst:
            illnesses_lst.append(pointer.data)
        self.__all_illnesses_core(pointer.positive_child, illnesses_lst)
        self.__all_illnesses_core(pointer.negative_child, illnesses_lst)

    def paths_to_illness(self, illness):
        """
        this function returns all of the possible paths to a certain illness in this Diagnoser
        :param illness: a string containing a certain illness
        :return: a list of all of the possible paths to the specified illness
        """
        paths_lst = list()
        path = list()
        pointer = self.root
        self.__paths_to_illness_core(pointer, path, paths_lst, illness)
        return paths_lst

    def __paths_to_illness_core(self, pointer, path, paths_lst, illness):
        """
        this is a recursive backtracking core to the paths_to_illness function
        :param pointer: a pointer the Diagnosers root
        :param path: a list containg the current path taken
        :param paths_lst: a list that the correct paths to the illness are added to
        :param illness:  a string containing the name of the specified illness
        :return: None
        """
        if pointer is None:
            return
        if pointer.data == illness:
            paths_lst.append(deepcopy(path))
        path.append(True)
        self.__paths_to_illness_core(pointer.positive_child, path, paths_lst, illness)
        path.pop()
        path.append(False)
        self.__paths_to_illness_core(pointer.negative_child, path, paths_lst, illness)
        path.pop()

    def minimize(self, remove_empty=False):
        """
        this function minimises the size of the diagnoser tree without affecting its success rate
        :param remove_empty: a bool type the specifies wether to delete None diagnoses or not
        :return: None
        """
        self.__minimize_core(self.root, remove_empty)

    def __minimize_core(self, root, remove_empty):
        """
        a recursive core function for the minimize function
        :param root: a pointer to a node type object that contains root of the tree that is to be checked
        :param remove_empty: a bool type the specifies wether to delete None diagnoses or not
        :return: None or Node type object
        """
        if root is None:
            return
        if root.positive_child is None and root.negative_child is None:
            return root
        positive_diagnose = self.__minimize_core(root.positive_child, remove_empty)
        negative_diagnose = self.__minimize_core(root.negative_child, remove_empty)
        if is_equal(positive_diagnose,negative_diagnose):
            root.data, root.positive_child, root.negative_child = positive_diagnose.data, positive_diagnose.positive_child,positive_diagnose.negative_child
        if remove_empty and \
            ((positive_diagnose.data is None and negative_diagnose.data is not None) or
            (positive_diagnose.data is not None and negative_diagnose.data is None)):
            if positive_diagnose.data is not None:
                root.data, root.positive_child, root.negative_child = positive_diagnose.data, positive_diagnose.positive_child, positive_diagnose.negative_child
            else:
                root.data, root.positive_child, root.negative_child = negative_diagnose.data, negative_diagnose.positive_child, negative_diagnose.negative_child
        return root

def is_equal(root1, root2):
    """
	this function checks if two trees are identical
	:param root1: a Node type that contains the root of the first tree
	:param root2: a Node type that contains the root of the second tree
	:return: True if the two trees are identical and false otherwise
	"""
    if root1 is None and root2 is None:
        return True
    if root1.data == root2.data:
        return True and is_equal(root1.positive_child, root2.positive_child) and \
			   is_equal(root1.negative_child, root2.negative_child)
	return False


def build_tree(records, symptoms):
    """
    this function builds a diagnosing tree according to the given illness records and symptoms
    :param records: a list of records that contains the illness data
    :param symptoms: a list of strings that contains the symptoms that are to be checked
    :return: the root of the created diagnoser tree
    """
    root = __create_tree(symptoms)
    __place_illness(root, records)
    return Diagnoser(root)


def __create_tree(symptoms):
    """
    this function creates an empty tree with the symptoms at the junctions
    :param symptoms: a list of strings containing the given symptoms
    :return: the root of the created tree
    """
    if type(symptoms[0]) is not str:
        raise TypeError("illegal type for symptom")
    root = Node(None)
    if len(symptoms) > 0:
        root = Node(symptoms[0])
    symptoms = symptoms[1:]
    root.positive_child = Node(None)
    root.negative_child = Node(None)
    __create_tree_core(root.positive_child, symptoms)
    __create_tree_core(root.negative_child, symptoms)
    return root


def __create_tree_core(pointer, symptoms):
    """
    a recursive core function of the __create_tree function
    :param pointer: a pointer of the root of the to be created tree
    :param symptoms: a list of strings containg the given symptoms
    :return: None
    """
    if len(symptoms) == 0:
        return
    if type(symptoms[0]) is not str:
        raise TypeError("illegal type for symptom")
    pointer.data = symptoms[0]
    symptoms = symptoms[1:]
    pointer.positive_child = Node(None)
    pointer.negative_child = Node(None)
    __create_tree_core(pointer.positive_child, symptoms)
    __create_tree_core(pointer.negative_child, symptoms)


def __place_illness(pointer, records):
    """
    this function places the illnesses at the correct leaves of the empty diagnoser tree
    :param pointer: a pointer of the diagnoser tree which the illnesses are going to be placed in
    :param records: a list of records containing all of the illnesses that are to be placed in the tree
    :return: None
    """
    if len(records) == 0 or pointer is None:
        return
    if pointer.positive_child is None and pointer.negative_child is None:
        pointer.data = __most_common_illness(records)
    matching_records = list()
    unmatching_records = list()
    for record in records:
        if type(record) is not Record:
            raise TypeError("illegal type for record")
        if pointer.data in record.symptoms:
            matching_records.append(record)
        else:
            unmatching_records.append(record)
    __place_illness(pointer.positive_child, matching_records)
    __place_illness(pointer.negative_child, unmatching_records)


def __most_common_illness(records):
    """
    this function returns the most common illness in a records list
    :param records: a list of records that are to be checked
    :return: the name of the most common illness in the records list
    """
    illness_dict = dict()
    for record in records:
        if record.illness not in illness_dict.keys():
            illness_dict[record.illness] = 0
        illness_dict[record.illness] += 1
    return sorted(illness_dict.items(), key=lambda item: item[1], reverse=True)[0][0]


def optimal_tree(records, symptoms, depth):
    """
    this function returns the diagnoser with the highest success rate for the given records, symptoms and depth
    :param records: a list of records that contains the given illness records
    :param symptoms: a list of strings that contain the given symptoms
    :param depth: an in the specifies the depth of the tree that will be created
    :return: a diagnoser object that contains the tree with the highest success rate for the given parameters
    """
    if depth < 0 or depth >= len(symptoms):
        raise ValueError("illegal depth for tree")
    if len(set(symptoms)) < len(symptoms):
        raise ValueError("duplicate symptom in symptom list")
    combinations_lst = list(itertools.combinations(symptoms, depth))
    best_diagnoser, best_success_rate = Diagnoser(Node(None)), 0
    for combination in combinations_lst:
        # add try and except for the for the appropriate exceptions
        candidate_diagnoser = build_tree(records, combination)
        candidate_success_rate = candidate_diagnoser.calculate_success_rate(records)
        if candidate_success_rate > best_success_rate:
            best_diagnoser = candidate_diagnoser
            best_success_rate = candidate_success_rate
    return best_diagnoser


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # covid-19   cold

    flu_leaf = Node("covid-19", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

# Add more tests for sections 2-7 here.