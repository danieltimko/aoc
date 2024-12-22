from input_utils import *
from utils import *

from itertools import permutations


numerical_keypad = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    ' ': (3, 0),
    '0': (3, 1),
    'A': (3, 2),
}

directional_keypad = {
    ' ': (0, 0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}


def solve(codes, layers):
    def numerical(buttons):
        r, c = numerical_keypad['A']
        total_cost = 0
        for b in buttons:
            br, bc = numerical_keypad[b]
            dr, dc = r - br, c - bc
            presses = (-dr * 'v') if dr < 0 else (dr * '^')
            presses += (-dc * '>') if dc < 0 else (dc * '<')
            min_cost = float("inf")
            for p in set(permutations(presses)):
                p = ''.join(p)
                good = True
                tr, tc = r, c
                for tb in p:
                    tr = tr + directions[tb][0]
                    tc = tc + directions[tb][1]
                    if (tr, tc) == numerical_keypad[' ']:
                        good = False
                if not good:
                    continue
                cost = 0
                positions = [directional_keypad['A']] * layers
                for button in f"{p}A":
                    cost += directional(button, positions, layers-1)
                min_cost = min(min_cost, cost)
            total_cost += min_cost
            r, c = br, bc
        return total_cost

    def directional(b, positions, layer):
        if layer == 0:
            return 1
        r, c = positions[layer]
        br, bc = directional_keypad[b]
        state = layer, r, c, br, bc
        if state in cache:
            cost = cache[state]
            positions[layer] = (br, bc)
            return cost
        dr, dc = r - br, c - bc
        presses = (-dr * 'v') if dr < 0 else (dr * '^')
        presses += (-dc * '>') if dc < 0 else (dc * '<')
        min_cost = float("inf")
        for p in set(permutations(presses)):
            temp_positions = positions.copy()
            p = ''.join(p)
            tr, tc = r, c
            good = True
            for tb in p:
                tr = tr + directions[tb][0]
                tc = tc + directions[tb][1]
                if (tr, tc) == directional_keypad[' ']:
                    good = False
            if good:
                cost = 0
                for button in f"{p}A":
                    cost += directional(button, temp_positions, layer-1)
                min_cost = min(min_cost, cost)
        positions[layer] = directional_keypad[b]
        cache[state] = min_cost
        return min_cost

    cache = {}
    return sum(numerical(code) * int(code[:-1].lstrip('0')) for code in codes)


def run():
    codes = read_n_lines_one_string()
    print(solve(codes, layers=3))
    print(solve(codes, layers=26))


if __name__ == "__main__":
    run()
