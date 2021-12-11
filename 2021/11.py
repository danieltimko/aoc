
def flash(arr, flashed, row, col):
    if (row, col) in flashed:
        return 0
    flashes = 1
    flashed.add((row, col))
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if 0 <= col+dc < len(arr[0]) and 0 <= row+dr < len(arr):
                arr[row+dr][col+dc] += 1
                if arr[row+dr][col+dc] > 9:
                    flashes += flash(arr, flashed, row+dr, col+dc)
    return flashes


def simulate(arr):
    task1 = 0
    task2 = 0
    flashes = 0
    step = 1
    while True:
        flashed = set()
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                arr[row][col] += 1
                if arr[row][col] > 9:
                    flashes += flash(arr, flashed, row, col)
        for row, col in flashed:
            arr[row][col] = 0

        if step == 100:
            task1 = flashes
        if len(flashed) == len(arr) * len(arr[0]) and not task2:
            task2 = step
        if task1 and task2:
            return task1, task2
        step += 1


def run():
    with open('input') as file:
        arr = list(map(lambda line: list(map(int, (line.strip()))), file.readlines()))
        print(*simulate(arr))


run()
