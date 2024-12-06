from input_utils import *
from utils import *


moves = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}


def find_guard(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                return r, c


def task1(grid):
    r, c = find_guard(grid)
    visited = set()
    while True:
        visited.add((r, c))
        direction = grid[r][c]
        nr = r + moves[direction][0]
        nc = c + moves[direction][1]
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            return len(visited)
        if grid[nr][nc] == '#':
            dirs = list(moves.keys())
            grid[r][c] = dirs[(dirs.index(direction)+1) % 4]
        else:
            grid[r][c] = '.'
            grid[nr][nc] = direction
            r, c = nr, nc


def is_stuck(grid, r, c):
    visited = set()
    while True:
        direction = grid[r][c]
        if (r, c, direction) in visited:
            return True
        visited.add((r, c, direction))
        nr = r + moves[direction][0]
        nc = c + moves[direction][1]
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            return False
        if grid[nr][nc] == '#':
            dirs = list(moves.keys())
            grid[r][c] = dirs[(dirs.index(direction)+1) % 4]
        else:
            grid[r][c] = '.'
            grid[nr][nc] = direction
            r, c = nr, nc


def task2(grid):
    r, c = find_guard(grid)
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                tgrid = deepcopy(grid)
                tgrid[i][j] = '#'
                if is_stuck(tgrid, r, c):
                    result += 1
    return result


def run():
    grid = read_grid()
    print(task1(deepcopy(grid)))
    print(task2(deepcopy(grid)))


if __name__ == "__main__":
    run()
