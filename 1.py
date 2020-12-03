
def xor(a, b):
    return (a and not b) or (not a and b)


def find(arr, n):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i != j != k and arr[i] + arr[j] + arr[k] == n:
                    return arr[i] * arr[j] * arr[k]


def run():
    with open('input') as file:
        lines = list(map(lambda line: int(line.strip()), file.readlines()))
        print(find(lines, 2020))


run()
