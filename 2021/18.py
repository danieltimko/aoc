from __future__ import annotations

from math import floor, ceil
from typing import List


class SnailfishNumber:
    def __init__(self, s, depth=0):
        self.depth: int = depth
        self.items: List[SnailfishNumber | int] = []
        self.parse(s)

    def __str__(self):
        s = "["
        for i in range(len(self.items)):
            s += str(self.items[i])
            if i != len(self.items)-1:
                s += ','
        s += "]"
        return s

    def __add__(self, other):
        new_number = SnailfishNumber(f"[{self},{other}]")
        new_number.reduce()
        return new_number

    def parse(self, s):
        i = 1
        while i < len(s)-1:
            if s[i] == '[':
                start = i
                depth = 1
                while depth != 0:
                    i += 1
                    if s[i] == '[':
                        depth += 1
                    elif s[i] == ']':
                        depth -= 1
                self.items.append(SnailfishNumber(s[start:i+1], self.depth+1))
            elif s[i] != ',':
                num = ""
                while s[i] not in ",]":
                    num += s[i]
                    i += 1
                self.items.append(int(num))
            i += 1

    def increase_depths(self):
        self.depth += 1
        for item in self.items:
            if type(item) == SnailfishNumber:
                item.increase_depths()

    def add_to_leftmost(self, n):
        if type(self.items[0]) == SnailfishNumber:
            self.items[0].add_to_leftmost(n)
        else:
            self.items[0] += n

    def add_to_rightmost(self, n):
        if type(self.items[1]) == SnailfishNumber:
            self.items[1].add_to_rightmost(n)
        else:
            self.items[1] += n

    def reduce(self):
        while True:
            exploded = self.try_exploding()
            if exploded == (-1, -1):
                splitted = self.try_splitting()
                if not splitted:
                    break

    def try_exploding(self, depth=0):
        for i in range(len(self.items)):
            item = self.items[i]
            if type(item) == SnailfishNumber:
                if depth == 3:
                    items = tuple(item.items)
                    self.items[i] = 0
                    left, right = items
                else:
                    left, right = item.try_exploding(depth=depth+1)
                if i == 0 and right > 0:
                    if type(self.items[1]) == SnailfishNumber:
                        self.items[1].add_to_leftmost(right)
                    else:
                        self.items[1] += right
                    right = 0
                elif i == 1 and left > 0:
                    if type(self.items[0]) == SnailfishNumber:
                        self.items[0].add_to_rightmost(left)
                    else:
                        self.items[0] += left
                    left = 0
                if left != -1 or right != -1:
                    return left, right
        return -1, -1

    def try_splitting(self):
        for i in range(len(self.items)):
            item = self.items[i]
            if type(item) == SnailfishNumber:
                if item.try_splitting():
                    return True
            elif type(item) == int:
                if item >= 10:
                    left, right = floor(item/2), ceil(item/2)
                    self.items[i] = SnailfishNumber(f"[{left},{right}]", self.depth + 1)
                    i -= 1
                    return True
        return False

    def calc_magnitude(self):
        left, right = self.items
        lmag = left.calc_magnitude() if type(left) == SnailfishNumber else left
        rmag = right.calc_magnitude() if type(right) == SnailfishNumber else right
        return 3*lmag + 2*rmag


def task1(arr):
    result = arr[0]
    for number in arr[1:]:
        result += number
    return result.calc_magnitude()


def task2(arr):
    maxmag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if (mag := (arr[i] + arr[j]).calc_magnitude()) > maxmag:
                    maxmag = mag
    return maxmag


def run():
    with open('input') as file:
        arr = list(map(lambda line: SnailfishNumber(line.strip()), file.readlines()))
        print(task1(arr))
        print(task2(arr))


run()
