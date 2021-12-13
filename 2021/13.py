
def print_grid(dots):
    y_bounds = min(y for (_, y) in dots), max(y for (_, y) in dots)
    x_bounds = min(x for (x, _) in dots), max(x for (x, _) in dots)

    for y in range(y_bounds[0], y_bounds[1] + 1):
        for x in range(x_bounds[0], x_bounds[1] + 1):
            print(".#"[(x, y) in dots], end="")
        print()


def fold_val(val, n):
    if (val if val < n else 2 * n - val) < 0:
        print('here')
    return val if val < n else 2 * n - val


def fold_all(dots, axis, n):
    return {(fold_val(x, n) if axis == 'x' else x, fold_val(y, n) if axis == 'y' else y)
            for (x, y) in dots}


def solve(dots, folds):
    for i in range(len(folds)):
        axis, n = folds[i]
        dots = fold_all(dots, axis, n)
        if i == 0:
            print(f"task1 = {len(dots)}")
    print_grid(dots)


def run():
    with open('input') as file:
        a, b = file.read().split('\n\n')
    dots = set()
    folds = []
    for line in a.split('\n'):
        x, y = list(map(int, line.strip().split(',')))
        dots.add((x, y))
    for line in b.split('\n'):
        axis, n = line.strip()[11:].split('=')
        folds.append((axis, int(n)))

    solve(dots, folds)


run()
