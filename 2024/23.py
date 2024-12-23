from input_utils import *


def task1(graph):
    triplets = set()
    for node in graph:
        neighbors = graph.get(node, [])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if neighbors[i] in graph.get(neighbors[j], []):
                    triplets.add(tuple(sorted([node, neighbors[i], neighbors[j]])))
    return len(triplets)


def task2(graph):
    def bron_kerbosch(R, P, X):
        if not P and not X:
            yield R
        V = P.copy()
        for v in V:
            N_v = set(graph[v])
            yield from bron_kerbosch(R | {v}, P & N_v, X & N_v)
            P.remove(v)
            X.add(v)

    max_cliq = max(bron_kerbosch(set(), set(graph), set()), key=lambda c: len(c))
    return ','.join(sorted(max_cliq))


def run():
    graph = read_graph(sep='-', weighted=False, bidirectional=True)
    print(task1(graph))
    print(task2(graph))


if __name__ == "__main__":
    run()
