from input_utils import *

from copy import deepcopy


class Monkey:
    def __init__(self, items, op, test):
        self.items = items
        self.op = op
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"ITEMS {self.items}, OP {self.op}, TEST {self.test}"

    def turn(self, task):
        q = []
        while self.items:
            lvl = self.items.pop(0)  # Inspect
            self.inspections += 1
            lvl = self.update_worry_level(lvl)
            if task == 1:
                lvl //= 3
            if lvl % self.test[0] == 0:
                q.append((lvl, self.test[1]))
            else:
                q.append((lvl, self.test[2]))
        return q

    def update_worry_level(self, lvl):
        if self.op[1] == '+':
            if self.op[2] == 'old':
                return lvl + lvl
            else:
                return lvl + int(self.op[2])
        elif self.op[1] == '*':
            if self.op[2] == 'old':
                return lvl * lvl
            else:
                return lvl * int(self.op[2])


def solve(monkeys, task):
    modul = 1
    for monkey in monkeys:
        modul *= monkey.test[0]
    inspections = 0
    for r in range(20 if task == 1 else 10000):
        for i in range(len(monkeys)):
            q = monkeys[i].turn(task)
            inspections += len(q)
            for lvl, to_who in q:
                monkeys[to_who].items.append(lvl % modul)
    inspection_counts = sorted([m.inspections for m in monkeys])
    return inspection_counts[-1] * inspection_counts[-2]


def run():
    monkeys = []
    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 7):
            items = list(map(int, lines[i+1].strip().split(': ')[1].split(', ')))
            op = lines[i+2].strip().split('= ')[1].split(' ')
            n = int(lines[i+3].strip().split(' ')[-1])
            m1 = int(lines[i+4].strip().split(' ')[-1])
            m2 = int(lines[i+5].strip().split(' ')[-1])
            monkeys.append(Monkey(items, op, (n, m1, m2)))

    print(solve(deepcopy(monkeys), task=1))
    print(solve(deepcopy(monkeys), task=2))


if __name__ == "__main__":
    run()
