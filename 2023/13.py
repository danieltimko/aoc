from input_utils import *


def find_mirror(rows, cols, ignore=""):
    # along X axis
    for c in range(len(cols)-1):
        mirror = True
        i = 0
        while c-i >= 0 and c+i+1 < len(cols):
            if c+i + 1 < len(cols) and cols[c-i] != cols[c+i+1]:
                mirror = False
                break
            i += 1
        if mirror and ignore != f"{c} cols":
            return c+1, f"{c} cols"
    # along Y axis
    for r in range(len(rows)-1):
        mirror = True
        i = 0
        while r-i >= 0 and r+i+1 < len(rows):
            if r+i+1 < len(rows) and rows[r-i] != rows[r+i+1]:
                mirror = False
                break
            i += 1
        if mirror and ignore != f"{r} rows":
            return (r+1) * 100, f"{r} rows"
    return None


def flip(rows, cols, r, c):
    # TODO change to mutable types for efficiency
    rows[r] = rows[r][:c] + "#."[rows[r][c] == "#"] + rows[r][c+1:]
    cols[c] = cols[c][:r] + "#."[cols[c][r] == "#"] + cols[c][r+1:]


def task1(grids):
    return sum(find_mirror(rows, cols)[0] for rows, cols in grids)


def task2(grids):
    result = 0
    for rows, cols in grids:
        found = False
        for r in range(len(rows)):
            for c in range(len(cols)):
                mirror = find_mirror(rows, cols)
                flip(rows, cols, r, c)
                new_mirror = find_mirror(rows, cols, ignore=mirror[1])
                if new_mirror is not None:
                    result += new_mirror[0]
                    found = True
                    break
                flip(rows, cols, r, c)
            if found:
                break
    return result


def run():
    grids = read_n_groups_n_lines_one_string()
    for g in range(len(grids)):
        cols = []
        for c in range(len(grids[g][0])):
            cols.append(''.join(grids[g][r][c] for r in range(len(grids[g]))))
        grids[g] = (grids[g], cols)

    print(task1(grids))
    print(task2(grids))


if __name__ == "__main__":
    run()
