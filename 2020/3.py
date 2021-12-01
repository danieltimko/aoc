
def cnt(grid, slope_right, slope_down):
    row = slope_down
    col = slope_right
    cnt = 0
    rows = len(grid)
    cols = len(grid[0])
    while row < rows:
        if grid[row][col % cols] == '#':
            cnt += 1
        row += slope_down
        col += slope_right
    return cnt


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        grid = [line for line in lines]
        slopes = [cnt(grid, 1, 1), cnt(grid, 3, 1), cnt(grid, 5, 1), cnt(grid, 7, 1), cnt(grid, 1, 2)]
        mul = 1
        for slope in slopes:
            mul *= slope
        print(mul)

run()
