from input_utils import *


def task1(list1, list2):
    return sum(abs(a-b) for (a, b) in zip(sorted(list1), sorted(list2)))


def task2(list1, list2):
    return sum(x * list2.count(x) for x in list1)


def run():
    inp = read_n_lines_n_numbers(sep='   ')
    list1 = [x[0] for x in inp]
    list2 = [x[1] for x in inp]
    print(task1(list1, list2))
    print(task2(list1, list2))


if __name__ == "__main__":
    run()
