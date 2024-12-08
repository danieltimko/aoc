from input_utils import *
from utils import *

from itertools import combinations


def solve(grid, task):
    freqs = defaultdict(lambda: [])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                freqs[grid[r][c]].append((r, c))
    antinodes = set()
    for vals in freqs.values():
        for (r1, c1), (r2, c2) in list(combinations(vals, 2)):
            rdiff = r1-r2
            cdiff = c1-c2
            if task == 1:
                node1 = (r1+rdiff, c1+cdiff)
                node2 = (r2-rdiff, c2-cdiff)
                if _is_on_map(grid, *node1):
                    antinodes.add(node1)
                if _is_on_map(grid, *node2):
                    antinodes.add(node2)
            elif task == 2:
                r, c = r1, c1
                while _is_on_map(grid, r, c):
                    antinodes.add((r, c))
                    r += rdiff
                    c += cdiff
                r, c = r2, c2
                while _is_on_map(grid, r, c):
                    antinodes.add((r, c))
                    r -= rdiff
                    c -= cdiff
    return len(antinodes)


def _is_on_map(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def run():
    grid = read_grid()

    print(solve(grid, task=1))
    print(solve(grid, task=2))


if __name__ == "__main__":
    run()
