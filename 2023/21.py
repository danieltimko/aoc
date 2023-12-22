import sys

from input_utils import *
from collections import defaultdict, deque


def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 'S':
                return r, c


def bfs(grid, start, task=1, odd=True, limit=0):
    q = deque([(start, 0)])
    visited = set()
    reachable = set()
    while q:
        (r, c), i = q.popleft()
        if (r, c) in visited:  # TODO move
            continue
        visited.add((r, c))
        if task == 1:
            if i > 64:
                break
            if i % 2 == 0:
                reachable.add((r, c))
        else:
            if limit and i > limit:
                break
            if (odd and i % 2 == 1) or (not odd and i % 2 == 0):
                reachable.add((r, c))
        for adj in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            if adj[0] not in range(len(grid)) or adj[1] not in range(len(grid[0])):
                continue
            if grid[adj[0]][adj[1]] in '.S' and adj not in visited:
                q.append((adj, i+1))
    return len(reachable), reachable


def count_dots(grid):
    return sum(row.count('.') for row in grid)


def get_reachable_nodes(grid, start):
    q = deque([(start, 0)])
    visited = set()
    while q:
        (r, c), i = q.popleft()
        if (r, c) in visited:  # TODO move
            continue
        visited.add((r, c))
        for adj in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
            if adj[0] not in range(len(grid)) or adj[1] not in range(len(grid[0])):
                continue
            if grid[adj[0]][adj[1]] in '.S' and adj not in visited:
                q.append((adj, i + 1))
    return visited


def task2(grid):
    start = find_start(grid)
    n_steps = 26501365

    # number of nodes reachable from specific node in odd/even number of steps
    # subresults = {
    #     from_position: len(get_reachable_nodes(grid, from_position))
    #     for from_position in [
    #         start,  # odd
    #         (start[0], 0),  # even
    #         (start[0], len(grid)-1),  # even
    #         (0, start[1]),  # even
    #         (len(grid)-1, start[1]),  # even
    #         # TODO probably also need to include corners
    #     ]
    # }
    result = 0
    # number of grids that are fully flooded (with odd number of steps)
    # assumption: grid size is also odd, and start (S) is in the center

    def sequence(n):
        # 1, 5, 13, 25, 41, 61, ...
        return 2*(n+1)**2 - 2*(n+1) + 1

    # max distance to any fully flooded sub-grid
    # fully flooded meaning that all odd-reachable nodes are in range
    dist_to_last = n_steps // len(grid) - 1
    fully_flooded_grids = sequence(dist_to_last)
    # print(fully_flooded_grids * len(grid))
    # TODO WIP
    if dist_to_last % 2 == 0:
        even = (dist_to_last+1)**2
        odd = dist_to_last**2
    else:
        even = dist_to_last**2
        odd = (dist_to_last+1)**2
    result += odd * bfs(grid, start, task=2, odd=True)[0]
    result += even * bfs(grid, start, task=2, odd=False)[0]
    # now located in the center of the last fully flooded grid
    remaining_steps = n_steps - dist_to_last * len(grid)
    print(result)
    print(remaining_steps, "remaining steps")
    edge_starts = [
        ((len(grid)-1, start[1]), remaining_steps-len(grid)//2-1, True),  # U
        ((len(grid)-1, start[1]), remaining_steps-len(grid)-len(grid)//2-1, False),  # UU
        ((0, start[1]), remaining_steps-len(grid)//2-1, True),  # D
        ((0, start[1]), remaining_steps-len(grid)-len(grid)//2-1, False),  # DD
        ((start[0], len(grid)-1), remaining_steps-len(grid)//2-1, True),  # L
        ((start[0], len(grid)-1), remaining_steps-len(grid)-len(grid)//2-1, False),  # LL
        ((start[0], 0), remaining_steps-len(grid)//2-1, True),  # R
        ((start[0], 0), remaining_steps-len(grid)-len(grid)//2-1, False),  # RR
    ]
    for edge_start, steps, odd in edge_starts:
        result += bfs(grid, edge_start, task=2,
                      odd=odd, limit=steps)[0]
    corner_starts = [
        ((0, 0), remaining_steps-1, dist_to_last, True),
        ((0, 0), remaining_steps-len(grid)-1, dist_to_last+1, False),
        ((0, len(grid)-1), remaining_steps-1, dist_to_last, True),
        ((0, len(grid)-1), remaining_steps-len(grid)-1, dist_to_last+1, False),
        ((len(grid)-1, 0), remaining_steps-1, dist_to_last, True),
        ((len(grid)-1, 0), remaining_steps-len(grid)-1, dist_to_last+1, False),
        ((len(grid)-1, len(grid)-1), remaining_steps-1, dist_to_last, True),
        ((len(grid)-1, len(grid)-1), remaining_steps-len(grid)-1, dist_to_last+1, False),
    ]
    for corner_start, steps, reps, odd in corner_starts:
        reachable = bfs(grid, corner_start, task=2,
                        odd=odd, limit=steps)[0]
        result += reps * reachable
    print(614864614526014)
    return result


def run():
    grid = read_grid()

    # print(bfs(grid, find_start(grid), task=1)[0])
    print(task2(grid))
    614864614526014

    """
    1. calculate number of steps required to flood a single grid 
    when entering with % 2 == 0/1, along with number of flooded tiles.
    note: does it matter from where am I entering? probably not
    2. start at grid coordinates (0, 0) and move by 1 to all sides with 
    incremented steps counter and call recursively on neighbors, like a
    grid-level BFS... do it until counter would exceed the limit
    remember coordinates of visited grids
    3. manually run local BFS here (on all grids on border)
    
    - this will not be enough though... some kind of jumping and caching
    will be required 
    
    - try to calculate for each coordinate in a single grid the distances
    to all sides    
    
     
    """

if __name__ == "__main__":
    run()
