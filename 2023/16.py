from input_utils import *
from collections import defaultdict


def deflect(beam, mirror):
    row, col, direction = beam
    if mirror == '\\':
        return {
            "right": (row+1, col, "down"),
            "up": (row, col-1, "left"),
            "left": (row-1, col, "up"),
            "down": (row, col+1, "right")
        }[direction]
    return {
        "right": (row-1, col, "up"),
        "up": (row, col+1, "right"),
        "left": (row+1, col, "down"),
        "down": (row, col-1, "left")
    }[direction]


def split(beam, splitter):
    row, col, direction = beam
    if splitter == "|" and direction in ("left", "right"):
        return {(row-1, col, "up"), (row+1, col, "down")}
    elif splitter == "-" and direction in ("up", "down"):
        return {(row, col-1, "left"), (row, col+1, "right")}
    else:
        return {make_step(beam)}


def make_step(beam):
    row, col, direction = beam
    return {
        "left": (row, col-1, direction),
        "right": (row, col+1, direction),
        "up": (row-1, col, direction),
        "down": (row+1, col, direction),
    }[direction]


def task1(grid, starting_beam=(0, 0, "right")):
    beams = {starting_beam}
    visited = defaultdict(lambda: set())
    while True:
        new_beams = set()
        stop = True
        for beam in beams:
            row, col, direction = beam
            if (row not in range(0, len(grid)) or
                    col not in range(0, len(grid[0])) or
                    direction in visited[(row, col)]):
                continue
            stop = False
            visited[(row, col)].add(direction)
            tile = grid[row][col]
            if tile in "/\\":
                new_beams.add(deflect(beam, tile))
            elif tile in "|-":
                new_beams |= split(beam, tile)
            else:
                new_beams.add(make_step(beam))
        beams = new_beams
        if stop:
            return len(visited)


def task2(grid):
    ans = 0
    for r in range(len(grid)):
        ans = max(ans, task1(grid, (r, 0, "right")))
        ans = max(ans, task1(grid, (r, len(grid[0])-1, "left")))
    for c in range(len(grid[0])):
        ans = max(ans, task1(grid, (0, c, "down")))
        ans = max(ans, task1(grid, (len(grid)-1, c, "up")))
    return ans


def run():
    grid = read_grid()

    print(task1(grid))
    print(task2(grid))


if __name__ == "__main__":
    run()
