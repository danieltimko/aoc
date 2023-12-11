from input_utils import *


def find_empty_rows(grid):
    rows = []
    for row in range(len(grid)):
        if grid[row].count("#") == 0:
            rows.append(row)
    return rows


def find_empty_cols(grid):
    cols = []
    for col in range(len(grid[0])):
        if [grid[row][col] for row in range(len(grid))].count("#") == 0:
            cols.append(col)
    return cols


def find_galaxies(grid):
    galaxies = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                galaxies.append((row, col))
    return galaxies


def dist(r1, c1, r2, c2, empty_rows, empty_cols, task):
    d = abs(r2-r1) + abs(c2-c1)
    gap = 1 if task == 1 else 999999
    for r in empty_rows:
        if r in range(r1, r2):
            d += gap
    for c in empty_cols:
        if c in range(c1, c2) or c in range(c2, c1):
            d += gap
    return d


def solve(grid, task):
    empty_rows = find_empty_rows(grid)
    empty_cols = find_empty_cols(grid)
    galaxies = find_galaxies(grid)
    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            result += dist(*galaxies[i], *galaxies[j], empty_rows, empty_cols, task)
    return result


def run():
    grid = read_n_lines_one_string()

    print(solve(grid, task=1))
    print(solve(grid, task=2))


if __name__ == "__main__":
    run()
