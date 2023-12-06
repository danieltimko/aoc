from input_utils import *


def get_result(times, distances):
    result = 1
    for i in range(len(times)):
        wins = len(list(filter(lambda t: (times[i] - t) * t > distances[i],
                               range(1, times[i]))))
        result *= wins
    return result


def run():
    lines = read_n_lines_one_string()
    times = list(map(int, lines[0].split(':')[1].strip().split()))
    distances = list(map(int, lines[1].split(':')[1].strip().split()))
    task2_time = int(lines[0].split(':')[1].replace(' ', ''))
    task2_distance = int(lines[1].split(':')[1].replace(' ', ''))

    print(get_result(times, distances))
    print(get_result([task2_time], [task2_distance]))


if __name__ == "__main__":
    run()
