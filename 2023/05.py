from input_utils import *


def intersect(r1, r2):
    if r1[-1] < r2[0] or r2[-1] < r1[0]:
        return None
    return range(max(r1[0], r2[0]), min(r1[-1], r2[-1])+1)


def task1(seeds, maps):
    minval = float("inf")
    for seed in seeds:
        val = seed
        for m in maps:
            for rule in m:
                if val in range(rule[1], rule[1]+rule[2]):
                    diff = val - rule[1]
                    val = rule[0] + diff
                    break
        minval = min(minval, val)
    return minval


def task2(seeds, maps):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[i], seeds[i]+seeds[i+1]))
    minval = float("inf")
    for seed_range in seed_ranges:
        ranges = [seed_range]
        for m in maps:
            new_ranges = []
            for r in ranges:
                found_any = False
                for rule in m:
                    intersection = intersect(r, range(rule[1], rule[1]+rule[2]))
                    if intersection:
                        found_any = True
                        diff = intersection[0] - rule[1]
                        translated = range(rule[0] + diff, rule[0] + diff + len(intersection))
                        new_ranges.append(translated)
                        left = range(r[0], rule[1])
                        right = range(rule[1]+rule[2], r[-1])
                        if left:
                            ranges.append(left)
                        if right:
                            ranges.append(right)
                if not found_any:
                    new_ranges.append(r)
            ranges = new_ranges
            if not ranges:
                break
        minval = min(minval, min(r[0] for r in ranges))
    return minval


def run():
    groups = read_n_groups_n_lines_one_string()
    seeds = list(map(int, groups[0][0].split(': ')[1].split(' ')))
    maps = []
    for group in groups[1:]:
        rows = group[1:]
        rules = []
        for row in rows:
            rules.append(list(map(int, row.split(' '))))
        maps.append(rules)
    print(task1(seeds, maps))
    print(task2(seeds, maps))


if __name__ == "__main__":
    run()
