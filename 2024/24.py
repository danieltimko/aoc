from input_utils import *
from utils import *


def task1(groups):
    vals = dict(map(lambda s: (s.split(': ')[0], int(s.split(': ')[1])), groups[0]))
    eqs = []
    for line in groups[1]:
        eqs.append(re.match(r"(\w+)\s+(\w+)\s+(\w+)\s*->\s*(\w+)", line).groups())
    zs = {}
    while not zs or not all(z != -1 for z in zs.values()):
        for l, op, r, w in eqs:
            if l in vals and r in vals:
                vals[w] = solve_gate(vals[l], vals[r], op)
            if w.startswith('z'):
                zs[w] = vals[w] if w in vals else -1
    z = ''.join(str(vals[w]) for w in sorted(zs, key=lambda w: int(w[1:]), reverse=True))
    return int(z, 2)


def solve_gate(l, r, op):
    if op == "AND":
        return l & r
    elif op == "OR":
        return l | r
    elif op == "XOR":
        return l ^ r


def run():
    groups = read_n_groups_n_lines_one_string()
    print(task1(groups))
    # cph,jqn,kwb,qkf,tgr,z12,z16,z24


if __name__ == "__main__":
    run()
