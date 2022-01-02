#################################################################
# FILE : ex3.py
# WRITER : Gaberiel Dubin , dubingabie , 209386481
# EXERCISE : intro2cse ex3 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def sum_list(lst):
    """a function that receives a list as a parameter
       and returns its sam using a for loop"""
    list_sum = 0
    for i in range(len(lst)):
        list_sum += lst[i]
    return list_sum


def input_list():
    """ a function that receives multiple string inputs that contain
        number digits and returns a list with all of the numbers
        the user has typed and their input at the end using a while loop
        ,input function and the append function"""
    user_input = input()
    inputs_list = list()
    while user_input != "":
        inputs_list.append(float(user_input))
        user_input = input()
    inputs_list.append(sum_list(inputs_list))
    return inputs_list


def inner_product(vec_1, vec_2):
    """ a function that receives two lists of the same length containing float or int numbers
        and returns the sum of the multiplications between each two corresponding cells
        and returns it"""
    inner_multiplication = None
    if len(vec_1) == len(vec_2):
        inner_multiplication = 0
        VECTOR_LENGTH = len(vec_1)
        for i in range(VECTOR_LENGTH):
            inner_multiplication += vec_1[i] * vec_2[i]
    return inner_multiplication


def increasing_monotonous(sequence):
    """ a function thatt receives a list of numbers as a parameter
        and returns true if the numbers that make up the list
        are an increasing monotonous sequence when they are
        ordered by cell index and false if otherwise"""
    SEQUENCE_LENGTH = len(sequence)-1
    for i in range(SEQUENCE_LENGTH):
        if sequence[i] > sequence[i+1]:
            return False
    return True


def really_increasing_monotonous(sequence):
    """ a function that receives a list of numbers as a parameter
        and returns true if the numbers that make up the list
        are a really increasing monotonous sequence when they are
        ordered by cell index and false if otherwise"""
    SEQUENCE_LENGTH = len(sequence)-1
    for i in range(SEQUENCE_LENGTH):
        if sequence[i] >= sequence[i+1]:
            return False
    return True


def decreasing_monotonous(sequence):
    """ a function that receives a list of numbers as a parameter
        and true if the numbers that make up the list
        are a decreasing monotonous sequence when they are
        ordered by cell index and false if otherwise"""
    SEQUENCE_LENGTH = len(sequence)-1
    for i in range(SEQUENCE_LENGTH):
        if sequence[i] < sequence[i+1]:
            return False
    return True


def really_decreasing_monotonous(sequence):
    """ a function that receives a list of numbers as a parameter
        and returns true if the numbers that make up the list
        are a really decreasing monotonous sequence when they are
        ordered by cell index and false if otherwise"""
    SEQUENCE_LENGTH = len(sequence)-1
    for i in range(SEQUENCE_LENGTH):
        if sequence[i] <= sequence[i+1]:
            return False
    return True


def sequence_monotonicity(sequence):
    """ a function that receives a sequence of numbers (int or float types) inside a list
        and returns a boolean list containing monotony attributes of that sequence"""
    attribute_list = [True, True, True, True]
    if len(sequence) > 1:
        attribute_list[1] = really_increasing_monotonous(sequence)
        if attribute_list[1]:
            attribute_list[0] = True
        else:
            attribute_list[0] = increasing_monotonous(sequence)
        attribute_list[3] = really_decreasing_monotonous(sequence)
        if attribute_list[3]:
            attribute_list[2] = True
        else:
            attribute_list[2] = decreasing_monotonous(sequence)
    return attribute_list


def monotonicity_inverse(def_bool):
    """ a function that receives as an input a list containing boolean
        variables defining the monotony of a sequence of numbers and
        returns sequence matching the specifications """
    monotonous_sequence = None
    if def_bool == [True, False, True, False]:
        monotonous_sequence = [1, 1, 1, 1]
    if def_bool == [True, True, False, False]:
        monotonous_sequence = [1, 2, 3, 4]
    if def_bool == [True, False, False, False]:
        monotonous_sequence = [1, 1, 2, 3]
    if def_bool == [False, False, True, True]:
        monotonous_sequence = [4, 3, 2, 1]
    if def_bool == [False, False, True, False]:
        monotonous_sequence = [4, 3, 3, 1]
    if def_bool == [False, False, False, False]:
        monotonous_sequence = [0, -1, 0, -1]
    return monotonous_sequence


def is_prime(num):
    """ a function that receives a number and returns true
        if its a prime number or false if otherwise"""
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and (i != 1):
            return False
    return True


def primes_for_asafi(n):
    """ a function that receives a natural number and returns
        a list with the length of that number containing prime numbers"""
    primes_list = []
    prime_num_candidate = 2
    while len(primes_list) < n:
        if is_prime(prime_num_candidate):
            primes_list.append(prime_num_candidate)
        prime_num_candidate += 1
    return primes_list


def add_vector(vec_lst, vec_to_add):
    """ a function that receives two lists of the same length that contain numbers
        as parameters and adds up all of the corresponding cells to the first list """
    for i in range(len(vec_lst)):
        vec_lst[i] += vec_to_add[i]
    return vec_lst


def sum_of_vectors(vec_lst):
    """ a function that receives a list containing other lists of the same length
        containing int or float type numbers and sums up corresponding cells
        in each list into one list and returns it"""
    vec_sum = None
    if len(vec_lst) > 0:
        vec_sum = list(vec_lst[0])
        for i in range(1, len(vec_lst)):
            add_vector(vec_sum, vec_lst[i])
    return vec_sum


def num_of_orthogonal(vectors):
    """ a function that receives a list of lists containing numbers (int or float types) as input
        and counts the amount of list pairs that when you multiply corresponding cells
        and sum the multiplications they add up to 0 and returns that amount"""
    num_of_ortho_vecs = 0
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if inner_product(vectors[i], vectors[j]) == 0:
                num_of_ortho_vecs += 1
    return num_of_ortho_vecs


