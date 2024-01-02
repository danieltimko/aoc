from input_utils import *
import networkx as nx


def run():
    lines = read_n_lines_one_string()
    graph = nx.Graph()
    for line in lines:
        node, neighbors = line.split(': ')
        for nei in neighbors.split(' '):
            graph.add_edge(node, nei, weight=1)

    size, partitions = nx.stoer_wagner(graph)
    assert size == 3
    print(len(partitions[0]) * len(partitions[1]))


if __name__ == "__main__":
    run()
