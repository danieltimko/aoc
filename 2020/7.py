from pprint import pprint


def count_paths_to(G, node, visited):
    count = 0
    visited.add(node)
    if node in G:
        for neighbor, val in G[node]:
            if neighbor not in visited:
                count += count_paths_to(G, neighbor, visited)
    return count + 1


def count_bags(G, node):
    count = 0
    if node in G:
        for neighbor, val in G[node]:
            count += val * (count_bags(G, neighbor) + 1)
    return count


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split(' bags contain ')), file.readlines()))
        G = {}
        G_transposed = {}
        for line in lines:
            node_from = line[0]
            if line[1] == 'no other bags.':
                continue
            for node_to in line[1][:-1].split(', '):
                splitted = node_to.split(' ', 1)
                val = int(splitted[0])
                node_to = splitted[1].rsplit(' ', 1)[0]
                if node_to not in G_transposed:
                    G_transposed[node_to] = []
                if node_from not in G:
                    G[node_from] = []
                G[node_from].append((node_to, val))
                G_transposed[node_to].append((node_from, val))

        # pprint(G_transposed)
        # pprint(G)

        # print(count_paths_to(G_transposed, "shiny gold", set()) - 1)
        print(count_bags(G, "shiny gold"))


run()
