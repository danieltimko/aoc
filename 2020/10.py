
def count_differences(arr):
    diff_one = 0
    diff_three = 0
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff == 1:
            diff_one += 1
        elif diff == 2:
            diff_one += 2
        elif diff == 3:
            diff_three += 1
    return diff_one * diff_three


def count_arrangements(arr):
    dynamic = [0 for _ in range(len(arr))]
    dynamic[len(arr)-1] = 1
    for i in range(len(arr)-2, -1, -1):
        count = 0
        for j in range(1, 4):
            if i < len(arr)-j and arr[i+j] - arr[i] <= 3:
                count += dynamic[i+j]
        dynamic[i] = count
    return dynamic[0]


def run():
    with open('input') as file:
        arr = [0] + sorted(list(map(lambda line: int(line.strip()), file.readlines())))
        arr.append(arr[len(arr)-1] + 3)
        print(count_differences(arr))
        print(count_arrangements(arr))


run()
