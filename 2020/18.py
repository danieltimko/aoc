
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

        print(task1(expressions))
        print(task2(expressions))


run()
