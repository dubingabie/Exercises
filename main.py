from functools import reduce
from copy import deepcopy
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # x = TreeNode(1,
    #              TreeNode(2,
    #                       TreeNode(3), TreeNode(4)),
    #              TreeNode(5,
    #                       TreeNode(6), TreeNode(9)))
    # y = TreeNode(1,
    #              TreeNode(2,
    #                       TreeNode(3), TreeNode(9)),
    #              TreeNode(5,
    #                       TreeNode(6), TreeNode(4)))
    # print(equal_trees(x,y))
###############################################################################
def get_level(root, level,level_lst):
    if not root:
        return
    if level == 0:
        level_lst.append(root.data)
        return
    get_level(root.left, level-1, level_lst)
    get_level(root.right, level-1, level_lst)


def equal_trees(x, y):
    are_equal = True
    if not x and not y:
        return are_equal
    if not x and y or not y and x:
        are_equal = False
    level = 0
    while y and x:
        x_level = list()
        y_level = list()
        get_level(x, level, x_level)
        get_level(y, level, y_level)
        if not len(x_level):
            break
        if set(x_level) == set(y_level):
            level += 1
        else:
            are_equal = False
            break
    return are_equal

################################################################################
def get_fun_k_series(k,fun):
    series_lst = list()
    while k:
        series_lst.append(k)
        k = fun(k)
    return series_lst

def n_of_sums(n,k,fun):
    fun_series = get_fun_k_series(k,fun)
    all_sums = list()
    __n_of_sums_core(n, fun_series, [], all_sums)
    return len(all_sums)

def __n_of_sums_core(n,fun_series,sum_lst,all_sums):
    if not len(fun_series):
        return
    n_sum = sum(sum_lst)
    if n_sum == n:
        add_sum_lst(sum_lst, all_sums)
        return
    if n_sum > n:
        return
    for i in range(len(fun_series)):
        sum_lst.append(fun_series[i])
        __n_of_sums_core(n, fun_series[0:i] + fun_series[i+1:], sum_lst, all_sums)
        sum_lst.remove(fun_series[i])

def add_sum_lst(sum_lst, all_sums):
    sum_lst_set = set()
    for num in sum_lst:
        sum_lst_set.add(num)
    if sum_lst_set not in all_sums:
        all_sums.append(sum_lst_set)

#################################################################################

def appear_at_least(word_list, k):
    apr_dict = reduce(insert_into_dict, word_list, {})
    apr_over_k = filter(lambda x: x[1] >= k, apr_dict.items())
    over_k_words = map(lambda x: x[0], apr_over_k)
    return set(over_k_words)


def insert_into_dict(apr_dict, word):
    if word in apr_dict:
        apr_dict[word] += 1
    else:
        apr_dict[word] = 1
    return apr_dict

##################################################################################

def rev_list_rec(lst):
    if not len(lst):
        return []
    return [lst[-1]] + rev_list_rec(lst[:-1])

###################################################################################

def decode(codebook, cipher):
    all_ciphers = list()
    __decode_core(codebook,cipher, all_ciphers, "")
    return all_ciphers

def __decode_core(codebook, cipher, all_ciphers, cur_cipher):
    if not len(cipher):
        all_ciphers.append(cur_cipher[:-1])
        return
    for i in range(len(cipher)+1):
        if cipher[:i] in codebook.keys():
            cur_cipher += codebook[cipher[:i]] + " "
            __decode_core(codebook, cipher[i:], all_ciphers, cur_cipher)
            cur_cipher = cur_cipher[:-len(codebook[cipher[:i]]) -1]

    # cipher = "abcdefghij"
    # codebook = {"hij":"lies", "ab":"hide", "cdef":"your","efg":"secrets","abcd":"old",
    #             "xyz":"submarine","efghij":"spies","ghij":"messages", "abz":"rocket"}
################################################################################

