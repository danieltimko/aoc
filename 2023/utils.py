import math


def compute_lcm(x, y):
    return (x*y)//math.gcd(x, y)


def lcm(arr):
    # math.lcm() in Python3.9+
    result = arr[0]
    for n in arr:
        result = (n * result) // (math.gcd(n, result))
    return result
