from input_utils import *


def task1(locks, keys, height):
    count = 0
    for lock in locks:
        for key in keys:
            fits = True
            for c in range(len(lock)):
                if lock[c]+key[c]+2 > height:
                    fits = False
            if fits:
                count += 1
    return count


def run():
    groups = read_n_groups_n_lines_one_string()
    keys = []
    locks = []
    height = len(groups[0])
    for group in groups:
        cols = []
        for c in range(len(group[0])):
            count = 0
            for r in range(len(group)):
                if group[r][c] == '#':
                    count += 1
            cols.append(count-1)
        if group[0].count('#') == len(group[0]):
            locks.append(cols)
        else:
            keys.append(cols)
    print(task1(locks, keys, height))


if __name__ == "__main__":
    run()
