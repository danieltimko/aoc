
def solve(G, task):
    def DFS(vertex, visited, double=None):
        if vertex.islower() and vertex in visited:
            if task == 2 and not double and vertex not in ['start', 'end']:
                double = vertex
            else:
                return 0
        if vertex.islower():
            visited.add(vertex)
        if vertex == 'end':
            visited.remove(vertex)
            return 1
        count = 0
        if vertex in G:
            for neighbor in G[vertex]:
                count += DFS(neighbor, visited, double)
        if vertex.islower() and vertex != double:
            visited.remove(vertex)
        return count

    return DFS('start', set())


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split('-')), file.readlines()))
        G = {}
        for line in lines:
            edge_from, edge_to = line
            if edge_from not in G:
                G[edge_from] = []
            if edge_to not in G:
                G[edge_to] = []
            G[edge_from].append(edge_to)
            G[edge_to].append(edge_from)

    print(solve(G, 1))
    print(solve(G, 2))


run()
