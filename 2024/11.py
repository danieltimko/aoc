from input_utils import *
from utils import *


def solve(arr, n):
    stones = defaultdict(lambda: 0)
    for x in arr:
        stones[x] = 1
    for rep in range(n):
        for x, c in stones.copy().items():
            s = str(x)
            stones[x] -= c
            if stones[x] == 0:
                del stones[x]
            if x == 0:
                stones[1] += c
            elif len(s) % 2 == 0:
                stones[int(s[:len(s) // 2])] += c
                stones[int(s[len(s) // 2:])] += c
            else:
                stones[x*2024] += c
    return sum(stones.values())


def run():
    arr = read_one_line_n_numbers(sep=' ')
    print(solve(arr, n=25))
    print(solve(arr, n=75))


if __name__ == "__main__":
    run()
