from input_utils import *


def digit_to_char(n):
    if n == -1:
        return '-'
    if n == -2:
        return '='
    return str(n)


def char_to_digit(c):
    if c == '-':
        return -1
    elif c == '=':
        return -2
    return int(c)


def decimal_to_snafu(num, i):
    if i == 0:
        return digit_to_char(num) if num in range(-2, 3) else ""
    mul = num // (5 ** i)
    mul = max(-2, mul)
    mul = min(2, mul)
    if result := decimal_to_snafu(num - mul * 5 ** i, i - 1):
        return digit_to_char(mul) + result
    if mul in range(-2, 2):
        if result := decimal_to_snafu(num - (mul + 1) * 5 ** i, i - 1):
            return digit_to_char(mul+1) + result
    return ""


def snafu_to_decimal(s):
    number = 0
    for i in range(0, len(s)):
        mul = char_to_digit(s[-i-1])
        number += mul * 5 ** i
    return number


def task1(numbers):
    result = sum(snafu_to_decimal(n) for n in numbers)
    highest_power = 0
    while 5**highest_power <= result:
        highest_power += 1
    return decimal_to_snafu(result, highest_power).lstrip('0')


def run():
    numbers = read_n_lines_one_string()
    print(task1(numbers))


if __name__ == "__main__":
    run()
