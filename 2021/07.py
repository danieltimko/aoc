
def nsum(n):
    return n*(n+1)//2


def calc_fuel(arr, task):
    return min(
        sum(abs(x-y) if task == 1 else nsum(abs(x-y)) for y in arr)
        for x in arr
    )


def run():
    with open('input') as file:
        arr = list(map(int, file.readlines()[0].split(',')))
        print(calc_fuel(arr, task=1), calc_fuel(arr, task=2))


run()
