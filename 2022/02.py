from input_utils import *

mapping = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

beats = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

loses_to = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}


def _to_num(c):
    if c in "ABC":
        return ord(c) - ord('A') + 1
    return ord(c) - ord('X') + 1


def task1(lines):
    score = 0
    for line in lines:
        l, r = map(_to_num, line)
        if l == r:
            outcome = 3
        elif (l == 1 and r == 2) or (l == 2 and r == 3) or (l == 3 and r == 1):
            outcome = 6
        else:
            outcome = 0
        score += outcome + r
    return score


def task2(lines):
    score = 0
    for line in lines:
        if line[1] == 'Z':
            move = loses_to[line[0]]
            score += 6 + _to_num(move)
        elif line[1] == 'Y':
            score += 3 + _to_num(line[0])
        else:
            score += _to_num(beats[line[0]])
    return score


def run():
    lines = read_n_lines_n_strings(' ')
    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
