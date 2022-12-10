from input_utils import *


def task1(lines):
    values = []
    x = 1
    for op in lines:
        values.append(x)
        if op[0] == 'addx':
            x += int(op[1])
            values.append(x)
    result = 0
    for x in [20, 60, 100, 140, 180, 220]:
        result += values[x-2]*x
    return result, values


def task2(lines):
    values = task1(lines)[1]
    crt = ""
    for i in range(len(values)):
        crt += ".#"[abs(values[i-1] - i%40) <= 1]
    for i in range(6):
        print(crt[i*40:(i+1)*40])


def run():
    lines = read_n_lines_n_strings(' ')

    print(task1(lines)[0])
    task2(lines)


if __name__ == "__main__":
    run()
