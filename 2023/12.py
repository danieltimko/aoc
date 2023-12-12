from input_utils import *


# BF for part1
"""
def find_all_options(s, i=0):
    if i == len(s):
        return [s]
    options = []
    if s[i] == "?":
        options += find_all_options(s[:i]+"#"+s[i+1:], i+1)
        options += find_all_options(s[:i]+"."+s[i+1:], i+1)
        return options
    else:
        return find_all_options(s, i+1)


def verify(s, rules):
    groups = list(filter(lambda x: x != "", s.split('.')))
    if len(groups) != len(rules):
        return False
    for i in range(len(rules)):
        if len(groups[i]) != rules[i]:
            return False
    return True


def task1(rows):
    result = 0
    for springs, rules in rows:
        all_options = find_all_options(springs)
        valid_options = list(filter(lambda option: verify(option, rules), all_options))
        result += len(valid_options)
    return result
"""


# DP for part 1+2
def solve(rows, task):
    def calc_state(si=0, ri=0, length=0):
        # (char index, rule index, current # group length)
        state = (si, ri, length)
        if state in cache:
            return cache[state]
        if si == len(springs):
            if ri == len(rules):
                return length == 0
            elif ri == len(rules) - 1:
                return length == rules[ri]
            return 0

        cache[state] = 0
        if springs[si] in ".?":
            if length == 0:
                # next . -- just continue
                cache[state] += calc_state(si + 1, ri, 0)
            elif ri < len(rules) and rules[ri] == length:
                # . ending a group of # -- move on to the next rule
                cache[state] += calc_state(si + 1, ri + 1, 0)
        if springs[si] in "#?":
            # next # in group -- continue
            cache[state] += calc_state(si + 1, ri, length + 1)
        return cache[state]

    cache = {}
    if task == 2:
        for i in range(len(rows)):
            base = rows[i][0]
            for _ in range(4):
                rows[i][0] += f"?{base}"
            rows[i][1] *= 5
    result = 0
    for springs, rules in rows:
        result += calc_state(0, 0, 0)
        cache.clear()
    return result


def run():
    lines = read_n_lines_one_string()
    rows = list(map(lambda row: [row[0], list_to_int(row[1].split(","))],
                    [line.split(' ') for line in lines]))

    print(solve(rows, task=1))
    print(solve(rows, task=2))


if __name__ == "__main__":
    run()
