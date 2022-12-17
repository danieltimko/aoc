from input_utils import *

import itertools


rock_types = [
    [
        "..####.",
    ],
    [
        "...#...",
        "..###..",
        "...#...",
    ],
    [
        "....#..",
        "....#..",
        "..###..",
    ],
    [
        "..#....",
        "..#....",
        "..#....",
        "..#....",
    ],
    [
        "..##...",
        "..##...",
    ]
]


def draw_grid(grid):
    for row in range(len(grid)):
        for col in grid[-row-1]:
            print(col, end='')
        print()
    print()


def move_left(grid, positions):
    positions.sort(key=lambda p: p[1])
    new_positions = []
    for row, col in positions:
        assert grid[row][col] == '#'
        if col == 0 or (grid[row][col-1] == '#' and (row, col-1) not in positions):
            return positions
    for row, col in positions:
        new_positions.append((row, col-1))
        grid[row][col-1] = '#'
        grid[row][col] = '.'
    return new_positions


def move_right(grid, positions):
    positions.sort(key=lambda p: p[1], reverse=True)
    new_positions = []
    for row, col in positions:
        assert grid[row][col] == '#'
        if col == 6 or (grid[row][col+1] == '#' and (row, col+1) not in positions):
            return positions
    for row, col in positions:
        new_positions.append((row, col+1))
        grid[row][col+1] = '#'
        grid[row][col] = '.'
    return new_positions


def move_down(grid, positions):
    positions.sort(key=lambda p: p[0])
    new_positions = []
    for row, col in positions:
        assert grid[row][col] == '#'
        if row == 0 or (grid[row][col] == '#' and grid[row-1][col] == '#' and (row-1, col) not in positions):
            return None
    for row, col in positions:
        new_positions.append((row-1, col))
        grid[row-1][col] = '#'
        grid[row][col] = '.'
    return new_positions


def fall(grid, rock, pattern):
    for _ in range(3):
        grid.append(list('.......'))
    for row in range(len(rock)):
        grid.append(list(rock[-row-1]))
    positions = []
    for row in range(len(grid)-len(rock), len(grid)):
        for col in range(7):
            if grid[row][col] == '#':
                positions.append((row, col))

    while True:
        pattern_index, direction = next(pattern)
        if direction == '>':
            positions = move_right(grid, positions)
        elif direction == '<':
            positions = move_left(grid, positions)
        if (positions := move_down(grid, positions)) is None:
            while grid[-1] == list('.......'):
                grid.pop()
            return pattern_index


def get_depths(grid):
    depths = ''  # interpret it as string so it's hashable
    for c in range(7):
        i = 1
        while i < len(grid) and grid[-i][c] != '#':
            i += 1
        depths += str(i) + ','
    return depths


def task1(pattern):
    rocks = itertools.cycle(enumerate(rock_types))
    grid = []
    pattern = itertools.cycle(enumerate(pattern))
    for i in range(2022):
        fall(grid, next(rocks)[1], pattern)
    draw_grid(grid)
    return len(grid)


def task2(pattern):
    """
    The state is (position in pattern, stone index, depths of columns)
    Value of state is (iteration, height)
    """
    iterations = 1000000000000
    rocks = itertools.cycle(enumerate(rock_types))
    grid = []
    pattern = itertools.cycle(enumerate(pattern))
    states = dict()
    cycle_found = False
    i = 0
    while i <= iterations:
        rock_index, rock = next(rocks)
        pattern_index = fall(grid, rock, pattern)
        depths = get_depths(grid)
        state = (rock_index, pattern_index, depths)
        if not cycle_found and state in states:
            cycle_found = True
            cycle_start, starting_height = states[state]
            cycle_length = i - cycle_start
            repetitions = (iterations-i) // cycle_length
            # print(f"CYCLE at iteration {i}: length {cycle_length}, {repetitions} repetitions")
            # print(f"starting at {cycle_start}, ending at {i}")
            # print(f"height increment: {len(grid) - starting_height} ({len(grid)} - {starting_height})")
            i += cycle_length * repetitions
            hidden_height = repetitions * (len(grid) - starting_height)
            # print(f"hidden height {hidden_height}")
        else:
            states[state] = (i, len(grid))
        i += 1
    return len(grid) + hidden_height - 1  # TODO why is it off-by-one?


def run():
    with open(INPUT_FILE_PATH) as f:
        pattern = f.readlines()[0].strip()

    print(task1(pattern))
    print(task2(pattern))


if __name__ == "__main__":
    run()
