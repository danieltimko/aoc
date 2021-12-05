
def count_intersections(arr, task):
    M = {}
    for line in arr:
        fromx, fromy = line[0]
        tox, toy = line[1]
        if task == 1 and fromx != tox and fromy != toy:
            continue
        xs = [x for x in range(min(fromx, tox), max(fromx, tox) + 1)]
        ys = [y for y in range(min(fromy, toy), max(fromy, toy) + 1)]
        if tox < fromx:
            xs = xs[::-1]
        if toy < fromy:
            ys = ys[::-1]
        for i in range(max(len(xs), len(ys))):
            point = (xs[i] if len(xs) > 1 else xs[0], ys[i] if len(ys) > 1 else ys[0])
            if point not in M:
                M[point] = 0
            M[point] += 1

    count = 0
    for val in M.values():
        if val > 1:
            count += 1

    return count


def run():
    with open('input') as file:
        lines = list(map(lambda line: (line.strip().split(' -> ')), file.readlines()))
        arr = []
        for line in lines:
            point_from, point_to = line
            fromx, fromy = map(int, point_from.split(','))
            tox, toy = map(int, point_to.split(','))
            arr.append(((fromx, fromy), (tox, toy)))
        print(count_intersections(arr, task=1))
        print(count_intersections(arr, task=2))


run()
