from input_utils import *


def task1(monkeys):
    def solve(monkey):
        right = monkeys[monkey]
        if isinstance(right, list):
            first = right[0] if right[0].isnumeric() else solve(right[0])
            second = right[2] if right[2].isnumeric() else solve(right[2])
            op = right[1]
            return eval(f"{first}{op}{second}")
        else:
            return int(right)
    return int(solve("root"))


def task2(monkeys):
    def solve(monkey, result):
        right = monkeys[monkey]
        if isinstance(right, list):
            leftop, humn_is_left = right[0] if right[0].isnumeric() else solve(right[0], None)
            rightop, humn_is_right = right[2] if right[2].isnumeric() else solve(right[2], None)
            operation = right[1]
            if monkey == 'root':
                result = rightop if humn_is_left else leftop

            if result and (humn_is_left or humn_is_right):
                if operation == '=':
                    return solve(right[0], result) if humn_is_left else solve(right[2], result)
                if operation == '+':
                    return solve(right[0], result - rightop) if humn_is_left else solve(right[2], result - leftop)
                if operation == '-':
                    return solve(right[0], result + rightop) if humn_is_left else solve(right[2], leftop - result)
                if operation == '*':
                    return solve(right[0], result / rightop) if humn_is_left else solve(right[2], result / leftop)
                if operation == '/':
                    return solve(right[0], result * rightop) if humn_is_left else solve(right[2], leftop / result)
            return eval(f"{leftop}{operation}{rightop}"), humn_is_left or humn_is_right
        else:
            if monkey == 'humn':
                return result or int(right), True
            return int(right), False

    monkeys["root"][1] = "="
    return int(solve('root', None)[0])


def run():
    monkeys = dict()
    with open(INPUT_FILE_PATH) as f:
        for line in f.readlines():
            left, right = line.strip().split(': ')
            if right.isnumeric():
                monkeys[left] = int(right)
            else:
                monkeys[left] = right.split(' ')

    print(task1(monkeys))
    print(task2(monkeys))


if __name__ == "__main__":
    run()
