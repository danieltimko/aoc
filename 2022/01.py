from input_utils import *


def task1(groups):
    sums = list(map(sum, groups))
    return max(sums), sums


def task2(groups):
    return sum(sorted(task1(groups)[1])[-3:])


def run():
    groups = read_n_groups_n_lines_one_number()
    print(task1(groups)[0])
    print(task2(groups))


if __name__ == "__main__":
    run()
