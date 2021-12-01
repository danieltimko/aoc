
def task1(instructions):
    x = 0
    y = 0
    angle = 90
    for instruction in instructions:
        command = instruction[0]
        value = int(instruction[1:])
        if command == 'E':
            x += value
        elif command == 'W':
            x -= value
        elif command == 'N':
            y += value
        elif command == 'S':
            y -= value
        elif command == 'F':
            if angle == 270:
                x -= value
            elif angle == 180:
                y -= value
            elif angle == 90:
                x += value
            else:
                assert angle == 0
                y += value
        elif command == 'L':
            angle = (angle - value) % 360
        elif command == 'R':
            angle = (angle + value) % 360
    return abs(x) + abs(y)


def rotate_waypoint_right(waypoint_x, waypoint_y, value):
    if value % 360 == 0:
        return waypoint_x, waypoint_y
    elif value % 270 == 0:
        return -waypoint_y, waypoint_x
    elif value % 180 == 0:
        return -waypoint_x, -waypoint_y
    else:
        assert value % 90 == 0
        return waypoint_y, -waypoint_x


def task2(instructions):
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1
    for instruction in instructions:
        command = instruction[0]
        value = int(instruction[1:])
        if command == 'E':
            waypoint_x += value
        elif command == 'W':
            waypoint_x -= value
        elif command == 'N':
            waypoint_y += value
        elif command == 'S':
            waypoint_y -= value
        elif command == 'F':
            x += waypoint_x * value
            y += waypoint_y * value
        elif command == 'L':
            waypoint_x, waypoint_y = rotate_waypoint_right(waypoint_x, waypoint_y, 360-value)
        elif command == 'R':
            waypoint_x, waypoint_y = rotate_waypoint_right(waypoint_x, waypoint_y, value)

    return abs(x) + abs(y)


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        print(task1(lines), task2(lines))


run()
