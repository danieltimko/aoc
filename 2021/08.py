SEGMENT_COUNTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def task1(lines):
    count = 0
    for line in lines:
        for digit in line[1]:
            if len(digit) in [2, 4, 3, 7]:
                count += 1
    return count


def str_to_set(s):
    return set([c for c in s])


def task2(lines):
    count = 0
    for line in lines:
        wires = [set() for _ in range(10)]

        # UNIQUE COUNT OF DIGITS (1,4,7,8)
        for digit in line[0]:
            if len(digit) == 2:
                wires[1] = str_to_set(digit)
            elif len(digit) == 4:
                wires[4] = str_to_set(digit)
            elif len(digit) == 3:
                wires[7] = str_to_set(digit)
            elif len(digit) == 7:
                wires[8] = str_to_set(digit)

        # 6 DIGITS (0,6,9)
        for digit in line[0]:
            s = str_to_set(digit)
            if len(digit) == 6 and s & wires[4] == wires[4]:
                wires[9] = s
        for digit in line[0]:
            s = str_to_set(digit)
            if len(digit) == 6 and s != wires[9]:
                if s & wires[1] == wires[1]:
                    wires[0] = s
                else:
                    wires[6] = s

        # 5 DIGITS (2,3,5)
        for digit in line[0]:
            s = str_to_set(digit)
            if len(digit) == 5 and s & wires[1] == wires[1]:
                wires[3] = s
        for digit in line[0]:
            s = str_to_set(digit)
            if len(digit) == 5 and s != wires[3] and len(s | wires[6]) == 7:
                wires[2] = s
        for digit in line[0]:
            s = str_to_set(digit)
            if len(digit) == 5 and s != wires[2] and s != wires[3]:
                wires[5] = s

        # TRANSLATE OUTPUT
        output = ""
        for digit in line[1]:
            for i in range(10):
                if wires[i] == str_to_set(digit):
                    output += str(i)
        count += int(output)

    return count


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split(' | ')), file.readlines()))
        lines = list(map(lambda line: (line[0].split(' '), line[1].split(' ')), lines))
        print(task1(lines))
        print(task2(lines))


run()