class Interval:
    def __init__(self,a,b):
        borders = [a,b]
        self.right_border = max(borders)
        self.left_border = min(borders)

    def __get_operands(self, other):
        return self.left_border ,self.right_border, other.left_border, other.right_border

    def __add__(self, other):
        a, b, c, d = self.__get_operands(other)
        border_arithmetic_list = [a+c, a+d, b+c, b+d]
        return Interval(min(border_arithmetic_list),max(border_arithmetic_list))

    def __sub__(self, other):
        a, b, c, d = self.__get_operands(other)
        border_arithmetic_list = [a - c, a - d, b - c, b - d]
        return Interval(min(border_arithmetic_list),max(border_arithmetic_list))

    def __mul__(self, other):
        a, b, c, d = self.__get_operands(other)
        border_arithmetic_list = [a * c, a * d, b * c, b * d]
        return Interval(min(border_arithmetic_list), max(border_arithmetic_list))

    def __truediv__(self, other):
        a, b, c, d = self.__get_operands(other)
        if c <= 0 <= d:
            raise ValueError(f'{other} contains 0, so it can not be used')
        border_arithmetic_list = [a / c, a / d, b / c, b / d]
        return Interval(min(border_arithmetic_list), max(border_arithmetic_list))

    def __str__(self):
        return f'[{self.left_border},{self.right_border}]'

    # inty = Interval(2,4)
    # inty1 = Interval(3,1)
    # inty2 = Interval(-1,2)
    # inty3 = Interval(4,4)
    # inty4 = Interval(0,0)
    # #print(inty/inty2)
    # print(inty/(inty3+inty2))
    # print(inty3-inty2)
    # print(inty*inty3)
    # print(inty*inty3-inty2)
    # print(inty*(inty3-inty2))

##############################################################################################
def get_all_family(child,family):
    if not child:
        return
    family.add(child)
    get_all_family(child.right, family)
    get_all_family(child.left, family)

def family_tree(child1, child2):
    family1 = set()
    get_all_family(child1, family1)
    family2 = set()
    get_all_family(child2, family2)
    return True if family1.intersection(family2) else False

    # x = TreeNode('Ety', None, None)
    # y = TreeNode('Malka', x, None)
    # z = TreeNode('Iosi', y, x)
    # u = TreeNode('Ely', z, None)
    # v = TreeNode('Avi', None, None)
    # print(family_tree(u,x))
    # print(family_tree(x,x))
    # print(family_tree(v,x))

###############################################################################################

def make_stack():
    lst = list()
    def stack(x=None):
        if x:
            lst.insert(0, x)
        else:
            if lst:
                x = lst.pop(0)
        return x
    return stack
##############################################################################################

def depth_check(f):
    depth_lst = [0,0]
    def inner(*args, **kwargs):
        depth_lst[0] += 1
        depth_lst[1] = max(depth_lst)
        recursive_call = f(*args, **kwargs)
        depth_lst[0] -= 1
        if depth_lst[0] == 0:
            recursion_depth = depth_lst[1]
            depth_lst[1] = 0
            return recursive_call ,recursion_depth
        return recursive_call
    return inner

def combination_lock(*args):
        combination = [*args]
        correct_combination = True
        for i in len(combination):
            def check_combination(x,i):
                if i == len(combination):
                    return True
                if x != combination[i]:
                    return False
                
        return

def fizz(lst):
    for i in range(2, len(lst), 3):
        lst[i] = "Fizz"


def buzz(lst):
    for i in range(4, len(lst), 5):
        if lst[i] == "Fizz":
            lst[i] += "Buzz"
        else:
            lst[i] = "Buzz"

def fizz_buzz(n):
    lst = list(range(1, n+1))
    fizz(lst)
    buzz(lst)
    for i in range(len(lst)):
        print(lst[i])

#    f = combination_lock(1,2,3)
#    print(f(1)(2)(3))
#

if __name__ == "__main__":
    fizz_buzz(100)