def diff(cuboid1, cuboid2):
    for i in range(3):
        if cuboid1[i][0] > cuboid2[i][1] or cuboid2[i][0] > cuboid1[i][1]:
            return {cuboid1}  # no intersection
    intersection = tuple((max(cuboid1[i][0], cuboid2[i][0]),
                          min(cuboid1[i][1], cuboid2[i][1])) for i in range(3))
    slices = {
        ((cuboid1[0][0], intersection[0][0] - 1), cuboid1[1], cuboid1[2]),
        ((intersection[0][1] + 1, cuboid1[0][1]), cuboid1[1], cuboid1[2]),
        (intersection[0], (cuboid1[1][0], intersection[1][0] - 1), cuboid1[2]),
        (intersection[0], (intersection[1][1] + 1, cuboid1[1][1]), cuboid1[2]),
        (intersection[0], intersection[1], (cuboid1[2][0], intersection[2][0] - 1)),
        (intersection[0], intersection[1], (intersection[2][1] + 1, cuboid1[2][1]))
    }
    return {(x, y, z) for x, y, z in slices if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]}


def area(cuboid):
    a = cuboid[0][1] - cuboid[0][0] + 1
    b = cuboid[1][1] - cuboid[1][0] + 1
    c = cuboid[2][1] - cuboid[2][0] + 1
    return a*b*c


def in_task1_range(cuboid):
    for i in range(3):
        if cuboid[i][0] < -50 or cuboid[i][1] > 50:
            return False
    return True


def solve(arr, task):
    cuboids = set()
    for on, cuboid in arr:
        if task == 1 and not in_task1_range(cuboid):
            continue
        for existing_cuboid in cuboids.copy():
            cuboids.remove(existing_cuboid)
            cuboids |= diff(existing_cuboid, cuboid)
        if on:
            cuboids.add(cuboid)
    return sum(area(cuboid) for cuboid in cuboids)


def run():
    with open('input') as file:
        arr = list(map(lambda line: (line.strip().split(' ')), file.readlines()))
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] == 'on'
            arr[i][1] = tuple(map(lambda x: tuple(map(int, x[2:].split('..'))), arr[i][1].split(',')))
    print(solve(arr, 1))
    print(solve(arr, 2))


run()
