
orientations = [
    ((0, 1, 2), (1, 1, 1)),
    ((0, 1, 2), (1, -1, -1)),
    ((0, 1, 2), (-1, 1, -1)),
    ((0, 1, 2), (-1, -1, 1)),
    ((0, 2, 1), (1, 1, -1)),
    ((0, 2, 1), (1, -1, 1)),
    ((0, 2, 1), (-1, 1, 1)),
    ((0, 2, 1), (-1, -1, -1)),
    ((1, 0, 2), (1, 1, -1)),
    ((1, 0, 2), (1, -1, 1)),
    ((1, 0, 2), (-1, 1, 1)),
    ((1, 0, 2), (-1, -1, -1)),
    ((1, 2, 0), (1, 1, 1)),
    ((1, 2, 0), (1, -1, -1)),
    ((1, 2, 0), (-1, 1, -1)),
    ((1, 2, 0), (-1, -1, 1)),
    ((2, 0, 1), (1, 1, 1)),
    ((2, 0, 1), (1, -1, -1)),
    ((2, 0, 1), (-1, 1, -1)),
    ((2, 0, 1), (-1, -1, 1)),
    ((2, 1, 0), (1, 1, -1)),
    ((2, 1, 0), (1, -1, 1)),
    ((2, 1, 0), (-1, 1, 1)),
    ((2, 1, 0), (-1, -1, -1)),
]


def try_all_orientations(scanner_a, scanner_b):
    for i in range(24):
        axes, rotation = orientations[i]
        for a in scanner_a:
            for b in scanner_b:
                scanner_position = (a[0]-b[axes[0]]*rotation[0],
                                    a[1]-b[axes[1]]*rotation[1],
                                    a[2]-b[axes[2]]*rotation[2])
                overlap = 0
                absolute_points = set()
                for relative in scanner_b:
                    absolute = (scanner_position[0] + relative[axes[0]] * rotation[0],
                                scanner_position[1] + relative[axes[1]] * rotation[1],
                                scanner_position[2] + relative[axes[2]] * rotation[2])
                    absolute_points.add(absolute)
                    if absolute in scanner_a:
                        overlap += 1
                if overlap >= 12:
                    return scanner_position, absolute_points


def locate_scanners(arr):
    scanner_positions = {0: (0, 0, 0)}
    beacons = [set() for _ in range(len(arr))]
    beacons[0] = set(arr[0])
    cache = set()
    while len(scanner_positions) < len(arr):
        located = False
        for i in scanner_positions:
            for j in range(len(arr)):
                if (i, j) in cache or (j, i) in cache or j in scanner_positions:
                    continue
                print(f"trying to match {i} and {j}")
                if result := try_all_orientations(beacons[i], arr[j]):
                    print(f"[{j}] scanner position = {result[0]}")
                    scanner_positions[j] = result[0]
                    beacons[j] = result[1]
                    located = True
                cache.add((i, j))
            if located:
                break
        if len(scanner_positions) == len(arr):
            break
    return scanner_positions, beacons


def task1(beacons):
    return len(set([beacon for scanner in beacons for beacon in scanner]))


def task2(scanner_positions):
    return max(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
               for a in scanner_positions.values() for b in scanner_positions.values())


def run():
    with open('input') as file:
        scanners = []
        for line in file.readlines():
            if line.startswith('---'):
                scanners.append([])
            elif line[0] != '\n':
                scanners[-1].append(tuple(map(int, line.strip().split(','))))

        scanner_positions, beacons = locate_scanners(scanners)
        print(task1(beacons))
        print(task2(scanner_positions))


run()
