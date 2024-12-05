from input_utils import *
from utils import *

from collections import defaultdict


def solve(rules, updates):
    m = defaultdict(lambda: [])
    for rule in rules:
        m[rule[0]].append(rule[1])
    task1 = 0
    task2 = 0
    for update in updates:
        good = True
        for x in update:
            for y in m[x]:
                if y in update and update.index(x) > update.index(y):
                    good = False
                    break
            if not good:
                break
        if good:
            task1 += update[len(update)//2]
        else:
            adj = defaultdict(lambda: [])
            vertices = set()
            for x, y in rules:
                if x in update and y in update:
                    adj[x].append(y)
                    vertices.add(x)
                    vertices.add(y)
            task2 += toposort(adj, vertices)[len(update)//2]
    return task1, task2


def run():
    groups = read_n_groups_n_lines_one_string()
    rules = list(map(lambda line: list(map(int, line.split('|'))), groups[0]))
    updates = list(map(lambda line: list(map(int, line.split(','))), groups[1]))
    print(solve(rules, updates))


if __name__ == "__main__":
    run()
