
def get_val(arr, row, col):
    if not (0 <= row < len(arr) and 0 <= col < len(arr[0])):
        return 10
    return arr[row][col]


def is_low_point(arr, row, col):
    val = arr[row][col]
    return (val < get_val(arr, row-1, col) and
            val < get_val(arr, row+1, col) and
            val < get_val(arr, row, col-1) and
            val < get_val(arr, row, col+1))


def task1(arr):
    output = 0
    low_points = []
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if is_low_point(arr, row, col):
                output += 1 + arr[row][col]
                low_points.append((row, col))
    return output, low_points


def task2(arr, low_points):
    def BFS(from_pos):
        visited = set()
        stack = [(from_pos[0], from_pos[1], -1)]
        area = 0
        while stack:
            row, col, prevval = stack.pop()
            if get_val(arr, row, col) == 10:
                continue
            if (row, col) in visited:
                continue
            val = arr[row][col]
            if val < prevval or val == 9:
                continue
            area += 1
            visited.add((row, col))
            for neighbor in ([(row-1, col), (row+1, col), (row, col-1), (row, col+1)]):
                stack.append((neighbor[0], neighbor[1], val))
        return area

    mul = 1
    for val in sorted([BFS(x) for x in low_points], reverse=True)[:3]:
        mul *= val
    return mul


def run():
    with open('input') as file:
        arr = list(map(lambda line: list(map(int, (line.strip()))), file.readlines()))

        out1, low_points = task1(arr)
        print(out1)
        print(task2(arr, low_points))


run()
