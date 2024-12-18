from input_utils import *


def solve(positions, size=70):
    i = 0
    while True:
        visited = set()
        for (x, y) in positions[:i]:
            visited.add((x, y))
        stack = [((0, 0), 0)]
        success = False
        while stack:
            (x, y), hops = stack.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) == (size, size):
                success = True
                if i == 1024:
                    task1 = hops
                break
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if nx < 0 or nx > size or ny < 0 or ny > size:
                    continue
                stack.append(((nx, ny), hops+1))
        if not success:
            return task1, positions[i-1]
        i += 1


def run():
    positions = read_n_lines_n_numbers()
    print(solve(positions))


if __name__ == "__main__":
    run()
