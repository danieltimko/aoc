from input_utils import *
import re


def task1(lines):
    result = 0
    for line in lines:
        matches = re.findall(r"mul\(\d+,\d+\)", line)
        for match in matches:
            a, b = match[4:-1].split(',')
            result += int(a) * int(b)
    return result


def task2(lines):
    result = 0
    enabled = True
    for line in lines:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for m in matches:
            if m == "do()":
                enabled = True
            elif m == "don't()":
                enabled = False
            elif enabled:
                a, b = m[4:-1].split(',')
                result += int(a) * int(b)
    return result


def run():
    lines = read_n_lines_one_string()

    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
