from input_utils import *

from copy import copy


class Resources:
    def __init__(self, ore, clay, obsidian, geode):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __str__(self):
        return f"{self.ore} ore, {self.clay} clay, {self.obsidian} obsidian, {self.geode} geode"


class Blueprint(Resources):
    def __init__(self, index, ore, clay, obsidian, geode):
        super().__init__(ore, clay, obsidian, geode)
        self.index = index


def collect(robots, resources):
    resources.ore += robots.ore
    resources.clay += robots.clay
    resources.obsidian += robots.obsidian
    resources.geode += robots.geode


def move(bp, robots, resources, time, time_cap) -> int:
    if time > time_cap:
        # print(resources)
        return resources.geode

    # Try to build geode robot
    if resources.ore >= bp.geode[0] and resources.obsidian >= bp.geode[1]:
        collect(robots, resources)
        new_resources = copy(resources)
        new_resources.ore -= bp.geode[0]
        new_resources.obsidian -= bp.geode[1]
        new_robots = copy(robots)
        new_robots.geode += 1
        return move(bp, new_robots, new_resources, time + 1, time_cap)

    # Try to build obsidian robot
    if resources.ore >= bp.obsidian[0] and resources.clay >= bp.obsidian[1]:
        collect(robots, resources)
        new_resources = copy(resources)
        new_resources.ore -= bp.obsidian[0]
        new_resources.clay -= bp.obsidian[1]
        new_robots = copy(robots)
        new_robots.obsidian += 1
        return move(bp, new_robots, new_resources, time + 1, time_cap)

    results = []
    can_build_ore = resources.ore >= bp.ore
    can_build_clay = resources.ore >= bp.clay
    if can_build_ore and can_build_clay:
        # Try both
        building_ore = True
        building_clay = True
        waiting = False
    elif can_build_ore or can_build_clay:
        # Try also waiting for the resources for the other one
        building_ore = can_build_ore
        building_clay = can_build_clay
        waiting = True
    else:
        building_ore = False
        building_clay = False
        waiting = True

    # Collect resources AFTER building the robot
    collect(robots, resources)

    # Try to build ore robot
    if building_ore:
        new_resources = copy(resources)
        new_resources.ore -= bp.ore
        new_robots = copy(robots)
        new_robots.ore += 1
        results.append(move(bp, new_robots, new_resources, time+1, time_cap))
    # Try to build clay robot
    if building_clay:
        new_resources = copy(resources)
        new_resources.ore -= bp.clay
        new_robots = copy(robots)
        new_robots.clay += 1
        results.append(move(bp, new_robots, new_resources, time+1, time_cap))
    if waiting:
        results.append(move(bp, copy(robots), copy(resources), time + 1, time_cap))
    return max(results)


def task1(bps):
    result = 0
    for bp in bps:
        geodes = move(bp, Resources(1, 0, 0, 0), Resources(0, 0, 0, 0), 1, 24)
        result += geodes * bp.index
    return result


def task2(bps):
    result = 1
    for bp in bps[:3]:
        geodes = move(bp, Resources(1, 0, 0, 0), Resources(0, 0, 0, 0), 1, 32)
        result *= geodes
    return result


def run():
    bps = []
    with open(INPUT_FILE_PATH) as f:
        for line in f.readlines():
            index = int(line.split(':')[0].split(' ')[1])
            costs = [int(w) for w in line.strip().split(' ') if w.isnumeric()]
            bps.append(Blueprint(index, costs[0], costs[1],
                                 (costs[2], costs[3]),
                                 (costs[4], costs[5])))

    print(task1(bps))
    print(task2(bps))


if __name__ == "__main__":
    run()
