from input_utils import *


def calc_positions(arr):
    positions = dict()
    for i in range(len(arr)):
        positions[arr[i]] = i
    return positions


def mix(arr, repetitions):
    length = len(arr)
    positions = calc_positions(arr)
    order = arr.copy()

    for _ in range(repetitions):
        for item in order:
            _, num = item
            n = (num % (length-1))
            if n == 0:
                continue
            old_index = positions[item]
            new_index = (positions[item] + n) % length
            left = arr[:new_index+1]
            right = arr[new_index+1:]
            if old_index > new_index:
                right.remove(item)
            elif old_index < new_index:
                left.remove(item)
            arr = left + [item] + right
            positions = calc_positions(arr)

    zero_index = [i for i in range(len(arr)) if arr[i][1] == 0][0]
    indices = [(zero_index + i*1000) % length for i in range(1, 4)]
    return sum([arr[i][1] for i in indices])


def run():
    # There can be duplicate numbers! Give each number an id.
    arr_task1 = list(enumerate(read_n_lines_one_number()))
    arr_task2 = list(map(lambda x: (x[0], x[1]*811589153), arr_task1))

    print(mix(arr_task1, 1))
    print(mix(arr_task2, 10))


if __name__ == "__main__":
    run()
