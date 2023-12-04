from input_utils import *


def task1(arr):
    result = 0
    for winning, mine in arr:
        n = len(set(winning) & set(mine))
        result += int(2 ** (n-1))
    return result


def task2(arr):
    counts = [1] * len(arr)
    for i, (winning, mine) in enumerate(arr):
        n = len(set(winning) & set(mine))
        for j in range(i+1, i+n+1):
            if j >= len(arr):
                break
            counts[j] += counts[i]
    return sum(counts)


def run():
    inp = read_n_lines_one_string()
    arr = []
    for line in inp:
        line = line.split(': ')[1]
        winning = line.split(' | ')[0].split(' ')
        winning = list(filter(lambda x: x != '', winning))
        winning = list(map(lambda x: int(x), winning))
        mine = line.split(' | ')[1].split(' ')
        mine = list(filter(lambda x: x != '', mine))
        mine = list(map(lambda x: int(x), mine))
        arr.append((mine, winning))

    print(task1(arr))
    print(task2(arr))


if __name__ == "__main__":
    run()
