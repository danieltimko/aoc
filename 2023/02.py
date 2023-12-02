import math

from input_utils import *


class Game:
    def __init__(self, line):
        self.id = int(line.split(" ")[1].split(':')[0])
        self.sets = []
        # so splitting by ; was basically useless, great
        sets = line.split(": ")[1].split('; ')
        for s in sets:
            _set = []
            for x in s.split(", "):
                cnt, color = x.split(" ")
                _set.append((int(cnt), color))
            self.sets.append(_set)


def task1(games):
    id_sum = 0
    for game in games:
        valid = True
        for _set in game.sets:
            for cnt, color in _set:
                if ((color == "red" and cnt > 12) or
                        (color == "green" and cnt > 13) or
                        (color == "blue" and cnt > 14)):
                    valid = False
        if valid:
            id_sum += game.id
    return id_sum


def task2(games):
    result = 0
    for game in games:
        maxs = {"red": 0, "green": 0, "blue": 0}
        for _set in game.sets:
            for cnt, color in _set:
                maxs[color] = max(cnt, maxs[color])
        result += math.prod(maxs.values())
    return result


def run():
    lines = read_n_lines_one_string()
    games = [Game(line) for line in lines]

    print(task1(games))
    print(task2(games))


if __name__ == "__main__":
    run()
