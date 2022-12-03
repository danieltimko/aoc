from input_utils import *


def _to_prio(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def task1(lines):
    prios = 0
    for line in lines:
        left, right = line[:len(line)//2], line[len(line)//2:]
        for c in set(left) & set(right):
            prios += _to_prio(c)
    return prios


def task2(lines):
    prios = 0
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    for group in groups:
        for c in set(group[0]) & set(group[1]) & set(group[2]):
            prios += _to_prio(c)
    return prios


def run():
    lines = read_n_lines_one_string()
    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
