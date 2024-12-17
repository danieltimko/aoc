from input_utils import *

import re


def task1(program, a, b, c):
    program = list(map(int, program.split(',')))
    i = 0
    output = ''
    while i < len(program):
        op = program[i]
        lit = program[i+1]
        combo = program[i+1]
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c

        if op == 0:
            a = int(a / 2**combo)
        elif op == 1:
            b ^= lit
        elif op == 2:
            b = combo % 8
        elif op == 3:
            if a != 0:
                i = combo-2
        elif op == 4:
            b ^= c
        elif op == 5:
            output += f'{combo % 8},'
        elif op == 6:
            b = int(a / 2**combo)
        elif op == 7:
            c = int(a / 2**combo)
        i += 2
    return output[:-1]


def task2(raw_program, b, c):
    program = list(map(int, raw_program.split(',')))
    subsolutions = [0]
    for i in range(len(program)):
        temp = []
        for prev_a in subsolutions:
            for j in range(8):
                a = prev_a*8 + j
                digit = int(task1(raw_program, a, b, c)[0])
                if digit == program[len(program)-i-1]:
                    temp.append(a)
        subsolutions = temp
    return subsolutions[0]


def run():
    lines = read_n_lines_one_string()
    a, b, c = [int(re.search(r'\d+', lines[i]).group(0)) for i in range(3)]
    program = lines[-1].split(': ')[1]
    print(task1(program, a, b, c))
    print(task2(program, b, c))


if __name__ == "__main__":
    run()
