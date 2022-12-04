from input_utils import *


def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]


def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def task1(lines):
    return sum(contains(x[0], x[1]) or contains(x[1], x[0]) for x in lines)


def task2(lines):
    return sum(overlaps(x[0], x[1]) for x in lines)


def run():
    lines = read_n_lines_one_string()
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        lines[i] = list(map(lambda s: list(map(int, s.split('-'))), lines[i]))
    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
