import math

from collections import defaultdict
from copy import deepcopy


def compute_lcm(x, y):
    return (x*y)//math.gcd(x, y)


def lcm(arr):
    # math.lcm() in Python3.9+
    result = arr[0]
    for n in arr:
        result = (n * result) // (math.gcd(n, result))
    return result


def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def toposort(adj, vertices):
    stack = []
    visited = defaultdict(lambda: False)
    for v in vertices:
        if not visited[v]:
            _toposort_visit(v, adj, visited, stack)
    return stack


def _toposort_visit(v, adj, visited, stack):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            _toposort_visit(i, adj, visited, stack)
    stack.append(v)
