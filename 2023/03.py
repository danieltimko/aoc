from input_utils import *


def get_numbers(grid):
    numbers = [[] for _ in range(len(grid))]
    for r in range(len(grid)):
        num_start = None
        for c in range(len(grid)+1):
            if c != len(grid) and grid[r][c].isdigit():
                if num_start is None:
                    num_start = c
            elif num_start is not None:
                numbers[r].append((num_start, c - 1))
                num_start = None
    return numbers


def task(grid):
    numbers = get_numbers(grid)
    non_part_numbers = []
    symbols = {}
    for row in range(len(numbers)):
        for start, end in numbers[row]:
            is_part_number = False
            found_symbols = []
            for r in range(row-1, row+2):
                for c in range(start-1, end+2):
                    if (r in range(0, len(grid)) and
                        c in range(0, len(grid[0])) and
                            grid[r][c] != '.' and not grid[r][c].isdigit()):
                        found_symbols.append((r, c))
                        is_part_number = True
            num = int(grid[row][start:end + 1])
            if is_part_number:
                non_part_numbers.append(num)
            for s in found_symbols:
                if s in symbols:
                    if not symbols[s][1]:
                        symbols[s] = symbols[s][0] * num, True
                else:
                    symbols[s] = num, False
    return sum(non_part_numbers), sum([s[0] for s in symbols.values() if s[1]])


def run():
    grid = read_n_lines_one_string()
    print(task(grid))


if __name__ == "__main__":
    run()
