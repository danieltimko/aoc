from input_utils import *
from utils import *


def search(grid, r, c, height, task, peaks):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
    if int(grid[r][c]) != height+1:
        return 0
    if grid[r][c] == '9':
        if task == 1 and (r, c) in peaks:
            return 0
        peaks.add((r, c))
        return 1
    n = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        n += search(grid, r+dr, c+dc, int(grid[r][c]), task, peaks)
    return n


def solve(grid, task):
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '0':
                diff = search(grid, r, c, -1, task, set())
                result += diff
    return result


def run():
    grid = read_n_lines_one_string()
    print(solve(grid, task=1))
    print(solve(grid, task=2))


if __name__ == "__main__":
    run()
