from input_utils import *
from utils import range_intersect

from collections import defaultdict
from copy import deepcopy


def can_move(bricks, brick):
    if brick[0][2] == 1:
        return False
    for b in bricks:
        if b[1][2] != brick[0][2]-1:
            continue
        x_intersect = range_intersect(range(b[0][0], b[1][0]+1),
                                      range(brick[0][0], brick[1][0]+1))
        y_intersect = range_intersect(range(b[0][1], b[1][1]+1),
                                      range(brick[0][1], brick[1][1]+1))
        if x_intersect and y_intersect:
            return False
    return True


def fall(bricks, brick, n=1):
    # TODO brick lookup could be surely optimized
    if not can_move(bricks, brick):
        return False
    brick[0][2] -= n
    brick[1][2] -= n
    return True


def solve(bricks):
    any_fell = True
    while any_fell:
        any_fell = False
        for brick in bricks:
            any_fell = fall(bricks, brick) or any_fell
    bricks = list(map(lambda b: (tuple(b[0]), tuple(b[1])), bricks))
    supported_by = defaultdict(lambda: set())
    supports = defaultdict(lambda: set())
    for b1 in bricks:
        for b2 in bricks:
            if b1[1][2] != b2[0][2]-1:
                continue
            x_intersect = range_intersect(range(b1[0][0], b1[1][0] + 1),
                                          range(b2[0][0], b2[1][0] + 1))
            y_intersect = range_intersect(range(b1[0][1], b1[1][1] + 1),
                                          range(b2[0][1], b2[1][1] + 1))
            if x_intersect and y_intersect:
                supported_by[b2].add(b1)
                supports[b1].add(b2)
    disintegrable = []
    total_impact = 0
    for brick in bricks:
        if all(len(supported_by[brick_up]) > 1 for brick_up in supports[brick]):
            disintegrable.append(brick)
        else:
            total_impact += calc_impact(deepcopy(supports),
                                        deepcopy(supported_by), brick) - 1
    return len(disintegrable), total_impact


def calc_impact(supports, supported_by, brick):
    impact = 1
    for brick_up in supports[brick]:
        supported_by[brick_up].remove(brick)
        if not supported_by[brick_up]:
            impact += calc_impact(supports, supported_by, brick_up)
    return impact


def run():
    lines = read_n_lines_one_string()
    bricks = []
    for line in lines:
        ends = line.split('~')
        bricks.append([list_to_int(end.split(',')) for end in ends])
    bricks.sort(key=lambda cube: cube[1][2])
    print(solve(bricks))


if __name__ == "__main__":
    run()
