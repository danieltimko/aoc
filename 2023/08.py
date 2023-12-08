from input_utils import *
import itertools
import math


def compute_lcm(x, y):
    return (x*y)//math.gcd(x, y)


def lcm(arr):
    # math.lcm() in Python3.9+
    result = arr[0]
    for n in arr:
        result = (n * result) // (math.gcd(n, result))
    return result


def simulate_single_start(steps, nodes, starting_node="AAA", task=1):
    current = starting_node
    i = 0
    for step in itertools.cycle(steps):
        current = nodes[current][step == "R"]
        i += 1
        if current == "ZZZ" or (task == 2 and current[-1] == "Z"):
            return i


def simulate_multiple_starts(steps, nodes):
    starts = list(filter(lambda k: k[-1] == 'A', nodes.keys()))
    factors = []
    for start in starts:
        factors.append(simulate_single_start(steps, nodes, start, 2))
    return lcm(factors)  # with assumption that single start has single end


def run():
    lines = read_n_lines_one_string()
    steps = lines[0]
    nodes = {}
    for line in lines[2:]:
        node = line.split(' = ')[0]
        left = line.split(' = ')[1].split(', ')[0][1:]
        right = line.split(' = ')[1].split(', ')[1][:-1]
        nodes[node] = (left, right)

    print(simulate_single_start(steps, nodes))
    print(simulate_multiple_starts(steps, nodes))


if __name__ == "__main__":
    run()
