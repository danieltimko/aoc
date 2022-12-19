from input_utils import *


def get_adjacent(x, y, z):
    return [
        (x-1, y, z),
        (x+1, y, z),
        (x, y-1, z),
        (x, y+1, z),
        (x, y, z-1),
        (x, y, z+1),
    ]


def bfs(cubes, start, target):
    q = [start]
    visited = {start}
    count = 0
    while q:
        count += 1
        cube = q.pop(0)
        if cube == target or count > 2000:
            return True
        for adj in get_adjacent(*cube):
            if adj not in visited and adj not in cubes:
                q.append(adj)
                visited.add(adj)
    return False


def task1(cubes):
    cubes_set = set([(c[0], c[1], c[2]) for c in cubes])
    count = 0
    for x, y, z in cubes:
        for adj in get_adjacent(x, y, z):
            if adj not in cubes_set:
                count += 1
    return count


def task2(cubes):
    cubes_set = set([(c[0], c[1], c[2]) for c in cubes])
    count = 0
    for index, (x, y, z) in enumerate(cubes):
        # print(index)
        for i, adj in enumerate(get_adjacent(x, y, z)):
            # pick (9, 3, 17) as an arbitrary position and hope it's not "inside"
            if adj not in cubes_set and bfs(cubes_set, adj, (9, 3, 17)):
                count += 1
    return count


def run():
    cubes = read_n_lines_n_numbers(',')

    print(task1(cubes))
    print(task2(cubes))


if __name__ == "__main__":
    run()
