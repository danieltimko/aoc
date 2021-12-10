
PAIRS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

TASK1_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

TASK2_POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def solve(lines):
    task1_output = 0
    task2_scores = []
    for line in lines:
        stack = []
        broken = False
        for c in line:
            if c in PAIRS.values():
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != PAIRS[c]:
                    task1_output += TASK1_POINTS[c]
                    broken = True
                    break
                stack.pop()
        if not broken and stack:
            n = 0
            for x in stack[::-1]:
                n = n*5 + TASK2_POINTS[x]
            task2_scores.append(n)
    return task1_output, sorted(task2_scores)[len(task2_scores) // 2]


def run():
    with open('input') as file:
        lines = list(map(lambda line: line.strip(), file.readlines()))
        print(*solve(lines))


run()
