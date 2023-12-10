from input_utils import *


def find_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                return row, col


def get_neighbors(pipe):
    if pipe == "|":
        return [(-1, 0), (1, 0)]
    if pipe == "-":
        return [(0, -1), (0, 1)]
    if pipe == "L":
        return [(-1, 0), (0, 1)]
    if pipe == "J":
        return [(-1, 0), (0, -1)]
    if pipe == "7":
        return [(1, 0), (0, -1)]
    if pipe == "F":
        return [(1, 0), (0, 1)]
    assert pipe == '.'
    return []


def task1(grid):
    maxdist = 0
    start = find_start(grid)
    stack = [(start, 0)]
    visited = set()
    loop = []
    while stack:
        (r, c), dist = stack.pop()
        if (r, c) in visited:
            continue
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        visited.add((r, c))
        loop.append((r, c))
        maxdist = max(maxdist, dist)
        if grid[r][c] == "S":
            neighbors = [(dr, dc) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                         if (-dr, -dc) in get_neighbors(grid[r + dr][c + dc])]
        else:
            neighbors = get_neighbors(grid[r][c])
        for (dr, dc) in neighbors:
            stack.append(((r+dr, c+dc), dist+1))
    return loop


def calculate_area(grid, visited, loop, start):
    stack = [start]
    reaches_outside = False
    reaches_loop = False
    area = 0
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            reaches_outside = True
            continue
        if (r, c) in loop:
            reaches_loop = True
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        area += 1
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            stack.append((r+dr, c+dc))
    return reaches_loop, reaches_outside, area


def get_lefthand_neighbors(pipe, direction):
    if pipe == "|":
        return [(0, -1)] if direction == "up" else [(0, 1)]
    if pipe == "-":
        return [(-1, 0)] if direction == "right" else [(1, 0)]
    if pipe == "L":
        return [(1, 0), (0, -1)] if direction == "left" else []
    if pipe == "J":
        return [(1, 0), (0, 1)] if direction == "down" else []
    if pipe == "7":
        return [(-1, 0), (0, 1)] if direction == "right" else []
    if pipe == "F":
        return [(-1, 0), (0, -1)] if direction == "up" else []
    if pipe == "S":
        # TODO edge case
        return []


def update_direction(current_direction, pipe):
    if pipe == "L":
        return {"down": "right", "left": "up"}[current_direction]
    if pipe == "J":
        return {"down": "left", "right": "up"}[current_direction]
    if pipe == "7":
        return {"right": "down", "up": "left"}[current_direction]
    if pipe == "F":
        return {"up": "right", "left": "down"}[current_direction]
    return current_direction


def task2(grid, loop):
    # start at | for convenience
    while True:
        r, c = loop[0]
        pr, pc = loop[-1]
        pipe = grid[r][c]
        previous_pipe = grid[pr][pc]
        if pipe == "|" and previous_pipe != "S":
            break
        loop = loop[1:] + [loop[0]]
    direction = "up" if loop[-1][0] > loop[0][0] else "down"
    lefthand_nodes = []
    for r, c in loop:
        pipe = grid[r][c]
        lefthand_nodes += [(r+dr, c+dc) for dr, dc in get_lefthand_neighbors(pipe, direction)]
        direction = update_direction(direction, pipe)
    loop_set = set(loop)
    visited = set()
    total_area = 0
    for r, c in lefthand_nodes:
        if (r, c) not in visited:
            reaches_loop, reaches_outside, area = calculate_area(grid, visited, loop_set, (r, c))
            if reaches_loop and not reaches_outside:
                total_area += area
    return total_area


def run():
    grid = read_n_lines_one_string()

    loop = task1(grid)
    print(len(loop) // 2)
    print(task2(grid, loop))


if __name__ == "__main__":
    run()
