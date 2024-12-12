from input_utils import *
from utils import *


def solve(grid, task):
    def dfs(r, c):
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        area = 0
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[r][c] != grid[nr][nc]:
                fences.add((r+(nr-r)*0.1, c+(nc-c)*0.1))
            else:
                area += dfs(nr, nc)
        return area + 1

    result = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            fences = set()
            region_area = dfs(i, j)
            if task == 1:
                result += region_area * len(fences)
            else:
                sides = 0
                rows = defaultdict(lambda: [])
                cols = defaultdict(lambda: [])
                for fr, fc in fences:
                    rows[fr].append(fc)
                    cols[fc].append(fr)
                for row in rows:
                    if row % 1 == .0:
                        continue
                    row = sorted(rows[row])
                    for k in range(len(row)-1):
                        if row[k] != row[k+1]-1:
                            sides += 1
                    sides += 1
                for col in cols:
                    if col % 1 == .0:
                        continue
                    col = sorted(cols[col])
                    for k in range(len(col)-1):
                        if col[k] != col[k+1]-1:
                            sides += 1
                    sides += 1
                result += region_area * sides
    return result


def run():
    grid = read_n_lines_one_string()
    print(solve(grid, task=1))
    print(solve(grid, task=2))


if __name__ == "__main__":
    run()
