from input_utils import *


def run_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def task1(steps):
    return sum(run_hash(step) for step in steps)


def task2(steps):
    boxes = [[] for _ in range(256)]
    for step in steps:
        lbl = step[:-1] if "-" in step else step[:-2]
        b = run_hash(lbl)
        if step[-2] == "=":
            lens = (step[:-2], int(step[-1]))
            replaced = False
            for i in range(len(boxes[b])):
                if boxes[b][i][0] == lbl:
                    boxes[b][i] = lens
                    replaced = True
            if not replaced:
                boxes[b].append(lens)
        else:
            boxes[b] = list(filter(lambda lens: lens[0] != lbl, boxes[b]))
    return sum((1+b)*(1+x)*(boxes[b][x][1])
               for b in range(len(boxes)) for x in range(len(boxes[b])))


def run():
    steps = read_one_line_n_strings(',')

    print(task1(steps))
    print(task2(steps))


if __name__ == "__main__":
    run()
