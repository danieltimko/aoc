
def task1(arr):
    gamma = ""
    epsilon = ""
    for col in range(len(arr[0])):
        ones = 0
        for row in range(len(arr)):
            if arr[row][col] == '1':
                ones += 1
        if ones > len(arr)-ones:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def task2(arr):
    def calc(oxygen):
        remaining = arr.copy()
        for col in range(len(remaining[0])):
            ones = 0
            for row in remaining:
                if row[col] == '1':
                    ones += 1
            if ones >= len(remaining)-ones:
                for row in range(len(arr)):
                    if arr[row] in remaining and \
                            ((oxygen and arr[row][col] == '0') or
                             (not oxygen and arr[row][col] == '1')):
                        remaining.remove(arr[row])
            else:
                for row in range(len(arr)):
                    if arr[row] in remaining and \
                            ((oxygen and arr[row][col] == '1') or
                             (not oxygen and arr[row][col] == '0')):
                        remaining.remove(arr[row])
            if len(remaining) == 1:
                return int(remaining[0], 2)

    return calc(True) * calc(False)


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        print(task1(lines))
        print(task2(lines))


run()
