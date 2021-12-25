from copy import deepcopy


def simulate(grid):
    step = 0
    while True:
        new_grid1 = deepcopy(grid)
        changed = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != '>':
                    continue
                right = 0 if col == len(grid[0])-1 else col+1
                if grid[row][right] == '.':
                    changed = True
                    new_grid1[row][right] = '>'
                    new_grid1[row][col] = '.'
        new_grid2 = deepcopy(new_grid1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if new_grid1[row][col] != 'v':
                    continue
                bottom = 0 if row == len(grid)-1 else row + 1
                if new_grid1[bottom][col] == '.':
                    changed = True
                    new_grid2[bottom][col] = 'v'
                    new_grid2[row][col] = '.'
        step += 1
        if not changed:
            break
        grid = new_grid2
    return step


def run():
    with open('input') as file:
        grid = list(map(lambda line: list(line.strip()), file.readlines()))
        print(simulate(deepcopy(grid)))


run()
