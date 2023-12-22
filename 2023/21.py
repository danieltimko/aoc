import sys

from input_utils import *
from collections import defaultdict, deque


def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 'S':
                return r, c


def bfs(grid, start, task=1, odd=True, limit=None):
    if limit is not None:
        assert limit % 2 == odd
    q = deque([(start, 0)])
    visited = set()
    reachable = set()
    while q:
        (r, c), i = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if task == 1:
            if i > 64:
                break
            if i % 2 == 0:
                reachable.add((r, c))
        else:
            if limit is not None and i > limit:
                break
            if (odd and i % 2 == 1) or (not odd and i % 2 == 0):
                reachable.add((r, c))
        for adj in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            if adj[0] not in range(len(grid)) or adj[1] not in range(len(grid[0])):
                continue
            if grid[adj[0]][adj[1]] in '.S':
                q.append((adj, i+1))
    return len(reachable), reachable


def task2(grid):
    """
    assumptions:
    - grid size is odd
    - start (S) is in the center
    - center row/col and also edges are free of obstacles
    """
    start = find_start(grid)
    n_steps = 26501365
    result = 0
    # max distance to any full sub-grid
    # full meaning that all odd/even reachable nodes are in range
    dist_to_last = n_steps // len(grid) - 1
    if dist_to_last % 2 == 0:
        even = (dist_to_last+1)**2
        odd = dist_to_last**2
    else:
        even = dist_to_last**2
        odd = (dist_to_last+1)**2
    result += even * bfs(grid, start, task=2, odd=True)[0]
    result += odd * bfs(grid, start, task=2, odd=False)[0]
    # now located in the center of the last full grid
    remaining_steps = n_steps - dist_to_last * len(grid)
    parity = bool(remaining_steps % 2)
    edge_starts = [
        ((len(grid)-1, start[1]), remaining_steps-len(grid)//2-1, parity),  # U
        ((len(grid)-1, start[1]), remaining_steps-len(grid)-len(grid)//2-1, not parity),  # UU
        ((0, start[1]), remaining_steps-len(grid)//2-1, parity),  # D
        ((0, start[1]), remaining_steps-len(grid)-len(grid)//2-1, not parity),  # DD
        ((start[0], len(grid)-1), remaining_steps-len(grid)//2-1, parity),  # L
        ((start[0], len(grid)-1), remaining_steps-len(grid)-len(grid)//2-1, not parity),  # LL
        ((start[0], 0), remaining_steps-len(grid)//2-1, parity),  # R
        ((start[0], 0), remaining_steps-len(grid)-len(grid)//2-1, not parity),  # RR
    ]
    for edge_start, steps, odd in edge_starts:
        result += bfs(grid, edge_start, task=2,
                      odd=odd, limit=steps)[0]
    corner_starts = [
        ((0, 0), remaining_steps-1, dist_to_last, not parity),
        ((0, 0), remaining_steps-len(grid)-1, dist_to_last+1, parity),
        ((0, len(grid)-1), remaining_steps-1, dist_to_last, not parity),
        ((0, len(grid)-1), remaining_steps-len(grid)-1, dist_to_last+1, parity),
        ((len(grid)-1, 0), remaining_steps-1, dist_to_last, not parity),
        ((len(grid)-1, 0), remaining_steps-len(grid)-1, dist_to_last+1, parity),
        ((len(grid)-1, len(grid)-1), remaining_steps-1, dist_to_last, not parity),
        ((len(grid)-1, len(grid)-1), remaining_steps-len(grid)-1, dist_to_last+1, parity),
    ]
    for corner_start, steps, reps, odd in corner_starts:
        reachable = bfs(grid, corner_start, task=2,
                        odd=odd, limit=steps)[0]
        result += reps * reachable
    return result


def run():
    grid = read_grid()

    print(bfs(grid, find_start(grid), task=1)[0])
    print(task2(grid))


if __name__ == "__main__":
    run()
