from input_utils import *

from collections import defaultdict


def pprint_grid(grid):
    for row in grid:
        print(''.join(row))


def expand_grid(grid: list):
    for i in range(len(grid)):
        grid[i] = ['.'] + grid[i] + ['.']
    grid.insert(0, ['.' for _ in range(len(grid[0]))])
    grid.append(['.' for _ in range(len(grid[0]))])


def reduce_grid(grid: list):
    while '#' not in grid[0]:
        grid.pop(0)
    while '#' not in grid[-1]:
        grid.pop()
    while '#' not in [r[0] for r in grid]:
        for i in range(len(grid)):
            grid[i] = grid[i][1:]
    while '#' not in [r[-1] for r in grid]:
        for i in range(len(grid)):
            grid[i] = grid[i][:-1]


def any_adjacent(grid, row, col):
    adj = [
        (row-1, col-1),
        (row-1, col),
        (row-1, col+1),
        (row, col-1),
        (row, col+1),
        (row+1, col-1),
        (row+1, col),
        (row+1, col+1),
    ]
    return any(grid[p[0]][p[1]] == '#' for p in adj)


def solve_task(grid, task):
    n_rounds = 10 if task == 1 else 10000
    grid = grid.copy()
    order = 'NSWE'
    for i in range(1, n_rounds+1):
        expand_grid(grid)
        propositions = dict()
        proposition_counts = defaultdict(lambda: 0)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '.':
                    continue
                if not any_adjacent(grid, r, c):
                    continue
                for direction in order:
                    if direction == 'N' and not any(grid[r-1][c+i] == '#' for i in [-1, 0, 1]):
                        propositions[(r, c)] = (r-1, c)
                        proposition_counts[(r-1, c)] += 1
                        break
                    if direction == 'S' and not any(grid[r+1][c+i] == '#' for i in [-1, 0, 1]):
                        propositions[(r, c)] = (r+1, c)
                        proposition_counts[(r+1, c)] += 1
                        break
                    if direction == 'W' and not any(grid[r+i][c-1] == '#' for i in [-1, 0, 1]):
                        propositions[(r, c)] = (r, c-1)
                        proposition_counts[(r, c-1)] += 1
                        break
                    if direction == 'E' and not any(grid[r+i][c+1] == '#' for i in [-1, 0, 1]):
                        propositions[(r, c)] = (r, c+1)
                        proposition_counts[(r, c+1)] += 1
                        break
        new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
        some_move = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '.':
                    continue
                if (r, c) not in propositions:
                    new_grid[r][c] = '#'
                    continue
                pr, pc = propositions[(r, c)]
                if proposition_counts[(pr, pc)] > 1:
                    new_grid[r][c] = '#'
                else:
                    some_move = True
                    new_grid[pr][pc] = '#'
        if task == 2 and not some_move:
            return i
        grid = new_grid
        reduce_grid(grid)
        order = order[1:] + order[0]
    if task == 1:
        return sum(row.count('.') for row in grid)


def run():
    grid = read_n_lines_one_string()
    grid = [list(row) for row in grid]

    print(solve_task(grid, task=1))
    print(solve_task(grid, task=2))


if __name__ == "__main__":
    run()
