from input_utils import *


def is_visible(grid, r, c):
    # from top
    x = [grid[i][c] for i in range(r)]
    if max(x) < grid[r][c]:
        return True

    # from bot
    x = [grid[i][c] for i in range(len(grid)-1, r, -1)]
    if max(x) < grid[r][c]:
        return True

    # from left
    x = [grid[r][i] for i in range(c)]
    if max(x) < grid[r][c]:
        return True

    # from right
    x = [grid[r][i] for i in range(len(grid[0])-1, c, -1)]
    return max(x) < grid[r][c]


def count_score(arr, val):
    for i in range(len(arr)):
        if arr[len(arr)-1-i] >= val:
            return i+1
    return len(arr)


def task1(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r == 0 or r == len(grid)-1 or
                    c == 0 or c == len(grid[0])-1 or
                    is_visible(grid, r, c)):
                count += 1
    return count


def task2(grid):
    maxscore = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            top = [grid[i][c] for i in range(r)]
            bot = [grid[i][c] for i in range(len(grid)-1, r, -1)]
            left = [grid[r][i] for i in range(c)]
            right = [grid[r][i] for i in range(len(grid[0])-1, c, -1)]
            maxscore = max(maxscore, (count_score(top, grid[r][c]) *
                                      count_score(bot, grid[r][c]) *
                                      count_score(left, grid[r][c]) *
                                      count_score(right, grid[r][c])))
    return maxscore


def run():
    grid = read_n_lines_one_string()

    print(task1(grid))
    print(task2(grid))


if __name__ == "__main__":
    run()
