from input_utils import *


def is_valid_position(row, col, nrows, ncols):
    return 0 <= row < nrows and 0 <= col < ncols


def is_valid_move(cfrom, cto, task):
    if cfrom == 'S':
        cfrom = 'a'
    elif cfrom == 'E':
        cfrom = 'z'
    if cto == 'S':
        cto = 'a'
    elif cto == 'E':
        cto = 'z'
    if task == 1:
        return ord(cto) - ord(cfrom) <= 1
    else:
        return ord(cfrom) - ord(cto) <= 1


def bfs(grid, start, task):
    q = [(start, 0, [start])]
    visited = {start}
    finish_chars = "E" if task == 1 else "aS"
    while q:
        position, nsteps, path = q.pop(0)
        row, col = position
        if grid[row][col] in finish_chars:
            return nsteps
        for neighbor in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if neighbor not in visited:
                if is_valid_position(neighbor[0], neighbor[1], len(grid), len(grid[0])) and \
                        is_valid_move(grid[row][col], grid[neighbor[0]][neighbor[1]], task):
                    q.append((neighbor, nsteps+1, path + [neighbor]))
                    visited.add(neighbor)


def run():
    grid = read_n_lines_one_string()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start1 = (row, col)
            if grid[row][col] == 'E':
                start2 = (row, col)

    print(bfs(grid, start1, task=1))
    print(bfs(grid, start2, task=2))


if __name__ == "__main__":
    run()
