from input_utils import *
from utils import *


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def total_rating(self):
        return self.x + self.m + self.a + self.s

    def eval_rule(self, rule):
        val = self.__dict__[rule[0][0]]
        return eval(f"{val}{rule[0][1:]}")


def task1(workflows, parts):
    ans = 0
    for part in parts:
        wf = 'in'
        while wf not in ('A', 'R'):
            for rule in workflows[wf]:
                if len(rule) == 1:
                    wf = rule[0]
                    break
                elif part.eval_rule(rule):
                    wf = rule[1]
                    break
        if wf == 'A':
            ans += part.total_rating()
    return ans


def task2(workflows):
    restrictions = {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001),
    }
    return get_total_combinations2(workflows, restrictions)


def get_total_combinations2(workflows, restrictions, wf='in'):
    if wf == 'A':
        return options_count(restrictions)
    if wf == 'R':
        return 0
    total = 0
    for rule in workflows[wf]:
        if len(rule) == 1:
            total += get_total_combinations2(workflows, restrictions, rule[0])
        else:
            opposite_rule = (f"{rule[0][0]}{'<>'[rule[0][1] == '<']}"
                             f"{int(rule[0][2:])+(1, -1)[rule[0][1] == '<']}")
            total += get_total_combinations2(workflows, intersect(restrictions, rule[0]), rule[1])
            restrictions = intersect(restrictions, opposite_rule)
    return total


def intersect(restrictions, restriction):
    new_restrictions = restrictions.copy()
    new_range = (range(1, int(restriction[2:])) if restriction[1] == '<' else
                 range(int(restriction[2:])+1, 4001))
    var = restriction[0]
    new_restrictions[var] = range_intersect(restrictions[var], new_range)
    return new_restrictions


def options_count(restrictions):
    options = 1
    for r in restrictions.values():
        if r is None:
            return 0
        options *= len(r)
    return options


def run():
    groups = read_n_groups_n_lines_one_string()
    workflows = {}
    parts = []
    for line in groups[0]:
        rules = []
        for rule in line[:-1].split('{')[1].split(','):
            rules.append(tuple(rule.split(':')))
        name = line.split('{')[0]
        workflows[name] = rules
    for line in groups[1]:
        numbers = []
        for var in line[1:-1].split(','):
            numbers.append(int(var.split('=')[1]))
        parts.append(Part(*numbers))

    print(task1(workflows, parts))
    print(task2(workflows))


if __name__ == "__main__":
    run()
