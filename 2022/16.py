from input_utils import *


def bfs(graph, source, target):
    """ Returns distance between the source valve and the target valve """
    visited = set()
    stack = [(source, 0)]
    while stack:
        valve, hops = stack.pop(0)
        if valve in visited:
            continue
        visited.add(valve)
        if valve == target:
            return hops
        for neighbor in graph[valve][1]:
            stack.append((neighbor, hops+1))


def get_relevant_valves(graph):
    return set(name for name, val in graph.items() if val[0] != 0)


def calc_flow(graph, opened):
    return sum(graph[valve][0] for valve in graph if valve in opened)


def powerset(valves: set):
    valves = list(valves)
    ps = []
    for i in range(2 ** len(valves)):
        ps.append(set(valves[j] for j in range(len(valves)) if 2**j & i))
    return ps


def solve_task(graph, task):
    def search(valve, visited, assigned, time):
        assert time <= time_cap
        flow = calc_flow(graph, visited)
        best_result = (time_cap - time + 1) * flow
        for next_valve in assigned - visited:
            spent_time = costs[(valve, next_valve)] + 1
            if time + spent_time > time_cap:
                continue
            result = search(next_valve, visited | {next_valve}, assigned, time + spent_time)
            result += spent_time * flow
            best_result = max(best_result, result)
        return best_result

    time_cap = 30 if task == 1 else 26
    # consider only valves with flow rate > 0
    valves = get_relevant_valves(graph)
    # precompute all costs
    costs = dict()
    for v1 in valves | {'AA'}:
        for v2 in valves:
            cost = bfs(graph, v1, v2)
            costs[(v1, v2)] = cost
            costs[(v2, v1)] = cost

    if task == 1:
        return search("AA", set(), valves, 1)

    best = 0
    for valves_for_me in list(powerset(valves)):
        valves_for_elephant = valves - valves_for_me
        # if len(valves_for_me) < 5 or len(valves_for_elephant) < 5:
        #     continue
        result_me = search("AA", set(), valves_for_me, 1)
        result_elephant = search("AA", set(), valves_for_elephant, 1)
        best = max(best, result_me + result_elephant)
    return best


def run():
    graph = dict()
    with open(INPUT_FILE_PATH) as f:
        for line in f.readlines():
            name = line[6:8]
            flow = int(line.split('=')[1].split(';')[0])
            if 'valves' in line:
                neighbors = line.strip().split('valves ')[1].split(', ')
            else:
                neighbors = [line.strip().split('valve ')[1]]
            graph[name] = (flow, neighbors)

    print(solve_task(graph, task=1))
    print(solve_task(graph, task=2))


if __name__ == "__main__":
    run()
