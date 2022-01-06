

def bunch_together(iterable, n):
    iter_obj = iter(iterable)
    while True:
        bunch_lst = list()
        for i in range(n):
            bunch_lst.append(next(iter_obj, None))
        yield tuple(bunch_lst)
        if not bunch_lst[-1]:
            break


if __name__ == "__main__":
    for x in bunch_together(range(10), 3):
        print(x)

