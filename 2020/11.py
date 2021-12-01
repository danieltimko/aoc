from copy import deepcopy, copy


def get_seat(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return "?"
    return grid[row][col]


def count_occupied(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == "#":
                count += 1
    return count


def count_adjacent(grid, row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            if get_seat(grid, r, c) == "#":
                count += 1
    return count


def look(grid, row, col, row_change, col_change):
    while True:
        row += row_change
        col += col_change
        seat = get_seat(grid, row, col)
        if seat in "?L":
            return False
        elif seat == "#":
            return True


def count_first_seen(grid, row, col):
    count = 0
    for row_change in range(-1, 2):
        for col_change in range(-1, 2):
            if row_change == col_change == 0:
                continue
            if look(grid, row, col, row_change, col_change):
                count += 1
    return count


def tick(grid, task):
    change = False
    new_grid = deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            seat = get_seat(grid, row, col)
            if seat in "?.":
                continue
            elif seat == "#":
                if (task == 1 and count_adjacent(grid, row, col) >= 4) or \
                        task == 2 and count_first_seen(grid, row, col) >= 5:
                    change = True
                    new_grid[row][col] = "L"
            elif seat == "L":
                if (task == 1 and count_adjacent(grid, row, col) == 0) or \
                        task == 2 and count_first_seen(grid, row, col) == 0:
                    change = True
                    new_grid[row][col] = "#"
    return new_grid, change


def get_result(grid, task):
    b = True
    while b:
        grid, b = tick(grid, 1) if task == 1 else tick(grid, 2)
    return count_occupied(grid)


def run():
    with open('input') as file:
        grid = list(map(lambda line: list(line.strip()), file.readlines()))
        print(get_result(grid, task=1), get_result(grid, task=2))


run()
