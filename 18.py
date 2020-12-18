
"""
def solve(expr, visited):
    print("...")
    last_sign = None
    result = None
    for i in range(len(expr)):
        print(f"i:{i}, expr: '{expr}', expr[i] = {expr[i]}, result: {result}")
        if visited[i]:
            continue
        if expr[i][0] == '(':
            expr[i] = expr[i][1:]
            inside = solve(expr[i:], visited)
            # print(f"right is {right_side}")
            # print(result, right_side)
            if not result:
                # print("1result = ", inside)
                result = inside
            else:
                result = result + inside if last_sign == '+' else result * inside
        elif expr[i][-1] == ')':
            print(f"{result} {last_sign} {int(expr[i][:-1])}")
            print('1return', result + int(expr[i][:-1]) if last_sign == '+' else result * int(expr[i][:-1]))
            visited[i] = True
            return result + int(expr[i][:-1]) if last_sign == '+' else result * int(expr[i][:-1])

        elif expr[i] == '+':
            last_sign = '+'
        elif expr[i] == '*':
            last_sign = '*'
        else:
            if not result:
                # print('2result = ', int(expr[i]))
                result = int(expr[i])
            else:
                print(f"{result} {last_sign} {int(expr[i])}")
                # print('3result = ', result + int(expr[i]) if last_sign == '+' else result * int(expr[i]))
                result = result + int(expr[i]) if last_sign == '+' else result * int(expr[i])
        visited[i] = True
    print('2return', result)
    return result
"""


def task1(expressions):
    result_sum = 0

    for expr in expressions:
        stack = []
        for i in range(len(expr)):
            if expr[i].isnumeric():
                if not stack or stack[-1] not in "+*":
                    stack.append(int(expr[i]))
                else:
                    if stack.pop() == "+":
                        stack.append(stack.pop() + int(expr[i]))
                    else:
                        stack.append(stack.pop() * int(expr[i]))
            elif expr[i] in "+*(":
                stack.append(expr[i])
            elif expr[i] == ")":
                temp = stack.pop()
                stack.pop()
                if stack and stack[-1] in "+*":
                    operator = stack.pop()
                    stack.append(stack.pop() + temp if operator == '+' else stack.pop() * temp)
                else:
                    stack.append(temp)
        result_sum += stack[0]

    return result_sum


def eval_last(stack):
    mul = 1
    while True:
        item = stack.pop()
        if item == "(":
            stack.append(mul)
            return
        if isinstance(item, int):
            mul *= item


def task2(expressions):
    result_sum = 0

    for expr in expressions:
        stack = ["("]
        for i in range(len(expr)):
            if expr[i].isnumeric():
                if stack and stack[-1] == "+":
                    stack.pop()
                    stack.append(stack.pop() + int(expr[i]))
                else:
                    stack.append(int(expr[i]))
            elif expr[i] in "+*(":
                stack.append(expr[i])
            elif expr[i] == ")":
                eval_last(stack)
                if stack[-2] == "+":
                    temp = stack.pop()
                    stack.pop()
                    stack.append(stack.pop() + temp)
        eval_last(stack)
        result_sum += stack[0]

    return result_sum


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip()), file.readlines()))
        expressions = []
        for line in lines:
            expressions.append(line.replace("(", "( ").replace(")", " )").split(" "))

        # print(task1(expressions))
        print(task2(expressions))


run()
