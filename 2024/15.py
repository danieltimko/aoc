from input_utils import *
from utils import *


def task1(grid, moves):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                rr, rc = r, c
    for m in moves:
        if m == '<':
            dr, dc = (0, -1)
        elif m == '>':
            dr, dc = (0, 1)
        elif m == 'v':
            dr, dc = (1, 0)
        else:
            dr, dc = (-1, 0)
        if grid[rr+dr][rc+dc] == 'O':
            r, c = rr+dr, rc+dc
            while grid[r][c] == 'O':
                r += dr
                c += dc
            if grid[r][c] == '.':
                grid[rr+dr][rc+dc] = '.'
                grid[r][c] = 'O'
        if grid[rr+dr][rc+dc] == '.':
            grid[rr][rc] = '.'
            rr, rc = rr+dr, rc+dc
            grid[rr][rc] = '@'
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                result += 100*r + c
    return result


def task2(grid, moves):
    grid = modify_grid(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                rr, rc = r, c
    for m in moves:
        if m == '<':
            dr, dc = (0, -1)
        elif m == '>':
            dr, dc = (0, 1)
        elif m == 'v':
            dr, dc = (1, 0)
        else:
            dr, dc = (-1, 0)
        if grid[rr+dr][rc+dc] == '[':
            move_box(grid, rr+dr, rc+dc, m)
        elif grid[rr+dr][rc+dc] == ']':
            move_box(grid, rr+dr, rc+dc-1, m)
        if grid[rr+dr][rc+dc] == '.':
            grid[rr][rc] = '.'
            rr, rc = rr+dr, rc+dc
            grid[rr][rc] = '@'
    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                result += 100*r + c
    return result


def modify_grid(grid):
    new_grid = []
    for r in grid:
        row = ''
        for c in r:
            if c == '#':
                row += '##'
            elif c == 'O':
                row += '[]'
            elif c == '.':
                row += '..'
            elif c == '@':
                row += '@.'
        new_grid.append(list(row))
    return new_grid


def move_box(grid, br, bc, m):
    if m == '<':
        if grid[br][bc-1] == ']':
            move_box(grid, br, bc-2, m)
        if grid[br][bc-1] == '.':
            grid[br][bc-1] = '['
            grid[br][bc] = ']'
            grid[br][bc+1] = '.'
    elif m == '>':
        if grid[br][bc+2] == '[':
            move_box(grid, br, bc+2, m)
        if grid[br][bc+2] == '.':
            grid[br][bc] = '.'
            grid[br][bc+1] = '['
            grid[br][bc+2] = ']'
    else:
        dr = 1 if m == 'v' else -1
        if grid[br+dr][bc] == '#' or grid[br+dr][bc+1] == '#':
            return
        if grid[br+dr][bc] == '[':
            move_box(grid, br+dr, bc, m)
        elif grid[br+dr][bc] == ']':
            if grid[br+dr][bc+1] == '[':
                new_grid = deepcopy(grid)
                move_box(new_grid, br+dr, bc-1, m)
                move_box(new_grid, br+dr, bc+1, m)
                if new_grid[br+dr][bc] == '.' and new_grid[br+dr][bc+1] == '.':
                    move_box(grid, br+dr, bc-1, m)
                    move_box(grid, br+dr, bc+1, m)
            else:
                move_box(grid, br+dr, bc-1, m)
        elif grid[br+dr][bc+1] == '[':
            move_box(grid, br+dr, bc+1, m)
        if grid[br+dr][bc] == '.' and grid[br+dr][bc+1] == '.':
            grid[br+dr][bc] = '['
            grid[br+dr][bc+1] = ']'
            grid[br][bc] = '.'
            grid[br][bc+1] = '.'


def run():
    groups = read_n_groups_n_lines_one_string()
    grid = list(map(lambda line: list(line.strip()), groups[0]))
    moves = "".join(groups[1])
    print(task1(deepcopy(grid), moves))
    print(task2(deepcopy(grid), moves))


if __name__ == "__main__":
    run()
