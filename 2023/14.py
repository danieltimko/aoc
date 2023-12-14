from input_utils import *
from collections import deque
from copy import deepcopy


def calculate_load(grid):
    load = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                load += (len(grid)-r)
    return load


def task1(grid, replace=True):
    for c in range(len(grid[0])):
        free_slots = deque()
        for r in range(len(grid)):
            if grid[r][c] == ".":
                free_slots.append(r)
            if grid[r][c] == "O":
                if not free_slots:
                    continue
                nxt = free_slots.popleft()
                if replace:
                    grid[nxt][c] = "O"
                    grid[r][c] = "."
                free_slots.append(r)
            if grid[r][c] == "#":
                free_slots.clear()
    return calculate_load(grid)


def rotate(grid):
    # clockwise
    new_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_grid[c][len(grid[0])-1-r] = grid[r][c]
    return new_grid


def hash_grid(grid):
    return ''.join(c for row in grid for c in row)


def execute_cycle(grid):
    for _ in range(4):
        task1(grid)
        grid = rotate(grid)
    return grid


def task2(grid):
    cache = {0: hash_grid(grid)}
    hashes = {hash_grid(grid)}
    i = 0
    while i != 1000000000:
        grid = execute_cycle(grid)
        h = hash_grid(grid)
        i += 1
        matches = [k for k, v in cache.items() if v == h]
        if matches:
            start = matches[0]
            length = i-start
            repetitions = (1000000000-start) // length
            i = start + repetitions*length
        cache[i] = h
        hashes.add(h)
    return calculate_load(grid)


def run():
    grid = read_grid()

    print(task1(grid, replace=True))
    print(task2(grid))


if __name__ == "__main__":
    run()
