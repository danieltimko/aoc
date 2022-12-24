from input_utils import *

from collections import defaultdict
from copy import deepcopy


def draw_grid(blizzards, possible_positions, width, height):
    for row in range(height):
        for col in range(width):
            count = len(blizzards[(row, col)])
            if (row, col) in possible_positions:
                c = 'X'
            elif count == 1:
                c = blizzards[(row, col)][0]
            elif count > 1:
                c = len(blizzards[(row, col)])
            elif row == 0 or col == 0 or row == height-1 or col == width-1:
                c = '#'
            else:
                c = '.'
            print(c, end='')
        print()


def is_step_possible(nxt, blizzards, width, height, target):
    if nxt == target:
        return True
    if (nxt[1] == 0 or
            nxt[1] == width-1 or
            nxt[0] == 0 or
            nxt[0] == height-1):
        return False
    return len(blizzards[(nxt[0], nxt[1])]) == 0


def move_blizzards(blizzards, width, height):
    new_blizzards = deepcopy(blizzards)
    for (row, col), bs in blizzards.items():
        for b in bs:
            new_blizzards[(row, col)].remove(b)
            if b == '<':
                nxt = (row, width-2) if col == 1 else (row, col-1)
            elif b == '>':
                nxt = (row, 1) if col == width-2 else (row, col+1)
            elif b == '^':
                nxt = (height-2, col) if row == 1 else (row-1, col)
            elif b == 'v':
                nxt = (1, col) if row == height-2 else (row+1, col)
            new_blizzards[nxt].append(b)
    for pos in new_blizzards:
        blizzards[pos] = new_blizzards[pos]


def start_trip(source, target, blizzards, width, height):
    time = 0
    possible_positions = {source}
    while target not in possible_positions:
        move_blizzards(blizzards, width, height)
        for row, col in possible_positions.copy():
            actions = [
                (row + 1, col),
                (row, col + 1),
                (row, col - 1),
                (row - 1, col)
            ]
            for nxt in actions:
                if is_step_possible(nxt, blizzards, width, height, target):
                    possible_positions.add(nxt)
        for pos in possible_positions.copy():
            if blizzards[pos]:
                possible_positions.remove(pos)
        time += 1
    return time


def solve_task(grid, task):
    blizzards = defaultdict(lambda: list())
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c = grid[row][col]
            if c not in '.#':
                blizzards[(row, col)].append(c)
    height = len(grid)
    width = len(grid[0])
    start_pos = (0, 1)
    end_pos = (height-1, width-2)
    if task == 1:
        return start_trip(start_pos, end_pos, blizzards, width, height)
    return (start_trip(start_pos, end_pos, blizzards, width, height) +
            start_trip(end_pos, start_pos, blizzards, width, height) +
            start_trip(start_pos, end_pos, blizzards, width, height))


def run():
    grid = read_n_lines_one_string()

    print(solve_task(grid, task=1))
    print(solve_task(grid, task=2))


if __name__ == "__main__":
    run()
