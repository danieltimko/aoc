from input_utils import *
from collections import defaultdict
from queue import PriorityQueue


def dijkstra(grid, task):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0])-1)
    min_length = 1 if task == 1 else 5
    max_length = 4 if task == 1 else 11
    visited = defaultdict(lambda: set())
    pq = PriorityQueue()
    pq.put((0, start, [(-1, -1)] * (max_length-1) + [start]))
    while not pq.empty():
        dist, node, last_n = pq.get()
        row, col = node
        length = get_line_length(last_n, task)
        if length in visited[node]:
            continue
        visited[node].add(length)
        if node == end and length[0] >= min_length:
            return dist
        for nr, nc in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if nr not in range(len(grid)) or nc not in range(len(grid[0])):
                continue  # out of grid
            if (nr, nc) == last_n[-2]:
                continue  # cannot reverse
            new_length = get_line_length(last_n[1:] + [(nr, nc)], task)
            if length[0] == new_length[0] == max_length:
                continue  # cannot go straight anymore, must turn
            if new_length[0] == 2 and length[0] < min_length and node != start:
                continue  # cannot turn yet, must continue straight
            if new_length in visited[(nr, nc)]:
                continue  # state already visited
            pq.put((dist + int(grid[nr][nc]), (nr, nc), last_n[1:] + [(nr, nc)]))


def get_line_length(last_n, task):
    n = 4 if task == 1 else 11
    if last_n[-2] == (-1, -1):
        return 1, ()
    for j in [0, 1]:
        i = 1
        while i < n and last_n[-i-1] != (-1, -1) and last_n[-i-1][j] == last_n[-i][j]:
            i += 1
        if i > 1:
            return i, (j, last_n[-2] != (-1, -1) and last_n[-1][j] < last_n[-2][j])
    assert False


def run():
    grid = read_grid()

    print(dijkstra(grid, task=1))
    print(dijkstra(grid, task=2))


if __name__ == "__main__":
    run()
