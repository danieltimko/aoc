
def find_nth_spoken(numbers, n):
    last_spoken = {}
    last_number = None
    for i in range(n):
        if i < len(numbers):
            last_spoken[numbers[i]] = (None, i)
            last_number = numbers[i]
        else:
            before_last, last = last_spoken[last_number]
            if before_last is None:
                if 0 in last_spoken:
                    last_spoken[0] = (last_spoken[0][1], i)
                else:
                    last_spoken[0] = (None, i)
                last_number = 0
            else:
                diff = last - before_last
                if diff in last_spoken:
                    last_spoken[diff] = (last_spoken[diff][1], i)
                else:
                    last_spoken[diff] = (None, i)
                last_number = diff
    return last_number


def run():
    with open('input') as file:
        line = list(map(lambda line: (line.strip()), file.readlines()))[0]
        numbers = list(map(lambda number: int(number), line.split(',')))
        print(find_nth_spoken(numbers, 2020), find_nth_spoken(numbers, 30000000))

run()
