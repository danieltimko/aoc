from input_utils import *

from queue import Queue


def solve(grid, cheat_length=20, threshold=100):
    def bfs(sr, sc, er, ec, cache, limit=float("inf")):
        if (sr, sc, er, ec) in cache:
            return cache[(sr, sc, er, ec)]
        visited = set()
        q = Queue()
        q.put((sr, sc, 0))
        while q:
            r, c, t = q.get()
            if (r, c) in visited or grid[r][c] == '#':
                continue
            if t > limit:
                return float("inf")
            visited.add((r, c))
            if (r, c) == (er, ec):
                cache[(sr, sc, er, ec)] = t
                return t
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != '#':
                    q.put((nr, nc, t+1))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                start = r, c
            elif grid[r][c] == 'E':
                end = r, c

    cost_no_cheating = bfs(*start, *end, {})  # ~10000
    result = 0
    cache = {}
    for r1 in range(len(grid)):
        for c1 in range(len(grid[0])):
            if grid[r1][c1] != '#':
                partial_cost = bfs(*start, r1, c1, cache, limit=cost_no_cheating-threshold)
                for r2 in range(r1-cheat_length, r1+cheat_length+1):
                    if r2 < 0 or r2 >= len(grid):
                        continue
                    max_dc = cheat_length-abs(r1-r2)
                    for c2 in range(c1-max_dc, c1+max_dc+1):
                        if c2 < 0 or c2 >= len(grid[0]) or grid[r2][c2] == '#':
                            continue
                        cheat_cost = abs(r1-r2) + abs(c1-c2)
                        if cost_no_cheating-threshold-partial_cost-cheat_cost < 0:
                            continue
                        cost = partial_cost + cheat_cost + bfs(
                            r2, c2, *end, cache, limit=cost_no_cheating-threshold-partial_cost-cheat_cost
                        )
                        if cost_no_cheating - cost >= threshold:
                            result += 1
    return result


def run():
    grid = read_grid()
    print(solve(grid, cheat_length=2, threshold=100))
    print(solve(grid, cheat_length=20, threshold=100))


if __name__ == "__main__":
    run()
