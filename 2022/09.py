from input_utils import *


def follow(head, tail, d, head_move=True):
    if head_move:
        if d == 'R':
            head = head[0]+1, head[1]
        elif d == 'L':
            head = head[0]-1, head[1]
        elif d == 'D':
            head = head[0], head[1]-1
        elif d == 'U':
            head = head[0], head[1]+1
    if abs(head[0]-tail[0]) == 1 and abs(head[1]-tail[1]) == 1:
        pass
    elif head[0] == tail[0] and abs(head[1]-tail[1]) <= 1:
        pass
    elif head[1] == tail[1] and abs(head[0]-tail[0]) <= 1:
        pass
    else:
        if head[0] != tail[0]:
            tail = (
                tail[0] + (1 if head[0] > tail[0] else -1),
                tail[1]
            )
        if head[1] != tail[1]:
            tail = (
                tail[0],
                tail[1] + (1 if head[1] > tail[1] else -1)
            )
    return head, tail


def draw(positions):
    for y in range(15, -15, -1):
        s = ""
        for x in range(-15, 15):
            s += ".#"[(x, y) in positions]
        print(s)
    print()


def task1(lines):
    positions = {(0, 0)}
    head = (0, 0)
    tail = (0, 0)
    for line in lines:
        d = line[0]
        n = int(line[1])
        for _ in range(n):
            head, tail = follow(head, tail, d)
            positions.add(tail)
    return len(positions)


def task2(lines):
    positions = {(0, 0)}
    knots = [(0, 0) for _ in range(10)]
    for line in lines:
        d = line[0]
        n = int(line[1])
        for j in range(n):
            for i in range(9, 0, -1):
                x = knots[i-1]
                knots[i], knots[i-1] = follow(knots[i], knots[i-1], d, i == 9)
                if knots[i-1] == x:
                    break
            positions.add(knots[0])
    return len(positions)


def run():
    lines = read_n_lines_n_strings(' ')

    print(task1(lines))
    print(task2(lines))


if __name__ == "__main__":
    run()
