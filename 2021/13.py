
def fold_along_x(grid, x):
    for row in range(len(grid)):
        assert not grid[row][x]

    new_cols = abs(len(grid[0])-1-min(x, len(grid[0])-1-x))
    new_grid = [[False for _ in range(new_cols)] for _ in range(len(grid))]

    for row in range(len(new_grid)):
        for col in range(len(new_grid[0])):
            i = x-col
            if x <= (len(grid[0]) - 1) // 2:
                if col < len(grid[0])-2*x-1:
                    new_grid[row][col] = grid[row][-col-1]
                else:
                    new_grid[row][col] = grid[row][col] or grid[row][x+i]
            else:
                if col + 2*i < len(grid[0]):
                    new_grid[row][col] = grid[row][col] or grid[row][col+2*i]
                else:
                    new_grid[row][col] = grid[row][col]
    return new_grid


def fold_along_y(grid, y):
    for col in range(len(grid[0])):
        assert not grid[y][col]

    new_rows = abs(len(grid)-1-min(y, len(grid)-1-y))
    new_grid = [[False for _ in range(len(grid[0]))] for _ in range(new_rows)]

    for col in range(len(new_grid[0])):
        for row in range(len(new_grid)):
            i = y-row
            if y <= (len(grid) - 1) // 2:
                if row < len(grid)-2*y-1:
                    new_grid[row][col] = grid[-row-1][col]
                else:
                    new_grid[row][col] = grid[row][col] or grid[y+i][col]
            else:
                if row + 2*i < len(grid):
                    new_grid[row][col] = grid[row][col] or grid[row+2*i][col]
                else:
                    new_grid[row][col] = grid[row][col]
    return new_grid


def count_dots(grid):
    return sum(row.count(True) for row in grid)


def solve(grid, folds):
    for i in range(len(folds)):
        axis, n = folds[i]
        if axis == 'x':
            grid = fold_along_x(grid, n)
        else:
            grid = fold_along_y(grid, n)
        if i == 0:
            print(f"task1 = {count_dots(grid)}")
    print_grid(grid)


def print_grid(grid):
    for row in grid:
        for c in row:
            print('.#'[c], end='')
        print()


def run():
    with open('input') as file:
        a, b = file.read().split('\n\n')
        dots = []
        folds = []
        maxrow = 0
        maxcol = 0
        for line in a.split('\n'):
            col, row = list(map(int, line.strip().split(',')))
            if row > maxrow:
                maxrow = row
            if col > maxcol:
                maxcol = col
            dots.append((row, col))

    grid = [[False for _ in range(maxcol+1)] for _ in range(maxrow+1)]

    for row, col in dots:
        grid[row][col] = True

    for line in b.split('\n'):
        axis, n = line.strip()[11:].split('=')
        folds.append((axis, int(n)))

    solve(grid, folds)


run()
