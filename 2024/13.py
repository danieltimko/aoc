from input_utils import *

import re
import sympy as sp


def solve(arcades):
    result = [0, 0]
    for (b1x, b1y), (b2x, b2y), p in arcades:
        for i in range(2):
            px, py = p[i]
            a, b = sp.symbols('a b', integer=True)
            eq1 = sp.Eq(a * b1x + b * b2x, px)
            eq2 = sp.Eq(a * b1y + b * b2y, py)
            solutions = sp.solve((eq1, eq2), (a, b))
            if solutions:
                a = solutions[a]
                b = solutions[b]
                if a >= 0 and b >= 0:
                    result[i] += 3 * a + b
    return result


def run():
    groups = read_n_groups_n_lines_one_string()
    arcades = []
    for g in groups:
        b1x, b1y = list(map(int, re.findall(r'\d+', g[0])))
        b2x, b2y = list(map(int, re.findall(r'\d+', g[1])))
        px1, py1 = list(map(int, re.findall(r'\d+', g[2])))
        px2, py2 = px1+10000000000000, py1+10000000000000
        arcades.append(((b1x, b1y), (b2x, b2y), [(px1, py1), (px2, py2)]))
    print(solve(arcades))


if __name__ == "__main__":
    run()
