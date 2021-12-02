
def task1(arr):
    horizontal = 0
    depth = 0
    for line in arr:
        command = line[0]
        x = int(line[1])
        if command == 'forward':
            horizontal += x
        elif command == 'down':
            depth += x
        elif command == 'up':
            depth -= x
    return horizontal * depth


def task2(arr):
    horizontal = 0
    depth = 0
    aim = 0
    for line in arr:
        command = line[0]
        x = int(line[1])
        if command == 'forward':
            horizontal += x
            depth += aim * x
        elif command == 'down':
            aim += x
        elif command == 'up':
            aim -= x
    return horizontal * depth


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split(' ')), file.readlines()))

        print(task1(lines))
        print(task2(lines))


run()
