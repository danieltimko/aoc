
def task1(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i+1] > arr[i]:
            count += 1
    return count


def task2(arr):
    count = 0
    for i in range(len(arr)-3):
        if arr[i+1] + arr[i+2] + arr[i+3] > arr[i] + arr[i+1] + arr[i+2]:
            count += 1
    return count


def run():
    with open('input') as file:
        lines = list(map(lambda line: int(line.strip()), file.readlines()))

        print(task1(lines))
        print(task2(lines))


run()
