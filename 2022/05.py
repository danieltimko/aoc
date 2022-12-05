from copy import deepcopy

from input_utils import *


def solve(stacks, actions, task):
    stacks = deepcopy(stacks)
    for action in actions:
        n, f, t = action
        if task == 1:
            for _ in range(n):
                stacks[t-1].append(stacks[f-1].pop())
        else:
            crates = stacks[f-1][-n:]
            for _ in range(n):
                stacks[f-1].pop()
            stacks[t-1] += crates
    return ''.join(stack[-1] for stack in stacks)


def run():
    stacks = [list() for _ in range(9)]
    actions = []
    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()
        reading_stacks = True
        for line in lines:
            if reading_stacks:
                if line == '\n':
                    reading_stacks = False
                    continue
                if '[' not in line:
                    continue
                crates = [line[i:i+4] for i in range(0, len(line), 4)]
                for i in range(len(crates)):
                    if '[' in crates[i]:
                        stacks[i].append(crates[i][1])
                    i += 1
            else:
                x = line.split(' ')
                actions.append((int(x[1]), int(x[3]), int(x[5])))
    for stack in stacks:
        stack.reverse()

    print(solve(stacks, actions, task=1))
    print(solve(stacks, actions, task=2))


if __name__ == "__main__":
    run()
