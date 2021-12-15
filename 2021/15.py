from queue import PriorityQueue


def is_valid_coord(arr, row, col):
    return 0 <= row < len(arr) and 0 <= col < len(arr[0])


def dijkstra(arr):
    pq = PriorityQueue()
    visited = set()
    pq.put((0, (0, 0)))
    while not pq.empty():
        total_cost, vertex = pq.get()
        row, col = vertex
        if vertex in visited:
            continue
        visited.add(vertex)
        if vertex == (len(arr)-1, len(arr[0])-1):
            return total_cost
        for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if is_valid_coord(arr, neighbor[0], neighbor[1]):
                pq.put((total_cost+int(arr[neighbor[0]][neighbor[1]]), (neighbor[0], neighbor[1])))
    return -1


def build_full_arr(arr):
    new_arr = []
    for row in range(len(arr)*5):
        s = ""
        for col in range(len(arr)*5):
            val = int(arr[row % len(arr)][col % len(arr[0])]) + row // len(arr) + col // len(arr[0])
            s += str(val if val <= 9 else val % 9)
        new_arr.append(s)
    return new_arr


def run():
    with open('input') as file:
        arr = list(map(lambda line: (line.strip()), file.readlines()))

        print(dijkstra(arr))
        print(dijkstra(build_full_arr(arr)))


run()
