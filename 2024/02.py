from input_utils import *


def _is_safe(line):
    if sorted(line) != line and sorted(line, reverse=True) != line:
        return False
    for i in range(len(line) - 1):
        diff = abs(line[i] - line[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def task1(lines):
    return sum(_is_safe(line) for line in lines)


def task2(lines):
    count = 0
    for line in lines:
        if _is_safe(line):
            count += 1
            continue
        for i in range(len(line)):
            if _is_safe(line[:i]+line[i+1:]):
                count += 1
                break
    return count


def run():
    lines = read_n_lines_n_numbers(sep=' ')
    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
