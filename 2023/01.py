from input_utils import *


def task1(inp):
    result = 0
    for line in inp:
        digits = list(filter(lambda c: c.isdigit(), line))
        result += int(f"{digits[0]}{digits[-1]}")
    return result


def task2(inp):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = 0
    for line in inp:
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for word in words:
                    if line[i:].startswith(word):
                        digits.append(words.index(word) + 1)
        result += int(f"{digits[0]}{digits[-1]}")
    return result


def run():
    inp = read_n_lines_one_string()
    print(task1(inp))
    print(task2(inp))


if __name__ == "__main__":
    run()
