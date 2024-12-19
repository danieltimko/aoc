from input_utils import *
from utils import *


def solve(patterns, queries):
    def dfs(s=""):
        if len(s) == len(query):
            return 1
        suffix = query[len(s):]
        if suffix in cache:
            return cache[suffix]
        total = 0
        for p in patterns:
            if query.startswith(s+p):
                total += dfs(s+p)
        cache[suffix] = total
        return total

    cache = {}
    task1, task2 = 0, 0
    for query in queries:
        n = dfs()
        task1 += bool(n)
        task2 += n
    return task1, task2


def run():
    lines = read_n_lines_one_string()
    patterns = lines[0].split(', ')
    queries = lines[2:]
    print(solve(patterns, queries))


if __name__ == "__main__":
    run()
