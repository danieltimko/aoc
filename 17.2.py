from copy import deepcopy
from math import inf


def pprint_space(space, z, w):
    print("===========================")
    print(f"z: {z}, w: {w}")
    x_from, x_to, y_from, y_to, _, _, _, _ = get_bounds(space)
    for x in range(x_from, x_to+1):
        for y in range(y_from, y_to+1):
            if y not in space[x] or z not in space[x][y] or w not in space[x][y][z]:
                print('.', end='')
            else:
                print(".#"[space[x][y][z][w]], end='')
        print()
    print("========================")


def count_active(space):
    count = 0
    for x, ys in space.items():
        for y, zs in ys.items():
            for z, ws in zs.items():
                for w, val in ws.items():
                    if val:
                        count += 1
    return count


def get_status(space, x, y, z, w):
    if x not in space.keys() or \
            y not in space[x].keys() or \
            z not in space[x][y].keys() or \
            w not in space[x][y][z].keys():
        return False
    return space[x][y][z][w]


def count_active_neighbors(space, x, y, z, w):
    active_neighbors = 0
    for x2 in range(x - 1, x + 2):
        for y2 in range(y - 1, y + 2):
            for z2 in range(z - 1, z + 2):
                for w2 in range(w - 1, w + 2):
                    if x2 == x and y2 == y and z2 == z and w2 == w:
                        continue
                    if get_status(space, x2, y2, z2, w2):
                        active_neighbors += 1
    return active_neighbors


def update(space, x, y, z, w, value):
    if x not in space.keys():
        space[x] = {}
    if y not in space[x].keys():
        space[x][y] = {}
    if z not in space[x][y].keys():
        space[x][y][z] = {}
    space[x][y][z][w] = value


def update_cube(space, new_space, x, y, z, w):
    active_neighbors = count_active_neighbors(space, x, y, z, w)
    # print(f"active neighbors of [{x}][{y}][{z}][{w}] = {active_neighbors}")
    if get_status(space, x, y, z, w):
        if not 2 <= active_neighbors <= 3:
            update(new_space, x, y, z, w, False)
    elif active_neighbors == 3:
        update(new_space, x, y, z, w, True)


def get_bounds(space):
    x_from, x_to = inf, -inf
    y_from, y_to = inf, -inf
    z_from, z_to = inf, -inf
    w_from, w_to = inf, -inf
    for x, ys in space.items():
        if x < x_from:
            x_from = x
        if x > x_to:
            x_to = x
        for y, zs in ys.items():
            if y < y_from:
                y_from = y
            if y > y_to:
                y_to = y
            for z, ws in zs.items():
                if z < z_from:
                    z_from = z
                if z > z_to:
                    z_to = z
                for w in ws.keys():
                    if w < w_from:
                        w_from = w
                    if w > w_to:
                        w_to = w
    return x_from, x_to, y_from, y_to, z_from, z_to, w_from, w_to


def task2(space, cycles):
    cycle = 0
    while cycle < cycles:
        new_space = deepcopy(space)
        x_from, x_to, y_from, y_to, z_from, z_to, w_from, w_to = get_bounds(space)

        for x in range(x_from - 1, x_to + 2):
            for y in range(y_from - 1, y_to + 2):
                for z in range(z_from - 1, z_to + 2):
                    for w in range(w_from - 1, w_to + 2):
                        update_cube(space, new_space, x, y, z, w)

        space = new_space
        cycle += 1
    return count_active(space)


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        space = {}
        for x in range(len(lines)):
            space[x] = {}
            for y in range(len(lines[x])):
                space[x][y] = {}
                space[x][y][0] = {0: lines[x][y] == '#'}
        print(task2(space, 6))


run()
