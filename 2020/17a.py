from copy import deepcopy
from math import inf


def pprint_space(space):
    print("===========================")
    row_from, row_to, col_from, col_to, dim_from, dim_to = get_bounds(space)
    for dimension in range(dim_from, dim_to+1):
        print(f"z={dimension}")
        any_active = False
        for row in range(row_from, row_to+1):
            for col in range(col_from, col_to+1):
                if get_status(space, row, col, dimension):
                    any_active = True
        if any_active:
            for row in range(row_from, row_to+1):
                for col in range(col_from, col_to+1):
                    print(".#"[get_status(space, row, col, dimension)], end='')
                print()
        print()
    print("========================")


def count_active(space):
    count = 0
    for row, cols in space.items():
        for col, dims in cols.items():
            for dim, val in dims.items():
                if val:
                    count += 1
    return count


def get_status(space, row, col, dimension):
    if row not in space.keys() or \
            col not in space[row].keys() or \
            dimension not in space[row][col].keys():
        return False
    return space[row][col][dimension]


def count_active_neighbors(space, row, col, dimension):
    active_neighbors = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            for d in range(dimension - 1, dimension + 2):
                if r == row and c == col and d == dimension:
                    continue
                if get_status(space, r, c, d):
                    active_neighbors += 1
    return active_neighbors


def update(space, row, col, dimension, value):
    if row not in space.keys():
        space[row] = {}
    if col not in space[row].keys():
        space[row][col] = {}
    space[row][col][dimension] = value


def update_cube(space, new_space, row, col, dimension):
    active_neighbors = count_active_neighbors(space, row, col, dimension)
    # print(f"active neighbors of [{row}][{col}][{dimension}] = {active_neighbors}")
    if get_status(space, row, col, dimension):
        if not 2 <= active_neighbors <= 3:
            update(new_space, row, col, dimension, False)
    elif active_neighbors == 3:
        update(new_space, row, col, dimension, True)


def get_bounds(space):
    row_from, row_to = inf, -inf
    col_from, col_to = inf, -inf
    dim_from, dim_to = inf, -inf
    for row, cols in space.items():
        if row < row_from:
            row_from = row
        if row > row_to:
            row_to = row
        for col, dims in cols.items():
            if col < col_from:
                col_from = col
            if col > col_to:
                col_to = col
            for dim in dims.keys():
                if dim < dim_from:
                    dim_from = dim
                if dim > dim_to:
                    dim_to = dim
    return row_from, row_to, col_from, col_to, dim_from, dim_to


def task1(space, cycles):
    cycle = 0
    while cycle < cycles:
        # print(f"{cycle+1}. cycle")
        new_space = deepcopy(space)
        row_from, row_to, col_from, col_to, dim_from, dim_to = get_bounds(space)

        for row in range(row_from - 1, row_to + 2):
            for col in range(col_from - 1, col_to + 2):
                for dimension in range(dim_from - 1, dim_to + 2):
                    update_cube(space, new_space, row, col, dimension)

        # pprint_space(new_space)
        space = new_space
        cycle += 1
    return count_active(space)


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        space = {}
        for row in range(len(lines)):
            space[row] = {}
            for col in range(len(lines[row])):
                space[row][col] = {0: lines[row][col] == '#'}
        print(task1(space, 6))


run()
