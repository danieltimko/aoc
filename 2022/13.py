from input_utils import *

import json
from functools import cmp_to_key


def compare(fst, snd):
    if type(fst) != list and type(snd) != list:
        if fst == snd:
            return 0
        return -1 if fst < snd else 1
    if type(fst) != list:
        fst = [fst]
    elif type(snd) != list:
        snd = [snd]
    if len(fst) == 0 or len(snd) == 0:
        if len(fst) == len(snd):
            return 0
        return -1 if len(fst) == 0 else 1
    for i in range(len(fst)):
        if i >= len(snd):
            return 1
        if (result := compare(fst[i], snd[i])) != 0:
            return result
    return 0 if len(fst) == len(snd) else -1


def task1(pairs):
    count = 0
    for i in range(len(pairs)):
        fst = json.loads(pairs[i][0])
        snd = json.loads(pairs[i][1])
        result = compare(fst, snd)
        if result == -1:
            count += i+1
    return count


def task2(pairs):
    packets = []
    for pair in pairs:
        packets.append(json.loads(pair[0]))
        packets.append(json.loads(pair[1]))
    dividers = [[[2]], [[6]]]
    packets += dividers
    packets.sort(key=cmp_to_key(compare))

    return (packets.index(dividers[0])+1) * (packets.index(dividers[1])+1)


def run():
    pairs = read_n_groups_n_lines_one_string()

    print(task1(pairs))
    print(task2(pairs))


if __name__ == "__main__":
    run()
