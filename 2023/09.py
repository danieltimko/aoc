from input_utils import *
import sympy


def rec(arr, task=1):
    new_arr = []
    for i in range(len(arr)-1):
        if isinstance(arr[i+1], str) or isinstance(arr[i], str):
            new_arr.append(f"({arr[i+1]}-{arr[i]})")
        else:
            new_arr.append(arr[i+1] - arr[i])
    if new_arr.count(0) == len(new_arr)-1:
        return new_arr
    return rec(new_arr, task)


def get_result(arr, task=1):
    result = 0
    for line in arr:
        line = line.copy()
        line.insert(len(line) if task == 1 else 0, "x")
        expr = rec(line, task)[-1] if task == 1 else rec(line, task)[0]
        equation = sympy.sympify(f"Eq({expr},0)")
        result += sympy.solve(equation)[0]
    return result


def run():
    arr = read_n_lines_n_numbers(sep=' ')

    print(get_result(arr, task=1))
    print(get_result(arr, task=2))


if __name__ == "__main__":
    run()
