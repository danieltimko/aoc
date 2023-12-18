from input_utils import *


def get_area(lines, task=2):
    if task == 2:
        update_lines(lines)
    # shift starting direction to L for convenience
    while lines[0][0] != "L":
        lines = lines[1:] + [lines[0]]
    results = []
    # guess to which side does the polygon enclose - right-hand or left-hand
    for guess in [False, True]:
        pos = (0, 0)  # (row, col)
        vertices = [pos]
        for i in range(len(lines)):
            direction, n, _ = lines[i]
            n = int(n)
            previous_direction = lines[i-1][0]
            next_direction = lines[0 if i == len(lines)-1 else i+1][0]
            # lht_now when assuming that polygon is on the LHS (guess == True)
            rht_now = guess ^ is_righthand_turn(direction, next_direction)
            # rht_previous when assuming that polygon is on the LHS (guess == True)
            lht_previous = guess ^ (not is_righthand_turn(previous_direction, direction))
            pos = {
                "L": (pos[0], pos[1] - n + lht_previous - rht_now),
                "R": (pos[0], pos[1] + n - lht_previous + rht_now),
                "D": (pos[0] + n - lht_previous + rht_now, pos[1]),
                "U": (pos[0] - n + lht_previous - rht_now, pos[1]),
            }[direction]
            vertices.append(pos)
        # shoelace
        n = 0
        for i in range(len(vertices)-1):
            n += vertices[i][1]*vertices[i+1][0]
            n -= vertices[i][0]*vertices[i+1][1]
        area = n // 2
        results.append(area)
    return results


def update_lines(lines):
    for i in range(len(lines)):
        color = lines[i][2]
        n = int(color[2:7], 16)
        direction = "RDLU"[int(color[7])]
        lines[i] = (direction, n, None)


def is_righthand_turn(d1, d2):
    return {
        "L": d2 == "U",
        "R": d2 == "D",
        "D": d2 == "L",
        "U": d2 == "R",
    }[d1]


def run():
    lines = read_n_lines_n_strings(' ')

    print(get_area(lines, task=1))
    print(get_area(lines, task=2))


if __name__ == "__main__":
    run()
