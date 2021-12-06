from copy import deepcopy


def calc(arr, days):
    for day in range(days):
        new = 0
        for i in range(len(arr)):
            arr[i][0] -= 1
            if arr[i][0] == -1:
                new += arr[i][1]
                arr[i][0] = 6
        arr.append([8, new])
    return sum(map(lambda x: x[1], arr))


def run():
    with open('input') as file:
        arr = list(map(lambda line: (line.strip().split(',')), file.readlines()))[0]
        arr = list(map(lambda x: [int(x), 1], arr))

        print(calc(deepcopy(arr), 80))
        print(calc(deepcopy(arr), 256))


run()
