from input_utils import *


rotation_left = {
    '^': '<',
    '>': '^',
    'v': '>',
    '<': 'v',
}

rotation_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}


def fill_to_width(grid):
    max_width = max(len(row) for row in grid)
    for i in range(len(grid)):
        grid[i] = grid[i] + (' ' * (max_width - len(grid[i])))


def get_next_position_task_1(grid, row, col, facing):
    if facing == 'v':
        if row == len(grid)-1 or grid[row+1][col] == ' ':
            row = 0
            while grid[row][col] == ' ':
                row += 1
            return row, col, facing
        return row+1, col, facing
    if facing == '^':
        if row == 0 or grid[row-1][col] == ' ':
            row = len(grid)-1
            while grid[row][col] == ' ':
                row -= 1
            return row, col, facing
        return row-1, col, facing
    if facing == '>':
        if col == len(grid[row])-1 or grid[row][col+1] == ' ':
            col = 0
            while grid[row][col] == ' ':
                col += 1
            return row, col, facing
        return row, col+1, facing
    if facing == '<':
        if col == 0 or grid[row][col-1] == ' ':
            col = len(grid[row])-1
            while grid[row][col] == ' ':
                col -= 1
            return row, col, facing
        return row, col-1, facing


def get_next_position_task_2(row, col, facing):
    # wow, so robust
    if facing == 'v':
        if row == 49 and col in range(100, 150):
            return col-50, 99, '<'
        if row == 149 and col in range(50, 100):
            return 100+col, 49, '<'
        if row == 199 and col in range(0, 50):
            return 0, 100+col, 'v'
        return row+1, col, facing
    if facing == '^':
        if row == 100 and col in range(0, 50):
            return 50+col, 50, '>'
        if row == 0 and col in range(50, 100):
            return 100+col, 0, '>'
        if row == 0 and col in range(100, 150):
            return 199, col-100, '^'
        return row-1, col, facing
    if facing == '>':
        if row in range(0, 50) and col == 149:
            return 149-row, 99, '<'
        if row in range(50, 100) and col == 99:
            return 49, 50+row, '^'
        if row in range(100, 150) and col == 99:
            return 149-row, 149, '<'
        if row in range(150, 200) and col == 49:
            return 149, row-100, '^'
        return row, col+1, facing
    if facing == '<':
        if row in range(0, 50) and col == 50:
            return 149-row, 0, '>'
        if row in range(50, 100) and col == 50:
            return 100, row-50, 'v'
        if row in range(100, 150) and col == 0:
            return 149-row, 50, '>'
        if row in range(150, 200) and col == 0:
            return 0, row-100, 'v'
        return row, col-1, facing


def get_next_position(grid, row, col, facing, task):
    if task == 1:
        return get_next_position_task_1(grid, row, col, facing)
    result = get_next_position_task_2(row, col, facing)
    return result


def solve_task(grid, s, start_at, task):
    steps = []
    while s:
        if s[0].isnumeric():
            nextl = s.find('L') if 'L' in s else len(s)
            nextr = s.find('R') if 'R' in s else len(s)
            nxt = min(nextl, nextr)
            steps.append(int(s[:nxt]))
            s = s[nxt:]
        elif s[0] == 'R':
            steps.append('R')
            s = s[1:]
        elif s[0] == 'L':
            steps.append('L')
            s = s[1:]
    row, col = start_at
    facing = '>'
    fill_to_width(grid)
    for step in steps:
        if step == 'L':
            facing = rotation_left[facing]
        elif step == 'R':
            facing = rotation_right[facing]
        else:
            for _ in range(step):
                next_row, next_col, next_facing = get_next_position(grid, row, col, facing, task)
                if grid[next_row][next_col] == '#':
                    break
                row, col, facing = next_row, next_col, next_facing
    return (row+1)*1000 + (col+1)*4 + '>v<^'.find(facing)


def run():
    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()
    grid = list(map(lambda line: line[:-1], lines[:-2]))
    s = lines[-1]
    start_at = 0, grid[0].find('.')  # (row, col)

    print(solve_task(grid, s, start_at, task=1))
    print(solve_task(grid, s, start_at, task=2))


if __name__ == "__main__":
    run()
