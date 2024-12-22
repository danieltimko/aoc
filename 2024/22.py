from input_utils import *
from utils import *


def mix(secret, val):
    return secret ^ val


def prune(secret):
    return secret % 16777216


def evolve(secret):
    secret = prune(mix(secret*64, secret))
    secret = prune(mix(secret//32, secret))
    return prune(mix(secret*2048, secret))


def evolve_n_times(secret, n):
    memory = []
    for _ in range(n):
        new_secret = evolve(secret)
        memory.append((new_secret%10 - secret%10, new_secret%10))
        secret = new_secret
    return secret, memory


def task1(arr):
    return sum(evolve_n_times(secret, 2000)[0] for secret in arr)


def task2(arr):
    diffs = {}
    for secret in arr:
        diffs[secret] = evolve_n_times(secret, 2000)[1]
    selling_points = defaultdict(lambda: 0)
    for secret in arr:
        d = diffs[secret]
        found = set()
        for i in range(4, 2000):
            window = tuple(x[0] for x in d[i-4:i])
            price = d[i-1][1]
            if window not in found:
                selling_points[window] += price
                found.add(window)
    return max(selling_points.values())


def run():
    arr = read_n_lines_one_number()
    print(task1(arr))
    print(task2(arr))


if __name__ == "__main__":
    run()
