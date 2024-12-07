from input_utils import *

import re


def solve(eqs, task):
    result = 0
    for val, eq in eqs:
        if f(val, eq, task):
            result += val
    return result


def f(val, eq, task, i=0):
    if i == len(eq):
        return eval_eq(eq) == val
    if eq[i] == ' ':
        eq[i] = '+'
        result = f(val, eq, task, i+1)
        eq[i] = ' '
        if result:
            return True
        eq[i] = '*'
        result = f(val, eq, task, i+1)
        eq[i] = ' '
        if not result and task == 2:
            eq[i] = '|'
            result = f(val, eq, i+1)
            eq[i] = ' '
        return result
    else:
        return f(val, eq, task, i+1)


def eval_eq(eq):
    ops = []
    for c in eq:
        if c in '+*|':
            ops.append(c)
    eq = list(map(int, re.split(r"[+*|]", ''.join(eq))))
    result = eq[0]
    for n, op in zip(eq[1:], ops):
        if op == '|':
            result = int(f"{result}{n}")
        else:
            result = eval(f"{result}{op}{n}")
    return result


def run():
    lines = read_n_lines_one_string()
    eqs = []
    for line in lines:
        val, eq = line.split(': ')
        eqs.append((int(val), list(eq)))
    print(solve(eqs, task=1))
    print(solve(eqs, task=2))


if __name__ == "__main__":
    run()
