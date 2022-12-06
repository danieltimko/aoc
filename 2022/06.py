from input_utils import *


def task1(s):
    for i in range(3, len(s)):
        if len(set(s[i-3:i+1])) == 4:
            return i+1


def task2(s):
    for i in range(13, len(s)):
        if len(set(s[i-13:i+1])) == 14:
            return i+1


def run():
    with open(INPUT_FILE_PATH) as f:
        s = f.read().strip()
        print(task1(s))
        print(task2(s))


if __name__ == "__main__":
    run()
