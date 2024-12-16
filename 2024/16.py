from input_utils import *

from queue import PriorityQueue


def solve(grid, task):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = r, c
            if grid[r][c] == 'E':
                end = r, c
    pq = PriorityQueue()
    pq.put((0, start, (0, 1), set()))
    visited = dict()
    tiles = set()
    min_cost = 0
    while not pq.empty():
        cost, (r, c), d, path = pq.get()
        if (r, c) == end:
            if task == 1:
                return cost
            if min_cost and cost > min_cost:
                return len(tiles)
            tiles |= path | {(r, c)}
            min_cost = cost
        if (r, c, d) in visited and cost > visited[(r, c, d)]:
            continue
        visited[(r, c, d)] = cost
        for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if d == (dr, dc):
                rotation_cost = 0
            elif d[0] == -dr or d[1] == -dc:
                rotation_cost = 2000
            else:
                rotation_cost = 1000
            if grid[nr][nc] != '#' and (nr, nc) not in path:
                pq.put((cost+rotation_cost+1, (nr, nc), (dr, dc), path | {(r, c)}))
    return len(tiles)


def run():
    grid = read_grid()
    print(solve(grid, 1))
    print(solve(grid, 2))


if __name__ == "__main__":
    run()
