import matplotlib.pyplot as plt
import numpy as np
import re

from input_utils import *
from utils import *


def solve(robots, width, height, task):
    positions = defaultdict(lambda: 0)
    for (x, y), _ in robots:
        positions[(x, y)] += 1
    robots = set(robots)
    t = 0
    while True:
        if task == 1 and t == 100:
            q = [0, 0, 0, 0]
            for (x, y), _ in robots:
                if 0 <= x < width // 2 and 0 <= y < height // 2:
                    q[0] += 1
                elif width // 2 < x < width and 0 <= y < height // 2:
                    q[1] += 1
                elif 0 <= x < width // 2 and height // 2 < y < height:
                    q[2] += 1
                elif width // 2 < x < width and height // 2 < y < height:
                    q[3] += 1
            return q[0] * q[1] * q[2] * q[3]
        if task == 2 and is_tree(robots, width, height, t):
            return t
        new_robots = set()
        for (x, y), (vx, vy) in robots:
            nx = (x + vx) % width
            ny = (y + vy) % height
            tmp = len(robots)
            new_robots.add(((nx, ny), (vx, vy)))
            assert len(robots) == tmp
        robots = new_robots
        t += 1


def is_tree(robots, width, height, t):
    grid = defaultdict(lambda: 0)
    for (x, y), _ in robots:
        grid[(x, y)] += 1
    img = np.zeros((height, width))
    candidate = False
    for y in range(height):
        seq = 0
        for x in range(width):
            seq = seq+1 if (x, y) in grid else 0
            if seq == 10:
                candidate = True
            img[y][x] = int((x, y) in grid)
    if candidate:
        plt.imshow(img*255)
        plt.axis('off')
        plt.title(t)
        plt.show(block=False)
        plt.pause(5)
        plt.close()
    return candidate


def run():
    lines = read_n_lines_n_strings(sep=' ')
    robots = []
    for pos, vel in lines:
        x, y = tuple(map(int, re.findall(r'-?\d+', pos)))
        vx, vy = tuple(map(int, re.findall(r'-?\d+', vel)))
        robots.append(((x, y), (vx, vy)))
    print(solve(robots, 101, 103, task=1))
    print(solve(robots, 101, 103, task=2))


if __name__ == "__main__":
    run()
