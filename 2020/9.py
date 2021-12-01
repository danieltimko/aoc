from collections import deque


def is_sum(arr, n):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == n:
                return True
    return False


def find_invalid_number(numbers, preamble=25):
    last_n = deque(numbers[:preamble])
    for number in numbers[preamble:]:
        if not is_sum(last_n, number):
            return number
        last_n.append(number)
        last_n.popleft()


def find_contiguous_sum(numbers, n):
    q = deque()
    q_sum = 0
    for number in numbers:
        if q_sum < n:
            q.append(number)
            q_sum += number
        while q_sum > n:
            q_sum -= q[0]
            q.popleft()
        if q_sum == n:
            return max(q) + min(q)


def run():
    with open('input') as file:
        numbers = list(map(lambda line: int(line.strip()), file.readlines()))
        invalid_number = find_invalid_number(numbers)
        print(invalid_number, find_contiguous_sum(numbers, invalid_number))


run()
