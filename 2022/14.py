from input_utils import *


def solve(grid, task):
    count = 0
    lowest = max(map(lambda r: r[1], grid))
    floor = lowest+2
    while True:
        sandx = 500
        sandy = 0
        while True:
            if task == 1 and sandy > lowest:
                return count
            if sandy == floor-1:
                grid.add((sandx, floor))
                grid.add((sandx-1, floor))
                grid.add((sandx+1, floor))
            if (sandx, sandy+1) not in grid:
                sandy = sandy+1
            elif (sandx-1, sandy+1) not in grid:
                sandx = sandx-1
                sandy = sandy+1
            elif (sandx+1, sandy+1) not in grid:
                sandx = sandx+1
                sandy = sandy+1
            else:
                grid.add((sandx, sandy))
                count += 1
                break
        if task == 2 and (sandx, sandy) == (500, 0):
            return count


def run():
    rocks = set()
    lines = read_n_lines_n_strings(' -> ')
    for points in lines:
        for i in range(1, len(points)):
            prev = list(map(int, points[i-1].split(',')))
            current = list(map(int, points[i].split(',')))
            if prev[0] == current[0]:
                for j in range(min(prev[1], current[1]), max(prev[1], current[1])+1):
                    rocks.add((prev[0], j))
            elif prev[1] == current[1]:
                for j in range(min(prev[0], current[0]), max(prev[0], current[0])+1):
                    rocks.add((j, prev[1]))

    print(solve(rocks.copy(), task=1))
    print(solve(rocks.copy(), task=2))


if __name__ == "__main__":
    run()
