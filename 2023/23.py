from input_utils import *
from collections import defaultdict, deque


def task1(grid, target):
    q = deque()
    q.append(((0, 1), set(), 0))
    longest_hike = 0
    while q:
        (r, c), path, dist = q.popleft()
        if (r, c) in path:
            continue
        if (r, c) == target:
            longest_hike = max(longest_hike, dist)
            continue
        if grid[r][c] == 'v':
            q.append(((r+1, c), path | {(r, c)}, dist + 1))
            continue
        if grid[r][c] == '>':
            q.append(((r, c+1), path | {(r, c)}, dist + 1))
            continue
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr not in range(len(grid)) or nc not in range(len(grid[0])):
                continue
            if grid[nr][nc] == '#':
                continue
            q.append(((nr, nc), path | {(r, c)}, dist + 1))
    return longest_hike


def task2(grid, target):
    graph = compress_grid(grid)
    q = deque()
    q.append(((0, 1), [], 0))
    longest_hike = 0
    while q:
        (r, c), path, dist = q.popleft()
        if (r, c) in path:
            continue
        if (r, c) == target:
            longest_hike = max(longest_hike, dist)
            continue
        for (nr, nc), d in graph[(r, c)]:
            q.append(((nr, nc), path + [(r, c)], dist + d))
    return longest_hike


def is_junction(grid, r, c):
    neighbors = 0
    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if nr not in range(len(grid)) or nc not in range(len(grid)):
            continue
        if grid[nr][nc] != '#':
            neighbors += 1
    return neighbors > 2


def compress_grid(grid):
    graph = defaultdict(lambda: [])
    stack = [((0, 1), (0, 1), 0)]
    visited = set()
    while stack:
        (r, c), last_junction, dist = stack.pop()
        if (((r, c) == (len(grid)-1, len(grid)-2)) or
                (is_junction(grid, r, c) and last_junction != (r, c))):
            graph[last_junction].append(((r, c), dist))
            graph[(r, c)].append((last_junction, dist))
            last_junction = (r, c)
            dist = 0
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for nr, nc in [(r - 1, c),
                       (r + 1, c),
                       (r, c - 1),
                       (r, c + 1)]:
            if nr not in range(len(grid)) or nc not in range(len(grid[0])):
                continue
            if grid[nr][nc] == '#':
                continue
            stack.append(((nr, nc), last_junction, dist + 1))
    return graph


def run():
    grid = read_grid()
    target = (len(grid)-1, len(grid)-2)

    print(task1(grid, target))
    print(task2(grid, target))


if __name__ == "__main__":
    run()
